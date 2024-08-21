// darwin.rs
// author: Jacob Curlin

// TODO:
// fix/complete any missing sensor / data collection
// revamp error handling
// create menubar widget        (use 'tauri' crate / library)


use battery::Manager;
use core_foundation_sys::base::{kCFAllocatorDefault, CFRelease};
use core_foundation_sys::string::{
    kCFStringEncodingUTF8, CFStringCreateWithCString, CFStringGetCStringPtr,
};
use default_net::{get_interfaces};
use io_kit_sys::{
    kIOMasterPortDefault, IOIteratorNext, IOObjectRelease, IORegistryEntryCreateCFProperty,
    IOServiceGetMatchingServices, IOServiceMatching,
};
use libc::{mach_port_t, KERN_SUCCESS};
use std::{
    collections::HashMap,
    ffi::{CStr, CString},
};
use sysinfo::{CpuExt, System, SystemExt, ComponentExt};
use uuid::Uuid;
use crate::types::{
    gpu::{Gpu, GpuHello},
    net::{Interface, InterfaceType },
};

pub(crate) type SensorError = crate::error::Error; 

// sensors

// MACHINE_ID
pub(crate) fn machine_id() -> crate::Result<Uuid> {
    let service_name = CString::new("IOPlatformExpertDevice").unwrap();
    let service = unsafe { IOServiceMatching(service_name.as_ptr()) };
    if service.is_null() {
        return Err(SensorError::KitError("IO Kit: IOServiceMatching call failed".to_string()));
    }

    let mut matched_services: mach_port_t = 0;
    let result = unsafe {
        IOServiceGetMatchingServices(kIOMasterPortDefault, service, &mut matched_services)
    };
    if result != KERN_SUCCESS {
        return Err(SensorError::KitError("IO Kit: IOServiceGetMatchingServices call failed".to_string()));
    }
    

    let platform_expert: mach_port_t = unsafe { IOIteratorNext(matched_services) };
    if platform_expert == 0 {
        return Err(SensorError::KitError("IO Kit: IOIteratorNext call failed".to_string()));
    }

    let uuid_key_name = CString::new("IOPlatformUUID").unwrap();
    let uuid_key = unsafe {
        CFStringCreateWithCString(
            std::ptr::null(),
            uuid_key_name.as_ptr(),
            kCFStringEncodingUTF8,
        )
    };
    let uuid_ref = unsafe {
        IORegistryEntryCreateCFProperty(platform_expert, uuid_key, kCFAllocatorDefault, 0)
    };
    if uuid_ref.is_null() {
        return Err(SensorError::KitError("IO Kit: IORegistryEntryCreateCFProperty call failed".to_string()));
    }

    let uuid_cstr =
        unsafe { CStr::from_ptr(CFStringGetCStringPtr(uuid_ref as _, kCFStringEncodingUTF8)) };
    let uuid_string = uuid_cstr.to_str();
    let uuid = Uuid::parse_str(uuid_string.unwrap());

    unsafe {
        IOObjectRelease(platform_expert);
        CFRelease(uuid_ref);
    }

    Ok(uuid?)
}

// HAS_BATTERY
pub(crate) fn has_battery() -> Result<bool, SensorError> {
    let manager = Manager::new().map_err(SensorError::BatteryError)?;
    let batteries = manager.batteries().map_err(SensorError::BatteryError)?;

    for battery in batteries {
        if battery.is_ok() {
            return Ok(true);
        }
    }

    Ok(false)
}

// BATTERY_PERCENT
pub(crate) fn battery_percent() -> Result<u8, SensorError> {
    let manager = Manager::new().map_err(SensorError::BatteryError)?;
    let batteries = manager.batteries().map_err(SensorError::BatteryError)?;

    for battery_result in batteries {
        if let Ok(battery) = battery_result {
            let battery_percent = (battery.state_of_charge().value * 100.0).round() as u8;
            return Ok(battery_percent);
        }
    }

    Err(SensorError::GenericError("battery_percentage : no Battery found".to_string()))
}

