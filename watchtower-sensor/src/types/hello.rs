use serde::{Deserialize, Serialize};

use super::{gpu::GpuHello, net::NetworkHello, disk::DiskHello};
use crate::types::{battery::BatteryHello, cpu::CpuHello, ram::RamHello};

#[derive(Debug, Serialize)]
pub(crate) struct Hello {
    #[serde(flatten)]
    inner: os_info::Info,
    battery: BatteryHello,
    cpu: CpuHello,
    ram: RamHello,
    network: NetworkHello,
    gpu: GpuHello,
    #[serde(rename = "disk")]
    disk: DiskHello,
}

impl Hello {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            inner: os_info::get(),
            battery: BatteryHello::collect()?,
            cpu: CpuHello::collect()?,
            ram: RamHello::collect()?,
            network: NetworkHello::collect()?,
            gpu: GpuHello::collect()?,
            disk: DiskHello::collect()?,
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn hello() {
        Hello::collect().unwrap();
    }
}
