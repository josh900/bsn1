# BSBtManager

Use the *BSBtManager* object to discover whether any BLE adapters are present and to receive events (for example, when adapters are added or removed). It can also be used to retrieve and modify Bluetooth advertising.

## Attributes

The *BSBtManager* object has the following attribute:

`readonly attribute Array adapters`: A list of all available Bluetooth adapters. If this list is empty, there are no adapters present.

## Events

Use the `onBtEvent()` callback to receive events:

`"add-adapter"`: An adapter has been added. The value reports the name of the adapter.

`"startup-complete"`: The initial advertising list has been built. This event is sent after any initial "add-adapter" events. Applications should wait for this event before detecting a missing adapter.

`"remove-adapter"`: An adapter has been removed. The value reports the name of the adapter.

`"update-advertising"`: Bluetooth advertising has changed. The value identifies the source of the change (from "brightscript" or "javascript"). If your script maintains a variable containing the advertising list, this event indicates that it may need to be refreshed.

> [!NOTE]
> Since additional events may be added in the future, your script should have the capacity to handle unrecognized events.

### Example

`btm.onbtevent = function (ev) { console.log("Event " + ev.name + "; parameter " + ev.parameter); }`

## Methods

The *BSBtManager* object has the following methods:

`object GetCurrentAdvertising()`

Returns a *BSBtAdvertisementList* object containing current advertisement parameters.

`boolean StartAdvertising(in object advertisement_list)`

Begins sending BLE advertisements using the specified *BSBtAdvertisementList* object. Calling this method will replace all previous advertisements, including persistent advertisements, regardless of whether they were set from JavaScript or BrightScript. To preserve advertisements, retrieve the current *BSBtAdvertisementList* and make changes as needed before passing it to `StartAdvertising()`.

`StartAdvertising(new BSBtAdvertisementList())`

Stops all advertisements.

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

`BSBtAdvertisementList`

The *BSBtAdvertisementList* object is a container for *BSBtAdvertisement* objects. Elements can be added to the end of the list using `push()` or removed using `pop()`. Existing elements can be accessed with indexing.

`BSBtAdvertisement`

The *BSBtAdvertisement* object represents a single BLE advertisement. It supports advertising data in standard formats or arbitrary custom values. Standard format values can be initialized on construction using a dictionary, but advanced custom fields must be set on the object. Supported modes are described below.

### Beacon Format

This mode uses a simple beaconing format:

`mode:"beacon"` 

`beaconUUID`: A string representation of a UUID, which can be in 16-bit, 32-bit, or 128-bit format. A 16-bit UUID must be exactly four hex digits with no punctuation;  a 32-bit UUID must be exactly eight hex digits with no punctuation; and a 128-bit UUID must be punctuated exactly as follows: "cd7b6f81-f738-4cad-aebf-d2a2ea36d996".

`beaconMajor`: An integer specifying the 2-byte Major value (0 to 65535)

`beaconMinor`: An integer specifying the 2-byte Minor value (0 to 65535)

`beacon_level`:(optional) An 8-bit signed integer (-127 to 128) that corresponds to the measurement of the Tx power level (in dBm) at 1 meter. The default level is -60.

`beaconManufacturer`:(optional) A 2-byte integer value (0 to 65535) specifying the beacon manufacturer. The default value is 76 (&H4C).

`connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable (for GATT or other services). Advertisements are non-connectable by default.

`persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Beacon advertisements are not persistent by default.

### Eddystone-URL Format

This mode uses the [Eddystone-URL](https://github.com/google/eddystone/tree/master/eddystone-url) format:

`mode:"eddystone-url"` 

`url`: The URL to encapsulate in the advertisement packet. If the URL is too long to fit in the packet, the StartAdvertising() call will return an AbortError exception that includes the description "Compressed URL is too long".

`tx_power`:(optional) An integer value specifying the Tx power level in dBm at 0 meters. The default value is -19, which corresponds to a level of -60dBm at 1 meter. The recommended calibration practice is to measure at 1 meter and add 41: For example, -65dBm RSSI leads to a value of -24.

`connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable (for GATT or other services).  Advertisements are non-connectable by default.

`persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Eddystone-URL advertisements are not persistent by default.

### Eddystone-UID format

This mode uses the [Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) format:

`mode`:"eddystone-uid"

`nameSpace`: A 10-byte value expressed as 20 hexadecimal digits

`instance`: A 6-byte value expressed as 12 hexadecimal digits

`tx_power`:(optional) An integer value specifying the Tx power level in dBm at 0 meters. The default value is -19, which corresponds to a level of -60dBm at 1 meter. The recommended calibration practice is to measure at 1 meter and add 41: For example, -65dBm RSSI leads to a value of -24.

`connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable (for GATT or other services).  Advertisements are non-connectable by default.

`persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Eddystone-URL advertisements are not persistent by default.

### Custom Format

This mode supports arbitrary custom data. Binary fields are specified as hexadecimal-encoded strings (e.g. the decimal values 12, 128 would be specified as "0C80"). All lists support `push()`/`pop()` calls and indexing. Duplicate values should not be included.

*   `mode:"custom"`
    
*   `manufacturerData`:(optional) A *BSBtManufacturerData* object containing the following fields:
    
    *   `manufacturer`: An unsigned 16-bit integer value
        
    *   `data`: Binary data
        
*   `serviceUUID`:(optional) A list of UUID strings.
    
*   `serviceData`:(optional) A *BSBtUUIDData* object containing the following fields:
    
    *   `uuid`: The UUID string
        
    *   `data`: Binary data
        
*   `soliciitUUID`:(optional) A list of UUID strings.
    
    *   connectable:(optional) A Boolean value indicating whether the advertisement should be connectable (for GATT or other services). Advertisements are non-connectable by default.
        
*   `persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Custom advertisements are not persistent by default.
    

## Examples

This script configures a simple advertisement and an Eddystone-URL advertisement and then begins advertising:

```
ads = new BSBtAdvertisementList();
ad1 = new BSBtAdvertisement({ mode: "beacon", beaconUUID: "41fac221-c8cb-41e7-b011-12d1016dd39e", beaconMajor: 400, beaconMinor: 123});
ads.push(ad1);
ad2 = new BSBtAdvertisement({ mode:"eddystone-url", url: "http://www.brightsign.biz"})
ads.push(ad2);

btm.StartAdvertising(ads);
```

This script finds beacons matching a UUID and forms a string with Major/Minor codes:

```
s = "";
for(i = 0; i < adList.length; i++) {
	if (adList[i].mode == "beacon"
		&& adList[i].beaconUUID == "434b2eb8-c28f-4089-8e7a-1e644bb13b9f") {
			s = s + "Beacon: " +  adList[i].beaconMajor + "," + adList[i].beaconMinor + " "
		}
}
```

This script looks for Eddystone-URL beacons and sends updates based on the current URL:

```
btm = new BSBtManager()
adList = btm.GetCurrentAdvertising()
for(i = 0; i < adList.length; i++) {
	// Brightsign.biz is now https
		if (adList[i].mode == "eddystone-url" && adList[i].url == "http://www.brightsign.biz")      {
			adList[i].url = "https://www.brightsign.biz"
		}
}
btm.StartAdvertising(adList)
```

This script produces an exception because the compressed URL is too long:

```
al = new BSBtAdvertisementList()
ad4 = new BSBtAdvertisement( { mode: "eddystone-url", url:"http://www.brightsign.biz/thisistoolong"} )
al.push(ad4)
b.StartAdvertising(al)
```