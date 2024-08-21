#[cfg(target_os = "macos")]
pub(crate) mod darwin;

#[cfg(target_os = "linux")]
pub(crate) mod linux;

#[cfg(windows)]
pub(crate) mod windows;

#[cfg(target_os = "macos")]
pub(crate) use self::darwin::*;
#[cfg(target_os = "linux")]
pub(crate) use self::linux::*;
#[cfg(windows)]
pub(crate) use self::windows::*;
