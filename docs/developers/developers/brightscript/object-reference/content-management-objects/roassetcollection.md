# roAssetCollection

This object is used to represent a collection of assets.

Object Creation: The *roAssetCollection* object is created with no parameters.

```
CreateObject("roAssetCollection")
```

You can populate an asset collection with individual calls to `AddAsset()` or `AddAssets()`. You can also populate an asset collection using the *roSyncSpec.GetAssets()* method, as shown below:

```
assetCollection = CreateObject("roAssetCollection")
 
localCurrentSync = CreateObject("roSyncSpec")
if localCurrentSync.ReadFromFile("local-sync.xml") then
	assetCollection = localCurrentSync.GetAssets("download")
endif
```

## ifFailureReason

##### GetFailureReason() As String

Returns additional information if a method fails. 

## ifAssetCollection 

##### AddAsset(asset\_info As Dynamic) As Boolean

Adds a single asset from an associative array or JSON-formatted string. If the argument is a string, it should match the format used for a single asset in a JSON sync spec. Returns true to indicate success and false to indicate failure. If false is returned more detailed information is available by calling the `GetFailureReason` method.

##### AddAssets(asset\_info\_array As Dynamic) As Boolean

Adds multiple assets from an enumerable object (an *roList*, *roArray*, or string containing a JSON-formatted array) that contains compatible associative arrays. Returns true to indicate success and false to indicate failure. If false is returned more detailed information is available by calling the `GetFailureReason` method.

##### GetAssetList() As roList

Returns an *roList* instance containing associative arrays of asset metadata. This method is not efficient and is, therefore, recommended for debugging and diagnostic purposes only.

Each associative array contains the following:

|     |     |     |     |
| --- | --- | --- | --- |
| name | String | Required | The name of the asset. For a file to be realized, it must have a valid filename (i.e. no slashes). |
| link | String | Required | The download location of the asset |
| size | Integer/String | Optional | The size of the asset. Use a string if you want to specify a number that is too large to fit into an integer (this allows file sizes larger than 2 GB). |
| hash | String | Optional | A string in the form of "hash\_algorithm:hash". See the next table for available hash algorithms. |
| change\_hint | String | Optional | Any string that will change in conjunction with the file contents. This is not necessary if the link or hash is supplied and always changes. |
| auth\_inherit | Boolean | Optional | Indication of whether or not this asset uses *roAssetFetcher* authentication information. The default is set to True. |
| auth\_user | Boolean | Optional | User to utilize for authentication when downloading only this asset. This automatically disables "auth\_inherit". |
| auth\_password | Boolean | Optional | Password to use when downloading only this asset. This automatically disables "auth\_inherit". |
| headers\_inherit | Boolean | Optional | The command to pass any header supplier to *roAssetFetcher* when fetching this asset. The default is true. |

> [!CAUTION]
> **Important**
> Any "optional" fields that are specified when populating the pool must also be specified when retrieving assets from the pool (i.e. they become "mandatory" once they are used for an asset). For example, if the hash value is specified when fetching into the pool, then it must also be specified when attempting to refer to files in the pool.

Hash algorithms:

|     |     |
| --- | --- |
| sha1 | If a sha1 is available, you can validate the hash as the file is downloaded. If such a hash is available, it should be used. The link and change\_hint properties have no effect on the pool file name, so the file is shared even if it is downloaded from different locations. |
| besha1 | This algorithm hashes some of the file along with the file size in order to verify the contents. It also moves the link and change\_hint properties into the pool filename. |
| MD5 | Uses the MD5 hash algorithm to validate files. |
| (none) | Without any hash, the file cannot be verified as it is downloaded, and the system will rely on the link and change\_hint properties to give the pool a unique filename. |