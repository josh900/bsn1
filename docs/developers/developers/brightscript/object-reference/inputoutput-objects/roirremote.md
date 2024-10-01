# roIRRemote

This object supports receiving and transmitting arbitrary Infrared remote control codes using the NEC protocol. You can also use this object to send PHC (Pronto Hex Code) commands. The best way to determine the required send values is to capture the codes received by *roIRRemote* when the remote buttons of the device are pressed and then send the same codes. 

> [!CAUTION]
> **Important**
> The *roIRRemote* object cannot be used to receive input over the 3.5mm IR port on the 4Kx42 and XDx32 series—use the *roIRReceiver* object instead.

NEC codes are expressed in 24 bits:

*   Bits 0-7: Button code
    
*   Bits 8-23: Manufacturer code
    

> [!NOTE]
> **Note**
> If the manufacturer code is zero, then the code is considered to be intended for the Roku SoundBridge remote control.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roIRRemotePress* to the attached message port.

## ifIRRemote

##### Send(protocol as String, code as Dynamic) As Boolean

Sends the specified code using the IR blaster. The system currently supports two IR transmission protocols: "NEC" and "PHC" (Pronto Hex Code). This method returns True if the code was successfully transmitted, but there is no way to determine from BrightScript if the controlled device actually received it.

## Pronto Hex Format 

Raw captures of Pronto Hex commands will likely not work with the inbuilt IR blaster, though they should work with [Iguanaworks](http://iguanaworks.net/) IR transceivers. This is a result of the trailing *off* periods, which are too long to be ecoded properly. Changing the *off* periods to all zeros ("0000") will fix this issue.

The following example sends an "ON" command to a Panasonic television using a single string of Pronto Hex Code. You can also provide Pronto Hex Code as an *roArray* of hex values, which results in less work for the script engine.

```
ir = CreateObject("roIRRemote")  

pronto_hex_Panasonic_on_str = " 0000 0071 0000 0032 0080 003F 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0030 0010 0030 0010 0030 0010 0030 0010 0010 0010 0010 0010 0010 0010 0030 0010 0030 0010 0030 0010 0030 0010 0030 0010 0010 0010 0030 0010 0000"

ir.Send("PHC", pronto_hex_lg_on_str)
```