# roBtManager

This object facilitates BLE one-way communication (i.e. "beaconing"): Use the *roBtManager* object to discover whether any BLE adapters are present and to send BLE advertisements using the adapters.

The JavaScript equivalent is [BSBtManager](../../../../developers/player-apis/brightscript-javascript-objects/bsbtmanager.md).

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roBtEvent* to the attached message port. Use these messages to detect insertion or removal of Bluetooth adapters.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Retrieves an arbitrary object set via the `SetUserData()` method.

## ifIdentity

##### GetIdentity() As Integer

Returns a unique number that can be used to identify events that originate from the object instance.

> [!NOTE]
> The *ifIdentity* interface has been deprecated. We recommend using the *ifUserData* interface instead.

## ifBtPeripheralManager

##### GetFailureReason() As String

Returns additional diagnostic information if a method returns False.

##### GetAdapterList() As roArray

Returns an array describing all available Bluetooth adapters. Each entry in the array consists of an associative array containing adapter properties. At present, each associative array contains a single `name` property that describes the adapter name. Use this method to determine if Bluetooth adapters are connected to the player.

##### StopAdvertising() As Boolean

Stops all BLE advertisements. This method returns True on success and False on failure.

##### GetAdvertisingList() As roArray

Returns an array describing all active Bluetooth advertisements. Each entry in the array consists of an associative array describing a single advertisement. The associative-array values correspond to the properties set using the `StartAdvertising()` method, but can also include default parameter values that were not set explicitly. Note that all UUID values will be returned in lowercase.

##### StartAdvertising(data As roAssociativeArray) As Boolean

Begins transmitting a BLE "beacon" message. This method returns True on success and False on failure. Each message can contain data in a standard format or arbitrary custom values. The message format is specified using the `mode` parameter, and other required values in the associative array will depend on the value of this parameter:

*   `mode:"beacon"`: This mode uses a simple beaconing format.
    
    *   `beacon_uuid`: A string representation of a UUID, which can be in 16-bit, 32-bit, or 128-bit format. A 16-bit UUID must be exactly four hex digits with no punctuation;  a 32-bit UUID must be exactly eight hex digits with no punctuation; and a 128-bit UUID must be punctuated exactly as follows: "cd7b6f81-f738-4cad-aebf-d2a2ea36d996".
        
    *   `beacon_major`: An integer specifying the 2-byte Major value (0 to 65535)
        
    *   `beacon_minor`: An integer specifying the 2-byte Minor value (0 to 65535)
        
    *   `beacon_level`:(optional) An 8-bit signed integer (-127 to 128) that corresponds to the measurement of the Tx power level (in dBm) at 1 meter. The default level is -60.
        
    *   `beacon_manufacturer`:(optional) A 2-byte integer value (0 to 65535) specifying the beacon manufacturer. The default value is 76 (&H4C).
        
    *   `connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable or not. Advertisements are non-connectable by default.
        
    *   `persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Beacon advertisements are persistent by default.
        
