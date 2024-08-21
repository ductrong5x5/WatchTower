use serde::{Deserialize, Serialize};

use crate::sys;

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct BatteryHello {
    has_battery: bool,
}

impl BatteryHello {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            has_battery: sys::has_battery()?,
        })
    }
}

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct Battery {
    percent: u8,
}

impl Battery {
    pub(crate) fn collect() -> crate::Result<Self> {
        Ok(Self {
            percent: sys::battery_percent()?,
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn battery() {
        Battery::collect().unwrap();
    }
}
