use thiserror::Error;

#[cfg(not(target_os = "macos"))]
use crate::sys::OsError;

#[derive(Debug, Error)]
pub enum Error {
    // cross compatibility
    #[error("no GPU found")]
    NoGpuFound,
    #[error("uuid error")]
    Uuid(#[from] uuid::Error),
    #[error("i/o error")]
    Io(#[from] std::io::Error),

    // darwin(macos) compatibility
    #[cfg(target_os = "macos")]
    #[error("Error: {0}")]
    GenericError(String),
    #[cfg(target_os = "macos")]
    #[error("IOKit Error, {0}")]
    KitError(String),
    #[cfg(target_os = "macos")]
    #[error("Battery error")]
    BatteryError(#[from] battery::Error),
    #[cfg(target_os = "macos")]
    #[error("Battery error")]
    ProcessorError(String),

    // partial compatibility 
    #[cfg(not(linux))]
    #[error("System tray error")]
    Tray(#[from] tray_item::TIError),
    #[cfg(not(target_os = "macos"))]
    #[error("os error")]
    Os(#[from] OsError),
    #[cfg(windows)]
    #[error("WMI error")]
    Wmi(#[from] wmi::WMIError),
}
