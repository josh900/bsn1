# BSCECTransmitter

For more information about available methods, refer to the [*roCecInterface*](../../../developers/brightscript/object-reference/inputoutput-objects/rocecinterface.md) entry. Note that you can only use this JavaScript class to send CEC messages. Use [*BSCECReceiver*](../brightscript-javascript-objects/bscecreceiver.md) to receive CEC messages.

When possible, JavaScript APIs should be used instead of BrightScript-Javascript Objects. The JavaScript API equivalent to this object is [cec](../../player-apis/javascript-apis/cec.md).

## Methods

`boolean SendRawMessage(in ArrayBuffer data)`

`boolean SendRawMessage(in ArrayBufferView data)`

`boolean SendRawMessage(in DOMString data)`

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

## Example

The following JavaScript example shows how to send a set of CEC messages:

```
function cecDisplayOn()
    {
        console.log("### cecDisplayOn ###");
        var cec_control = new BSCECTransmitter();
        var buffer = new Uint8Array(2);
        buffer[ 0 ] = 0x40;
        buffer[ 1 ] = 0x0D;
        cec_control.SendRawMessage(buffer);
    }

function cecDisplayOff()
    {
        console.log("### cecDisplayOff ###");
        var cec_control = new BSCECTransmitter();
        var buffer = new Uint8Array(2);
        buffer[ 0 ] = 0x40;
        buffer[ 1 ] = 0x36;
        cec_control.SendRawMessage(buffer);
    }
```