# roDiskErrorEvent

This object is returned while waiting on a message port that is connected to an *roDiskMonitor* object.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set

## ifDiskErrorEvent

##### GetDiskError() As Object

Returns an *roAssociativeArray* containing the following parameters:

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Description** |
| source | *roString* | The error type |
| time | *roDateTime* | The time at which the error occurred (with millisecond accuracy) |
| device | *roString* | The internal name for the device generating the error |
| error | *roString* | A description of the error (e.g."Timeout") |
| param | *roString* | The error parameter (use depends on type of error (e.g. the sector number)) |

Example:

```
aa = msgp.GetDiskError()
report = "Time: " + aa["Time"] + "Error: " + aa["source"] + " " + aa["error"] + " " + aa["device"] + " " + aa["param"]
```

> [!NOTE]
> This example uses an implicit conversion of *roDateTime*. You could also use *roDateTime.GetString()*.