// CPU_USAGE_PERCENT
pub(crate) fn cpu_usage_percent() -> crate::Result<u8> {
    let mut system = System::new_all();
    system.refresh_all();

    let mut cpu_usage: f32 = 0.0;
    let mut cpu_count: f32 = 0.0;
    for cpu in system.cpus() {
        cpu_usage += cpu.cpu_usage();
        cpu_count += 1.0;
    }
    cpu_usage /= cpu_count;

    Ok(cpu_usage as u8)
}

// CPU_NAME
pub(crate) fn cpu_name() -> crate::Result<String> {
    let mut system = System::new();
    system.refresh_cpu();

    let cpu_info = system
        .cpus()
        .first()
        .ok_or(SensorError::ProcessorError("Failed to get processor info.".to_string()))?;

    Ok(cpu_info.brand().to_owned())
}

// CPU_CLOCK_SPEED
pub(crate) fn cpu_clock_speed() -> crate::Result<u32> {
   Ok(0)  
    
    // todo: static clock speed
}

// CPU_CURRENT_CLOCK_SPEED
pub(crate) fn cpu_current_clock_speed() -> crate::Result<u32> {
    let (first_frequency, _) = get_m1_frequencies()?;
    Ok(first_frequency.unwrap())
}

// CPU_CURRENT_TEMPERATURE
pub(crate) fn cpu_current_temperature() -> crate::Result<Option<f32>> {
    get_m1_package_temperature()
}

// INSTALLED_RAM
pub(crate) fn installed_ram() -> crate::Result<u64> {
    let system = System::new_all();
    Ok(system.total_memory())
}

// RAM_USAGE
pub(crate) fn ram_usage() -> crate::Result<u64> {
    let system = System::new_all();
    Ok(system.used_memory())
}

// NETWORK_INFO
pub(crate) fn network_info() -> crate::Result<HashMap<String, Interface>> {
    let mut out = HashMap::new();

    let _interfaces = get_interfaces();

    for _interface in _interfaces {
        
        let mac_address = match _interface.mac_addr {
            Some(mac_addr) => {
                let mac_addr_bytes = mac_addr.octets();
                format!(
                    "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}",
                    mac_addr_bytes[0],
                    mac_addr_bytes[1],
                    mac_addr_bytes[2],
                    mac_addr_bytes[3],
                    mac_addr_bytes[4],
                    mac_addr_bytes[5],
                )
            }
            None => "00:00:00:00:00:00".to_string(),
        }; 

        let name = _interface.name;

        let description = _interface.description.unwrap_or("Interface".to_string());

        let r#type = match _interface.if_type {
            default_net::interface::InterfaceType::Ethernet => InterfaceType::Ethernet,
            default_net::interface::InterfaceType::GigabitEthernet => InterfaceType::Ethernet,
            default_net::interface::InterfaceType::IPOverAtm => InterfaceType::Ethernet,
            default_net::interface::InterfaceType::Ethernet3Megabit => InterfaceType::Ethernet,
            default_net::interface::InterfaceType::Isdn => InterfaceType::Ethernet,
            default_net::interface::InterfaceType::Ppp => InterfaceType::Loopback,
            default_net::interface::InterfaceType::Loopback => InterfaceType::Loopback,
            default_net::interface::InterfaceType::Wireless80211 => InterfaceType::WiFi,
            default_net::interface::InterfaceType::FastEthernetFx => InterfaceType::WiFi,
            _ => InterfaceType::Other,
        };

        let mut ip_addresses: Vec<String> = _interface
        .ipv4
        .iter()
        .map(|ipv4_net| ipv4_net.addr.to_string())
        .chain(
            _interface
                .ipv6
                .iter()
                .map(|ipv6_net| ipv6_net.addr.to_string()),
        )
        .collect();

        if ip_addresses.is_empty() {
            ip_addresses.push("0".to_string());
        }

        let tx = 0;
        let rx = 0;
            
        match r#type {  
            InterfaceType::Other => continue,   // (temp?) only collect interfaces of known types
            _ => {
                    out.insert(
                        mac_address,
                        Interface{ 
                            name,
                            description,
                            r#type,
                            ip_addresses,
                            rx,
                            tx,
                        },
                    ); 
            }
        }
    }                
    
    Ok(out)
} 



