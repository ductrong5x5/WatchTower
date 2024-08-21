pub(crate) mod data;
pub(crate) mod error;
pub(crate) mod message;
pub(crate) mod os;

pub(crate) use error::Error;
pub(crate) type Result<T, E = Error> = ::std::result::Result<T, E>;

use crate::message::MessageHeader;

fn main() -> color_eyre::Result<()> {
    color_eyre::install()?;
    tracing_subscriber::fmt::init();

    let header = MessageHeader::new()?;

    println!("{}", serde_json::to_string_pretty(&header)?);

    Ok(())
}
