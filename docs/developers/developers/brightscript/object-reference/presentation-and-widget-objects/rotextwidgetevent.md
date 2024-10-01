# roTextWidgetEvent

This event object is generated when a string or surface leaves the screen area of an *roTextWidget* instance.

## ifWidgetEvent

##### GetStringId() As Integer

Returns the ID of the string or surface that has disappeared from the screen.

## ifUserData

##### SetUserData(user\_data As Object) As Void

Sets the user data.

##### GetUserData() As Objecta

Returns the user data that has previously been set via `SetUserData()` (on either the event or source object). It will return Invalid if no data has been set.