# Sprint 2 Reflection
Jacob Curlin

## What you planned to do

- Get code compiling and commited for the mac_OS / 'darwin' implementation of our hardware statistics sensor
- (Both for the features I had planned on completing in S1, as well as most of the new features added for all sensors in S2)

## What you did not do

- I did not get GPU statistic collection functional. I believe that it is going to require a newer, seperate 
    Apple 'metal' library. I was unable to find GPU support, at least for my arm-based apple machine, in any of the popular mac_OS or system-agnostic hardware information crate libraries. 

## What problems you encountered

- GPU data collection on lastest mac_OS particularly on applie sililcon (arm)
- Apple keeps moving / abstracting the location of many of its API header files. This cost me far more time than it should have. 
- I'm unsatisfied with many of my function / data-type collection implementations, for example, my battery functions need more robust error handling. 
- Rust error handling in general is something that has been unexpectedly time-consuming and confusing to get the hang of as a beginnner
- I'd like to eventually refactor all of my functions to directly reference hardware API's etc. as is the case in my UUID function. 

## Issues you worked on

- https://github.com/utk-cs340-spring23/Watchtower/issues/19
- https://github.com/utk-cs340-spring23/Watchtower/issues/21
- https://github.com/utk-cs340-spring23/Watchtower/issues/22
- https://github.com/utk-cs340-spring23/Watchtower/issues/24
- https://github.com/utk-cs340-spring23/Watchtower/issues/20
- https://github.com/utk-cs340-spring23/Watchtower/issues/23 (incomplete)


## Files you worked on

- https://github.com/utk-cs340-spring23/Watchtower/blob/sprint2/watchtower-sensor/src/sys/darwin.rs
- https://github.com/utk-cs340-spring23/Watchtower/blob/sprint2/watchtower-sensor/build.rs
- https://github.com/utk-cs340-spring23/Watchtower/blob/sprint2/watchtower-sensor/src/error.rs
- https://github.com/utk-cs340-spring23/Watchtower/blob/sprint2/watchtower-sensor/src/sys/mod.rs
- https://github.com/utk-cs340-spring23/Watchtower/blob/sprint2/watchtower-sensor/Cargo.toml
- https://github.com/utk-cs340-spring23/Watchtower/blob/sprint2/watchtower-sensor/wrapper.h

## What you accomplished

- mac_OS sensor is now caught up to the other implementations, with the exception gpu statistics, which are complicated by the architecural changes with apples SOC chips. 
