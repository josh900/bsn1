# BSDatagramSocket

For more information about available methods, refer to the *roDatagramReceiver* and *roDatagramEvent* entries.

## Methods

`boolean BindLocalPort(in long port)`

`long GetLocalPort()`

`boolean JoinMulticastGroup(in DOMString group)`

`boolean SendTo(in DOMString dest, in long port, in ArrayBufferView data)`

`boolean SendTo(in DOMString dest, in long port, in DOMString data)`

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

## Events

The following event is available on the *BSDatagramSocket* object. It can receive an event of the type DatagramSocketEvent. Use getBytes() to retrieve the body of the UDP message.

`ondatagram`

### DatagramSocketEvent

The DatagramSocketEvent has the following attributes:

`readonly attribute DOMString remoteHost`

`readonly attribute int remotePort`  

The DatagramSocketEvent supports the following methods:

`ArrayBuffer getBytes()`

## Example

> [!NOTE]
> See [here](https://stackoverflow.com/questions/6965107/converting-between-strings-and-arraybuffers) to learn how to convert between strings and an `ArrayBuffer`.

```
var bsSocketMessage = new BSDatagramSocket();
bsSocketMessage.BindLocalPort(1234)
bsSocketMessage.ondatagram = function(e){

  var txtDec = new TextDecoder("utf-8");
  console.log("Received " + txtDec.decode(e.getBytes()));
};
```