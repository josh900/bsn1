# roControlUp, roControlDown

These objects are posted by an [*roControlPort*](../inputoutput-objects/rocontrolport.md) instance to the configured message port when inputs change state. An *roControlDown* event is posted when the input level goes from high to low. An *roControlUp* event is posted when the input level goes from low to high.

## ifInt

##### GetInt() As Integer

Retrieves the pin number associated with the event.

##### SetInt(value As Integer) As Void

Sets the value of the event.

## ifUserData

##### SetUserData(user\_data As Object) As Void

Sets the user data.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()` (on either the event or source object). It will return Invalid if no data has been set.

## ifSourceIdentity

##### GetSourceIdentity() As Integer

Retrieves the identity value that can be used to associate events with the source *roControlPort* instance.

> [!NOTE]
> The *ifSourceIdentity* interface has been deprecated. We recommend using the *ifUserData* interface instead.