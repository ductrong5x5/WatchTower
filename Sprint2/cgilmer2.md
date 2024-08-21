# Sprint 2

Name: Clayton Gilmer
NetID: cgilmer2
Group: Watchtower

### What you planned to do

- Add HTTP communications to the sensor
- Collect basic GPU information and statistics
- Collect network adapter information and statistics.

### What you did not do

I completed everything I had planned to do this sprint.

### What problems you encountered

### Issues you worked on

- https://github.com/utk-cs340-spring23/Watchtower/issues/3
- https://github.com/utk-cs340-spring23/Watchtower/issues/18
- https://github.com/utk-cs340-spring23/Watchtower/issues/17

### Files you worked on

- watchtower-sensor/Cargo.toml
- watchtower-sensor/Cargo.lock
- watchtower-sensor/src/error.rs
- watchtower-sensor/src/main.rs
- watchtower-sensor/src/message.rs
- watchtower-sensor/src/sys/darwin.rs
- watchtower-sensor/src/sys/linux.rs
- watchtower-sensor/src/sys/windows.rs
- watchtower-sensor/src/types/battery.rs
- watchtower-sensor/src/types/cpu.rs
- watchtower-sensor/src/types/gpu.rs
- watchtower-sensor/src/types/hello.rs
- watchtower-sensor/src/types/mod.rs
- watchtower-sensor/src/types/net.rs
- watchtower-sensor/src/types/ram.rs

### What you accomplished

I wrote a command-line interface for the sensor that allows specifiying a backend URL to send collected information to. 

I rigged up the HTTP communication glue such that the sensor can communicate with the backend.

I refactored the sensor such that certain immutable information is only collected and sent to the backend once.

I added the Windows implementation for collection of the following information:

GPU:
- Name
- Total VRAM
- In-use VRAM

Network (for each interface):
- Name
- Description
- MAC address
- Type (Ethernet, Wifi, Loopback, Other)
- Associated IP addresses
- Recieved and transmitted bytes
