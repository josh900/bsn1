# devicestatus

This object provides information about the device hardware, firmware, and features.

**devicestatus IDL**

```
interface devicestatus {
    Promise<BVNinformationList> getBVNPipelines();
    Promise<BVNinformationList> getBVNComponents();
    Promise<Powerinformation> getPowerStatus();
    Promise<ExtensionsinformationList> getExtensions();
    Promise<POEinformation> getPOEStatus();
};

interface Powerinformation {
    attribute String source;
    attribute String switch_mode;
    attribute String battery;
    attribute int soc_percent;
};

interface BVNinformation {
    attribute String name;
    attribute int index;
    attribute BVNRegisterList registers;
    attribute BVNPipelineList items;                //@Optional
};

interface BVNRegister {
    attribute String name;
    attribute int offset;
};

interface BVNPipeline {
    attribute String name;
};

interface Extensionsinformation {
    attribute String name;
    attribute int size;            //@Optional
    attribute String id;
};

interface POEpowerinformation {
    attribute float value;
    attribute String units;
};

interface POEinformation {
    attribute String status;
    attribute POEpowerinformation power;     //@Optional
};                                                                                                  
```

## Object Creation

To create a *devicestatus* object, load the *@brightsign/status* module using the `require()` method. 

```
var DeviceStatusClass = require("@brightsign/devicestatus");
var devicestatus = new DeviceStatusClass();
```

## devicestatus

##### getPowerStatus()

```
Promise<Powerinformation> getPowerStatus()
```

Returns the device battery status as "charging", "discharging", "complete", "absent", or "fault".

##### getExtensions()

```
Promise<ExtensionsinformationList> getExtensions()
```

Returns a promise which yields an object containing an `extensions` array with each element containing at least a `name` field. Other fields may also be present, but should not be relied on.

##### getPOEStatus()

```
Promise<POEinformation> getPOEStatus()
```

Returns information about whether PoE (Power over Ethernet) network is supported, available, and/or active on a device.

## Powerinformation

*   `source` string:  Possible values are "battery", "Ethernet", or "AC"
    
*   `switch_mode` string: Returns "soft" or "hard"
    
*   `battery` string: Possible values are "charging", "discharging", "complete", "absent", or "fault"
    
*   `soc_percent` int: The state of charge of the battery in percent from 0 (empty) to 100 (full)
    

## Extensionsinformation

*   `name` string: The name of the extension
    
*   `size` int: Some extensions return a size and others do not. Players that have AC3 or E-AC3 licenses installed will report those as extensions but no size will be included.
    

## POEpowerinformation

*   `value` float: Returns the "Power value"
    
*   `units` string: returns the "Power value" units ("W")
    

## POEinformation

*   `status` string:  The status string can be "active", "standby", or "inactive"
    
*   `power` POEpowerinformation: See `POEpowerinformation` above for details.
    

## Example

To get the power status of a device:

```
var DeviceStatusClass = require("@brightsign/devicestatus");
var devicestatus = new DeviceStatusClass();

devicestatus.getPowerStatus().then(
        function(data){
                console.log(JSON.stringify(data));
        })
    .catch(
        function(data){
                console.log("Error: " + data);
        })
```