# Variables, Literals, and Types

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Identifiers](#identifiers)
    *   [Examples](#examples)
*   [Types](#types)
*   [Type Declaration Characters](#type-declaration-characters)
*   [Literals (Constants)](#literals-constants)
*   [Array Literals](#array-literals)
*   [Associative Array Literals](#associative-array-literals)
*   [Invalid Object Return](#invalid-object-return)
*   [Numbers](#numbers)
    *   [Dynamic Typing](#dynamic-typing)
    *   [Type Conversion](#type-conversion)
    *   [Type Conversion and Accuracy](#type-conversion-and-accuracy)

## Identifiers

Identifiers are names of variables, functions, and labels. They also apply to BrightScript object methods (i.e. functions) and interfaces (which appear after a "." Dot Operator). Identifiers have the following rules:

*   Must start with an alphabetic character (a-z).
    
*   May consist of alphabetic characters, numbers, or the underscore symbol ("\_").
    
*   Are not case sensitive.
    
*   May be of any length.
    
*   May not be a [reserved word](../language-reference/reserved-words.md).
    
*   (**variables only**) May end with an optional type declaration ("$" for a string, "%" for an integer, "!" for a float, "#" for a double).
    

##### **Examples**

```
a
boy5
super_man$
42%
```

## Types

BrightScript supports both dynamic typing and declared types. This means that every value has a type determined at runtime, but variables can also be instructed to always contain a value of a specified type. If a value is assigned to a variable that has a specified type, the type of the value will be converted to the variable type if possible. If conversion is impossible, a runtime error will occur.

A variable that does not end in a type declaration may change its type dynamically. For example, the statement `a=4` will create an integer, while a following statement specifying that `a="hello"` will change the type of the variable a to a string.

BrightScript supports the following types:

*   **Boolean**: True or False
    
*   **Integer**: A 32-bit signed integer number
    
*   **Float**: The smallest floating point number format supported by either the hardware or software
    
*   **Double**: The largest floating point number format supported by either the hardware or software. Although Double is an intrinsically understood type, it is implemented internally with the *roIntrinsicDouble* object.
    
*   **String**: A sequence of ASCII (not UTF-8) characters. BrightScript uses two intrinsic string states:
    
    *   **Constant strings**: A statement such as `s="astring"` will create an intrinsic constant string.
        
    *   **roString instances**: Once a string is used in an expression, it becomes an *roString* instance. For example, the statement `s = s + "bstring"` will cause the intrinsic string `s` to convert to an *roString* instance. If this is followed by the statement `s2 = s`, the `s2` value will be a reference to `s`, not a copy of it. The behavior of reference counting strings is new to BrightScript version 3.0.
        
*   **Object**: A reference to a BrightScript object (i.e. a native component). Note that the `type()` function will not return "Object" but the type of object instead (e.g. *roList*, *roVideoPlayer*). Also note that there is no separate type for intrinsic BrightScript Objects. All intrinsic BrightScript Objects are built on the *roAssociativeArray* object type.
    
*   **Interface**: An interface in a BrightScript Object. If a  "." Dot Operator is used on an interface type, the member must be static (since there is no object context).
    
*   **Invalid**: A type that can have only one value: `Invalid`. This type is returned in various instances when no other type is valid (for example, when indexing an array that has never been sent). It can also be assigned to a variable with the statement `var = invalid`.
    

The following are examples of different types. The `?` statement is a shortcut for `print`, while the `type()` function returns a string that identifies the type of the passed expression.

```
BrightScript> ?type(1)                      
Integer
        
BrightScript> ?type(1.0)                        
Float
       
BrightScript> ?type("hello")                            
String
        
BrightScript> ?type(CreateObject("roList"))                   
roList  
    
BrightScript> ?type(1%)
Integer

BrightScript> b!=1
BrightScript> ?type(b!)
Float

BrightScript> c$="hello"
BrightScript> ?type(c$)
String

BrightScript> d="hello again"
BrightScript> ?type(d)
String

BrightScript> d=1
BrightScript> ?type(d)
Integer

BrightScript> d=1.0
BrightScript> ?type(d)
Float
 
BrightScript>e=invalid
BrightSCript>?type(e)
Invalid
```

## Type Declaration Characters

A type declaration may be used at the end of a variable or literal to fix its type. Variables with the same identifier but separate types are separate variables: For example, defining a$ and a% would create two independent variables.

|     |     |     |
| --- | --- | --- |
| **Character** | **Type** | **Examples** |
| $   | String | A$, ZZ$ |
| %   | Integer | A1%, SUM% |
| !   | Single-Precision (Float) | B!, N1! |
| #   | Double-Precision (Double) | A#, 1/3#, 2# |

## Literals (Constants)

The following are valid literal types:

*   Type Boolean: Either `True` or `False`
    
*   Type Invalid: `Invalid` only
    
*   Type String: A string in quotes (e.g. `"This is a string"`)
    
*   Type Integer: An integer in hex (e.g. `HFF`) or decimal (e.g. `255`) format
    
*   Type Float: A number with a decimal (e.g. `2.01`), in scientific notation (e.g. `1.23456E+30`), or with a Float type designator (e.g. `2!`)
    
*   Type Double: A number in scientific notation containing a double-precision exponent symbol (e.g. `1.23456789D-12`) or with a Double type declaration (e.g. `2.3#`)
    
*   Type Function: Similar to variable formatting (e.g. `MyFunction`)
    
*   Type Integer: LINE\_NUM – The current source line number
    

## Array Literals

The `[]` Array Operator can be used to declare an array. It can contain literals (constants) or expressions.

```
x = 5
Myarray = []
Myarray = [ 1, 2, 3]
Myarray = [ x+5, true, 1<>2, ["a","b"]]
```

## Associative Array Literals

The { } Associative Array Operator can be used to define an associative array. It can contain literals (constants) or expressions.

```
aa = { }
aa = {key1:"value", key2: 55, key3: 5+3 }
```

Arrays and associative arrays can also be defined with the following format: 

```
aa = {
   Myfunc1: aFunction
   Myval1 : "the value"
}
```

## Invalid Object Return

Many methods (i.e. functions) that return objects can also return Invalid (for example, in cases where there is no object to return). In these cases, the variable accepting the result must be dynamically typed since it may be assigned either type.

The following code will return a type mismatch: a$ is a string that has a string type declaration, and thus it cannot contain Invalid.

```
l = []
a$ = l.pop()
```

## Numbers

### Dynamic Typing

The following rules determine how integers, doubles, and floats are dynamically typed:

1.  If a constant contains 10 or more digits, or if `D` is used in the exponent, the number is Double. Adding a `#` type declaration also forces a constant to be a Double.
    
2.  If the number is not double precision and it contains a decimal point, the number is a Float. Expressing a number in scientific notation using the `E` exponent also forces a constant to be a Float.
    
3.  If neither of the above conditions is true for a constant, the number is an Integer.
    

### Type Conversion

When operations are performed on one or two numbers, the result must be typed as an Integer, Float, or Double. When an addition (+), subtraction (-), or multiplication (\*) operation is performed, the result will have the same degree of precision as the most precise operand: For example, multiplying an Integer by a Double will return a number that is a Double.

Only when both operands are Integers will the result be an Integer number. If the result of two Integer operands is outside the 32-bit range, the operation and return will be carried out with Doubles.

Division (/) operates using the same rules as above, except that it can never be carried out at the Integer level: When both operators are Integers, the operation and return will be carried out with Floats.

Comparison operations (e.g. <, >, =) will convert the numbers to the same type before they are compared. The less precise type will always be converted to the more precise type.

### Type Conversion and Accuracy

When a Float or Double number is converted to the Integer type, it is *rounded down*: The largest integer that is not greater than the number is used. This also happens when the INT function is called on a number.

When a Double number is converted to the Float type, it is *4/5 rounded*: The least significant digit is rounded up if the fractional part is >=5 (otherwise, it is left unchanged).

When a Float number is converted to the Double type, only the seven most significant digits will be accurate.