# BSIRReceiver

This class receives IR events. For more information, refer to the Object Reference Manual entry on *roIRReceiver*.

## Object Creation

A *BSIRReceiver* object must specify the hardware interface that will receive IR events, as well as the encoding(s) to look for:

`BSIRReceiver(DOMString interface, DOMString encoding)`

  
Valid hardware interfaces include the following:

*   "GPIO": Pin 1 of the GPIO connector
    
*   "IR-in": The 3.5mm IR input/output connector
    
*   "Iguana": The [Iguanaworks](http://iguanaworks.net/) IR transceiver. This source can support both NEC and RC5 encodings simultaneously.
    
*   “tvcontroller” : This virtual IR driver is only available on BrightSign built-in products. It reads the IR messages from UART and drives the roIRReceiver object like other IR receivers. A creation example would be:
    

```
BSIRReceiver(tvcontroller)
```

Valid encodings include the following (multiple encodings can be specified in the string using a ";"):

*   "NEC"
    
*   "RC5" (supported on the Iguanaworks device only)
    

NEC codes are expressed in 24 bits:

*   Bits 0-7: Button code
    
*   Bits 8-23: Manufacturer code
    

> [!NOTE]
> If the manufacturer code is zero, then the code is considered to be intended for the Roku SoundBridge remote control.

## Methods

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

## Events

These events are available on the *BSIRReceiver* object. Each event can receive an IRReceiverEvent event.

`onremotedown`

`onremoterepeat`

`onremoteup` (supported on the Iguanaworks device only)

#### IRReceiverEvent – Attributes

`readonly attribute DOMString irType;`

`readonly attribute unsigned long code;`

## Example

The following JavaScript example displays messages on the log when remote codes are received:

```
function myFunction()
{
    var ir_receiver = new BSIRReceiver("IR-in","NEC");

    ir_receiver.onremotedown = function(e){
        console.log('############ onremotedown: ' + e.irType + " - " + e.code);
    }

    ir_receiver.onremoteup = function(e){
        console.log('############ onremoteup: ' + e.irType + " - " + e.code);
    }
}
```