// GPU_INFO
pub(crate) fn gpu_info() -> crate::Result<GpuHello> {
    let mut system = System::new();
    system.refresh_cpu();

    let gpu_info= system
        .cpus()
        .first()
        .ok_or(SensorError::ProcessorError("Failed to get processor info.".to_string()))?;

    let gpu_name = gpu_info.brand().to_owned();

    let installed_mem = system.total_memory();

    Ok(GpuHello {
        name: gpu_name,
        installed_vram: installed_mem,
        max_frequency: Some(0),
    })
}


// GPU_STATISTICS
pub(crate) fn gpu_statistics() -> crate::Result<Gpu> {
    let (first_frequency, _) = get_m1_frequencies()?;
    let temperature = get_m1_package_temperature().unwrap_or(None);
    
    Ok(Gpu {
        current_frequency: first_frequency.or(Some(0)),
        current_vram_usage: 0 as u64,
        current_temperature: temperature.or(Some(0.0)),
    })
}
// [private darwin-specific functions]

// get apple-silicon platform package temperature
fn get_m1_package_temperature() -> crate::Result<Option<f32>> {
    let mut system = System::new();
    system.refresh_components_list();

    let mut sum = 0.0;
    let mut count = 0;
    let components = system.components();
    
    // loop through all components of format "PMU tdie" and compute / return the average temp value
    // ( "PMU tdie" refers to CPU die temps on ARM macs ) 
    // see: https://github.com/exelban/stats/blob/6b36d3e9773d3fa2c3fd3c6047227a55d16ea5e8/Modules/Sensors/values.swift#L101-L176
    for component in components {
        if component.label().contains("PMU tdie") {
            println!("Component: {} - {}", component.label(), component.temperature());
            sum += component.temperature();
            count += 1;
        }
    } 
    
    if count == 0 {             // if count is 0, (no matching compnents found) return None
        return Ok(None);
    }

    let avg = sum / count as f32;
    
    // return the average temperature
    Ok(Some(avg))
}

// this is a mess but it works. pending cleanup/refactor
// the only way to get the current frequency of the M1 macs at this time is to shell-out to powermetrics, which is closed source
// there is a guy on github who has reverse engineered the powermetrics binary for real-time frequency readings without shell-out, may attempt to implement this in the future
// requires elevation currently
fn get_m1_frequencies() -> crate::Result<(Option<u32>, Option<u32>)> {
    use std::process::{Command, Stdio};
    use std::io::{BufRead, BufReader};

    let powermetrics = Command::new("sudo")
        .arg("powermetrics")
        .arg("--samplers")
        .arg("gpu_power,cpu_power")
        .arg("-i1")
        .arg("-n1")
        .stdout(Stdio::piped())
        .spawn()
        .expect("Failed to run powermetrics");

    let output = BufReader::new(powermetrics.stdout.expect("Failed to read stdout"));

    let mut cpu_frequency = None;
    let mut gpu_active_frequency = None;

    for line in output.lines() {
        let line = line.expect("Failed to read output line");

        println!("{}", line);

        if line.contains("E-Cluster HW active frequency") {
            let words: Vec<&str> = line.split_whitespace().collect();
            cpu_frequency = words
                .iter()
                .position(|&word| word.contains("MHz"))
                .and_then(|pos| pos.checked_sub(1))
                .and_then(|pos| words.get(pos))
                .and_then(|word| word.parse::<u32>().ok());
        } else if line.contains("GPU active frequency") {
            let words: Vec<&str> = line.split_whitespace().collect();
            gpu_active_frequency = words
                .iter()
                .position(|&word| word.contains("MHz"))
                .and_then(|pos| pos.checked_sub(1))
                .and_then(|pos| words.get(pos))
                .and_then(|word| word.parse::<u32>().ok());
        }

        if cpu_frequency.is_some() && gpu_active_frequency.is_some() {
            break;
        }
    }

    match (cpu_frequency, gpu_active_frequency) {
        (Some(cpu_freq), Some(gpu_freq)) => {
            Ok((Some(cpu_freq as u32), Some(gpu_freq as u32))) 
            // println!("CPU frequency: {} MHz", cpu_freq);
            // println!("GPU frequency: {} MHz", gpu_freq);
        }
        _ => {
            return Err(SensorError::ProcessorError("Failed to get processor info.".to_string()));
        }
    }
}


