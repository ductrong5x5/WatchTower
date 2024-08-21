# Sprint 1

Name: Clayton Gilmer
NetID: cgilmer2
Group: Watchtower

### What you planned to do

- Create the JSON messaging framework for the sensor (https://github.com/utk-cs340-spring23/Watchtower/issues/15)
- Create the initial connect ("hello") message for the sensor (https://github.com/utk-cs340-spring23/Watchtower/issues/1)
- Collect Windows CPU, RAM, battery information (https://github.com/utk-cs340-spring23/Watchtower/issues/2)
- Set up sensor HTTP communications (https://github.com/utk-cs340-spring23/Watchtower/issues/3)

### What you did not do

- Set up sensor HTTP communications (https://github.com/utk-cs340-spring23/Watchtower/issues/3)

### What problems you encountered

- I had problems collecting CPU usage information initially, as Windows doesn't provide a straightforward method to do so.  

### Issues you worked on

- https://github.com/utk-cs340-spring23/Watchtower/issues/15
- https://github.com/utk-cs340-spring23/Watchtower/issues/1
- https://github.com/utk-cs340-spring23/Watchtower/issues/2

### Files you worked on

- watchtower-sensor/Cargo.toml
- watchtower-sensor/Cargo.lock
- watchtower-sensor/rustfmt.toml
- watchtower-sensor/src/error.rs
- watchtower-sensor/src/main.rs
- watchtower-sensor/src/message.rs
- watchtower-sensor/src/os/darwin.rs
- watchtower-sensor/src/os/linux.rs
- watchtower-sensor/src/os/mod.rs
- watchtower-sensor/src/os/windows.rs
- watchtower-sensor/src/types/battery.rs
- watchtower-sensor/src/types/cpu.rs
- watchtower-sensor/src/types/hello.rs
- watchtower-sensor/src/types/mod.rs
- watchtower-sensor/src/types/ram.rs

### What you accomplished

During sprint 1, I wrote the messaging/serialization framework that the sensor will use to serialize gathered data points to JSON.

I wrote the code for formatting the initial message sent to the backend ("hello") for the sensor. 

I also wrote initial Windows implementations for collecting the CPU core count and usage, battery status, and installed RAM/RAM usage.  
