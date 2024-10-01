# roSqliteDatabase

This is the main SQLite object that "owns" the database. You can create as many of these objects as you need. The JavaScript equivalent is to use the IndexedDB.

## ifSqliteDatabse

##### Open(path As String) As Boolean

Opens an existing database file. This method returns `True` upon success.

##### Create(path As String) As Boolean

Creates a new, empty database file. This method returns `True` upon success.

Passing `":memory:"` to this method creates a database in non-persistent storage. This is useful for high-volume database applications that might cause wear issues on an SD card. 

##### Close()

Closes an open database.

##### CreateStatement(sql\_text As String) As Object

Creates a new *roSqliteStatement* object using the specified SQL string.

##### RunBackground(sql\_text As String, associative\_array As Object) As Integer

Runs the specified SQL statement in the background and binds variables using the passed *roAssociativeArray*.

##### SetMemoryLimit(limit As Integer)

Sets the "soft" memory limit under which SQLite will attempt to remain (see the SQLite documentation for details).

> [!NOTE]
> The `SetMemoryLimit()` method sets global parameters. It must, therefore, be called before any other calls are made on the database object.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roSqliteEvent*  to the attached message port.

## Examples

Creating a database:

```
db = CreateObject("roSqliteDatabase")
 
print db
 
openResult = db.Create("SD:/test.db")
 
if openResult
    print "Created OK"
else
    print "Creation FAILED"
    end
endif
```

Creating a table in a database:

```
createStmt = db.CreateStatement("CREATE TABLE playback (md5 text PRIMARY KEY, path PATH, playback_count INT);")

print createStmt

if type(createStmt) <> "roSqliteStatement" then
    print "We didn't get a statement returned!!"
    end
endif

sqlResult = createStmt.Run()

print sqlResult

if sqlResult = SQLITE_COMPLETE
    print "Table Created OK"
else
    print "Table Creation FAILED"
endif

createStmt.Finalise()
```