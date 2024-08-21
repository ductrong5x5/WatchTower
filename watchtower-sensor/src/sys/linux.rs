use std::{fs::File, io::Read, path::Path, collections::HashMap, process::Command, ffi::{c_void, CStr, CString}};
use sysinfo::{CpuExt, System, SystemExt, MacAddr, NetworkExt};
// use std::{
//     collections::HashMap,
//     ffi::{c_void, CStr, CString},
//     mem::MaybeUninit,
//     str::FromStr,
// };

//use std::fs;
//use std::env;
//use substring::Substring;
use uuid::Uuid;
use crate::types::{
    gpu::{Gpu, GpuHello},
    net::{Interface, InterfaceType, Network, NetworkHello},
};

pub(crate) type OsError = rustix::io::Errno;

pub(crate) fn machine_id() -> crate::Result<Uuid> {
    let mut file = File::open("/etc/machine-id")?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;

    let digest = md5::compute(contents.trim());

    Ok(Uuid::from_bytes(*digest))
}

pub(crate) fn has_battery() -> crate::Result<bool> {
    let mut is_battery = false;
    if Path::new("/sys/class/power_supply/BAT0").exists() {
        is_battery = true;
    }
    Ok(is_battery as bool)
}

pub(crate) fn battery_percent() -> crate::Result<u8> {
    let percentage: u8;
    if Path::new("/sys/class/power_supply/BAT0").exists() {
        let mut file = File::open("/sys/class/power_supply/BAT0/capacity")?;
        let mut contents = String::new();

        file.read_to_string(&mut contents)?;

        percentage = contents.trim().parse().unwrap();
    } else {
        percentage = 100;
    }

    Ok(percentage as u8)
}

//may need to change the way the cpu percentage is gotten
pub(crate) fn cpu_usage_percent() -> crate::Result<u8> {
    let mut total: u32 = 0;
    let mut idle: u32;
    let mut percentage: u32 = 0;
    let mut file = File::open("/proc/stat")?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;

    for line in contents.lines() {
        let mut v: Vec<&str> = line.split(' ').collect();
        v[1] = "cpu";

        //get total
        for v in v.iter() {
            if v.contains("cpu") {
            } else {
                total = total + v.trim().parse::<u32>().unwrap();
            }
        }

        idle = v[5].parse().unwrap();
        idle = total - idle;
        percentage = total / idle;

        break;
    }
    Ok(percentage as u8)
}

pub(crate) fn installed_ram() -> crate::Result<u64> {
    let mut file = File::open("/proc/meminfo")?;
    let mut contents = String::new();
    let mut installed = 0;
    let mut iskb = false;

    file.read_to_string(&mut contents)?;
    //.expect("Unable to open file");

    for line in contents.lines() {
        if line.contains("MemTotal") {
            let v: Vec<&str> = line.split(' ').collect();

            for v in v.iter().rev() {
                if v.contains("kB") {
                    iskb = true;
                } else if iskb == true {
                    iskb = false;
                    installed = v.parse::<u64>().unwrap();
                }
            }
            break;
        }
    }

    Ok(installed * 1000 as u64)
}

pub(crate) fn cpu_name() -> crate::Result<String> {
    let mut file = File::open("/proc/cpuinfo")?;
    let mut contents = String::new();
    let mut name = "";
    let mut found = false;

    file.read_to_string(&mut contents)?;

    for line in contents.lines() {
        if line.contains("model name") {
            
            let mut v: Vec<&str> = line.split(' ').collect();
            for v in v.iter() {
                if found == true || v.contains(":") {
                    found = true;
                    //name = name + v + " ";
                    name = v
                }
                break;
            }
        }   
    }
    Ok(name.to_string())
}


pub(crate) fn cpu_clock_speed() -> crate::Result<u32> {
    let mut file = File::open("/sys/devices/system/cpu/cpu0/cpufreq.scaling_max_freq")?;
    let mut contents = String::new();
    let mut name = "";
    let mut speed = 0 as u32;

    file.read_to_string(&mut contents)?;

    for line in contents.lines() {
        name = line;
    }
    
    speed = name.parse::<u32>().unwrap();

    // let mut sys = System::new();
    // let mut count = 0;
    // let mut clock = 0;
    // sys.refresh_cpu();
    // for cpu in sys.cpus() {
    //     //clock = cpu.cpu_clock_speed();
    //     clock = cpu.get_cpu_frequency();
    //     count = count +1;
    // }
    //clock = clock / count;

    Ok(speed as u32)
}

pub(crate) fn cpu_current_clock_speed() -> crate::Result<u32> {
    let mut sys = System::new();
    let mut count = 0 as f32;
    let mut clock = 0 as f32;

    sys.refresh_cpu();
    for cpu in sys.cpus() {
        clock = cpu.cpu_usage();
        count = count +1.0;
    }

    clock = clock / count;

    Ok(clock as u32)
}

