# roIRDownEvent, roIRRepeatEvent, roIRUpEvent

An IR event object is generated when an IR button input (button press, button repeat, button release) is received by the *roIRReceiver* object. Use these objects to retrieve the message body of the IR input. 

> [!NOTE]
> The *roIRUpEvent* object is generated with the Iguanaworks IR transceiver only.

## ifInt

##### GetCode() As Integer

Returns the IR code received by the *roIRReceiver* instance.

##### SetCode(a As Integer)

Overrides the IR code received by the *roIRReceiver* instance, replacing it with the specified binary code. 

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned by `GetUserData()`.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set. 

## ifReceivedEvent

##### GetEncoding() As String

Returns the encodings setting of the *roIRReceiver* instance. This setting can be one of the following strings:

*   "NEC"
    
*   "RC5" (supported on the Iguanaworks IR transceiver only)