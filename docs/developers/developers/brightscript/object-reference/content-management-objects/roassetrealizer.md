# roAssetRealizer

This object contains functions for realizing files (i.e. extracting files from an asset pool and placing them into the standard file directory). Realizing a complete asset pool is not recommended because the process can be slow. Instead, the script should retrieve pool file locations using the *roAssetPoolFiles* object and use them to refer to files directly. The *roAssetRealizer* object is still useful for realizing files that must be in the root directory to work (e.g. autorun and firmware update files). The JavaScript equivalent is [assetrealizer](https://docs.brightsign.biz/display/DOC/assetrealizer).

Object Creation: The *roAssetRealizer* object requires two parameters upon creation: an *roAssetPool* object and a destination directory.

```
CreateObject("roAssetRealizer", pool As roAssetPool, destination_directory As String)
```

##### **Example**

```
pool = CreateObject("roAssetPool", "pool")
realizer = CreateObject ("roAssetRealizer", pool, "/")
```

## IfUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifAssetRealizer

##### GetFailureReason() As String

Yields additional useful information if a function return indicates an error.

##### EstimateRealizedSizeInMegabytes(spec As Object) As Integer

Returns the estimated amount of space that would be taken up by the specified sync spec.

##### Realize(spec As roSyncSpec/roAssetCollection) As roAssetRealizerEvent

Places the files into the destination directory specified in the passed *roSyncSpec* or *roAssetCollection*. If the pool does not contain the full set of required files, then this method will immediately fail before any files are changed (this method attempts to do as much work as possible before destructively modifying the file system). This method automatically checks the length of the file and any hashes that match the specification. If there is a mismatch, then the affected file is deleted and realization fails. This method indicates success or failure by returning an *roAssetRealizerEvent* object.

> [!NOTE]
> The pool and the destination must be in the same file system.

##### ValidateFiles(spec As Object, options As Object) As roAssociativeArray

Checks the hash of every file in the spec against the corresponding file in the destination path and returns an associative array containing each mismatched file name mapped to the reason. The options parameter is an *roAssociativeArray*, which can currently support a single option:

*   "DeleteCorrupt": Automatically deletes any files that do not match the expected hash. By default, these files are not deleted.