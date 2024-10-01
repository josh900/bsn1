# roReadFile

Object Creation: Creating an *roReadFile* object opens the specified file for reading only. Object creation fails if the file does not exist. 

```
CreateObject("roReadFile", filename As String)
```

## ifStreamRead

##### SetReceiveEol(eol\_sequence As String) As Void

Sets the EOL sequence when reading from the stream. The default EOL character is CR LF, (ASCII values 13 then 10). If you need to set this value to a non-printing character, use the `chr()` [global function](../../object-reference/global-functions.md).

##### ReadByte() As Integer

Reads a single byte from the stream, blocking if necessary. If the EOF is reached or there is an error condition, then a value less than 0 is returned.

##### ReadByteIfAvailable() As Integer

Reads a single byte from the stream if one is available. If no bytes are available, it returns immediately. A return value less than 0 indicates either that the EOF has been reached or no byte is available.

##### ReadLine() As String

Reads until it finds a complete end of the line sequence. If it fails to find the sequence within 4096 bytes, then it returns the 4096 bytes that are found. No data is discarded in this case.

##### ReadBlock(size As Integer) As String

Reads the specified number of bytes. The number is limited to 65536 bytes. In the event of an EOF or an error, fewer bytes than requested will be returned. Any null bytes in the file will mask any further bytes.

##### AtEof() As Boolean

Returns True if an attempt has been made to read beyond the end of the file. If the current position is at the end of the file, but no attempt has been made to read beyond it, this method will return False.

## ifStreamSeek

##### SeekAbsolute(offset As Integer) As Void

Seeks the specified offset. If the offset is beyond the end of the file, then the file will be extended upon the next write and any previously unoccupied space will be filled with null bytes.

##### SeekRelative(offset As Integer) As Void

Seeks to the specified offset relative to the current position. If the ultimate offset is beyond the end of the file, then the file will be extended as described in `SeekAbsolute()`.

##### SeekToEnd() As Void

Seeks to the end of the file.

##### CurrentPosition() As Integer

Retrieves the current position within the file.