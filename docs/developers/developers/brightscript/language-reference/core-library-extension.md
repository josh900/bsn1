# Core Library Extension

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

There are a number of built-in functions that are not part of the BrightScript Core Library. You can use the [LIBRARY](../language-reference/program-statements.md) statement to include this subset of functions:

```
LIBRARY "v30/bslCore.brs"
```

##### bslBrightScriptErrorCodes() As roAssociativeArray

Returns an associative array of name/value pairs corresponding to BrightScript error codes and their descriptions.

##### bslGeneralConstraints() As roAssociativeArray

Returns an associative array of name/value pairs corresponding to system constants.

##### bslUniversalControlEventCodes() As roAssociativeArray

Returns an associative array of name/value pairs corresponding to the remote key code constraints.

##### AsciiToHex(ascii As String) As String

Returns a hex-formatted version of the passed ASCII string.

##### HexToAscii(hex As String) As String

Returns an ASCII-formatted version of the passed hex string.

##### HexToInteger(hex As String) As Integer

Returns the integer value of the passed hex string.