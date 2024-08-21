use thiserror::Error;

use crate::os::OsError;

#[derive(Debug, Error)]
pub enum Error {
    #[error("os error")]
    Os(#[from] OsError),
    #[error("uuid error")]
    Uuid(#[from] uuid::Error),
    #[error("i/o error")]
    Io(#[from] std::io::Error)
}
