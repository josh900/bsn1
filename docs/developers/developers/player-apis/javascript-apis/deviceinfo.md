# deviceinfo

The *deviceinfo* object lets you identify device hardware, firmware, and features.

**deviceinfo IDL**

```
interface DeviceInfo {
    attribute String model;
    attribute String osVersion;
    attribute String bootVersion;
    attribute String serialNumber;
    attribute String family;
    
    int osVersionCompare(String version);
    int bootVersionCompare(String bootVersion);
    bool osVersionIsAtLeast(String version);
    bool bootVersionIsAtLeast(String bootVersion);
    bool hasFeature(String feature);
    Promise <String> getLoadStatistics(String item);
    Promise <TemperatureLocation> getTemperature();
    Promise <UsbTopologyInterface> getUsbTopology();
};

dictionary TemperatureLocation {
    float celsius;
};

interface UsbTopologyInterface {
    attribute String vid;
    attribute String pid;
    attribute String raw;
    attribute String fid;
    [optional] attribute String category;
    [optional] attribute String ident;
    attribute Array<UsbTopologyInterface> children;
};

```

## Object Creation

To create a *deviceinfo* object, load the `@brightsign/deviceinfo` module using the `require()` method. 

```
diClass = require("@brightsign/deviceinfo");
di = new diClass(); 

```

## DeviceInfo

##### getLoadStatistics()

```
Promise <String> getLoadStatistics(String item)
```

Provides current performance information related to the Linux kernel. The `item` can be any of the following:

*   `loadavg`: Provides information about system performance. The first three columns measure CPU and I/O utilization over the past 1, 5, and 10 minutes, respectively. The fourth column displays the number of currently running processes and the total number of processes. The last column displays the ID of the most recently used process.
    
*   `meminfo`: Displays physical and swap memory usage
    
*   `slabinfo`: Provides information about memory usage at the slab level
    
*   `stat`: Provides overall statistics about the system (for example, the number of page faults since the system booted)
    
*   `vmstat`: Displays detailed virtual memory statistics from the kernel
    
*   `zoneinfo`: Provides overall statistics about the system, broken down by system Node
    
*   `interrupts`: Displays which interrupts are in use and how many of each type there have been
    
*   `version`: Provides the kernel version
    

##### getTemperature()

```
<TemperatureLocation> getTemperature()
```

Returns:

*   `key` string:  A dynamic string location key
    
*   `value` float: The device temperature as a floating point value
    

##### getUsbTopology()

```
<UsbTopologyInterface> getUsbTopology()
```

Gets the USB topology of the player.

These attributes return information about the BrightSign player:

*   `model` string: Returns the model name for the BrightSign device running the script, as a string (for example, "HD1020" or "XD230").
    
*   `osVersion` string: Returns the OS version number for the BrightSign device running the script.
    
*   `bootVersion` string: Returns the version number of the BrightSign boot firmware, also known as "safe mode", as a string (for example, "1.0.4").
    
*   `serialNumber` string: Returns the device serial number which, if not an empty string, is unique to the unit running the script.
    
*   `family` string: Returns a single string that indicates the family to which the device belongs. A device family is a set of models that are all capable of running the same firmware.
    

##### osVersionCompare()

```
int osVersionCompare(String version)
```

This function returns an integer greater than zero if the current OS version is greater than the parameter, 0 if it is exactly equal, or less than zero if lesser. For example:

```
if (di.osVersionCompare("8.2") > 0) { console.log("Firmware version is greater than 8.2") }
```

or:

```
if (di.osVersionCompare("8.4") < 0) { console.log("Firmware version is less than 8.4") }
```

##### bootVersionCompare()

```
int bootVersionCompare(String bootVersion)
```

This function returns an integer greater than zero if the current boot loader version is greater than the parameter, 0 if it is exactly equal, or less than zero if lesser (see the examples for `osVersionCompare()`). 

##### osVersionIsAtLeast()

```
bool osVersionIsAtLeast(String version)
```

Returns `True` if the BrightSign OS version on the device is greater than or equal to the version number represented by the passed string (for example, "4.0.13").

##### bootVersionIsAtLeast()

```
bool bootVersionIsAtLeast(String bootVersion)
```

Returns `True` if the BrightSign boot OS version on the device is greater than or equal to the version number represented by the passed string (for example, "4.4.22").

##### hasFeature()

```
bool hasFeature(String feature)
```

Returns `True` if the player feature in the passed string (which is passed as a case-insensitive string parameter) is present on the current device and firmware. The possible features that can be queried from the script are listed below:

> [!CAUTION]
> **Important**
> If you pass a parameter other than one of those listed below, it may return False even if the feature is available on the hardware and firmware.

`"5v serial"`: A 5V serial port

`"audio1"`: The first audio output

`"audio2"`: A second audio output

