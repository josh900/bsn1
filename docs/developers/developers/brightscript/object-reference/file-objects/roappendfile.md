# roAppendFile

This object can be used to create a new file or append information to the end of an existing file.

Object Creation: Creating an *roAppendFile* object opens an existing file or creates a new file. The current position is set to the end of the file, and all writes are made to the end of the file.

```
CreateObject("roAppendFile", filename As String)
```

## ifStreamSend

##### SetSendEol(eol\_sequence As String) As Void

Sets the EOL sequence when writing to the stream. The default value is CR+LF. If you need to set this value to a non-printing character, use the `chr()` [global function](../../object-reference/global-functions.md).

##### SendByte(byte As Integer) As Void

Writes the specified byte to the stream.

##### SendLine(string As String) As Void

Writes the specified characters to the stream followed by the current EOL sequence.

##### SendBlock(a As Dynamic) As Void

Writes the specified characters to the stream. This method can support either a string or an *roByteArray*. If the block is a string, any null bytes will terminate the block.

##### Flush() As Void

Writes the stream to the file, blocking execution until all data is written out. 

##### AsyncFlush() As Void

Writes the stream to the file within a few seconds. The system will not block execution while writing to the file.

> [!NOTE]
> The system performs an asynchronous flush automatically when the object instance is destroyed (for instance, when the the variable containing it is reassigned). The stream is first written to the kernel, which then writes it to the file system when resources are available.

## ifStreamPosition

##### CurrentPosition() As Integer

Returns the current position within the file.