use std::collections::HashMap;

use serde::Serialize;
use sysinfo::{DiskExt, DiskType, SystemExt};

#[derive(Debug, Serialize)]
pub(crate) struct DiskInfo {
    r#type: DiskType,
    capacity: u64,
    usage: u64,
    is_removable: bool,
}

#[derive(Debug, Serialize)]
pub(crate) struct DiskHello {
    pub(crate) disks: HashMap<String, DiskInfo>,
}

impl DiskHello {
    pub(crate) fn collect() -> crate::Result<Self> {
        let mut out = Self {
            disks: HashMap::new(),
        };

        let mut query = sysinfo::System::new_all();
        query.refresh_disks();

        for disk in query.disks() {
            let info = DiskInfo {
                r#type: disk.type_(),
                capacity: disk.total_space(),
                usage: disk.total_space() - disk.available_space(),
                is_removable: disk.is_removable(),
            };

            out.disks
                .insert(disk.name().to_string_lossy().to_string(), info);
        }

        Ok(out)
    }
}

#[derive(Debug, Serialize)]
pub(crate) struct Disk {
    disks: HashMap<String, DiskInfo>,
}

impl Disk {
    pub(crate) fn collect() -> crate::Result<Self> {
        let mut out = Self {
            disks: HashMap::new(),
        };

        let mut query = sysinfo::System::new_all();
        query.refresh_disks();

        for disk in query.disks() {
            let info = DiskInfo {
                r#type: disk.type_(),
                capacity: disk.total_space(),
                usage: disk.total_space() - disk.available_space(),
                is_removable: disk.is_removable(),
            };

            out.disks
                .insert(disk.name().to_string_lossy().to_string(), info);
        }

        Ok(out)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn disk() {
        Disk::collect().unwrap();
    }
}
