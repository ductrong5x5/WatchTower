use std::{
    collections::HashMap,
    ffi::{c_void, CStr, CString},
    mem::MaybeUninit,
    str::FromStr,
};

use serde::Deserialize;
use uuid::Uuid;
use windows::{
    s, w,
    Win32::{
        Foundation::{ERROR_BUFFER_OVERFLOW, ERROR_SUCCESS, MAX_PATH},
        NetworkManagement::IpHelper::{
            GetAdaptersInfo, GetIfTable2, IF_TYPE_IEEE80211, IP_ADAPTER_INFO, MIB_IF_TABLE2,
            MIB_IF_TYPE_ETHERNET, MIB_IF_TYPE_LOOPBACK,
        },
        System::{
            Performance::{
                PdhAddEnglishCounterW, PdhCollectQueryData, PdhGetFormattedCounterValue,
                PdhOpenQueryW, PDH_FMT_COUNTERVALUE, PDH_FMT_DOUBLE,
            },
            Power::{GetSystemPowerStatus, SYSTEM_POWER_STATUS},
            Registry::{RegGetValueA, HKEY_LOCAL_MACHINE, RRF_RT_REG_SZ},
            SystemInformation::{
                GetPhysicallyInstalledSystemMemory, GlobalMemoryStatus, MEMORYSTATUS,
            },
        }, Storage::FileSystem::{FindFirstVolumeW, FindFirstVolumeA, FindVolumeClose, GetVolumePathNamesForVolumeNameA},
    },
};
use wmi::{COMLibrary, WMIConnection};

use crate::types::{
    gpu::{Gpu, GpuHello},
    net::{Interface, InterfaceType, Network, NetworkHello}, disk::{DiskHello, Disk},
};

pub(crate) type OsError = windows::core::Error;

pub(crate) fn machine_id() -> crate::Result<Uuid> {
    let mut value_size = u32::default();

    unsafe {
        RegGetValueA(
            HKEY_LOCAL_MACHINE,
            s!("SOFTWARE\\Microsoft\\Cryptography"),
            s!("MachineGuid"),
            RRF_RT_REG_SZ,
            None,
            None,
            Some(&mut value_size),
        )
        .ok()?;
    }

    let mut buf: Vec<u8> = Vec::with_capacity(value_size as usize);

    unsafe {
        RegGetValueA(
            HKEY_LOCAL_MACHINE,
            s!("SOFTWARE\\Microsoft\\Cryptography"),
            s!("MachineGuid"),
            RRF_RT_REG_SZ,
            None,
            Some(buf.as_mut_ptr() as *mut c_void),
            Some(&mut value_size),
        )
        .ok()?;

        buf.set_len(value_size as usize);
    }

    let binding = CString::from_vec_with_nul(buf).unwrap();

    Ok(Uuid::from_str(binding.to_str().unwrap())?)
}

pub(crate) fn has_battery() -> crate::Result<bool> {
    let mut status = SYSTEM_POWER_STATUS::default();

    unsafe {
        GetSystemPowerStatus(&mut status).ok()?;
    }

    // per MSDN (https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-system_power_status)
    // SYSTEM_POWER_STATUS.BatteryFlag is 128 if a system battery doesn't exist
    Ok(status.BatteryFlag != 128)
}

pub(crate) fn battery_percent() -> crate::Result<u8> {
    let mut status = SYSTEM_POWER_STATUS::default();

    unsafe {
        GetSystemPowerStatus(&mut status).ok()?;
    }

    Ok(status.BatteryLifePercent)
}

