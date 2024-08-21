battery_level.c is a short c program that demonstrates usage of apple's MacOS IOKit framework. The program fetches the current battery level percentage of the device and prints the result. This functionality is relevant to the MacOS client program for our hardware monitoring project. 
To compile (on MacOS) : 
gcc -o battery_level battery_level.c -framework IOKit -framework CoreFoundation
