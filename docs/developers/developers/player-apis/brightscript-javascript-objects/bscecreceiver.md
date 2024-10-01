# BSCECReceiver

For more information about available methods, refer to the [*roCecInterface*](../../../developers/brightscript/object-reference/inputoutput-objects/rocecinterface.md) entry. Note that you can only use this JavaScript class to receive CEC messages. Use [*BSCECTransmitter*](../brightscript-javascript-objects/bscectransmitter.md) to send CEC messages.

The JavaScript equivalent is [cec](../../player-apis/javascript-apis/cec.md).

## Events

The following events are available on the *BSCECReceiver* object. They can receive an event of the type *CECReceiverEvent*. 

`onececrxframe`

`oncectxcomplete`

### BSCECReceiverEvent – Attributes

`readonly attribute int status`

`readonly attribute DOMString data`

### BSCECReceiverEvent – Methods

`ArrayBuffer getBytes()`

## Methods

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

## Example

```
<script>
    function loadCec()
    {
        console.log("*** loadCec ***");

        var cec_in = new BSCECReceiver();

        cec_in.oncecrxframe = function(e){
           console.log('############ oncecrxframe: ' + e.data);
        }

        cec_in.oncectxcomplete = function(e){
           console.log('############ oncectxcomplete: ' + e.status);
        }
    }
</script>
```