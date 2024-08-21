use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use uuid::Uuid;

use crate::os;

#[derive(Debug, Deserialize, Serialize)]
pub(crate) struct MessageHeader {
    id: Uuid,
    timestamp: DateTime<Utc>,
}

impl MessageHeader {
    pub(crate) fn new() -> crate::Result<MessageHeader> {
        Ok(Self {
            id: os::machine_id()?,
            timestamp: Utc::now(),
        })
    }
}
