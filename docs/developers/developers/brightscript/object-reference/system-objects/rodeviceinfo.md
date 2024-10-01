# roDeviceInfo

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This object provides information about the device hardware, firmware, and features. The JavaScript equivalent is [deviceinfo](../../../../developers/player-apis/javascript-apis/deviceinfo.md) .

## ifDeviceInfo

##### GetModel() As String

Returns the model name for the BrightSign device running the script as a string (for example, "HD1020" or "XD230").

##### GetVersion() As String

Returns the version number of BrightSign firmware running on the device (for example, "4.0.13").

##### GetVersionNumber() As Integer

Returns the three most significant version numbers of the BrightSign firmware running on the device in comparable numeric form: `major*65536 + minor*256 + build`

> [!CAUTION]
> **Important**
> The return value for the `GetVersionNumber()` method does not include any additional version numbers after the first three: For example, firmware version 4.0.13.4 will be returned as 262157 (as if it were "4.0.13"). For this reason, we recommend using the `GetVersion()` or `FirmwareIsAtLeast()` methods to determine the current firmware version.

##### FirmwareIsAtLeast(version As String) As Boolean

Returns True if the BrightSign firmware version on the device is greater than or equal to the version number represented by the passed string (e.g. "4.0.13").

##### GetBootVersion() As String

Returns the version number of the BrightSign boot firmware, also known as "safe mode", as a string (for example, "1.0.4").

##### GetBootVersionNumber() As Integer

Returns the three most significant version numbers of the BrightSign boot firmware, also known as "safe mode," in comparable numeric form: `major*65536 + minor*256 + build.`

> [!CAUTION]
> **Important**
> The return value for the `GetBootVersionNumber()` method does not include any additional version numbers after the first three: For example, firmware version 1.0.4.1 will be returned as 65540 (as if it were "1.0.4"). For this reason, we recommend using the `GetBootVersion()` or `BootFirmwareIsAtLeast()` methods to determine the current boot firmware version.

##### BootFirmwareIsAtLeast(version As String) As Boolean

Returns True if the BrightSign boot firmware version on the device is greater than or equal to the version number represented by the passed string (e.g. "4.4.22").

##### GetTemperature() As roAssociativeArray

Returns an associative array containing a dynamic string location key and the temperature as a floating point value.

##### GetDeviceUptime() As Integer

Returns the number of seconds that the device has been running since the last power cycle or reboot.

##### GetDeviceLifetime() As Integer

##### GetLoadStatistics(parameters As roAssociativeArray) As String

Provides current performance information related to the Linux kernel. This method accepts an associative array with a single key/value pair formatted as `item:<parameter>`; it will then return a string containing information associated with that parameter. The following are recognized parameters:

*   "loadavg": Provides information about system performance. The first three columns measure CPU and I/O utilization over the past 1, 5, and 10 minutes, respectively. The fourth column displays the number of currently running processes and the total number of processes. The last column displays the ID of the most recently used process.
    
*   "meminfo": Displays physical and swap memory usage.
    
*   "slabinfo": Provides information about memory usage at the slab level.
    
*   "stat": Provides overall statistics about the system (e.g. the number of page faults since the system booted).
    
*   "vmstat": Displays detailed virtual memory statistics from the kernel.
    
*   "zoneinfo": Provides overall statistics about the system, broken down by system Node.
    
*   "interrupts": Displays which interrupts are in use and how many of each type there have been.
    
*   "version": Provides the kernel version.
    

Example:

```
stat = CreateObject("roDeviceInfo")
print stat.GetLoadStatistics({item:"interrupts"})
```

##### GetUSBTopology(return As roAssociativeArray) As Dynamic 

Returns the USB topology of the player, including the port enumeration, PID, and VID of each USB device. Use this method to determine whether certain USB devices are connected to certain ports. The passed associative array determines the return value:

*   `{}`: Returns the USB topology as a string list.
    
*   `{format: "xml"}`:  If `true`, returns the USB topology as an XML-formatted string.
    
*   `{format: "array"}`:  Returns an array of associative arrays. Each associative array contains information about a single USB port.
    
*   `rebuild`:  If `true`, ensures that the returned information is up to date with the current hardware status.
    

Updates information and returns it in XML format:

```
di = CreateObject("roDeviceInfo")
tp = di.GetUSBTopology({format: "xml", rebuild:true})
```

String list:

```
BrightScript Debugger> di = CreateObject("roDeviceInfo")
BrightScript Debugger> topo = di.GetUSBTopology({})
BrightScript Debugger> print topo
{
 "containers": [
  {
   "category": "HUB",
   "fid": "",
   "pid": 1552,
   "raw": "1-1",
   "type": "",
   "vid": 1507
  }
 ],
 "devices": [
  {
   "category": "HID",
   "fid": "B.0",
   "ident": "usb/hiddev0",
   "pid": 60931,
   "raw": "1-1.2:1.0",
   "type": "BP900",
   "vid": 2127
  }
...
```

XML string:

