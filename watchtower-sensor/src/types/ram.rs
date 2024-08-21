use serde::{Deserialize, Serialize};

use crate::sys;

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct RamHello {
    installed: u64,
}

impl RamHello {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            installed: sys::installed_ram()?,
        })
    }
}

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct Ram {
    usage: u64,
}

impl Ram {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            usage: sys::ram_usage()?,
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ram() {
        Ram::collect().unwrap();
    }
}
