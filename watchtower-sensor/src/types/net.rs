use std::collections::HashMap;

use serde::{Deserialize, Serialize};

use crate::sys;

#[derive(Debug, Hash, Deserialize, Serialize)]
pub(crate) enum InterfaceType {
    Loopback,
    Ethernet,
    WiFi,
    Other,
}

#[derive(Debug, Hash, Deserialize, Serialize)]
pub(crate) struct Interface {
    pub(crate) name: String,              // Name of this interface
    pub(crate) description: String,       // Description associated with interface
    pub(crate) r#type: InterfaceType,     // Interface type (see `InterfaceType` enum)
    pub(crate) ip_addresses: Vec<String>, // List of IP addresses associated with this interface
    pub(crate) rx: u64, // Recieved bytes
    pub(crate) tx: u64, // Transmitted bytes
}

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct NetworkHello {
    pub(crate) interfaces: HashMap<String, Interface>, // Key is MAC address
}

impl NetworkHello {
    pub fn collect() -> crate::Result<Self> {
        Ok(NetworkHello {
            interfaces: sys::network_info()?
        })
    }
}

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct Network {
    pub(crate) interfaces: HashMap<String, Interface>, // Key is MAC address
}

impl Network {
    pub fn collect() -> crate::Result<Self> {
        Ok(Network {
            interfaces: sys::network_info()?
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn network() {
        Network::collect().unwrap();
    }
}
