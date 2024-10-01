# roSerialPort

  

This object controls the serial port on the player, allowing you to transmit and receive serial data. The JavaScript equivalent is [BSSerialPort](../../../../developers/player-apis/brightscript-javascript-objects/bsserialport.md).

> [!NOTE]
> If the *serial\_with\_telnet* registry key is set to 1, serial communication via roSerialPort in scripts will be highly unreliable. See [this page](../../../../developers/brightsign-registry-keys.md) for more information about *serial\_with\_telnet*.

Object Creation: The *roSerialPort* object is created with two parameters.

```
CreateObject("roSerialPort", port As Dynamic, baud_rate As Integer)
```

*   `port As Integer`: The port enumeration of the serial device:
    
    *   Most standard serial devices (including the USB-serial port on the [LS424](https://docs.brightsign.biz/display/DOC/LS424+Hardware+Interfaces#LS424HardwareInterfaces-usb_serial)) enumerate on port 0, though port 1 may be available on the GPIO connector on some models if enabled. See [roControlPort.EnableAlternateFunction](https://docs.brightsign.biz/display/DOC/roControlPort#roControlPort-EnableAlternateFunction(buttonAsInteger,pin_functionAsString)AsBoolean).
        
    *   If more than one USB serial device is attached then the first one will be port 2, the second will be port 3, etc.
        
    *   To communicate with the serial port of an OPS display (i.e. with the HO523), use port 1.
        
    *   To communicate with a USB-serial device (such as a GPS receiver), use port 2.
        
*   `port As String`: If multiple USB-serial devices are connected to the player, the device can be specified with a friendly name (`"USB:<friendly_name>"`). This value corresponds to the `<fid>` value returned by the [roDeviceInfo.GetUSBTopology()](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673305/roDeviceInfo#GetUSBTopology(return-As-roAssociativeArray)-As-Dynamic-[inlineExtension]) method. The BrightSign shell `usblist` command can be used to discover friendly names. Note that RAW names are not guaranteed to stay the same between products or OS versions, so they are not recommended.
    
*   `baud_rate As Integer`: The baud rate for serial communication. The serial port supports the following baud rates: 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400.
    

##### **Example**

```
serial1 = CreateObject("roSerialPort", 0, 115200)
serial2 = CreateObject("roSerialPort", "USB:A/1", 57600) 
```

The *roSerialPort* object sends the following event types:

*   *roStreamLineEvent*: The line event is generated whenever the end of line string set using *SetEol* is found and contains a string for the whole line. This object implements the *ifString* and *ifUserData* interfaces.
    
*   *roStreamByteEvent*: The byte event is generated on every byte received. This object implements the *ifInt* and *ifUserData* interfaces.
    

## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

Sets the EOL sequence when writing to the stream. The default value is CR (ASCII value 13). If you need to set this value to a non-printing character, use the `chr()` [global function](../../object-reference/global-functions.md).

##### SendByte(byte As Integer) As Void

Writes the specified byte to the stream.

##### SendLine(string As String) As Void

Writes the specified characters to the stream followed by the current EOL sequence.

##### SendBlock(a As Dynamic) As Void

Writes the specified characters to the stream. This method can support either a string or an *roByteArray*. If the block is a string, any null bytes will terminate the block.

##### Flush()

## ifStreamReceive

##### SetLineEventPort(port As Object) As Void

Sets the message port that *roStreamLineEvent* events will be posted to.

##### SetByteEventPort(port As Object) As Void

Sets the message port that *roStreamByteEvent* events will be posted to.

##### SetByteArrayEventPort(port As Object) As Void

This method works like *SetByteEventPort* but causes *roStreamByteArrayEvent* messages to be posted to the message port when data is received. For some object types (for example, *roTCPStream*), this can be much more efficient since data no longer needs to be delivered to BrightScript a byte at a time, but since serial ports are comparatively slow it's possible that each event will still contain only a single character. 

##### SetReceiveEol(eol\_sequence As String)

Sets the sequence that will signify the end of line and cause a *roStreamLineEvent* to be delivered to the message port set by *SetLineEventPort*. If you need to set this value to a non-printing character, use the `chr()` [global function](../../object-reference/global-functions.md) or an *roByteArray*. If the sequence contains NUL bytes it must be passed as an *roByteArray* since strings may not contain NUL bytes.

To use a NUL byte as a line terminator:

```
eol = CreateObject("roByteArray")
eol.Push(0)
mp = CreateObject("roMessagePort")
client = CreateObject("roSerialPort", 0, 115200)
client.SetReceiveEol(eol)
client.SetLineEventPort(mp)
```

##### SetMatcher(matcher As Object) As Boolean

Instructs the stream to use the specified matcher. This method returns True if successful. Pass Invalid to this method to stop using the specified matcher.

## ifSerialControl

##### SetBaudRate(baud\_rate As Integer) As Boolean

Sets the baud rate of the device. The supported baud rates are as follows: 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400.

##### SetMode(mode As String) As Boolean

Sets the serial mode in "8N1" syntax. The first character is the number of data bits. It can be either 5, 6, 7, or 8. The second number is the parity. It can be "N"one, "O"dd, or "E"ven. The third is the number of stop bits. It can be 1 or 2.

##### SetEcho(enable As Boolean) As Boolean

Enables or disables serial echo. It returns True on success and False on failure.

##### SetEol(a As String)  
 

##### SetFlowControl(enable As Boolean) As Boolean

Enables or disable RTS/CTS handshaking over the serial port. This feature is currently only available on 4Kx42, XDx32, and HDx22 models.

##### SetInverted(inverted As Boolean) As Boolean

Inverts the TX/RX signal levels on the serial port. This allows the player to communicate with devices that use -12V to 12V signaling. Inversion is supported on the DE-9 (more commonly referred to as DB-9) and USB ports only. Passing True to the method enables inversion, whereas passing False disables it.

##### SendBreak(duration\_in\_ms As Integer) as Boolean

Sends a serial break or sets the serial break condition. This method returns True upon success and False upon failure.

*   `duration_in_ms = -1`: Sends a continuous break.
    
*   `duration_in_ms = 0`: Clears the break state.
    
*   `duration_in_ms >= 100`: Sets the break condition for the specified period of milliseconds (note that this integer is only accurate to the tenth of a second).
    

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## Example

This example script waits for a serial event and echoes the input received on the serial port to the shell:

```
serial = CreateObject("roSerialPort", 0, 9600)
p = CreateObject("roMessagePort")
serial.SetLineEventPort(p)

serial_only:
msg = Wait(0,p) ' Wait forever for a message.
if(type(msg) <> "roStreamLineEvent") goto serial_only 'Accept serial messages only.
serial.SendLine(msg) ' Echo the message back to serial.
```