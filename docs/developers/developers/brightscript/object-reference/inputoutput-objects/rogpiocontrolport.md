# roGpioControlPort

> [!CAUTION]
> **Important**
> New scripts should use *roControlPort* instead of *roGpioControlPort*.

This object is used to control and wait for events on the BrightSign generic GPIO control port. Typically, LEDs or buttons are connected to the GPIO port. Turning on a GPIO output changes the voltage on the GPIO port to 3.3V. Turning off a GPIO output changes the voltage on the GPIO port to 0V.

The GPIO ports are bidirectional and must be programmed as either inputs or outputs. The IDs range from 0–7. The `SetWholeState()` method will overwrite any prior output settings. The `SetOutputState()` takes an output ID (1, 2, or 6, for example). The `SetWholeState()` method takes a mask (for example, `SetWholeState(SetWholeState(2^1 + 2^2)` will set IDs 1 and 2).

The JavaScript equivalent is [controlport](../../../../developers/player-apis/javascript-apis/controlport.md).

## ifMessagePort

##### SetPort(obj As Object) As Void

## ifGpioControlPort

##### IsInputActive(input\_id As Integer) As Boolean  
 

##### GetWholeState() As Integer  
 

##### SetOutputState(output\_id As Integer, onState As Boolean) As Void  
 

##### SetWholeState(on\_state As Integer) As Void  
 

##### EnableInput(input\_id As Integer) As Boolean  
 

##### EnableOutput(output\_id As Integer) As Boolean

  

#####