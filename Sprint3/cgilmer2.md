# Sprint 3

Name: Clayton Gilmer  
NetID: cgilmer2  
Group: Watchtower  

### What you planned to do

- Refine CPU information collection (add temperature, current clock speed collection)
- Refine GPU information collection (temperature)
- Add disk information collection (for each disk - name, type, capacity, usage)
- Add method for error handling HTTP requests
- Add new "on-demand" update system

### What you did not do

- Add new "on-demand" update system

### What problems you encountered

- Collecting CPU/GPU temperatures on Windows requires usage of drivers, vendor specific things. Ultimately decided to scrap this, make it optional for other platforms
- Realized the "on-demand" update system would not get the proper attention it deserves this sprint, so moving it to next sprint

### Issues you worked on

- https://github.com/utk-cs340-spring23/Watchtower/issues/35
- https://github.com/utk-cs340-spring23/Watchtower/issues/34


### Files you worked on

- watchtower-sensor/Cargo.toml
- watchtower-sensor/src/bin/default.rs
- watchtower-sensor/src/bin/scratch.rs
- watchtower-sensor/src/lib.rs
- watchtower-sensor/src/message.rs
- watchtower-sensor/src/sys/windows.rs
- watchtower-sensor/src/types/cpu.rs
- watchtower-sensor/src/types/gpu.rs
- watchtower-sensor/src/types/hello.rs
- watchtower-sensor/src/types/mod.rs

### What you accomplished

- Refine CPU information collection (current clock speed collection)
- Add disk information collection (for each disk - name, type, capacity, usage)
- Add method for error handling HTTP requests
