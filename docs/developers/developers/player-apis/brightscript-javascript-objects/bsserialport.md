# BSSerialPort

For more information about available methods, refer to the [*roSerialPort*](../../../developers/brightscript/object-reference/inputoutput-objects/roserialport.md) entry.

If possible, use @brightsign/serialport with the Node Package [serialport](https://serialport.io/) instead of BSSerialPort. A basic reference implementation can be found in [this GitHub repository](https://github.com/brightsign/bs-node-serialport).

## Object Creation

`BSSerialPort(in unsigned long port);`

## Methods

`void SetBaudRate(in unsigned long baudRate) raises(DOMException)`

`void SetDataBits(in unsigned long dataBits) raises(DOMException)`

`void SetStopBits(in unsigned long stopBits) raises(DOMException)`

`void SetParity(in DOMString parity) raises(DOMException)`

`boolean SetEcho(in boolean flag) boolean`

`SetInverted(in boolean flag) boolean`

`SetFlowControl(in boolean flag)`

`void SetGenerateByteEvent(in boolean flag) raises(DOMException)`

`void SetGenerateLineEvent(in boolean flag) raises(DOMException)`

`void SetLineEnding(in DOMString eol) raises(DOMException)`

`boolean SendByte(in unsigned long byte)`

`boolean SendBytes(in ArrayBuffer data)`

`boolean SendBytes(in ArrayBufferView data)`

`boolean SendBytes(in DOMString data)`

`boolean SendBreak(in long duration_ms)`

`void Flush() raises(DOMException)`

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

## Events

The following events are available via the *BSSerialPort* object. Each event can receive a SerialPortEvent event.

`onserialbyte`

`onserialline`

### SerialPortEvent – Attributes

For the onserialbyte event:

`readonly attribute unsigned long sbyte`

For the onserialline event:

`readonly attribute DOMString sdata`

## Example

```
function serialOut()
{
    console.log("*** serialOut **");

    // '2' is the first externally connected USB  port on Cheetah
    var serial_out = new BSSerialPort(2);

    serial_out.SetBaudRate(115200);
    serial_out.SetDataBits(8);
    serial_out.SetStopBits(1);
    serial_out.SetParity("none");
    serial_out.SetEcho(true);

    serial_out.SetGenerateByteEvent(true);
    serial_out.SetGenerateLineEvent(true);

    serial_out.onserialbyte = function(e){
        console.log('### onserialbyte: ' + e.sbyte);
    }

    serial_out.onserialline = function(e){
        console.log('### onserialline: ' + e.sdata);
    }

    serial_out.SendByte(89);
    serial_out.SendByte(90);
    serial_out.SendByte(91);

    serial_out.SendBytes('Hello World!');
    serial_out.SendBytes(String.fromCharCode(64, 27, 66, 67))
}
```