//gets average temp of all thermal zones
pub(crate) fn cpu_current_temperature() -> crate::Result<Option<f32>> {
    let mut file = File::open("/sys/class/thermal/thermal_zone*/temp")?;
    let mut contents = String::new();
    let mut counter = 0 as f32;
    let mut temp = 0 as f32;


    file.read_to_string(&mut contents)?;

    for line in contents.lines() {
        counter = counter + 1.0;
        temp = temp + line.parse::<f32>().unwrap();
    }

    temp = temp / counter;


    //returns as Celsius
    Ok(Some(temp /300 as f32))

}


pub(crate) fn ram_usage() -> crate::Result<u64> {
    let mut file = File::open("/proc/meminfo")?;
    let mut contents = String::new();
    let mut total = 0;
    let mut free = 0;
    let mut buff = 0;
    let mut cache = 0;
    let mut slab = 0;
    let mut iskb = false;

    file.read_to_string(&mut contents)?;
    //.expect("Unable to open file");

    for line in contents.lines() {
        if line.contains("MemTotal") {
            let v: Vec<&str> = line.split(' ').collect();

            //incase of unknown formatiing gets the slit right before kb
            for v in v.iter().rev() {
                if v.contains("kB") {
                    iskb = true;
                } else if iskb == true {
                    iskb = false;
                    total = v.parse::<u64>().unwrap();
                }
            }
        }

        if line.contains("MemFree") {
            let v: Vec<&str> = line.split(' ').collect();
            for v in v.iter().rev() {
                if v.contains("kB") {
                    iskb = true;
                } else if iskb == true {
                    iskb = false;
                    free = v.parse::<u64>().unwrap();
                }
            }
        }

        if line.contains("Buffers") {
            let v: Vec<&str> = line.split(' ').collect();
            for v in v.iter().rev() {
                if v.contains("kB") {
                    iskb = true;
                } else if iskb == true {
                    iskb = false;
                    buff = v.parse::<u64>().unwrap();
                }
            }
        }

        if line.contains("Cached: ") {
            if line.contains("SwapCached") == false {
                let v: Vec<&str> = line.split(' ').collect();
                for v in v.iter().rev() {
                    if v.contains("kB") {
                        iskb = true;
                    } else if iskb == true {
                        iskb = false;
                        cache = v.parse::<u64>().unwrap();
                    }
                }
            }
        }

        if line.contains("Slab") {
            let v: Vec<&str> = line.split(' ').collect();
            for v in v.iter().rev() {
                if v.contains("kB") {
                    iskb = true;
                } else if iskb == true {
                    iskb = false;
                    slab = v.parse::<u64>().unwrap();
                }
            }
        }
    }

    total = total - (free + buff + cache + slab);

    Ok(total as u64)
}


//unfinished for sprint 2
pub(crate) fn network_info() -> crate::Result<HashMap<String, Interface>> {
    // // Use GetAdaptersInfo
    // let mut out = NetworkHello {
    //     interfaces: HashMap::new(),
    // };
    let mut out = HashMap::new();

    let mut system = System::new_all();
    system.refresh_networks();

    for (interface_name, network_data) in system.networks() {
        let name = interface_name.to_string();

        let MacAddr(mac_address_bytes) = network_data.mac_address();
        let mac_address = format!(
            "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}",
            mac_address_bytes[0],
            mac_address_bytes[1],
            mac_address_bytes[2],
            mac_address_bytes[3],
            mac_address_bytes[4],
            mac_address_bytes[5]
        );

        let r#type = InterfaceType::WiFi; //will implement diff types at a later time
        let description = name.clone();




            let mut ip_addresses: Vec<String> = Vec::new();
            ip_addresses.push("127.0.0.1".to_string());


            let mut file = File::open("/proc/net/dev")?;
            let mut contents = String::new();
            let mut out = Network {
                interfaces: HashMap::new(),
            };
            let mut firstRx: u64 = 0;
            let mut secondRx: u64 = 0;
            let mut firstTx: u64 = 0;
            let mut secondTx: u64 = 0;
        
            file.read_to_string(&mut contents)?;
                //.expect("Unable to open file");
        
            //get the change in bytes over 1 second to get the network transmission at the current time
            for line in contents.lines() {
                //2nd column is recieved bytes, 10th column is transmitted bytes
                if line.contains("wlp5s0") {
                    println!("{line}");
                    let v: Vec<&str> = line.split(' ').collect();
        
                    let mut count = 1;
                    for v in v.iter() {
                        if count == 2 {
                            firstRx = v.parse::<u64>().unwrap();
                        }
                        if count == 10 {
                            firstTx  = v.parse::<u64>().unwrap();
                        }
                        count += 1;
                    }
                    break;
                }
            }
        
            let duration = std::time::Duration::from_secs(1);
            std::thread::sleep(duration);
        
            file.read_to_string(&mut contents)?;
                //.expect("Unable to open file");
        
                for line in contents.lines() {
                    //2nd column is recieved bytes, 10th column is transmitted bytes
                    if line.contains("wlp5s0") {
                        println!("{line}");
                        let v: Vec<&str> = line.split(' ').collect();
            
                        let mut count = 1;
                        for v in v.iter() {
                            if count == 2 {
                                secondRx = v.parse::<u64>().unwrap();
                            }
                            if count == 10 {
                                secondTx  = v.parse::<u64>().unwrap();
                            }
                            count += 1;
                        }
                        break;
                    }
                }
        
        
                    let rx = firstRx - secondRx;
                    let tx = firstTx - secondTx;







            out.insert(
                mac_address,
                Interface {
                    name,
                    description,
                    r#type,
                    ip_addresses,
                    rx,
                    tx,
                },
            );

    }    

    Ok(out)
}


