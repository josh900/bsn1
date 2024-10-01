# roSqliteEvent

This event object is returned when a `RunBackground()` operation is called by the associated *roSqliteDatabase* object.

## ifSqliteEvent

##### GetTransactionId() As Integer

Returns an integer that matches the result of the originating `RunBackground()` operation.

##### GetSqlResult() As Integer

Returns the result code returned by the *roSqliteStatement.Run()* method. The possible return values are identical to the `Run()` method:

*   100: Statement complete
    
*   101: Busy
    
*   102: Rows available
    

> [!NOTE]
> This method can be used as the asynchronous alternative to the `Run()` method.