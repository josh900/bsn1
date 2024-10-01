# roInt, roFloat, roString

The [intrinsic types](http://docs.brightsign.biz/display/DOC/Variables%2C+Literals%2C+and+Types#Variables,Literals,andTypes-Types) `Int32`, `Float`, and `String` have object and interface equivalents. These are useful in the following situations:

*   An object is needed instead of a typed value (e.g. the *roList* object maintains a list of objects). When a function that expects a BrightScript object as a parameter is passed an integer, float, or string, BrightScript automatically creates the equivalent object.
    
*   If any object exposes the *ifInt*, *ifFloat*, or *ifString* interfaces, that object can be used in any expression that expects a typed value. For example, an [*roVideoEvent*](../../object-reference/presentation-and-widget-objects/rovideoevent-roaudioevent.md) can be used as an integer with a value representing the event ID.
    

**Integer Operations**

If "o" is of type *roInt*, then these statements will have the following effects:

*   `print o`: Prints the value of `o.GetInt()`
    
*   `i%=o`: Assigns the integer `i%` the value of `o.GetInt().`
    
*   `k=o`: Presumably `k` is automatically typed, so it becomes another reference to the *roInt* `o.`
    
*   `o=5`: This is NOT the same as `o.SetInt(5)`. Instead it releases `o`, changes the type of `o` to *roINT32* (`o` is automatically typed), and assigns it to 5.
    

## ifInt

*roInt* contains the *ifInt* interface, which provides the following:

##### GetInt() As Integer

Returns the integer value of the object. 

##### SetInt(value As Integer) As Void

Sets the integer value of the object. 

## ifIntOps

*roInt* also contains the *ifIntOps* interface, which provides the following:

##### ToStr() As String

Returns the integer value as a string. A space is not appended to the front for positive numbers.

## ifFloat

*roFloat* contains *the ifFloat* interface, which provides the following:

##### GetFloat() As Float

Returns the float value of the object. 

##### SetFloat(value As Float) As Void

Sets the float value of the object. 

## ifString

*roString* contains the *ifString* interface, which provides the following:

##### GetString() As String

Returns the string value of the object.

##### SetString(value As String) As Void

Sets the string value of the object.

## ifStringOps

*roString* also contains the *ifStringOps* interface, which provides the following:

> [!NOTE]
> Some [global functions](../../object-reference/global-functions.md) offer the same functionality as *ifStringOps* methods. The function indexes of *ifStringOps* methods start at zero, while those of global functions start at one.

##### SetString(str As String, str\_len As Integer)

Sets the string value of the object using the specified string and string-length values. This is similar to the `SetSeting()` method, which does not accept a parameter for string length.

##### AppendString(str As String, str\_len As Integer)

Appends to the string value of the object using the specified string and string-length values. This method modifies itself—this can cause unexpected results when you pass an intrinsic string type, rather than a string object.

##### **Example**

```
x="string"
x.ifstringops.appendstring("ddd",3)
print x 'will print 'string' 
y=box("string")
y.ifstringops.appendstring("ddd",3)
print y 'will print 'stringddd'
```

##### Len() As Integer

Returns the number of characters in a string.

##### GetEntityEncode() As String

Returns the string with certain characters replaced with HTML entity encoding sequences:

| Character | Replaced with |
| --- | --- |
| " (double quote) | &quot; |
| ' (single quote) | &apos; |
| <   | &lt; |
| \>  | &gt; |
| &   | &amp; |

##### Tokenize(delim As String) As roList

Splits a string into substrings using the specified delimiter character(s). The `delim` parameter can contain one or more characters to treat as delimiters. If the string object contains multiple contiguous delimiters, they will be treated as a single delimiter. This method returns the substrings as an *roList* object; the delimiters are not returned with the substrings.

##### **Example**

```
BrightScript> s = "one&&two"
BrightScript> print s.Tokenize("&")
one
two
```

##### Trim() As String

Returns the string with any leading and trailing whitespace characters (e.g. TAB, LF, CR, VT, FF, NO-BREAK SPACE) removed.

##### ToInt() As Integer

Returns the value of the string as an integer number.

##### ToFloat() As Float

Returns the value of the string as a floating point number.

##### Left(n As Integer) As String

Returns the first `n` characters of the string.

##### Right(n As Integer) As String

Returns the last `n` characters of the string.

##### Mid(start\_index As Integer) As String

Returns a subset of the string that begins at the zero-based `start_index` and terminates at the end of the string.

##### Mid(start\_index As Integer, n As Integer) As String

Returns a subset of the string, beginning at the zero-based `start_index` and consisting of `n` characters. If the string contains fewer than `n` characters after the specified `start_index`, this method will return all characters after the `start_index`.

##### Instr(substring As String) As Integer 

Returns the zero-based index of the first occurence of the substring in the string. If the substring does not occur in the string, this method returns -1. 

##### Instr(start\_index As Integer, substring As String) As Integer

Returns the zero-based index of the first occurence of the substring after the specified `start_index` in the string. If the substring does not occur after the specified `start_index`, this method returns -1.

> [!TIP]
> **Tip**
> `Instr()` is also offered as a [global function](../../object-reference/global-functions.md) (note that the string index of the global function starts at 1).

## Examples

```
BrightScript> o=CreateObject("roInt")
BrightScript> o.SetInt(555)
BrightScript> print o
555
BrightScript> print o.GetInt()
555
BrightScript> print o-55
500 
```

An integer value of 5 is converted to type *roInt* automatically because the `AddTail()` method expects a BrightScript object as its parameter:

```
BrightScript> list=CreateObject("roList")
BrightScript> list.AddTail(5)
BrightScript> print type(list.GetTail()) 
```

Here the `ListDir()` method returns an *roList* object containing *roString* objects:

```
BrightScript> l=ListDir("/")
BrightScript> for i=1 to l.Count():print l.RemoveHead():next
test_movie_3.vob
test_movie_4.vob
test_movie_1.vob
test_movie_2.vob
```