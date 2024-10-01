# roSystemLog

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This object enables recording of the system log on a BrightSign player. Note that BrightScript `print` values are not written to the system log; use the *ifStreamSend* methods to write to the log instead.

Object Creation: This object is created with no parameters:

```
CreateObject("roSystemLog")
```

## ifSystemLog

##### ReadLog() As roArray

Returns an array of strings. The strings correspond to lines in the system log, spanning from bootup to the most recent entry.

##### ReadNextLine() As String

Reads the next line of the recorded system log.

## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

Sets the EOL sequence when writing to the stream. The default value is CR+LF. If you need to set this value to a non-printing character, use the `chr()` [global function](../../object-reference/global-functions.md).

##### SendByte(byte As Integer) As Void

Writes the specified byte to the stream.

##### SendLine(string As String) As Void

Writes the specified characters to the stream followed by the current EOL sequence.

##### SendBlock(a As Dynamic) As Void

Writes the specified characters to the stream. This method can support either a string or an *roByteArray*. If the block is a string, any null bytes will terminate the block.

##### Flush() As Void

Writes the stream to the file, blocking execution until all data is written out.

## Writing to a Remote Syslog Server

BrightSign players can write to a remote syslog server using the standard syslog protocol (RFC 3164). To configure remote logging, write the "syslog" entry to the "networking" section of the [player registry](../../object-reference/hashing-and-storage-objects/roregistrysection.md):

##### **Example**

```
registry = CreateObject("roRegistrySection", "networking")
registry.Write("syslog", "my-syslog-server")
registry.Flush()
```

You can specify the syslog using either its IP address or hostname.