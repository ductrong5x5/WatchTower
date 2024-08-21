pub mod error;
pub mod message;
pub mod sys;
pub mod types;

pub use error::Error;
pub type Result<T, E = Error> = ::std::result::Result<T, E>;