`"audio3"`: A third audio output

`"brightscript1"`: BrightScript Version 1

`"brightscript2"`: BrightScript Version 2

`"component video"`: A component video output

`"ethernet"`: An Ethernet interface

`"gpio connector"`: A DA15 or Pheonix-style GPIO port 

`"hdmi"`: An HDMI**®** output

`"hdmi input"`: An HDMI input

`"hevc_decode"`: An H.265 video decoder

`"media_decryption"`: The ability to decrypt AES-encrypted media, including video, image, and audio files.

`"nand storage"`: NAND storage for the boot loader and firmware

`"networking"`: Any form of networking capability. A False return may indicate that no network is currently available.

`"reset button"`: A reset button

`"registry"`: On-board persistent storage

`"rtc"`: A real-time clock (RTC)

`"sd"`: SD- or SDHC-compatible storage

`"sdhc"`: SDHC-compatible storage only

`"serial port 0"`: The first serial port

`"serial port 1"`: A second serial port

`"serial port 2"`: A third serial port

`"svc button"`: A service ("SVC") button. Passing the legacy term `"gpio12 button"` will yield the same result.

`"usb"`: One or more USB interfaces

`"vga"`: A VGA output

`"video_encoder"`: A video encoder/transcoder

## TemperatureLocation

*   `celsius` float: Returns the temperature of the device in celsius, as a floating point number.
    

## UsbTopologyInterface

These attributes return the USB topology of the player, which can be used to determine whether certain USB devices are connected to certain ports. 

*   `vid` string:  Four character strings encoding the Vendor ID and Product ID in hexadecimal.  Leading zeros are present and alpha characters are lower case (for example, vid = "0b95").
    
*   `pid` string: Four character strings encoding the Vendor ID and Product ID in hexadecimal.  Leading zeros are present and alpha characters are lower case (for example, pid = "0b95").
    
*   `raw` string:  This is an internal (Linux) USB device node ID.
    
*   `fid` string:Ports that have USB devices connected to them will include a `fid` (friendly ID) value, which can be used to determine which physical port the USB device is connected to on the player. See [roDeviceInfo](https://docs.brightsign.biz/display/DOC/roDeviceInfo) for more information. 
    
*   `category`  string optional: This optional string describes the device type (for example, "HUB", "SERIAL", "NET", "HID", "AUDIO", or "OTHER").
    
*   `ident` string optional: This is an additional identifier. For devices of category "NET", the `ident` is the system network interface name (for example, "usb0").
    
*   `children` Array<<UsbTopologyInterface> optional: Children are present for devices of category "HUB". Child devices have the same structure, so nested hubs will produce nested child data.
    

## Example

This example returns the USB topology for the device:

```
diClass = require("@brightsign/deviceinfo");
di = new diClass();
 
usbTopology = await di.getUsbTopology();
 
parseTopology = function(usbT) {
  for(i in usbT) {
    let device = usbT[i];
    if (device.category === "HUB")
        parseTopology(device.children);   
    if (device.category === "NET")
        console.log("Found " + device.fid + " interface " + device.ident);
  }
};
 
parseTopology(usbTopology);
```

To replace BSDeviceInfo with the *deviceinfo* object:

```
if (typeof(BSDeviceInfo) === typeof undefined) 
{
  global.BSDeviceInfo = class BSDeviceInfo {
    constructor() {
      let fs = require('fs');
      let DeviceInfoClass = require('@brightsign/deviceinfo');
      let deviceInfo = new DeviceInfoClass();

      // Map properties and getters
      this.model = deviceInfo.model;
      this.version = deviceInfo.osVersion;
      this.bootVersion = deviceInfo.bootVersion;
      this.deviceUniqueId = deviceInfo.serialNumber;
      this.family = deviceInfo.family;
      Object.defineProperty(this, 'deviceUptime', {
          get: Object.getOwnPropertyDescriptor(deviceInfo, 'deviceUptime').get,
          enumerable: true,
      });
      // And methods
      this.VersionCompare = deviceInfo.osVersionCompare;
      this.BootVersionCompare = deviceInfo.bootVersionCompare;
      this.FirmwareIsAtLeast = deviceInfo.osVersionIsAtLeast;
      this.BootFirmwareIsAtLeast = deviceInfo.bootVersionIsAtLeast;
      this.HasFeature = deviceInfo.hasFeature;
      this.GetLoadStatistics = function(s) {
        let stats = new Set([ 'zoneinfo', 'loadavg', 'meminfo', 'stat', 'vmstat', 'interrupts', 'version', 'boardid' ]);
        var result  = 'n/a';
        if (stats.has(s)) {
          result = fs.readFileSync('/proc/' + s).toString();
        }
        return result;
      };
      // GetTemperature and GetUsbTopology are not present in the BSDeviceInfo class
    };
  };
}
```