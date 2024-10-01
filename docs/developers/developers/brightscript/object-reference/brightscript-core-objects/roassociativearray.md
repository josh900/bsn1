# roAssociativeArray

This object allows you to store objects in an associative array (also known as a map, dictionary, or hash table), a data structure that associates objects with string keys. 

> [!NOTE]
> Using nested `FOR EACH` loops to iterate over the same *roAssociativeArray* instance can lead to unexpected behavior. See the [FOR EACH statement description](../../../brightscript/language-reference/program-statements.md) for more details.

The *roAssociativeArray* object is created with no parameters: 

```
CreateObject("roAssociativeArray")
```

Alternatively, an associative array can be created using brackets:

```
aa1 = {}
aa2 = {key1:"value", key2: 55, key3: 5+3 }
```

## ifEnum

##### Reset() As Void

Resets the position to the first element of enumeration.

##### Next() As Dynamic

Returns a typed value at the current position and increments the position.

##### IsNext() As Boolean

Returns `true` if there is a next element.

##### IsEmpty() As Boolean

Returns `true` if the associative array contains no elements.

## ifAssociativeArray

##### AddReplace(key As String, value As Object) As Void

Adds a new entry to the associative array, associating the supplied object with the supplied key string. Only one object may be associated with a key, so any existing object linked to that key is discarded. This method is always case-sensitive when creating keys, whereas object-literal syntax (e.g. `aa={bright:"Sign"}`) is case-insensitive when creating keys unless `SetModeCaseSensitive()` is called.

##### Lookup(key As String) As Dynamic

Looks up the specified key and returns the associated object. If there is no object associated with the key string, then this method will return `Invalid`.

> [!TIP]
> **Tip**
> In many cases, the [Dot Operator](../../../brightscript/language-reference/operators.md) can be used as shorthand for the `Lookup()` and `AddReplace()` methods when working with associative arrays.

##### DoesExist(key As String) As Boolean

Looks up the specified key in the associative array. If the key exists, `true` is returned; otherwise, `false` is returned.

##### Delete(key As String) As Boolean

Looks for an object in the associative array linked to the specified key. If there is such an object, it is deleted and `true` is returned; otherwise, `false` is returned.

##### Clear() As Void

Removes all objects from the associative array.

##### SetModeCaseSensitive() As Void

Makes all subsequent actions case sensitive. All lookups and created keys (with the exception of the `AddReplace()` method) are case insensitive by default.

##### LookupCi(key As String) As Dynamic

Looks for an object in the array associated with the specified key. This method functions similarly to `Lookup()`, with the exception that key comparisons are always case insensitive, regardless of case mode.

##### Append(aa As roAssociativeArray) As Void

Appends a second associative array to the first.

## Examples

```
aa = CreateObject("roAssociativeArray") 
aa.AddReplace("Bright", "Sign")
aa.AddReplace("TMOL", 42) 
print aa.Lookup("tmol")
print aa.Lookup("bright") 
```

The above script returns the following: 

```
42
Sign
```

Alternatively, you can use the [Dot Operator](../../../brightscript/language-reference/operators.md) in place of the `AddReplace()` and `Lookup()` methods:

```
aa = {}
aa.bright = "Sign"
aa.tmol = 42 
print aa.tmol
print aa.bright
```

You can also specify an associative array as a multiline object literal:

```
aa = {
bright : "Sign",
tmol : 42,
pie : 3.14
}

```