// (temp) tests
#[cfg(test)]
mod tests {
    use super::*;

    // MACHINE_ID
    #[test]
    fn test_machine_id() {
        let id = machine_id().unwrap();
        println!("(darwin) MACHINE_ID [UUID]: {}", id);
    }

    // HAS_BATTERY
    #[test]
    fn test_has_battery() {
        let has_battery = has_battery().unwrap();
        println!("\n(darwin) HAS_BATTERY: {}", has_battery);
    }

    // BATTERY_PERCENT
    #[test]
    fn test_battery_percent() {
        let battery_percent = battery_percent().unwrap();
        println!("\n(darwin) BATTERY_PERCENT [%]: {}", battery_percent);
    }

    // CPU_USAGE_PERCENT
    #[test]
    fn test_cpu_usage_percent() {
        let cpu_usage_percent = cpu_usage_percent().unwrap();
        println!("\n(darwin) CPU_USAGE_PERCENT [%]: {}", cpu_usage_percent);
    }
    
    // CPU_NAME
    #[test]
    fn test_cpu_name() {
        let cpu_name = cpu_name().unwrap();
        println!("\n(darwin) CPU_NAME: {}", cpu_name);
    }

    // CPU_CLOCK_SPEED
    #[test]
    fn test_cpu_clock_speed() {
        let cpu_clock_speed = cpu_clock_speed().unwrap();
        println!("\n(darwin) CPU_CLOCK_SPEED [MHz]: {}", cpu_clock_speed);
    }

    // CPU_CURRENT_CLOCK_SPEED
    #[test]
    fn test_cpu_current_clock_speed() {
        let cpu_current_clock_speed = cpu_current_clock_speed().unwrap();
        println!(
            "\n(darwin) CPU_CURRENT_CLOCK_SPEED [MHz]: {}",
            cpu_current_clock_speed
        );
    }

    // CPU_CURRENT_TEMPERATURE
    #[test]
    fn test_cpu_current_temperature() {
        let cpu_current_temperature = cpu_current_temperature().unwrap().unwrap();
        println!("\n(darwin) CPU_CURRENT_TEMPERATURE [C]: {}", cpu_current_temperature);
    }

    /*  INSTALLED_RAM
    #[test]
    fn test_installed_ram() {
        let installed_ram = installed_ram().unwrap();
        println!("\n(darwin) INSTALLED_RAM [bytes]: {}", installed_ram);
    }
    */

    // RAM_USAGE
    #[test]
    fn test_ram_usage() {
        let ram_usage = ram_usage().unwrap();
        println!(
            "\n(darwin) RAM_USAGE [bytes]: {}   [MB]: {} ;   [GB]: {}",
            ram_usage,
            ram_usage / 1024 / 1024,
            ram_usage / 1024 / 1024 / 1024
        );
        let installed_ram = installed_ram().unwrap();
        let ram_usage_percent = (ram_usage as f64 / installed_ram as f64) * 100.0;
        println!("(darwin) RAM_USAGE [%]: {}", ram_usage_percent);
    }

    // NETWORK_INFO
    #[test]
    fn test_network_info() {
        let network_info = network_info().unwrap();
        println!("\n(darwin) NETWORK_INFO: {:#?}", network_info);
    }
    // test for gpu_info

    // GPU_INFO
    #[test]
    fn test_gpu_info() {
        let gpu_info = gpu_info().unwrap();
        println!("\n(darwin) GPU_INFO: {:#?}", gpu_info);
    } 
    
    // GPU_STATISTICS
    #[test]
    fn test_gpu_statistics() {
        let gpu_statistics = gpu_statistics().unwrap();
        println!("\n(darwin) GPU_STATISTICS: {:#?}", gpu_statistics);
    }

}





