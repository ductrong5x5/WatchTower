use serde::{Deserialize, Serialize};

use crate::sys;

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct CpuHello {
    name: String,
    core_count: usize,
    thread_count: usize,
    clock_speed: u32, // MHz
}

impl CpuHello {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            name: sys::cpu_name()?,
            core_count: num_cpus::get_physical(),
            thread_count: num_cpus::get(),
            clock_speed: sys::cpu_clock_speed()?,
        })
    }
}

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct Cpu {
    usage_percent: u8,
    current_clock_speed: u32,
    current_temperature: Option<f32>, // celsius
}

impl Cpu {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            usage_percent: sys::cpu_usage_percent()?,
            current_clock_speed: sys::cpu_current_clock_speed()?,
            current_temperature: sys::cpu_current_temperature()?,
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn cpu() {
        Cpu::collect().unwrap();
    }
}
