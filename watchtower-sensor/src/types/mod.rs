use serde::Serialize;

pub(crate) mod battery;
pub(crate) mod cpu;
pub(crate) mod gpu;
pub(crate) mod hello;
pub(crate) mod net;
pub(crate) mod ram;
pub(crate) mod disk;

#[derive(Debug, Serialize)]
pub(crate) enum MessageType {
    #[serde(rename = "hello")]
    Hello(hello::Hello),
    #[serde(rename = "battery")]
    Battery(battery::Battery),
    #[serde(rename = "cpu")]
    Cpu(cpu::Cpu),
    #[serde(rename = "ram")]
    Ram(ram::Ram),
    #[serde(rename = "net")]
    Net(net::Network),
    #[serde(rename = "gpu")]
    Gpu(gpu::Gpu),
    #[serde(rename = "disk")]
    Disk(disk::Disk)
}
