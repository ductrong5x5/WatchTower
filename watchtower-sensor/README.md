# watchtower-sensor

This program collects various bits of system information:

- Battery
    - Is a battery installed?
    - Battery percentage
- CPU
    - Name
    - Core count
    - Thread count
    - Max clock speed
    - Current clock speed
    - Load percent
    - Temperature (not implemented on Windows)
- Disks (for each)
    - Name
    - Type (SSD, HDD, other)
    - Is this disk removable?
    - Capacity
    - Usage
- GPU
    - Name
    - Installed VRAM
    - Max frequency (not implemented on Windows)
    - Current VRAM usage
    - Current frequency (not implemented on Windows)
    - Current temperature (not implemented on Windows)
- Network interfaces (for each)
    - Name
    - Description
    - MAC address
    - Type (Loopback, Wifi, Ethernet, Other)
    - IP addresses
    - Recieved bytes
    - Transmitted bytes
- RAM
    - Installed amount
    - Current usage

Collected information is serialized to JSON and sent over HTTP POST request to
a configured backend. 

# How to...
## ...compile the sensor

- Ensure some sort of C++ compiler toolchain is installed.
- Follow the instructions at https://www.rust-lang.org/tools/install.
- Run `cargo build --release` within this directory.  

## ...run the sensor

- Compile following the instructions above.
- On Linux, install the mesa-utils package.
- Run `cargo run --bin sensor -- --hostname <backend URL> --checkin_interval <checkin time in seconds>` within this directory.

## ...compile the Windows installer

- Compile the sensor following the instructions above.
- Install Inno Setup.
- Open `watchtower-sensor/installer/windows/sensor.iss` in Inno Setup Compiler.
- Press the Compile button (Ctrl+F9).
- The compiled installer will be in `watchtower-sensor/installer/windows/Output`.

## ..install on Windows

- Download the [compiled sensor installer](https://cdn.discordapp.com/attachments/1072668307460735046/1105160819978813440/WatchtowerSensorInstall.exe).
- Run the installer executable.
- Click next, then a Notepad window will pop up.
- Adjust checkin interval (in seconds) as needed, change backend URL to match your backend.
- Click next, and leave the checkbox for running the sensor executable checked.
- The sensor is now persistently installed.
