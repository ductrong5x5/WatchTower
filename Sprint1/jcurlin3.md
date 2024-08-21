#  **Sprint 1 Reflection**

## ***What you planned to do***
	
I’m currently responsibe for the Darwin implementation of the client-side sensor component, which currently collects the UUID, battery info, CPU info, and memory info on MacOS devices for our hardware-monitor server system. I planned on fully implementing this for Sprint 1. 

For the pre-project assignment in which we were tasked with using a piece of the tech-stack planned for our projects,
I used apple’s IOKIT Framework to pull a system UUID from a MacOS devices IO Registry. 
I implemented this in C, and while the framework and its documentation appeared overwhelming at first, 
I was able to get a working prototype with only a few lines of code and help from resources such as
stack-overflow and a few blogs. This in-turn lead me to underestimate the difficulty of replicating similar 
functionality in Rust. Here are the knowledge/skill dependencies that, in retrospective, were learned and utilized later on.  

- Rust 
- Rust Cargo 
- Rust Bindgen Crate 
- Rust FFI Interface, 
- Rust libC crate 
- MacOS core_foundation framework 
- MacOS IOKit framework 
- sysctl 
 

## ***What you did not do***

- Commit code. 

## ***What problems you encountered***

- I overestimated my ability to pick up rust and immedately begin producing. Prior to this course,
    I had not used any languages besides C and C++, with some high school java. I hadn't worked on a project 
    larger than a main file and a single header, let alone kernel driver API's. 
- I failed to recognize and accept the fact that I wasn't going to be able to achieve the robust level of 
    code I was aiming for in my first go-around. I should have accepted this much earlier and refocused on 
    simply getting something that compiled, regardless of how many external libraries etc. I had to use. 

## ***Issues you worked on***

- mac_OS / 'darwin' implementation of our hardware sensor

## ***Files you worked on***

- my notes below

## ***What you accomplished***

- I made significant progress in Rust knowledge / abilities. 

       

### Some of My Notes 

CURLIN - Working Notes

-- RESOURCES -- 

Accessing macOS System Information : (source) https://wiki.freepascal.org/Accessing_macOS_System_Information


-- MACHINE PORTS -- : (source) https://docs.darlinghq.org/internals/macos-specifics/mach-ports.html

port                : conceptually, a message queue similar to a Unix pipe; a kernel-control communication channel.
port right          : a handle to a port that allows sending (enqueuing) or receiving (dequeuing) messages
                        similar to how a file descriptor connects to the read or write end of a pipe.
    receive right   : allows for receiving of messages sent to the port.
    send right      : allows for sending messages to the port.
    send-one right  : allows for sending a single message to the port before disappearing.
    port set right  : denotes a 'port set' rather than a single port. Dequeuing a message from a port set dequeues a
                        message from one of the ports that it contains. Port sets can be used to listen on several ports
                        simultaneously. 
port right name     : a specific integer value that a task uses to refer to a port right that it holds, similar to how
                        a file descriptor is used by a process to refer to an open file.

task port           : a send right to a port whose receive right is held by the kernel. allows for the manipulation
                        of the task it refers to, including reading and writing memory, manipulation threads, killing task.
host port           : a send right to another port whose receive right is held by the kernel. allows for the retreival
                        of information about the kernel and the host machine, such as the OS version, number of processors,
                        memory usage statistics, etc.
task name port      : an apple extension, an unprivileged version of the task port. references the task, but does not 
                        permit control of it. 
bootstrap port      : a send right to the 'bootstrap server' (launchd on darwin). the 'bootstrap server' serves as a
                        'server registry', allowing other servers to export their ports under well known reverse-DNS 
                        names (i.e. 'com.apple.system.something'), and for the look-up of ports by such names.


-- PROCEDURE --     : (source) https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/MakingHWAccessible/MakingHWAccessible.html#//apple_ref/doc/uid/TP30000698

1. Get the I/O Kit Master Port.
    kernResult = IOMasterPort(MACH_PORT_NULL, &masterPort);
