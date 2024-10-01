# Language Reference

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

The following are some general characteristics of BrightScript, as compared to other common scripting languages:

*   BrightScript is not case sensitive.
    
*   Statement syntax is similar to Python, Basic, Ruby, and Lua (and dissimilar to C).
    
*   Like JavaScript and Lua, objects and named data-entry structures are associative arrays.
    
*   BrightScript supports dynamic typing (like JavaScript) and declared types (like C and Java).
    
*   Similar to .Net and Java, BrightScript uses "interfaces" and "components" (i.e. objects).
    

BrightScript code is compiled into bytecode that is run by an interpreter. The compilation step occurs every time a script is loaded and run. Similar to JavaScript, there is no separate compilation step that results in a saved binary file.

BrightScript and its component architecture are written in 100% C for speed, efficiency, and portability. Since many embedded processors do not have floating-point units, BrightScript makes extensive use of the "integer" type. Unlike some languages (including JavaScript), BrightScript only uses floating point numbers when necessary.