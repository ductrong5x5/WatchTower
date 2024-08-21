/* Jacob Curlin, Assignment 4: Hello Plus */
/* Fetch/print device battery level on MacOS using IOKit framework */

#include <stdio.h>
#include <IOKit/ps/IOPSKeys.h>
#include <IOKit/ps/IOPowerSources.h>

int main() {
    CFTypeRef info = IOPSCopyPowerSourcesInfo();
    CFArrayRef list = IOPSCopyPowerSourcesList(info);

    CFDictionaryRef battery = IOPSGetPowerSourceDescription(info, CFArrayGetValueAtIndex(list, 0));

    int level = 0;
    CFNumberRef level_val = CFDictionaryGetValue(battery, CFSTR(kIOPSCurrentCapacityKey));
    CFNumberGetValue(level_val, kCFNumberSInt32Type, &level);

    printf("Battery level: %d%%\n", level);
    return 0;
}
