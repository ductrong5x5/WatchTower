use std::{
    ffi::{c_void, CString},
    str::FromStr,
};

use uuid::Uuid;
use windows::{
    s,
    Win32::System::Registry::{RegGetValueA, HKEY_LOCAL_MACHINE, RRF_RT_REG_SZ},
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