pub(crate) fn cpu_usage_percent() -> crate::Result<u8> {
    let mut hquery = isize::default();
    let mut hcounter = isize::default();

    unsafe {
        if PdhOpenQueryW(None, 0, &mut hquery) != ERROR_SUCCESS.0 {
            return Err(crate::error::Error::Os(windows::core::Error::from_win32()));
        }

        if PdhAddEnglishCounterW(
            hquery,
            w!("\\Processor(_Total)\\% Processor Time"),
            0,
            &mut hcounter,
        ) != ERROR_SUCCESS.0
        {
            return Err(crate::error::Error::Os(windows::core::Error::from_win32()));
        }

        PdhCollectQueryData(hquery);

        // per MSDN this has to be a minimum of one second :(
        let duration = std::time::Duration::from_secs(1);
        std::thread::sleep(duration);

        PdhCollectQueryData(hquery);
    }

    let mut counter_val = PDH_FMT_COUNTERVALUE::default();

    unsafe {
        PdhGetFormattedCounterValue(hcounter, PDH_FMT_DOUBLE, None, &mut counter_val);
    }

    Ok(unsafe { counter_val.Anonymous.doubleValue as u8 })
}

#[allow(non_camel_case_types, non_snake_case)]
#[derive(Debug, Deserialize)]
struct Win32_Processor {
    Name: String,
    MaxClockSpeed: u32,
    CurrentClockSpeed: u32,
}

pub(crate) fn cpu_name() -> crate::Result<String> {
    let com = COMLibrary::new()?;
    let wmi = WMIConnection::new(com)?;

    let results: Vec<Win32_Processor> = wmi.query()?;

    if !results.is_empty() {
        return Ok(results[0].Name.clone());
    } else {
        panic!();
    }
}

pub(crate) fn cpu_clock_speed() -> crate::Result<u32> {
    let com = COMLibrary::new()?;
    let wmi = WMIConnection::new(com)?;

    let results: Vec<Win32_Processor> = wmi.query()?;

    if !results.is_empty() {
        return Ok(results[0].MaxClockSpeed);
    } else {
        panic!();
    }
}

pub(crate) fn cpu_current_clock_speed() -> crate::Result<u32> {
    let com = COMLibrary::new()?;
    let wmi = WMIConnection::new(com)?;

    let results: Vec<Win32_Processor> = wmi.query()?;

    if !results.is_empty() {
        return Ok(results[0].CurrentClockSpeed);
    } else {
        panic!();
    }
}

pub(crate) fn cpu_current_temperature() -> crate::Result<Option<f32>> {
    Ok(None)
}

pub(crate) fn installed_ram() -> crate::Result<u64> {
    let mut installed = u64::default();

    unsafe {
        GetPhysicallyInstalledSystemMemory(&mut installed).ok()?;
    }

    Ok(installed * 1000)
}

pub(crate) fn ram_usage() -> crate::Result<u64> {
    let mut memory_status = MEMORYSTATUS::default();

    unsafe {
        GlobalMemoryStatus(&mut memory_status);
    }

    Ok((memory_status.dwTotalPhys - memory_status.dwAvailPhys)
        .try_into()
        .unwrap())
}