```
BrightScript Debugger> di = CreateObject("roDeviceInfo")
BrightScript Debugger> topo = di.GetUSBTopology({xml: true})
BrightScript Debugger> print topo
<topology>
	<device>
  		<raw>8-1:1.0</raw>
  		<fid>C.0</fid>
  		<category>HID</category>
  		<vid>084f</vid>
  		<pid>ee03</pid>
		<ident>usb/hiddev0</ident>
  		<type>BP900</type>
	</device>
	<devices raw="2-1.4" category="HUB" vid="05e3" pid="0610" >
   		<device>
    		<raw>2-1.4.1:1.0</raw>
    		<fid>A/4.0</fid>
    		<category>AUDIO</category>
    		<vid>05a7</vid>
    		<pid>40fa</pid>
   		</device>
   		<device>
    		<raw>2-1.4.1:1.2</raw>
    		<fid>A/4.2</fid>
    		<category>HID</category>
    		<vid>05a7</vid>
    		<pid>40fa</pid>
  		</device>
...
```

Array:

```
BrightScript Debugger> di = CreateObject("roDeviceInfo")
BrightScript Debugger> topo = di.GetUSBTopology({array: true})
BrightScript Debugger> print topo[0]
vid:  05a7
pid:  40fa
fid: A.0
category: AUDIO
raw: 2-1.4.1:1.0
ident: usb/hiddev0
```

Ports that have USB devices connected to them will include a `fid` (Friendly ID) value (only array and XML-string returns include this value). Use the `fid` to determine which physical port on the player the USB device is connected to. The following table matches `fid` values to the ports on different model lines:

| Model Family | Friendly ID (fid) | Location |
| --- | --- | --- |
| LS424/LS423 | A   | Front (USB-C) |
| HDx24/HDx23 | A   | Front (USB-A) |
| HS123 | A   | N/A (M.2 connector) |
| HO523 | A   | Upper Front (USB-A) |
|     | B   | Lower Front (USB-A) |
|     | C   | Back (JAE TX-25) |
| XDx33/XDx34 | A   | Front (USB-C) |
| B   | Back (USB-A) |
| XTx43/XTx44 | A   | Back (USB-A) |
| B   | Front (USB-C) |

A `fid` value of `<port>.<int>` (e.g. "B.0") indicates that the USB device is directly connected to the player, while a value of `<port>/<int>.<int>` (e.g. "A/4.2") indicates a device connected through a USB hub. The last integer specifies the endpoint: For example, if a USB device presents as both an HID and audio device, they will be listed as separate devices with different endpoint numbers. Also note that there can be more than one layer of port numbers if multiple USB hubs are connected together (e.g. "A/4.0.0").

##### GetDeviceUniqueId() As String

Returns an identifier that, if not an empty string, is unique to the unit running the script.

##### GetFamily() As String

Returns a single string that indicates the family to which the device belongs. A device family is a set of models that are all capable of running the same firmware.

##### HasFeature(feature As String) As Boolean

Returns True if the player feature, which is passed as a case-insensitive string parameter, is present on the current device and firmware. The possible features that can be queried from the script are listed below:

> [!CAUTION]
> **Important**
>  If you pass a parameter other than one of those listed below, it may return False even if the feature is available on the hardware and firmware.

*   `"5v serial"`: A 5V serial port
    
*   `"audio1"`: The first audio output
    
*   `"audio2"`: A second audio output
    
*   `"audio3"`: A third audio output
    
*   `"brightscript1"`: BrightScript Version 1
    
*   `"brightscript2"`: BrightScript Version 2
    
*   `"component video"`: A component video output
    
*   `"ethernet"`: An Ethernet interface
    
*   `"FindMemberFunction"`: The global function of that name is available for use. See the [GlobalFunctions](https://docs.brightsign.biz/display/DOC/Global+Functions) page for details.
    
*   `"gpio connector"`: A DA15 or Phoenix-style GPIO port 
    
*   `"hdmi"`: An HDMI® output
    
*   `"hdmi input"`: An HDMI input
    
*   `"hevc_decode"`: An H.265 video decoder
    
*   `"media_decryption"`: The ability to decrypt AES-encrypted media, including video, image, and audio files.
    
*   `"nand storage"`: NAND storage for the boot loader and firmware
    
*   `"networking"`: Any form of networking capability. A False return may indicate that no network is currently available.
    
*   `"reset button"`: A reset button
    
*   `"registry"`: On-board persistent storage
    
*   `"rtc"`: A real-time clock (RTC)
    
*   `"sd"`: SD- or SDHC-compatible storage
    
*   `"sdhc"`: SDHC-compatible storage only
    
*   `"serial port 0"`: The first serial port
    
*   `"serial port 1"`: A second serial port
    
*   `"serial port 2"`: A third serial port
    
*   `"svc button"`: A service ("SVC") button. Passing the legacy term `"gpio12 button"` will yield the same result.
    
*   `"usb"`: One or more USB interfaces
    
*   `"vga"`: A VGA output
    
*   `"video_encoder"`: A video encoder/transcoder
    

Example:

```
di = CreateObject("roDeviceInfo")
print di.GetModel()
print di.GetVersion(), di.GetVersionNumber()
print di.GetBootVersion(), di.GetBootVersionNumber()
print di.GetDeviceUptime(), di.GetDeviceBootCount()
```

On a particular system, this will generate the following:

```
HD1010
3.2.41           197161
3.2.28           197148
 14353           3129 
```