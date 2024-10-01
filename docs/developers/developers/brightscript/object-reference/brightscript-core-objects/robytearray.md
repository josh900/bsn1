# roByteArray

This object contains functions for converting strings to or from a byte array, as well as to or from ASCII hex or ASCII base64. 

> [!NOTE]
> If you are converting a byte array to a string, and the byte array contains a zero, the string conversion will end at that point.

The byte array will automatically resize to become larger as needed. If you wish to disable this behavior, use the `SetResize()` method. If an uninitialized index is read, Invalid is returned. 

Since *roByteArray* supports the *ifArray* interface, it can be accessed with the `[]` array operator. The byte array is always accessed as unsigned bytes while this interface is being used. This object also supports the *ifEnum* interface, and so can be used with a `FOR EACH` statement. 

The JavaScript equivalent is `Blob()`. Note that JavaScript now has [typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays) (for example, [Uint8Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)) . 

## ifByteArray

##### WriteFile(file\_path As String) As Boolean

Writes the bytes contained in the byte array to the specified file. This method returns True if successful.

##### WriteFile(file\_path As String, start\_index As Integer, length As Integer) As Boolean

Writes a subset of the bytes contained in the byte array to the specified file. This method writes `length` bytes, beginning at `start_index` of the byte array.

##### ReadFile(file\_path As String) As Boolean

Reads the specified file into the byte array. This operation will discard any data currently contained in the byte array.

##### ReadFile(file\_path As String, start\_index As Integer, length As Integer) As Boolean

Reads a section of the specified file into the byte array. This method reads `length` bytes, beginning at `start_index` of the file. This operation will discard any data currently contained in the byte array.

##### AppendFile(file\_path As String) As Boolean

Appends the contents of the byte array to the specified file.

##### SetResize(minimum\_allocation\_size As Integer, autoresize As Boolean)

Expands the size of the byte array to the `minimum_allocation_size` if it is less than the `minimum_allocation_size`. This method also accepts a Boolean parameter that specifies whether the byte array should be resized automatically or not.

##### ToHexString() As String

Returns a hexadecimal string representation of the contents of the byte array. Each byte is represented as two hex digits.

##### FromHexString(hex\_string As String)

Writes the contents of the passed hexadecimal string to the byte array. The passed string must contain an even number of hex digits. This operation will discard any data currently contained in the byte array.

##### ToBase64String() As String

Returns the contents of the byte array as a base64-formatted string.

##### FromBase64String(base\_64\_string As String)

Writes the contents of a valid base64-formatted string to the byte array. This operation will discard any data currently contained in the byte array.

##### ToAsciiString() As String

Returns the contents of the byte array as an ASCII-formatted string.

##### FromAsciiString(ascii\_string As String)

Writes the contents of a valid ASCII-formatted string to the byte array. This operation will discard any data currently contained in the byte array.

##### GetSignedByte(index As Integer) As Integer

Returns the signed byte at the specified zero-based index in the byte array. To read an unsigned byte within a byte array, use the *ifArrayGet.GetEntry()* method or the `[]` array operator.

##### GetSignedLong(index As Integer) As Integer

Retrieves the integer located at the specified long-word index of the byte array. Note that this method cannot accept a byte index as its parameter.

##### IsLittleEndianCPU() As Boolean

Returns True if the CPU architecture is little-endian.

## ifArray

##### Peek() As Dynamic

Returns the last (highest index) array entry without removing it.

##### Pop() As Dynamic

Returns the last (highest index) entry and removes it from the array.

##### Push(entry As Dynamic)

Adds a new highest index entry to the end of the array.

##### Shift() As Dynamic

Removes index zero from the array and shifts all other entries down by one unit.

##### Unshift(entry As Dynamic)

Adds a new index zero to the array and shifts all other entries up by one unit.

##### Delete(index As Integer) As Boolean

Deletes the indicated array entry and shifts all above entries down by one unit.

##### Count() As Integer

Returns the index of the highest entry in the array plus one (i.e. the length of the array).

##### Clear()

Deletes every entry in the array.

##### Append(array As roArray)

Appends one *roArray* to another. If the passed *roArray* contains entries that were never set to a value, they are not appended.

> [!NOTE]
> The two appended objects must be of the same type.

## ifEnum

##### Reset()

Resets the position to the first element of enumeration.

##### Next() As Dynamic

Returns a typed value at the current position and increment position.

##### IsNext() As Boolean

Returns True if there is a next element.

##### IsEmpty() As Boolean

Returns True if there is not an exact statement.

## ifArrayGet

##### GetEntry(index As Integer) As Dynamic

Returns an array entry of a given index. Entries start at zero. If this method attempts to fetch an entry that has not been set, it will return Invalid.

## ifArraySet

##### SetEntry(index As Integer, entry As Dynamic)

Sets an entry of a given index to the passed type value.