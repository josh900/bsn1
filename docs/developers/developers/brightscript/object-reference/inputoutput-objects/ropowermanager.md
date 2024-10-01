# roPowerManager

The *roPowerManager* object is used to report the battery state of the device.  

Object Creation: The *roPowerManager* object is created as follows:

```
CreateObject("roPowerManager")
```

## ifPowerManager

##### GetPowerSource() As String

Returns either "Battery", "AC", or "Ethernet", depending on the power source.

##### GetBatteryStatus() As Object

Returns the following values:

*   `state` string: Returns the device battery status as either "charging", "discharging", "charge-complete", or "charge-fault"
    
*   `soc_percent` int: The level of charge of the battery as a percentage.
    
*   `hardware_version` string: The hardware version number
    

##### PowerOff()

Indicates that the charger should cut the power

##### SetPowerSwitchMode(as A String)

Takes either "hard" or "soft"

##### GetPowerSwitchMode() As String

Returns whether it is set to "hard" or "soft"

## ifMessagePort

##### SetPort(as A Object)

Which message port should be used to get messages from the power manager.