# roArray

This object stores objects in a continuous array of memory locations. Since an *roArray* contains BrightScript components, and there are object wrappers for most intrinsic data types, entries can either be different types or all of the same type. 

Object Creation: The *roArray* object is created with two parameters. 

```
CreateObject("roArray", size As Integer, resize As Boolean)
```

*   `size`: The initial number of entries allocated for the array.
    
*   `resize`: If true, the array will be resized larger to accommodate more entries if needed. If the array is large, this process might take some time.
    

The [DIM](../../../brightscript/language-reference/program-statements.md) statement may be used instead of the `CreateObject()` function to create a new array. The `DIM` statement can be advantageous because it automatically creates array-of-array structures for multi-dimensional arrays. 

## ifArray

##### Peek() As Dynamic

Returns the last (highest index) array entry without removing it.

##### Pop() As Dynamic

Returns the last (highest index) entry and removes it from the array.

##### Push(entry As Dynamic)

Adds a new highest-index entry to the end of the array.

##### Shift() As Dynamic

Removes index zero from the array and shifts all other entries down by one unit.

##### Unshift(entry As Dynamic)

Adds a new index zero to the array and shifts all other entries up by one unit.

##### Delete(index As Integer) As Boolean

Deletes the indicated array entry and shifts all above entries down by one unit.

##### Count() As Integer

Returns the length of the array (i.e. the index of the highest entry in the array plus one).

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

Returns a typed value at the current position and increments the position.

##### IsNext() As Boolean

Returns True if there is a next element.

##### IsEmpty() As Boolean

Returns True if there is not an exact statement.

## ifArrayGet

##### GetEntry(index As Integer) As Dynamic

Returns an array entry of a given index. Entries start at zero. If the entry at the specified index has not been set, this method will return Invalid.

## ifArraySet

##### SetEntry(a As Integer, b As Dynamic)

Sets an entry of a given index to the passed type value.