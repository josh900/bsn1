# roAssetRealizerEvent

This event object is returned by the *roAssetRealizer.Realize()* method. It yields information about the success or failure of the realization process.

## ifAssetRealizerEvent

##### GetEvent() As Integer 

Returns an integer value indicating the type of the event:

|     |     |     |
| --- | --- | --- |
| 101 | EVENT\_REALIZE\_SUCCESS | The specified sync list was successfully realized. |
| \-102 | EVENT\_REALIZE\_INCOMPLETE | Realization could not begin because at least one of the required files is not available in the pool. |
| \-103 | EVENT\_REALIZE\_FAILED\_SAFE | Realization has failed. Nothing has been written to the destination, so it is likely safe to continue the realization process. More information is about the failure is available via the `GetFailureReason()` and `GetName()` methods. |
| \-104 | EVENT\_REALIZE\_FAILED\_UNSAFE | Realization has failed while running, and changes have been made to destination files. It may not be safe to continue the realization process. More information about the failure is available via the `GetFailureReason()` and `GetName()` methods. |

##### GetName() As String

Retrieves the name of the affected file if the realization process fails.

##### GetResponseCode() As Integer

Retrieves the *roUrlTransfer* response code associated with the event (if any).

##### GetFailureReason() As String

Returns additional information if the realization process fails.

##### GetFileIndex() As Integer

Retrieves the zero-based index number of the the file in the sync spec.

## ifUserData

##### SetUserData(user\_data As Object) As Void

Sets the user data.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()` (on either the event or source object). It will return Invalid if no data has been set.