use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use uuid::Uuid;

use crate::{
    sys,
    types::{
        battery::Battery, cpu::Cpu, gpu::Gpu, hello::Hello, net::Network, ram::Ram, disk::Disk, MessageType,
    },
};

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct MessageHeader {
    id: Uuid,
    timestamp: DateTime<Utc>,
}

impl MessageHeader {
    pub(crate) fn new() -> crate::Result<MessageHeader> {
        Ok(Self {
            id: sys::machine_id()?,
            timestamp: Utc::now(),
        })
    }
}

#[derive(Debug, Serialize)]
pub struct Message {
    #[serde(flatten)]
    variant: MessageType,
    #[serde(flatten)]
    header: MessageHeader,
}

impl Message {
    pub fn hello() -> crate::Result<Message> {
        Ok(Message {
            variant: MessageType::Hello(Hello::collect()?),
            header: MessageHeader::new()?,
        })
    }

    pub fn battery() -> crate::Result<Message> {
        Ok(Message {
            variant: MessageType::Battery(Battery::collect()?),
            header: MessageHeader::new()?,
        })
    }

    pub fn cpu() -> crate::Result<Message> {
        Ok(Message {
            variant: MessageType::Cpu(Cpu::collect()?),
            header: MessageHeader::new()?,
        })
    }

    pub fn ram() -> crate::Result<Message> {
        Ok(Message {
            variant: MessageType::Ram(Ram::collect()?),
            header: MessageHeader::new()?,
        })
    }

    pub fn net() -> crate::Result<Message> {
        Ok(Message {
            variant: MessageType::Net(Network::collect()?),
            header: MessageHeader::new()?,
        })
    }

    pub fn gpu() -> crate::Result<Message> {
        Ok(Message {
            variant: MessageType::Gpu(Gpu::collect()?),
            header: MessageHeader::new()?,
        })
    }

    pub fn disk() -> crate::Result<Message> {
        Ok(
            Message {
                variant: MessageType::Disk(Disk::collect()?),
                header: MessageHeader::new()?,
            }
        )
    }
}
