# roCecRxFrameEvent

If an *roMessagePort* is attached to an *roCecInterface* instance, it may receive events of type *roCecRxFrameEvent*.

## ifCecRxFrameEvent

##### GetByteArray() As roByteArray

Returns the message data as an *roByteArray*.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned by `GetUserData()`.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.