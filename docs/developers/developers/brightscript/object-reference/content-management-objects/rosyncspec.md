# roSyncSpec

This object represents a parsed sync spec. It allows you to retrieve various parts of the specification with methods.

## ifSyncSpec

##### GetFailureReason() As String

Returns information if an *roSyncSpec* method indicates failure.

##### ReadFromFile(filename As String) As Boolean

Populates the sync spec by reading the specified file. This method returns True upon success and False upon failure.

##### ReadFromString(spec As String) As Boolean

Populates the sync spec by reading the passed string. This method returns True upon success and False upon failure.

##### WriteToFile(filename As String) As Boolean

Writes out the current sync spec to the specified file as XML. Because the XML is regenerated, it is possible this file may not be textually identical to the specification that was read. This method returns True upon success and False upon failure.

##### WriteToFile(filename As String, options As roAssociativeArray) As Boolean

Writes out the current sync spec to the specified file as XML or JSON. The `options` associative array can currently contain the `format` parameter, which can have a value of "xml" or "json". Because the XML/JSON is regenerated, it is possible this file may not be textually identical to the specification that was read. This method returns True upon success and False upon failure.

##### WriteToString() As String

Writes out the current sync spec to a string and returns it as XML. This method returns an empty string if the write operation fails.

##### WriteToString(options As roAssociativeArray) As String

Writes out the current sync spec to a string and returns it as XML or JSON. The `options` associative array can currently contain the `format` parameter, which can have a value of "xml" or "json". This method returns an empty string if the write operation fails.

##### GetMetadata(section As String) As roAssociativeArray

Returns an *roAssociativeArray* object containing the information stored in the specified metadata section of the sync spec (typically "client" or "server"). This method returns 0 if the read operation fails.

If the sync spec is formatted as XML, then all returned values will be strings. If the spec spec is formatted as JSON, the JavaScript types will be converted as follows:

| JavaScript type | BrightScript type |
| --- | --- |
| Array | roArray |
| Object | roAssociativeArray |
| String | String |
| Boolean | Boolean |
| Number | Double |
| Null | Invalid |

##### LookupMetadata(section As String, field As String) As String

Provides a shortcut for looking up specified metadata items in the specified section without needing to create a temporary *roAssociativeArray* object. This method returns an empty string if the read operation fails.

##### GetFileList(section As String) As roList

Returns an *roList* object containing *roAssociativeArray* objects for each file in the specified section of the sync spec. This method returns Invalid if the read operation fails.

##### GetFile(section As String, index As Integer) As roAssociativeArray

Returns an *roAssociativeArray* object for the file in the specified section and at the specified index. This method returns Invalid if the read operation fails.

##### GetName() As String

Returns the name supplied for the sync spec in the <sync> XML element.

##### EqualTo(other As roSyncSpec) As Boolean

Compares the contents of the *roSyncSpec* object with another *roSyncSpec* object. This method compares the parsed contents of each sync spec rather than the XML files themselves.

##### VerifySignature(signature as String, obfuscated\_passphrase as String) As Boolean

De-obfuscates the passphrase and uses it to verify the signature of the sync spec. This method returns True upon success and False upon failure.

##### FilterFiles(section As String, criteria As roAssociativeArray) As roSyncSpec

Returns a new *roSyncSpec* object that is a copy of the existing object, except that the specified section is filtered using the specified criteria. The criteria are matched against the file metadata. Multiple criteria can be specified in the passed associative array, and all criteria must be met for a file to be returned with the new *roSyncSpec*.

The following call will yield an *roSyncSpec* object with a "download" section that has been filtered so that only files of the group "scripts" will remain.

```
filtered_spec = spec.FilterFiles("download", { group: "scripts" })
```

##### FilesEqualTo(spec As roSyncSpec) As Boolean

Compares the contents of the sync spec to another sync spec and returns `true` if they're identical. This method compares the parsed contents of the sync specs, rather than the XML/JSON itself.

##### GetAssets(section As String) As Object

Retrieves a list of assets from the sync spec in a form that's compatible with *roAssetPool* and its associated objects.