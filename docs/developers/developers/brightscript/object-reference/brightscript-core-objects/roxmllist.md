# roXMLList

The JavaScript equivalent to this object is `DOMParser()`.

## ifXMLList

##### Simplify() As Object

Returns an *roXmlElement* if the list contains exactly one element. Otherwise, it will return itself.

##### GetAttributes() As Object  
 

##### GetText() As String  
 

##### GetChildElements() As Object  
 

##### GetNamedElements(a As String) As Object

Returns a new XMLList that contains all *roXmlElements* that match the name of the passed element. This action is the same as using the dot operator on an *roXmlList*.

##### GetNamedElementsCi(a As String) As Object

## ifList

##### Count() As Integer

Returns the number of elements in the list.

##### ResetIndex() As Boolean

Resets the current index or position in the list to the head element.

##### AddTail(obj As Object) As Void

Adds a typed value to the tail of the list.

##### AddHead(obj As Object) As Void

Adds a typed value to the head of the list.

##### RemoveIndex() As Object

Removes an entry from the list at the current index or position and increments the index or position in the list. It returns Invalid when the end of the list is reached.

##### GetIndex() As Object

Retrieves an entry from the list at the current index or position and increments the index or position in the list. It returns Invalid when the end of the list is reached.

##### RemoveTail() As Object

Removes the entry at the tail of the list.

##### RemoveHead() As Object

Removes the entry at the head of the list.

##### GetTail() As Object

Retrieves the entry at the tail of the list and keeps the entry in the list.

##### GetHead() As Object

Retrieves the entry at the head of the list and keeps the entry in the list.

##### Clear() As Void

Removes all elements from the list.

## ifEnum

##### Reset()

Resets the position to the first element of enumeration.

##### Next() As Dynamic

Returns a typed value at the current position and increment position.

##### IsNext() As Boolean

Returns True if there is a next element.

##### IsEmpty() As Boolean

Returns True if there is not an exact statement.

## ifArray

##### Peek() As Dynamic

Returns the last (highest index) array entry without removing it.

##### Pop() As Dynamic

Returns the last (highest index) entry and removes it from the array.

##### Push(a As Dynamic)

Adds a new highest index entry to the end of the array.

##### Shift() As Dynamic

Removes index zero from the array and shifts all other entries down by one unit.

##### Unshift(a As Dynamic)

Adds a new index zero to the array and shifts all other entries up by one unit.

##### Delete(a As Integer) As Boolean

Deletes the indicated array entry and shifts all above entries down by one unit.

##### Count() As Integer

Returns the index of the highest entry in the array plus one (i.e. the length of the array).

##### Clear() As Void

Deletes every entry in the array.

##### Append(a As Object) As Void

Appends one *roArray* to another. If the passed *roArray* contains entries that were never set to a value, they are not appended.

> [!NOTE]
> The two appended objects must be of the same type.

## ifArrayGet 

##### GetEntry(a As Integer) As Dynamic

Returns an array entry of a given index. Entries start at zero. If an entry that has not been set is fetched, Invalid is returned.

## ifArraySet

##### SetEntry(a As Integer, b As Dynamic) As Void

Sets an entry of a given index to the passed type value.