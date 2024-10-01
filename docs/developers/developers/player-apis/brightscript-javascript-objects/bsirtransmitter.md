# BSIRTransmitter

This class receives IR events. For more information, refer to the Object Reference Manual entry on *roIRTransmitter*.

## Object Creation

A *BSIRTransmitter* object must specify the hardware interface that will output the IR signal:

`BSIRTransmitter (in DOMString interface)`

Valid hardware interfaces include the following:

*   "IR-out": The 3.5mm IR input connector (available on XDx30 players) or 3.5mm IR input/output connector (available on XTx43, 4Kx42, XDx33, and XDx32 players)
    
*   "Iguana": The [Iguanaworks](http://iguanaworks.net/) IR transceiver
    

## Methods

`boolean Send(in DOMString Type, in unsigned long code)`

`boolean SetSendPolarity(in boolean polarity)`

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

## Example

```
<script>
    var irTransmitter = new BSIRTransmitter("IR-out");

    function irCode1()
    {
        console.log('############ irCode1');
        irTransmitter.Send("NEC", 65284);
    }
    function irCode2()
    {
        console.log('############ irCode2');
        irTransmitter.Send("NEC", 65288);
    }
    function irCode3()
    {
        console.log('############ irCode3');
        irTransmitter.Send("NEC", 65290);
    }
</script>
```