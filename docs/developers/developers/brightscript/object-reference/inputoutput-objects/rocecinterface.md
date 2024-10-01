# roCecInterface

This object provides access to the HDMI® CEC channel.

Object Creation: The *roCecInterface* object is created with no parameters.

```
CreateObject("roCecInterface")
```

When possible, JavaScript APIs should be used instead of BrightScript-Javascript Objects. The JavaScript API equivalent to this object is [cec](../../../../developers/player-apis/javascript-apis/cec.md).

## IfCecInterface

##### SendRawMessage(packet As roByteArray) As Void

Sends a message on the CEC bus. The frame data should be provided as an *roByteArray*, with the destination address in the low 4 bits of the first octet.

The system software automatically replaces the high 4 bits of the first octet with the source address. It also copies the physical address of the player into the following messages automatically prior to transmission: ActiveSource, InactiveSource, SystemAudioModeRequest.

> [!NOTE]
> As of BrightSign OS 8.2.55, the CEC implementation for AU series 5 products will reply to these messages with the correct data, without involving the script:
> *   CEC\_MSG\_GET\_CEC\_VERSION
>     
> *   CEC\_MSG\_ABORT
>     
> *   CEC\_MSG\_GIVE\_DEVICE\_POWER\_STATUS
>     
> *   CEC\_MSG\_GIVE\_OSD\_NAME
>     
> *   CEC\_MSG\_GIVE\_DEVICE\_VENDOR\_ID
>     
> *   CEC\_MSG\_GIVE\_FEATURES
>     
> *   CEC\_MSG\_GIVE\_PHYSICAL\_ADDR
>     
> *   CEC\_MSG\_USER\_CONTROL\_PRESSED
>     
> *   CEC\_MSG\_USER\_CONTROL\_RELEASED
>     
> *   CEC\_MSG\_REPORT\_PHYSICAL\_ADDR

> [!TIP]
> **Tip**
> Use the `UseInitiatorAddressFromPacket()` method to prevent the system software from replacing source bits.

##### UseInitiatorAddressFromPacket(enable As Boolean) As Boolean

Removes the source address included in CEC messages by system software if passed `true`. This method allows you to transmit unmodified bytes via CEC.

##### GetLogicalAddress() As Integer

Returns the current logical address. This method will return the unregistered address (0x0f) to indicate that the logical address has not been negotiated. In this case, messages can still be sent, but the receivers will behave differently and may not process all messages.

##### EnableCecDebug(filename As String) As Void

Enables CEC debugging. This method will write a log of all CEC packets to the specified file.

##### GetPhysicalAddress() As roByteArray

Returns the CEC physical address, which is sometimes required when processing CEC messages.

##### PortName ()

Optional. This can be:

*   default: the default output for the platform, normally HDMI-1
    
*   HDMI-X : X is a number from 1 up to the number of HDMI outputs on the platform
    
*   eARC: on the AU335 (the default)
    

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via SetUserData(). It will return Invalid if no data has been set.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roCecRxFrameEvent and roCecTxCompleteEvent* to the attached message port.