2. Obtain a matching dictionary for the specified device/driver class.
    driver_class = IOServiceMatching( *IOKitClassName* );
3. Locate an instance of the driver by iterating through the list of current driver instances.
    kernResult = IOServiceGetMatchingServices(masterPort, *driver class*, &iterator);
    if (driver_iter != KERN_SUCCESS)
    {
        printf("IOServiceGetMatchingServices returned %d\n\n", kernResult);
        return 0;
    }
    serviceObject = IOIteratorNext(iterator);
    IOObjectRelease(iterator);
4. Create a connection to this driver instance (the user-client object on the other side of the connection).


-> CORE FOUNDATION <- 

-- Crates

core-foundation         : high-level/idiomatic Rust API for CF, provides types and functions
core-foundation-sys     : low-level Rust API for CF, provides bindings generated from sys headers and rust-safe wrappers for common functions

-- Types / Structs

CFRange             : a structure representing a range of sequential items in a container such as characters in a buffer or elements in a collection
    pub struct CFRange { location (CFIndex of starting index) , length (CFIndex of number of values in range) }

-- Functions / Bindings

CFStringGetBytes    : fetches a range of characters from a string into a byte buffer after converting the characters to a specific encoding
    pub unsafe extern fn CFStringGetBytes 
    ( 
        *string*,                       (CFStringRef: reference to CFString to be read into Rust String)
        *range*,                        (CFRange: range of values)
        *encoding*,                     (CFStringEncoding: string encoding type (kCFStringEncodingUTF8 for UTF encoding))
        *lossbyte*,                     (UInt8 (single byte used to replace any illegal or malformed bytes in the input string when converting to encoding)) 
        *isexternalrepresentation*,     (Boolean (false: input string is assumed to be in the native representation for specified encoding)
        *buffer*,                       (*mut UInt8: pointer to buffer used to store result of the string encoding operation)
        *maxbuflength*,                 (CFIndex: maximum number of bytes that can be written to the 'buffer' specified)
        *usedbuflength*                 (CFIndex: current number of bytes written/used in the 'buffer' specified)
    ) -> CFIndex                        (CFIndex: (return value) number of bytes written to buffer)



!! IOMasterPort depricated on macOS 12.0+, use IOMainPort
    (source) https://github.com/shirou/gopsutil/pull/1191/commits/4c3edcfe56bb265ffc9ce117dc7cfc760a0b5e36#diff-b8d4a8f58b8cca182bfcb491b81b70f4c1d284a22a044ffb88549f00d5be0ff8



https://zameermanji.com/blog/2021/7/13/using-bindgen-with-system-frameworks-on-macos/

https://github.com/betwixt-labs/bebop/issues/220

Crates & Modules:
- Crate: synonymous with ‘library’ or ‘package’ in other languages
- Cargo is Rust’s crate (‘library’) management tool
- Crates can produce executables or libraries, depending on the project
- Each crate has an implicit ‘root module’ that contains the code for the crate
- Sub-modules can be defined in a tree under the root module, allowing code to be partitioned within the crate itself

Defining Modules:
- Modules can be defined with the mod keyword

Example of module definition within arc/lib.rs:

mod module_1
{
	mod submodule_1 {…}
	mod submodule_2 {…}
}

Mod module_2
{
	……..
}

// note — since this crate doesn’t have a main() function and is called lib.rs, cargo will automatically build it as a library

Crates:

libc

Features: 

std: std library (enabled by default)
extra_traits: derives debug, eq, hash, and partialeq
const-external-fn: changes some external functions into const external fn ‘s 

bindgen:

- bindgen automatically generates Rust FFI bindings to C and C++ libraries
- 





Build Scripts:

- Placing a file named ‘build.rs’ in the root of a package will cause Cargo to compile that script and execute it just before building the package
- Example use cases: building bundled c libraries, finding c libraries on host system, generating rust module from spec, performing platform-specific configuration needed for the crate

https://zameermanji.com/blog/2021/7/13/using-bindgen-with-system-frameworks-on-macos/

https://github.com/betwixt-labs/bebop/issues/22