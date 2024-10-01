# roAssetPool

An *roAssetPool* instance represents a pool of files for synchronization. You can instruct this object to populate the pool based on a sync spec and then realize it in a specified directory when required. The JavaScript equivalent is [assetpool](https://docs.brightsign.biz/display/DOC/assetpool).

Object Creation: The *roAssetPool* object is created with a single parameter representing the rooted path of the pool.

```
CreateObject("roAssetPool", pool_path As String)
```

Example:

```
pool = CreateObject ("roAssetPool", "SD:/pool")
```

## ifAssetPool

##### GetFailureReason() As String  
 

##### ProtectAssets(name As String, collection As Object) As Boolean

Requests that the files specified in the "download" section of a sync spec receive a certain amount of protection. Specified files will not be deleted when the system software needs to reduce the size of the pool to make space.

##### UnprotectAssets(name As String) As Boolean

Removes the protected status placed on the specified files by the `ProtectAssets()` method. Asset collections are reference counted at the system-software level. As a result, when calling `UnprotectAssets()`, you must pass the same object that you previously passed to `ProtectAssets()`.

##### UnprotectAllAssets() As Boolean

Removes the protected status placed on any files in the asset pool using the `ProtectAssets()` method. 

##### ReserveMegabytes(size As Integer) As Boolean

Reserves the specified amount of storage space. This method is dynamic: The system software attempts to keep the space free even when parallel processes are filling up the storage.

##### SetMaximumPoolSizeMegabytes(maximum\_size As Integer) As Boolean

Specifies the maximum size of an *roAssetPool* instance in megabytes. This method is more resource-intensive than `ReserveMegabytes()`, but it is useful when creating multiple pools on a storage device.

##### GetPoolSizeInMegabytes() As Integer

Returns the current size of the asset pool (in megabytes). 

##### Validate(sync\_spec As Object, options As roAssociativeArray) As Boolean

Checks the SHA1, BESHA1, or MD5 hash value of files that are in the sync spec and are currently present in the pool. This method returns True if all checks pass and False if one or more checks fail. Calling `GetFailureReason()` will return information about the corrupt file(s). Note that a True return may not mean that all files in the sync spec are currently present in the pool. The second parameter represents a table of validation options: The key specifies the option and the value specifies whether the option is enabled or not (as a Boolean value). Currently, the only option is "DeleteCorrupt", which determines whether the method should automatically delete corrupt files or not.

##### QueryFiles(sync\_spec As roAssociativeArray) As roAssociativeArray

Determines whether the specified files are present in the asset pool. This method returns an associative array with filename keys and corresponding Boolean values.

##### AssetsReady(collection As Object) As Boolean

Returns `true` if the specified files are ready in the asset pool.