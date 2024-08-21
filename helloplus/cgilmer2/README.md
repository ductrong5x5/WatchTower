# watchtower-sensor

This program gathers a unique system ID (from the `HKLM:\SOFTWARE\Microsoft\Cryptography\MachineGuid` registry key on Windows, `/etc/machine-id` on Linux),  
and retrieves the current time and date.  

The gathered data is serialized to a pretty JSON string and printed to stdout.

Code from this will be used as the basis for our sensor component.

## How to run

- Ensure some sort of C++ compiler toolchain is installed.
- Follow the instructions at https://www.rust-lang.org/tools/install.
- Run `cargo run` within this directory.  