// pub(crate) fn network_statistics() -> crate::Result<Network> {
//     //turns out what is stored in the file is total data sent and recieved
//     let mut file = File::open("/proc/net/dev")?;
//     let mut contents = String::new();
//     let mut out = Network {
//         interfaces: HashMap::new(),
//     };
//     let mut firstRx: u64 = 0;
//     let mut secondRx: u64 = 0;
//     let mut firstTx: u64 = 0;
//     let mut secondTx: u64 = 0;

//     file.read_to_string(&mut contents)?;
//         //.expect("Unable to open file");

//     //get the change in bytes over 1 second to get the network transmission at the current time

//     for line in contents.lines() {
//         //2nd column is recieved bytes, 10th column is transmitted bytes
//         if line.contains("wlp5s0") {
//             println!("{line}");
//             let v: Vec<&str> = line.split(' ').collect();

//             let mut count = 1;
//             for v in v.iter() {
//                 if count == 2 {
//                     firstRx = v.parse::<u64>().unwrap();
//                 }
//                 if count == 10 {
//                     firstTx  = v.parse::<u64>().unwrap();
//                 }
//                 count += 1;
//             }
//             break;
//         }
//     }

//     let duration = std::time::Duration::from_secs(1);
//     std::thread::sleep(duration);


//     file.read_to_string(&mut contents)?;
//         //.expect("Unable to open file");

//         for line in contents.lines() {
//             //2nd column is recieved bytes, 10th column is transmitted bytes
//             if line.contains("wlp5s0") {
//                 println!("{line}");
//                 let v: Vec<&str> = line.split(' ').collect();
    
//                 let mut count = 1;
//                 for v in v.iter() {
//                     if count == 2 {
//                         secondRx = v.parse::<u64>().unwrap();
//                     }
//                     if count == 10 {
//                         secondTx  = v.parse::<u64>().unwrap();
//                     }
//                     count += 1;
//                 }
//                 break;
//             }
//         }

//             //need to get the mac address for next sprint
//              let mac_address = format!(
//                 "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}",
//                 12, 22, 32, 42, 52, 62
//             );

//             let rx = firstRx - secondRx;
//             let tx = firstTx - secondTx;

//             out.interfaces
//                 .insert(mac_address, InterfaceStatistics { rx, tx });
   

//     Ok(out)

// }

pub(crate) fn gpu_info() -> crate::Result<GpuHello> {
    let output = Command::new("glxinfo")
                           .arg("-B")
                            .output()
                            .expect("glxinfo command failed");
    let info = output.stdout;
    let mut card = " ";
    let mut ismb = false;
    let mut total;
    let mut available;

    //println!("info[0]");
    for line in info.lines() {
        if line.contains("OpenGl render string") {
            let v: Vec<&str> = line.split(' ').collect();


            //card = v[3] + " " + v[4] + " " + v[5];
        }
     
        if line.contains("Total avalible memory:") {
            let v: Vec<&str> = line.split(' ').collect();

            for v in v.iter().rev() {
                if v.contains("MB") {
                    ismb = true;
                } else if ismb == true {
                    ismb = false;
                    total = v.parse::<u64>().unwrap();
                }
            }

        }

        if line.contains("currently available ") {
            let v: Vec<&str> = line.split(' ').collect();

            for v in v.iter().rev() {
                if v.contains("MB") {
                    ismb = true;
                } else if ismb == true {
                    ismb = false;
                    available = v.parse::<u64>().unwrap();
                }
            }

        }

    }


    let name = card.to_string();
    let installed_vram = total;

        return Ok(GpuHello { name, installed_vram});

    //need to add a conditional to detect gpu


    Err(crate::Error::NoGpuFound)

}

