use std::{fs::File, io::Read};

use uuid::Uuid;

pub(crate) type OsError = rustix::io::Errno;

pub(crate) fn machine_id() -> crate::Result<Uuid> {
    let mut file = File::open("/etc/machine-id")?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;

    let digest = md5::compute(contents.trim());

    Ok(Uuid::from_bytes(*digest))
}