# roSequenceMatchEvent

  

This object is generated whenever *roSequenceMatcher* matches a specified byte sequence pattern. 

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned by `GetUserData()`.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.