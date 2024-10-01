# roRegistrySection

This object represents a section of the registry, enabling the organization of settings within the registry. It allows the section to be read or written. The JavaScript equivalent is [registry](https://docs.brightsign.biz/display/DOC/registry) (see [BrightScript-JavaScript Migration Guide](../../../../developers/player-apis/brightscript-javascript-migration-guide.md) for the method equivalents).

Object Creation: This object must be supplied with a registry-section name upon creation.

```
CreateObject("roRegistrySection", section As String)
```

Writes do not always take effect immediately to prevent the system from exceeding the maximum number of writes on the onboard persistent storage. At most, 60 seconds after a write to the registry, the newly written data will be automatically written out to persistent storage. If, for some reason, the change must be written immediately, then the `Flush()` method should be called. All changes will be written automatically prior to exiting the application.

## ifRegistrySection

##### Read(key As String) As String

Reads and returns the value of the specified key. Performing `Read()` on an entry that does not exist, or on a key within a section that does not exist, will return an empty string ("").

##### Write(key As String, value As String) As Boolean

Replaces the value of the specified key.

##### Delete(key As String) As Boolean

Deletes the specified key.

##### Exists(key As String) As Boolean

Returns True if the specified key exists.

##### Flush() As Boolean

Flushes the contents of the registry out to persistent storage.

##### GetKeyList() As roList

Returns a list containing one entry per registry key in this section.

##### **Example**

```
registrySection = CreateObject("roRegistrySection", "widget-usage")
' An empty entry will read as an empty string and therefore be converted to zero.
hits = val(registrySection.Read("big-red-button-hits"))
hits = hits + 1
registrySection.Write("big-red-button-hits", strI(hits))
```