pub(crate) fn gpu_statistics() -> crate::Result<Gpu> {
    //run glxinfo, get 1- (current avalible / total vram)


    let output = Command::new("glxinfo")
                           .arg("-B")
                            .output()
                            .expect("glxinfo command failed");
    let info = output.stdout;
    let mut ismb = false;
    let mut total;
    let mut available;

    //println!("info[0]");
    for line in info.lines() {
        
     
        if line.contains("Total avalible memory:") {
            let v: Vec<&str> = line.split(' ').collect();

            for v in v.iter().rev() {
                if v.contains("MB") {
                    ismb = true;
                } else if ismb == true {
                    ismb = false;
                    total = v.parse::<u64>().unwrap();
                }
            }

        }

        if line.contains("currently available ") {
            let v: Vec<&str> = line.split(' ').collect();

            for v in v.iter().rev() {
                if v.contains("MB") {
                    ismb = true;
                } else if ismb == true {
                    ismb = false;
                    available = v.parse::<u64>().unwrap();
                }
            }

        }

    }

  
    let usage = available / total;



        Ok(Gpu {
            current_vram_usage: usage as u64,
        })

}

#[cfg(test)]
mod tests {
    use super::*;

    // MACHINE_ID
    #[test]
    fn test_machine_id() {
        let id = machine_id().unwrap();
        println!("(Linux) MACHINE_ID [UUID]: {}", id);
    }

    // HAS_BATTERY
    #[test]
    fn test_has_battery() {
        let has_battery = has_battery().unwrap();
        println!("\n(Linux) HAS_BATTERY: {}", has_battery);
    }

    // BATTERY_PERCENT
    #[test]
    fn test_battery_percent() {
        let battery_percent = battery_percent().unwrap();
        println!("\n(Linux) BATTERY_PERCENT [%]: {}", battery_percent);
    }

    // CPU_USAGE_PERCENT
    #[test]
    fn test_cpu_usage_percent() {
        let cpu_usage_percent = cpu_usage_percent().unwrap();
        println!("\n(Linux) CPU_USAGE_PERCENT [%]: {}", cpu_usage_percent);
    }
    
    // CPU_NAME
    #[test]
    fn test_cpu_name() {
        let cpu_name = cpu_name().unwrap();
        println!("\n(Linux) CPU_NAME: {}", cpu_name);
    }

    // CPU_CLOCK_SPEED
    #[test]
    fn test_cpu_clock_speed() {
        let cpu_clock_speed = cpu_clock_speed().unwrap();
        println!("\n(Linux) CPU_CLOCK_SPEED [MHz]: {}", cpu_clock_speed);
    }

    // CPU_CURRENT_CLOCK_SPEED
    #[test]
    fn test_cpu_current_clock_speed() {
        let cpu_current_clock_speed = cpu_current_clock_speed().unwrap();
        println!(
            "\n(Linux) CPU_CURRENT_CLOCK_SPEED [MHz]: {}",
            cpu_current_clock_speed
        );
    }

    // CPU_CURRENT_TEMPERATURE
    #[test]
    fn test_cpu_current_temperature() {
        let cpu_current_temperature = cpu_current_temperature().unwrap().unwrap();
        println!("\n(Linux) CPU_CURRENT_TEMPERATURE [C]: {}", cpu_current_temperature);
    }

    /*  INSTALLED_RAM
    #[test]
    fn test_installed_ram() {
        let installed_ram = installed_ram().unwrap();
        println!("\n(darwin) INSTALLED_RAM [bytes]: {}", installed_ram);
    }
    */

    // RAM_USAGE
    #[test]
    fn test_ram_usage() {
        let ram_usage = ram_usage().unwrap();
        println!(
            "\n(Linux) RAM_USAGE [bytes]: {}   [MB]: {} ;   [GB]: {}",
            ram_usage,
            ram_usage / 1024 / 1024,
            ram_usage / 1024 / 1024 / 1024
        );
        let installed_ram = installed_ram().unwrap();
        let ram_usage_percent = (ram_usage as f64 / installed_ram as f64) * 100.0;
        println!("(Linux) RAM_USAGE [%]: {}", ram_usage_percent);
    }

    // NETWORK_INFO
    #[test]
    fn test_network_info() {
        let network_info = network_info().unwrap();
        println!("\n(Linux) NETWORK_INFO: {:#?}", network_info);
    }
    // test for gpu_info

    // GPU_INFO
    #[test]
    fn test_gpu_info() {
        let gpu_info = gpu_info().unwrap();
        println!("\n(Linux) GPU_INFO: {:#?}", gpu_info);
    } 
    
    // GPU_STATISTICS
    #[test]
    fn test_gpu_statistics() {
        let gpu_statistics = gpu_statistics().unwrap();
        println!("\n(Linux) GPU_STATISTICS: {:#?}", gpu_statistics);
    }

}
