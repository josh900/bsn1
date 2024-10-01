# Built-In Functions

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

*   [Type()](#type)
*   [GetGlobalAA()](#getglobalaa)
*   [Rnd()](#rnd)
*   [Box()](#box)
*   [Run()](#run)
*   [Eval()](#eval)
*   [GetLastRunCompileError()](#getlastruncompileerror)
*   [GetLastRunRuntimeError()](#getlastrunruntimeerror)

BrightScript features a set of built-in, module-scope, intrinsic functions. A number of file I/O, string, mathematics, and system functions are also available via the *roGlobal* object.

## Type()

`Type(a As Variable) As String` 

This function returns the type of the passed variable and/or object.

## GetGlobalAA()

`GetGlobalAA() As Object`

This function fetches the global associative array for the current script.

## Rnd()

`Rnd(range As Integer) As Integer`  
`Rnd(0) As Float`

If passed a positive, non-zero integer, this function returns a pseudo-random integer between 1 and the argument value. The range includes the argument value: For example, calling `Rnd(55)` will return a pseudo-random integer greater than 0 and less than 56.

If the argument is 0, this function returns a pseudo-random Float value between 0 and 1.

> [!NOTE]
> **Note**
> The `Rnd()` functions utilize a pseudo-random seed number that is generated internally and not accessible to the user.

## Box()

`Box(type As Dynamic) As Object`

This function returns an object version of the specified intrinsic type. Objects will be passed through.

##### **Example**

```
b = box("string")
b = box(b)  ' b does not change
```

## Run()

`Run(file_name As String, [optional_arg As Dynamic, …]) As Dynamic`  
`Run(file_names As roArray, [optional_arg As Dynamic, …]) As Dynamic`

This function runs one or more scripts from the current script. You may append optional arguments, which will be passed to the `Main()` function of the script(s). The called script may also return arguments to the caller script.

If a string file name is passed, the function will compile and run the corresponding file. If an array of files is passed, the function will compile each file, link them together, and run them.

##### **Example**

```
Sub Main()
       Run("test.brs")
       BreakIfRunError(LINE_NUM)
       Print Run("test2.brs", "arg 1", "arg 2")
       if Run(["file1.brs","file2.brs"])<>4 then stop
       BreakIfRunError(LINE_NUM)
       stop
End Sub


Sub BreakIfRunError(ln)
       el=GetLastRunCompileError()
       if el=invalid then
             el=GetLastRunRuntimeError()
             if el=&hFC or el=&hE2 then return  
             'FC==ERR_NORMAL_END, E2=ERR_VALUE_RETURN
             print "Runtime Error (line ";ln;"): ";el
             stop
       else
             print "compile error (line ";ln;")"
             for each e in el
                    for each i in e
                          print i;": ";e[i]
                    end for
             end for
      
             stop
       end if
End Sub
```

## Eval()

`Eval(code_snippet As String) As Dynamic`

This function runs the passed code snippet in the context of the current function. The function compiles the snippet, then executes the byte-code. If the code compiles and runs successfully, it will return zero. If the code compiles successfully, but encounters a runtime error, it will return an integer indicating the error code (using the same codes as the `GetLastRunRuntimeError()` function). If compilation fails, it will return an *roList* object; the *roList* structure is identical to that of the `GetLastRunCompileError()` function.

The `Eval()` function can be useful in two cases:

*   When you need to dynamically generate code at runtime.
    
*   When you need to execute a statement that could result in a runtime error, but you don’t want code execution to stop.
    

##### **Example**

```
PRINT Eval("1/0") 'Returns a divide by zero error.
```

## GetLastRunCompileError()

GetLastRunCompileError() As roList

This function returns an *roList* object containing compile errors (or Invalid if no errors occurred). Each *roList* entry is an *roAssociativeArray* object containing the following keys:

*   `ERRSTR`: The compile error type (as String)
    
*   `FILESPEC`: The file URI of the script containing the error (as String)
    
*   `ERRNO`: The error number (as Integer)
    
*   `LINENO`: The line number where the error occurs (as Integer)
    

The following are possible `ERRNO` values:

|     |     |     |     |
| --- | --- | --- | --- |
| **Error Code** |     | **Description** | **Expanded Description** |
| &hBF | 191 | ERR\_NW | `ENDWHILE` statement occurs without statement. |
| &hBE | 190 | ERR\_MISSING\_ENDWHILE | `WHILE` statement occurs without `ENDWHILE` statement. |
| &hBC | 188 | ERR\_MISSING\_ENDIF | End of script reached without finding an `ENDIF` statement. |
| &hBB | 187 | ERR\_NOLN | No line number found. |
| &hBA | 186 | ERR\_LNSEQ | Line number sequence error. |
| &hB9 | 185 | ERR\_LOADFILE | Error loading file. |
| &hB8 | 184 | ERR\_NOMATCH | `MATCH` statement does not match. |
| &hB7 | 183 | ERR\_UNEXPECTED\_EOF | Unexpected end of string encountered during string compilation. |
| &hB6 | 182 | ERR\_FOR\_NEXT\_MISMATCH | Variable on `NEXT` does not match `FOR`. |
| &hB5 | 181 | ERR\_NO\_BLOCK\_END |     |
| &hB4 | 180 | ERR\_LABELTWICE | Label defined more than once. |
| &hB3 | 179 | ERR\_UNTERMED\_STRING | Literal string does not have end quote. |
| &hB2 | 178 | ERR\_FUN\_NOT\_EXPECTED |     |
| &hB1 | 177 | ERR\_TOO\_MANY\_CONST |     |
| &hB0 | 176 | ERR\_TOO\_MANY\_VAR |     |
| &hAF | 175 | ERR\_EXIT\_WHILE\_NOT\_IN\_WHILE |     |
| &hAE | 174 | ERR\_INTERNAL\_LIMIT\_EXCEDED |     |
| &hAD | 173 | ERR\_SUB\_DEFINED\_TWICE |     |
| &hAC | 172 | ERR\_NOMAIN |     |
| &hAB | 171 | ERR\_FOREACH\_INDEX\_TM |     |
| &hAA | 170 | ERR\_RET\_CANNOT\_HAVE\_VALUE |     |
| &hA9 | 169 | ERR\_RET\_MUST\_HAVE\_VALUE |     |
| &hA8 | 168 | ERR\_FUN\_MUST\_HAVE\_RET\_TYPE |     |
| &hA7 | 167 | ERR\_INVALID\_TYPE |     |
| &hA6 | 166 | ERR\_NOLONGER | Feature no longer supported. |
| &hA5 | 165 | ERR\_EXIT\_FOR\_NOT\_IN\_FOR |     |
| &hA4 | 164 | ERR\_MISSING\_INITILIZER |     |
| &hA3 | 163 | ERR\_IF\_TOO\_LARGE |     |
| &hA2 | 162 | ERR\_RO\_NOT\_FOUND |     |
| &hA1 | 161 | ERR\_TOO\_MANY\_LABELS |     |
| &hA0 | 160 | ERR\_VAR\_CANNOT\_BE\_SUBNAME |     |
| &h9F | 159 | ERR\_INVALID\_CONST\_NAME |     |
| &h9E | 158 | ERR\_CONST\_FOLDING |     |

## GetLastRunRuntimeError()

`GetLastRunRuntimeError() As Integer`

This function returns the error code that resulted from the last `Run()` function.

These codes indicate a normal result:

|     |     |     |     |
| --- | --- | --- | --- |
| **Error Code** |     | **Description** | **Expanded Description** |
| &hFF | 255 | ERR\_OKAY |     |
| &hFC | 252 | ERR\_NORMAL\_END | Execution ended normally, but with termination (e.g. END, shell "exit", window closed). |
| &hE2 | 226 | ERR\_VALUE\_RETURN | Return executed with value returned on the stack. |
| &hE0 | 224 | ERR\_NO\_VALUE\_RETURN | Return executed without value returned on the stack. |

The following codes indicate runtime errors:

|     |     |     |     |
| --- | --- | --- | --- |
| **Error Code** |     | **Description** | **Expanded Description** |
| &hFE | 254 | ERR\_INTERNAL | Unexpected condition occurred. |
| &hFD | 253 | ERR\_UNDEFINED\_OPCD | Opcode could not be handled. |
| &hFB | 251 | ERR\_UNDEFINED\_OP | Expression operator could not be handled. |
| &hFA | 250 | ERR\_MISSING\_PARN |     |
| &hF9 | 249 | ERR\_STACK\_UNDER | No value to pop off the stack. |
| &hF8 | 248 | ERR\_BREAK | `scriptBreak()` function called. |
| &hF7 | 247 | ERR\_STOP | STOP statement executed. |
| &hF6 | 246 | ERR\_RO0 | bscNewComponent failed because object class not found. |
| &hF5 | 245 | ERR\_R01 | BrightScript member function call does not have right number of parameters. |
| &hF4 | 244 | ERR\_RO2 | BrightScript member function not found in object or interface. |
| &hF3 | 243 | ERR\_RO3 | BrightScript interface not a member of the object. |
| &hF2 | 242 | ERR\_TOO\_MANY\_PARAM | Too many function parameters to handle. |
| &hF1 | 241 | ERR\_WRONG\_NUM\_PARAM | Number of function parameters incorrect. |
| &hF0 | 240 | ERR\_RVIG | Function returns a value, but is ignored. |
| &hEF | 239 | ERR\_NOTPRINTABLE | Value not printable. |
| &hEE | 238 | ERR\_NOTWAITABLE | `WAIT` statement cannot be applied to object because object does not have an *roMessagePort* interface. |
| &hED | 237 | ERR\_MUST\_BE\_STATIC | Interface calls from rotINTERFACE type must be static. |
| &hEC | 236 | ERR\_RO4 | "." Dot Operator used on object that does not contain legal object or interface reference. |
| &hEB | 235 | ERR\_NOTYPEOP | Operation attempted on two type-less operands. |
| &hE9 | 233 | ERR\_USE\_OF\_UNINIT\_VAR | Uninitialized variable used illegally. |
| &hE8 | 232 | ERR\_TM2 | Non-numeric index applied to array. |
| &hE7 | 231 | ERR\_ARRAYNOTDIMMED |     |
| &hE6 | 230 | ERR\_USE\_OF\_UNINIT\_BRSUBREF | Reference to uninitialized SUB. |
| &hE5 | 229 | ERR\_MUST\_HAVE\_RETURN |     |
| &hE4 | 228 | ERR\_INVALID\_LVALUE | Left side of the expression is invalid. |
| &hE3 | 227 | ERR\_INVALID\_NUM\_ARRAY\_IDX | Number of array indexes is invalid. |
| &hE1 | 225 | ERR\_UNICODE\_NOT\_SUPPORTED |     |
| &hE0 | 224 | ERR\_NOTFUNOPABLE |     |
| &hDF | 223 | ERR\_STACK\_OVERFLOW |     |
| &h20 | 32  | ERR\_CN | Continue (`cont` or `c`) not allowed. |
| &h1C | 28  | ERR\_STRINGTOLONG |     |
| &h1A | 26  | ERR\_OS | String space has run out. |
| &h18 | 24  | ERR\_TM | A Type Mismatch (string /number operation mismatch) has occurred. |
| &h14 | 20  | ERR\_DIV\_ZERO |     |
| &h12 | 18  | ERR\_DD | Attempted to re-dimension array. |
| &h10 | 16  | ERR\_BS | Array subscript out of bounds. |
| &h0E | 14  | ERR\_MISSING\_LN |     |
| &h0C | 12  | ERR\_OUTOFMEM |     |
| &h08 | 8   | ERR\_FC | Invalid parameter passed to function/array (e.g. a negative matrix dim or square root). |
| &h06 | 6   | ERR\_OD | Out of data (READ). |
| &h04 | 4   | ERR\_RG | Return without Gosub. |
| &h02 | 2   | ERR\_SYNTAX |     |
| &h00 | 0   | ERR\_NF | `Next` without `For`. |