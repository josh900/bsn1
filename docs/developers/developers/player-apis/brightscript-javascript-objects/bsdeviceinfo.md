# BSDeviceInfo

For more information about available methods, refer to the *roDeviceInfo* entry. The JavaScript equivalent is [deviceinfo](../../player-apis/javascript-apis/deviceinfo.md).

## Attributes

`readonly attribute DOMString model`

`readonly attribute DOMString version`

`readonly attribute int deviceUptime`

`readonly attribute int deviceLifetime`

`readonly attribute int deviceBootCount`

`readonly attribute DOMString bootVersion`

`readonly attribute DOMString deviceUniqueId`

`readonly attribute DOMString family`

## Methods

`int VersionCompare(in DOMString version)`

`int BootVersionCompare(in DOMString version)`

`boolean HasFeature(in DOMString feature)`

## Example

The following JavaScript example posts device information on the page when the button is clicked:

```
function deviceInfo()
{
    var device_info = new BSDeviceInfo();
    document.getElementById("modelText").innerHTML = device_info.model;
    document.getElementById("versionText").innerHTML = device_info.version;
    document.getElementById("bversionText").innerHTML = device_info.bootVersion;
    document.getElementById("serialText").innerHTML = device_info.deviceUniqueId;
    document.getElementById("familyText").innerHTML = device_info.family;

    document.getElementById("uptime").innerHTML = device_info.deviceUptime;
    document.getElementById("lifetime").innerHTML = device_info.deviceLifetime;
    document.getElementById("bootcount").innerHTML = device_info.deviceBootCount;

    if(device_info.VersionCompare("4.7.36") > 0)
    {
        document.getElementById("version1").innerHTML = "Version > 4.7.36"
    }
    else
    {
        document.getElementById("version1").innerHTML = "Version <= 4.7.36"
    }
    
	if(device_info.HasFeature("Six Channel Audio"))
    {
        document.getElementById("feature").innerHTML = "6 Channel Audio Available"
    }
    else
    {
        document.getElementById("feature").innerHTML = "6 Channel Audio NOT Available"
    }
}
```