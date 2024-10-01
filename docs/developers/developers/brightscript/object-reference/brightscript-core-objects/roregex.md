# roRegex

This object allows the implementation of the regular-expression processing provided by the PCRE library. The JavaScript equivalent is `RegExp()`.

This object is created with a string to represent the matching-pattern and a string to indicate flags that modify the behavior of one or more matching operations: 

```
CreateObject("roRegex", "[a-z]+", "i") 
```

The match string (in the example above, `"[a-z]+"`, which matches all lowercase letters) can include most Perl compatible regular expressions found in the [PCRE documentation](http://pcre.org/). 

This object supports any combination of the following behavior flags (in the example above, "i", which can be modified to match both uppercase and lowercase letters):

*   `"i"`: Case-insensitive match mode.
    
*   `"m"`: Multiline mode. The start-line ("^") and end-line ("$") constructs match immediately before or after any newline in the subject string. They also match at the absolute beginning or end of a string.
    
*   `"s"`: Dot-all mode, which includes a newline in the ".\*" regular expression. This modifier is equivalent to "/s" in Perl.
    
*   `"x"`: Extended mode, which ignores whitespace characters except when escaped or inside a character class. This modifier is equivalent to "/x" in Perl.
    

## ifRegex

##### IsMatch(string As String) As Boolean

Returns True if the string is consistent with the matching pattern.

##### Match(string As String) As roArray

Returns an *roArray* of matched substrings from the string. The entire match is returned in the form `array[0]`.This will be the only entry in the array if there are no parenthetical substrings. If the matching pattern contains parenthetical substrings, the relevant substrings will be returned as an array of length n+1, where `array[0]` is the entire match and each additional entry in the array is the match for the corresponding parenthetical expression.

##### Replace(string As String, subset As String) As String

Replaces the first occurrence of a matching pattern in the string with the subset and returns the result.

The subset may contain numbered back-references to parenthetical substrings.

##### **Example**

```
 > r = CreateObject("roRegex", "(\d+)\s+(\w+)", "")
 > ? r.Replace("123 abc", "word:\2 number:\1")
 > word:abc number:123
```

##### ReplaceAll(string As String, subset As String) As String

Replaces the all occurrences of a matching pattern in the string with the subset and returns the result.

##### **Example**

```
 > r = CreateObject("roRegex", "a", "i")
 > ? r.ReplaceAll("Abracadabra", "x")
 xbrxcxdxbrx
```

##### Split(string As String) As roList

Uses the matching pattern as a delimiter and splits the string on the delimiter boundaries. The function returns an *roList* of strings that were separated by the matching pattern in the original string.