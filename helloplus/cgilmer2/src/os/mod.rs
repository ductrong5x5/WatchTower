#[cfg(unix)]
pub(crate) mod unix;

#[cfg(windows)]
pub(crate) mod windows;

#[cfg(unix)]
pub(crate) use self::unix::*;
#[cfg(windows)]
pub(crate) use self::windows::*;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_ok() {
        assert!(machine_id().is_ok());
    }
}