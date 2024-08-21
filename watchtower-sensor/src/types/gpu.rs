use serde::{Deserialize, Serialize};

use crate::sys;

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct GpuHello {
    pub(crate) name: String,
    pub(crate) installed_vram: u64,
    pub(crate) max_frequency: Option<u32>, // MHz
}

impl GpuHello {
    pub(crate) fn collect() -> crate::Result<Self> {
        sys::gpu_info()
    }
}

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct Gpu {
    pub(crate) current_vram_usage: u64,
    pub(crate) current_frequency: Option<u32>,
    pub(crate) current_temperature: Option<f32>,
}

impl Gpu {
    pub(crate) fn collect() -> crate::Result<Self> {
        sys::gpu_statistics()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn gpu() {
        Gpu::collect().unwrap();
    }
}
