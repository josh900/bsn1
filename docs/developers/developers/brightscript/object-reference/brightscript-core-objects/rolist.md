# roList

This object functions as a general-purpose, doubly linked list. It can be used as a container for arbitrary-length lists of BrightSign objects. The array operator \[ \] can be used to access any element in an ordered list. 

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

##### Clear()

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

Returns the last (highest index) list entry without removing it.

##### Pop() As Dynamic

Returns the last (highest index) entry and removes it from the list.

##### Push(entry As Dynamic)

Adds a new highest-index entry to the end of the list.

##### Shift() As Dynamic

Removes index zero from the list and shifts all other entries down by one unit.

##### Unshift(entry As Dynamic)

Adds a new index zero to the list and shifts all other entries up by one unit.

##### Delete(index As Integer) As Boolean

Deletes the indicated list entry and shifts all above entries down by one unit.

##### Count() As Integer

Returns the length of the list (i.e. the index of the highest entry in the list plus one).

##### Clear()

Deletes every entry in the list.

##### Append(list As roList)

Appends one *roList* to another. If the passed *roList* contains entries that were never set to a value, they are not appended.

> [!NOTE]
> The two appended objects must be of the same type.

## ifArrayGet 

##### GetEntry(a As Integer) As Dynamic

Returns a list entry of a given index. Entries start at zero. If an entry that has not been set is fetched, Invalid is returned.

## ifArraySet

##### SetEntry(a As Integer, b As Dynamic)

Sets an entry of a given index to the passed type value.

## Example

```
list = CreateObject("roList")
list.AddTail("a")
list.AddTail("b")
list.AddTail("c")
list.AddTail("d") 
list.ResetIndex()
x= list.GetIndex()
while x <> invalid
print x
x = list.GetIndex()
end while 
print list[2]
```