*   `mode:"eddystone-url"`: This mode uses the [Eddystone-URL](https://github.com/google/eddystone/tree/master/eddystone-url) format.
    
    *   `url`: The URL to encapsulate in the advertisement packet. If the URL is too long to fit in the packet, the `StartAdvertising()` call will return False and `GetFailureReason()` will report "Compressed URL is too long".
        
    *   `tx_power`:(optional)  An integer value that corresponds to the measurement of the Tx power level (in dBm) at 0 meters. The default value is -19, which corresponds to a level of -60dBm at 1 meter. The recommended calibration practice is to measure the RSSI in a circle at 1 meter from the beacon, then add 41 to the average measured signal strength to get the `tx_power` value: For example, measuring a -65dBm RSSI at 1 meter yields a **TxPower** value of -2
        
        *   Note that the `tx_power` value does not modify the power level of the Bluetooth transmitter (this requires [physical attenuation](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2063892481/Accessories+FAQ#Can-I-modify-the-power-level-of-the-Bluetooth-module-transmitter%3F)). Rather, the `tx_power` value is transmitted to Bluetooth clients in the BLE advertisement. Clients can then compare this value to the current RSSI of the signal to determine their approximate distance from the beacon.
            
    *   `connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable or not. Advertisements are non-connectable by default.
        
    *   `persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Eddystone-URL advertisements are persistent by default.
        
*   `mode:"eddystone-uid"`: This mode uses the [Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) format.
    
    *   `namespace`: A 10-byte value expressed as 20 hexadecimal digits
        
    *   `instance`: A 6-byte value expressed as 12 hexadecimal digits
        
    *   `tx_power`:(optional) An integer value specifying the Tx power level in dBm at 0 meters. The default value is -19, which corresponds to a level of -60dBm at 1 meter. The recommended calibration practice is to measure at 1 meter and add 41: For example, -65dBm RSSI leads to a value of -24.
        
    *   `connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable (for GATT or other services).  Advertisements are non-connectable by default.
        
    *   `persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Eddystone-URL advertisements are not persistent by default.
        
*   `mode:"custom"`: This mode supports arbitrary custom data in a vendor-specific field. 
    
    *   `cutom_manufacturer_data`:(optional) An associative array containing two keys:
        
        *   `manufacturer`: A 2-byte integer value (0 to 65535)
            
        *   `data`: An *roByteArray* instance containing data
            
    *   `service_uuid`:(optional) A set of ServiceUUID elements, which can be specified as either an array of UUID strings or an array of associative arrays containing a `uuid` key/value pair. Each associative array can also contain a `data` key, which specifies ServiceData as an *roByteArray* instance.
        
    *   `connectable`:(optional) A Boolean value indicating whether the advertisement should be connectable or not. Advertisements are non-connectable by default.
        
    *   `persistent`:(optional) A Boolean value indicating whether the advertisement should persist after every reboot. Custom advertisements are not persistent by default.
        

To specify multiple advertisements, pass an array of associative arrays to the `StartAdvertising()` method. Advertisements will be sent in rotation. The method will fail if one or more advertisement is incorrect—try each advertisement individually and call `GetFailureReason()` to determine which advertisement is causing the error.

Calling the `StartAdvertising()` method will replace any previous advertisements. You can change a list of advertisements by modifying the array and calling `StartAdvertising()` again.

## Examples

This script uses *roBtManager.GetAdapterList()* to determine if there are any Bluetooth adapters available:

```
btm = CreateObject("roBtManager")
if btm.GetAdapterList().Count() > 0 then print "Bluetooth available"
```

This script constructs two associative arrays for advertising with the "beacon" format and then broadcasts them both:

```
adv1 = { mode : "beacon", beacon_uuid : "41fac2b21-c8cb-41e7-b011-12d1016dd39e", beacon_major : 400, beacon_minor : 22 }
adv2 = { mode : "beacon", beacon_manufacturer: &H4C, beacon_uuid : "41fac221-c8cb-41e7-b011-12d1016dd39e", beacon_major : &H1234, beacon_minor : &HFF01, beacon_level : -50 }
 
advlist = [adv1, adv2]
bm.StartAdvertising(advlist)
```

The associative array can also be constructed in parts:

```
adv1 = { mode: "beacon"}
adv1.Append({ beacon_uuid : "41fac221-c8cb-41e7-b011-12d1016dd39e" })
adv1.Append({ beacon_major : 32000, beacon_minor : 100 })
```

This script constructs an advertisement with the "Eddystone-URL" format. It uses the optional `tx_power` parameter as well:

```
adv1 = { mode: "eddystone-url", url: "http://www.brightsign.biz", tx_power: -24}
```

This script constructs a custom-formatted advertisement:

```
custom_adv = CreateObject("roByteArray")
custom_adv.FromHexString("0215434B2EB8C28F40898E7A1E644BB13B9FA000B001C5")
adv2 = { mode : "custom", custom_manufacturer_data : { manufacturer: &H4C, data : custom_adv } }
```