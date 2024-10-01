# roAssetPoolFiles

This object allows for interacting with files in an asset pool. The JavaScript equivalent is [assetpoolfiles](../../../../developers/player-apis/javascript-apis/assetpoolfiles.md).

Object Creation: The *roAssetPoolFiles* object is created with two parameters.

```
CreateObject("roAssetPoolFiles", pool As roAssetPool, assets As Dynamic)
```

The `assets` argument can be either an *roAssetCollection* or *roSyncSpec* object. If multiple object instances requires use of an *roAssetCollection* instance, it will be more efficient to convert *roSyncSpec* to *roAssetCollection* by calling `GetAssets()` once and then passing that collection to all object instances requiring it.

This object works similarly to the *roSyncPoolFiles* object.

## ifAssetPoolFiles

##### GetFailureReason() As String

Returns explanatory text if `GetPoolFilePath()` returns an empty string or `GetPoolFileInfo()` returns Invalid.

##### MoveFileIntoPool(source\_filename As String, asset\_name As String) As Boolean

Moves an arbitrary file into the appropriate location in the asset pool. The source file must be in the same filesystem as the asset pool. This method accepts two parameters:

*   `source_filename` string: The path of an existing file in the filesystem
    
*   `asset_name` string: The name of an asset within the asset collection associated with the *roAssetPoolFiles* instance. If the asset size is known, it will be checked against the source file. The move operation will fail if the `asset_name` does not match any asset in the pool or if the file size does not match the known asset size.
    

This method returns `true` on success and `false` on failure. Use the `GetFailureReason()` method to retrieve an error description.

##### GetPoolFilePath(asset\_name As String) As String

Looks up the specified file name in the asset collection and uses the information to determine the actual name of the file in the pool. This method returns an empty string if the name is not found in the asset collection, or if the file is not found in the pool.

##### GetPoolFileInfo(asset\_name As String) As Object

Looks up the specified file name in the asset collection and returns all available information, including the pool file path, as an associative array. This method returns Invalid if the asset name is not found in the asset collection. If the file is not found in the pool, information from the asset collection will be returned without the pool path. See the table below for a description of assets in the associative array.

|     |     |     |
| --- | --- | --- |
| **Field** | **Value** | **Description** |
| name | String | Asset name |
| link | String | Asset URL |
| size | String |     |
| hash | String | Hash in algorithm ":" hash format |
| change\_hint | String | Only present if set |
| auth\_user | String | Only present if set |
| auth\_password | String | Only present if set |
| auth\_inherit | Boolean |     |
| headers\_inherit | Boolean |     |
| probe | String | Probe data |
| path | String | Absolute path of the file in the pool (or "invalid" if the file is not in the pool) |