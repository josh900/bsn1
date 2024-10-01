# roSqliteStatement

This object is created by calling the `CreateStatement()` method on an *roSqliteDatabase* object. The JavaScript equivalent is to use the IndexedDB.

## ifSqliteStatement

All *bind* methods return True upon success.

##### BindByName(associative\_array As Object) As Boolean

Binds the SQL variable(s) using the names contained in the SQL statement.

##### BindByOffset(associative\_array/enumerable As Object) As Boolean

Binds the SQL variable(s) using the index contained in the SQL statement. If passed an associative array, this method will convert the keys of the associative array into numeric offsets when binding. If passed an enumerable object (e.g. *roArray*), it will bind the values of the enumerable in the order that they are stored.

##### BindText(variable/index As Object, value As String) As Boolean

Binds the SQL variable indicated by the name or index parameter to the passed string value.

##### BindInteger(variable/index As Object, value As Integer) As Boolean

Binds the SQL variable indicated by the name or index parameter to the passed integer value.

##### Run() As Integer

Runs the SQL statement immediately and waits for the integer result. The following are possible integer result codes:

*   100: Statement complete
    
*   101: Busy
    
*   102: Rows available
    

##### RunBackground() As Integer

Runs the SQL statement in the background. You can use *roSqliteDatabase.SetPort()* to set a message port that will receive an *roSqliteEvent* message at a later point. The RunBackground() call will result in an integer transaction ID, which will appear in the *roSqliteEvent* message that matches the transaction.

##### GetData() As Object

Returns an associative array of name/value pairs that are available after a SELECT (or similar) operation.

##### Finalise()

Finalizes the statement. This method should be applied to statements before the parent database is closed. The object should not be used after this method is called. Also note that objects are automatically finalized when they are deleted.

## Examples

The following script inserts into a table using the `BindByName()` method:

```
insertStmt = db.CreateStatement("INSERT INTO playback (md5,path,playback_count) VALUES(:md5_param,:path_param,:pc_param);")

print insertStmt

if type(insertStmt) <> "roSqliteStatement" then
    print "We didn't get a statement returned!!"
    end
endif

params = { md5_param: "ABDEF12346",  path_param: "/foo/bar/bing/bong", pc_param: 11 }

bindResult = insertStmt.BindByName(params)

if bindResult
    print "BindByName OK"
else
    print "BindByName FAILED"
    end
endif

sqlResult = insertStmt.Run()

print sqlResult

if sqlResult = SQLITE_COMPLETE
    print "Table Insertion OK"
else
    print "Table Insertion FAILED"
endif

insertStmt.Finalise()
```

The following script inserts into a table in the background:

```
' This examples assume you have set a message port on your roSqliteDatabase instance
'

insertStmt = db.CreateStatement("INSERT INTO playback (md5,path,playback_count) VALUES(:md5_param,:path_param,:pc_param);")

print insertStmt

if type(insertStmt) <> "roSqliteStatement" then
    print "We didn't get a statement returned!!"
    end
endif

params = { md5_param: "ABDEF12348",  path_param: "/foo/bar/bing/bong", pc_param: 13 }

bindResult = insertStmt.BindByName(params)

if bindResult
    print "BindByName OK"
else
    print "BindByName FAILED"
    end
endif

expectedId = insertStmt.RunBackground()

e = mp.WaitMessage(10000)
if e <> invalid then
    if type(e) = "roSqliteEvent" then
        transId = e.GetTransactionId()
        sqlResult = e.GetSqlResult()
        print transId
        print sqlResult
        if transId <> expectedId then
            print "Incorrect transaction Id"
            end
        endif
        if sqlResult <> SQLITE_COMPLETE then
            print "SQL Insertion Failed"
            end
        endif
    else
        print "RunBackground() - Wrong event - FAILED"
        end
    endif
else
    print "RunBackground() - No Response - FAILED"
    end
endif

' You don't need to call Finalise() since that'll be done by the background processor.
```

The following script queries from a table:

```
selectStmt = db.CreateStatement("SELECT * FROM playback;")

if type(selectStmt) <> "roSqliteStatement" then
    print "We didn't get a statement returned!!"
    end
endif

sqlResult = selectStmt.Run()

print sqlResult

while sqlResult = SQLITE_ROWS
    resultsData = selectStmt.GetData()
    print resultsData;
    sqlResult = selectStmt.Run()
end while

selectStmt.Finalise()
```