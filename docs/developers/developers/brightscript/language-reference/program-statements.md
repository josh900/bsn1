# Program Statements

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

*   [Statement Syntax](#statement-syntax)
*   [LIBRARY](#library)
*   [DIM](#dim)
*   [Assignment ("=")](#assignment)
*   [END](#end)
*   [STOP](#stop)
*   [GOTO](#goto)
*   [RETURN](#return)
*   [PRINT](#print)
*   [FOR / END FOR](#for-end-for)
*   [FOR EACH IN / END FOR](#for-each-in-end-for)
    *   [Nesting FOR EACH Statements](#nesting-for-each-statements)
*   [WHILE / EXIT WHILE](#while-exit-while)
*   [IF / THEN / ELSE](#if-then-else)
*   [Block IF / ELSEIF / THEN / ENDIF](#block-if-elseif-then-endif)
*   [Function() As Type / End Function](#function-as-type-end-function)

BrightScript supports the following statement types (note that BrightScript is not case sensitive). The syntax of each statement is documented in more detail later in this chapter.

*   `Library`
    
*   `Dim`
    
*   `=` (assignment)
    
*   `End`
    
*   `Stop`
    
*   `Goto`
    
*   `Rem <or> '`
    
*   `print`
    
*   `For / To / End For / Step / Exit For <or> Next`
    
*   `For Each / In / End For / Exit For <or> Next`
    
*   `While / End While / Exit While`
    
*   `Function / End Function / As / Return`
    

##### **Example**

```
Function Main() As Void
 
       dim cavemen[10]
 
       cavemen.push("fred")
       cavemen.push("barney")
       cavemen.push("wilma")
       cavemen.push("betty")
 
       for each caveman in cavemen
             print caveman
       end for
 
End Function
```

## Statement Syntax

Each line may contain a single statement. However, a colon (:) may be used to separate multiple statements on a single line.

##### **Example**

```
myname = "fred"
if myname="fred" then yourname = "barney":print yourname
```

## LIBRARY 

`LIBRARY Filename.brs`

The LIBRARY statement allows you to include your own BrightScript libraries (*.brs* files), which can then be utilized by your script. The LIBRARY statement(s) must occur at the beginning of a script, before any other statements, functions, operators, etc.

The system locates a library by searching the directory containing the current script, as well as the `SYS:/script-lib/` directory. Note that the `Run()` function does not currently change the path of a LIBRARY statement to that of the called script (i.e. the system will continue searching the directory of the caller script). On the other hand, running a script directly from the BrightSign shell does modify the library search path to that of the called script.

The first statement will include a library in the same folder as the script, while the second will include a library in a sub-folder.

```
LIBRARY "myBSL1.brs"
LIBRARY "new_lib/myBSL2.brs"
```

The following statement will include the [*bslCore.brs*](../language-reference/core-library-extension.md) library, which has some useful BrightScript features, from the `SYS:/script-lib/` directory.

```
LIBRARY "v30/bslCore.brs"
```

## DIM 

`DIM Name (dim1, dim2, …, dimK)`

The `DIM` (“dimension”) statement provides a shortcut for creating *roArray* objects. It sets the variable Name to type “roArray”. It can create arrays of arrays as needed for multi-dimensionality. The dimension passed to `DIM` is the index of the maximum entry to be allocated (i.e. the array initial size = dimension+1), though the array will be resized larger automatically if needed.

The following two lines create identical arrays.

```
Dim array[5]
array = CreateObject("roArray", 6, true)
```

> [!NOTE]
> **Note**
> The expression x\[a,b\] is equivalent to x\[a\]\[b\].

The following script demonstrates useful operations on a DIM array.

```
Dim c[5, 4, 6]


For x = 1 To 5
   For y = 1 To 4
        For z = 1 To 6
           c[x, y, z] = k
           k = k + 1
       End for
   End for
End for


k=0
For x = 1 To 5
    For y = 1 To 4
       For z = 1 To 6
          If c[x, y, z] <> k Then print"error" : Stop
          k = k + 1
          End for
   End for
End for
```

## Assignment ("=")

`variable = expression`

The assignment statement (“=”) assigns a variable to a new value.

In each of the following lines, the variable on the left side of the equals operator is assigned the value of the constant or expression on the right side of the equals operator.

```
a$="a rose is a rose"
b1=1.23
x=2.23
x=x-b1
```

## END

The `END` statement terminates script execution normally.

## STOP

The `STOP` statement interrupts script execution, returns a “STOP” error, and invokes the debugger. Use the `cont` command at the debugger prompt to continue execution of the script or the `step` command to execute a single step in the script.

## GOTO

`GOTO label`

The `GOTO` statement transfers program control to the line number specified by `label`. The `GOTO label` statement results in a branching operation. A `label` is an identifier terminated with a colon on a line that contains no other statements or expressions. 

##### **Example**

```
mylabel:
print "Hello World"
goto mylabel
```

## RETURN

`RETURN expression`

The `RETURN` statement returns from a function back to its caller. If the function is not type Void, `RETURN` can also return a value to the caller.

## PRINT

`PRINT [#output_object], [@location], item list`

The PRINT statement prints an item or list of items in the console. The item(s) may be strings, integers, floats, variables, or expressions. An object with an *ifInt*, *ifFloat*, or *ifString* interface may also be printed. If the `output_object` is specified, this statement will print to an object with an *ifStreamSend* interface.

If the statement is printing a list of items, the items must be separated with semicolons or commas. If semicolons are used, spaces are not inserted between printed items; if commas are used, the cursor will automatically advance to the next print zone before printing the next item.

Positive numbers and zero are printed with a leading space (without a plus sign). Spaces are not inserted before or after strings.

##### **Example**

```
x = 5 : print 25; " is equal to"; x ^2  
' prints "25 is equal to 25"
```

##### **Example**

```
a$ = "string"
print a$;a$,a$;" ";a$
'prints "stringstring	string string"
```

Each print zone in the following example is 16 characters wide. The cursor moves to the next print zone each time a comma is encountered.

```
> print "zone 1","zone 2","zone 3","zone 4"
'prints "zone 1          zone 2           zone 3           zone 4"
```

##### **Example**

```
print "print statement #1 ";
print "print statement #2"
'prints "print statement #1 print statement #2"
```

In some cases, semicolons can be dropped. For example, the following statement is legal:

```
Print "this is a five "5"!!"
```

A trailing semicolon overrides the cursor-return so that the next `PRINT` statement begins where the last left off. If no trailing punctuation is used with a `PRINT` statement, the cursor drops to the beginning of the next line.

#### \[@location\]

If the console you are printing to has the *ifTextField* interface, you can use the `@` character to specify where printing will begin.

##### **Example**

```
print #m.text_field,@width*(height/2-1)+(width-len(msg$))/2,msg$;
```

Whenever you use `PRINT @` on the bottom line of the display, an automatic line-feed causes all displayed lines to move up one line. To prevent this from happening, use a trailing semicolon at the end of the statement.

#### TAB (expression)

This statement moves the cursor to the specified position on the current line (modulo the width of the console if the TAB position is greater than the console width).

##### **Example**

```
print tab(5)"tabbed 5";tab(25)"tabbed 25"
```

Note the following about the `TAB` statement:

*   The `TAB` statement may be used several times in a `PRINT` list.
    
*   No punctuation is required after a `TAB` statement.
    
*   Numerical expressions may be used to specify a `TAB` position.
    
*   The `TAB` statement cannot be used to move the cursor to the left.
    
*   If the cursor is beyond the specified position, the `TAB` statement is ignored.
    

#### POS(x)

This statement returns an integer that indicates the current cursor position from 0 to the maximum width of the window. This statement requires a dummy argument in the form of any numeric expression.

```
print tab(40) pos(0)   'prints 40 at position 40

print "these" tab(pos(0)+5)"words" tab(pos(0)+5)"are";
print tab(pos(0)+5)"evenly" tab(pos(0)+5)"spaced"
```

## FOR / END FOR

`FOR counter_variable = initial_value TO final_value STEP increment / END FOR <or> NEXT`

The `FOR` statement creates an iterative loop that allows a sequence of program statements to be executed a specified number of times.

The `initial_value`, `final_value`, and `increment` can be any expression. The first time the `FOR` statement is executed, these three variables are evaluated and their values are saved; changing the variables during the loop will have no affect on the operation of the loop. However, the `counter_variable` must not be changed, or the loop will not operate normally. The first time the `FOR` statement is executed, the counter is set to both the value and type of the `initial_value`.

At the beginning of each loop, the value of the `counter_variable` is compared with the `final_value`. If the value of the `counter_variable` is greater than the `final_value`, the loop will complete and execution will continue with the statement following the `END FOR` (or `NEXT`) statement. If, on the other hand, the counter has not yet exceeded the `final_value`, control passes to the first statement after the `FOR` statement. If increment is a negative number, the loop will complete when the value of the `counter_variable` is less than the `final_value`.

When program flow reaches the `END FOR` (or `NEXT`) statement, the counter is incremented by the specified increment amount (or decremented if increment is a negative value). If the `STEP [increment]` language is not included in the `FOR` statement, the increment defaults to 1.

Use `EXIT FOR` to exit a `FOR` block prematurely.

The following script decrements `i` at the beginning of each loop until it is less than 1.

```
for i=10 to 1 step -1
       print i
end for
```

## FOR EACH IN / END FOR

`FOR EACH item IN object / END FOR <or> NEXT` 

The `FOR EACH` statement can iterate through a set of items in any object that has an *ifEnum* interface (i.e. an enumerator). The `FOR` block is terminated with the `END FOR` (or `NEXT`) statement. Objects that are ordered intrinsically (such as *roList*) are enumerated in order, while objects that have no intrinsic order (such as *roAssociativeArray*) are enumerated in apparent random order. It is possible to delete entries as they are enumerated.

Use `EXIT FOR` to exit a `FOR` block prematurely.

The following objects can be enumerated: *roList*, *roArray*, *roAssociativeArray*, *roMessagePort*.

The following script iterates over an associative array in random order, prints each key/value pair, then deletes it.

```
aa={joe: 10, fred: 11, sue:9}
For each n in aa
   Print n;aa[n]
   aa.delete[n]
end for
```

### Nesting FOR EACH Statements

The `FOR EACH` statement can only track one pointer per object instance, so nesting `FOR EACH` loops that iterate on the same object may cause the series to terminate prematurely:

```
values = {a: 1, b: 2, c: 3, d: 4, e: 5, f: 6}

for each key_outer in values
	print "outer: ";key_outer;" : ";values[key_outer]
	for each key_inner in values 'THIS WILL CAUSE PROBLEMATIC BEHAVIOR
		print "inner: ";key_inner;" : ";values[key_inner]
	end for
end for
```

To work around this limitation with associative arrays, copy the keys to an array and iterate on the array in the nested `FOR EACH` loop:

```
values = {a: 1, b: 2, c: 3, d: 4, e: 5, f: 6}
valuesArray = []

for each key in values 'Copy the keys to an array
	valuesArray.push(key)
end for

for each key_outer in values
	print "outer: ";key_outer;" : ";values[key_outer]
	for each key_inner in valuesArray 'Iterate over the array of keys
		print "inner: ";key_inner;" : ";values[key_inner]
	end for
end for
```

## WHILE / EXIT WHILE

`WHILE expression / EXIT WHILE`

A `WHILE` loop executes until the specified expression is false. Use the `EXIT WHILE` statement to exit a `WHILE` block prematurely.

```
k=0
while k<>0
   k=1
   Print "loop once"
end while
 
while true
   Print "loop once"
   Exit while
End while
```

## IF / THEN / ELSE

`IF expression THEN statements [ELSE statements]`

> [!NOTE]
> This is the single-line form of the IF THEN ELSE statement; see the next section for more details about the block form of the IF THEN ELSE statement.

The `IF` statement instructs the interpreter to test the following expression. If the expression is True, control will proceed to the statements immediately following the expression. If the expression is False, control will jump to either the matching `ELSE` statement (if there is one) or to the next program line after the block.

##### **Example**

```
if x>127 then print "out of range" : end
```

`THEN` is optional in the above and similar statements. However, `THEN` is sometimes required to eliminate ambiguity, as in the following example:

```
if y=m then m=o 'won't work without THEN
```

## Block IF / ELSEIF / THEN / ENDIF

The block (i.e. multi-line) form of IF / THEN / ELSE has the following syntax:

```
If BooleanExpression [ Then ]
   [ Block ]
   [ ElseIfStatement+ ]
   [ ElseStatement ]
End If
 
ElseIfStatement ::=
   ElseIf BooleanExpression [ Then ]
   [ Block ]
 
ElseStatement ::=
   Else
   [ Block ]
```

##### **Example**

```
vp_msg_loop:
        msg=wait(tiut, p)
        if type(msg)="rovideoevent" then                                            
            if debug then print "video event";msg.getint()
            if lm=0 and msg.getint() = meden then
                if debug then print "videofinished"
                retcode=5
                return
            endif
        else if type(msg)="rogpiobutton" then
            if debug then print "button press";msg
            if esc0 and msg=b0 then retcode=1:return
            if esc1 and msg=b1 then retcode=2:return
            if esc2 and msg=b2 then retcode=3:return
            if esc3 and msg=b3 then retcode=4:return
        else if type(msg)=" Invalid" then
            if debug then print "timeout"
            retcode=6
            return
        endif
 
        goto vp_msg_loop
```

## Function() As Type / End Function

`Function name(parameter As Type, …) As Type`

> [!NOTE]
> Each function has its own scope.

A function is declared using the `Function()` statement. The parentheses may contain one or more optional parameters; parameters can also have default values and expressions.

The type of each parameter may be declared. The return type of the function may also be declared. If a parameter type or return type is not declared, it is Dynamic by default. Intrinsic types are passed by value (and a copy is made), while objects are passed by reference. The `Sub` statement can be used instead of `Function` as a shortcut for creating a function with return type Void.

A parameter can be one of the following types:

*   Integer
    
*   Float
    
*   Double
    
*   String
    
*   Object
    
*   Dynamic
    

The function return can be one of the following types:

*   Void
    
*   Integer
    
*   Float
    
*   Double
    
*   String
    
*   Object
    
*   Dynamic
    

#### "M" Identifier 

If a function is called from an associative array, then the local variable `m` is set to the associative array in which the function is stored. If the function is not called from an associative array, then its `m` variable is set to an associative array that is global to the module and persists across calls.

The `m` identifier should only be used for the purpose stated above: We do not recommend using `m` as a general-purpose identifier.

##### **Example**

```
sub main()
   obj={
       add: add
       a: 5
       b: 10
       }
 
   obj.add()
   print obj.result
end sub
 
function add() As void
    m.result=m.a+m.b
end function
```

#### Anonymous Functions

A function without a name declaration is considered anonymous.

The following is a simple anonymous function declaration:

```
myfunc=function (a, b)
       Return a+b
end function
 
print myfunc(1,2)
```

Anonymous functions can also be used with associative-array literals:

```
q = {
 
starring : function(o, e)
str = e.GetBody()
print "Starring: " + str 
toks = box(str).tokenize(",")
for each act in toks
actx = box(act).trim()
if actx <> "" then
print "Actor: [" + actx + "]"
                o.Actors.Push(actx)
endif
end for
return 0
end function
}
 
q.starring(myobj, myxml)
```