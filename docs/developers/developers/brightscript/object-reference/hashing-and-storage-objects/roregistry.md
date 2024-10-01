# roRegistry

The registry is an area of memory where a small number of persistent settings can be stored. Access to the registry is available through the *roRegistry* object. The JavaScript equivalent is [registry](https://docs.brightsign.biz/display/DOC/registry) (see [BrightScript-JavaScript Migration Guide](../../../../developers/player-apis/brightscript-javascript-migration-guide.md) for the method equivalents).

This object is created with no parameters:

```
CreateObject("roRegistry")
```

## ifRegistry

##### GetSectionList() As roList

Returns a list with one entry for each registry section.

##### Delete(section As String) As Boolean

Deletes the specified section and returns an indication of success.

##### Flush() As Boolean

Flushes the registry out to persistent storage.