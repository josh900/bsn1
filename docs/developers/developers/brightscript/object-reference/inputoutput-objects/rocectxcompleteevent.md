# roCecTxCompleteEvent

If an *roMessagePort* is attached to an *roCecInterface* instance, it may receive events of type *roCecTxCompleteEvent*.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned by `GetUserData()`.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifCecTxCompleteEvent   

##### GetStatusByte() As Integer

Returns the message data as an integer.

|     |     |
| --- | --- |
| 0   | Transmission successful |
| 128 | Unable to send, CEC hardware powered down |
| 129 | Internal CEC error |
| 130 | Unable to send, CEC line jammed |
| 131 | Arbitration error |
| 132 | Bit-timing error |
| 133 | Destination address not acknowledged |
| 134 | Data byte not acknowledged |