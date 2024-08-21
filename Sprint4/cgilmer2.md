# Sprint 4

Name: Clayton Gilmer  
NetID: cgilmer2  
Group: Watchtower  

### What you planned to do

- Allow for a configuration file to configure the sensor as an alternative to CLI.
- Create an installer executable for Windows.
- Create a system tray icon on Windows.

### What you did not do

- N/A.

### What problems you encountered

- I did not encounter any serious problems this sprint.

### Issues you worked on

- https://github.com/utk-cs340-spring23/Watchtower/issues/53
- https://github.com/utk-cs340-spring23/Watchtower/issues/52
- https://github.com/utk-cs340-spring23/Watchtower/issues/51

### Files you worked on

- watchtower-sensor/build.rs
- watchtower-sensor/icon.ico
- watchtower-sensor/Cargo.toml
- watchtower-sensor/README.md
- watchtower-sensor/sensor.rc
- watchtower-sensor/installer/windows/config.json
- watchtower-sensor/installer/windows/sensor.iss
- watchtower-sensor/src/bin/sensor.rs
- watchtower-sensor/src/bin/scratch.rs
- watchtower-sensor/src/sys/windows.rs
- watchtower-sensor/src/types/disk.rs
- watchtower-sensor/src/types/mod.rs
- watchtower-sensor/src/types/net.rs

### What you accomplished

- Allow for a configuration file to configure the sensor as an alternative to CLI.
- Create an installer executable for Windows.
- Create a system tray icon on Windows.
- Fix disk/network data collection such that new network interfaces/disks are accounted for at runtime.