pub(crate) fn network_info() -> crate::Result<HashMap<String, Interface>> {
    // Use GetAdaptersInfo
    let mut out = HashMap::new();

    let mut buf = Vec::<IP_ADAPTER_INFO>::with_capacity(0);

    unsafe {
        let mut capacity: u32 = 0;

        if GetAdaptersInfo(Some(buf.as_mut_ptr()), &mut capacity) == ERROR_BUFFER_OVERFLOW.0 {
            assert!(capacity as usize % std::mem::size_of::<IP_ADAPTER_INFO>() == 0);

            buf.reserve_exact(capacity as usize / std::mem::size_of::<IP_ADAPTER_INFO>());
            if GetAdaptersInfo(Some(buf.as_mut_ptr()), &mut capacity) != ERROR_SUCCESS.0 {
                return Err(crate::Error::Os(windows::core::Error::from_win32()));
            }

            assert!(capacity as usize % std::mem::size_of::<IP_ADAPTER_INFO>() == 0);

            buf.set_len(capacity as usize / std::mem::size_of::<IP_ADAPTER_INFO>());
        } else {
            return Err(crate::Error::Os(windows::core::Error::from_win32()));
        }

        for adapter in buf {
            let name = CStr::from_ptr(adapter.AdapterName.as_ptr() as *const i8)
                .to_string_lossy()
                .to_string()
                .replace('\"', "");

            let mac_address = format!(
                "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}",
                adapter.Address[0],
                adapter.Address[1],
                adapter.Address[2],
                adapter.Address[3],
                adapter.Address[4],
                adapter.Address[5]
            );

            let description = CStr::from_ptr(adapter.Description.as_ptr() as *const i8)
                .to_string_lossy()
                .to_string()
                .replace('\"', "");

            let r#type = match adapter.Type {
                MIB_IF_TYPE_LOOPBACK => InterfaceType::Loopback,
                MIB_IF_TYPE_ETHERNET => InterfaceType::Ethernet,
                IF_TYPE_IEEE80211 => InterfaceType::WiFi,
                _ => InterfaceType::Other,
            };

            let ip_addresses = {
                let mut list: Vec<String> = Vec::new();
                let mut current = adapter.IpAddressList;

                list.push(
                    CStr::from_ptr(current.IpAddress.String.as_ptr() as *const i8)
                        .to_string_lossy()
                        .to_string(),
                );

                while !current.Next.is_null() {
                    current = *current.Next;

                    list.push(
                        CStr::from_ptr(current.IpAddress.String.as_ptr() as *const i8)
                            .to_string_lossy()
                            .to_string(),
                    );
                }

                list
            };

            out.insert(
                mac_address,
                Interface {
                    name,
                    description,
                    r#type,
                    ip_addresses,
                    rx: 0,
                    tx: 0,
                },
            );
        }
    }

    unsafe {
        let mut uninit = MaybeUninit::<*mut MIB_IF_TABLE2>::uninit();

        GetIfTable2(uninit.as_mut_ptr())?;

        let table = uninit.assume_init();

        let entries =
            std::slice::from_raw_parts((*table).Table.as_ptr(), (*table).NumEntries as usize);

        for entry in entries {
            let mac_address = format!(
                "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}",
                entry.PhysicalAddress[0],
                entry.PhysicalAddress[1],
                entry.PhysicalAddress[2],
                entry.PhysicalAddress[3],
                entry.PhysicalAddress[4],
                entry.PhysicalAddress[5]
            );

            let rx = entry.InOctets;
            let tx = entry.OutOctets;

            match out.get_mut(&mac_address) {
                Some(iface) => {
                    iface.rx = rx;
                    iface.tx = tx;
                },
                None => continue,
            }
        }
    }

    Ok(out)
}

pub(crate) fn gpu_info() -> crate::Result<GpuHello> {
    let com = COMLibrary::new()?;
    let wmi = WMIConnection::new(com)?;

    #[allow(non_camel_case_types, non_snake_case)]
    #[derive(Debug, Deserialize)]
    struct Win32_VideoController {
        Caption: String,
        AdapterRAM: u64,
    }

    let results: Vec<Win32_VideoController> = wmi.query()?;

    // just get first GPU for now
    if !results.is_empty() {
        return Ok(GpuHello {
            name: results[0].Caption.clone(),
            installed_vram: results[0].AdapterRAM,
            max_frequency: None,
        });
    }

    Err(crate::Error::NoGpuFound)
}

pub(crate) fn gpu_statistics() -> crate::Result<Gpu> {
    let mut hquery = isize::default();
    let mut hcounter = isize::default();

    unsafe {
        if PdhOpenQueryW(None, 0, &mut hquery) != ERROR_SUCCESS.0 {
            return Err(crate::error::Error::Os(windows::core::Error::from_win32()));
        }

        if PdhAddEnglishCounterW(
            hquery,
            w!("\\GPU Process Memory(*)\\Dedicated Usage"),
            0,
            &mut hcounter,
        ) != ERROR_SUCCESS.0
        {
            return Err(crate::error::Error::Os(windows::core::Error::from_win32()));
        }

        PdhCollectQueryData(hquery);
    }

    let mut counter_val = PDH_FMT_COUNTERVALUE::default();

    unsafe {
        PdhGetFormattedCounterValue(hcounter, PDH_FMT_DOUBLE, None, &mut counter_val);

        Ok(Gpu {
            current_vram_usage: counter_val.Anonymous.doubleValue as u64,
            current_frequency: None,
            current_temperature: None,
        })
    }
}
