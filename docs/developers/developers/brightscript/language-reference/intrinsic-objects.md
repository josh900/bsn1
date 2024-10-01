# Intrinsic Objects

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

In general, this manual uses the term “object” to refer to “BrightScript components”, which are C or C++ components with interfaces and member functions that BrightScript uses directly. With the exception of some core objects (*roArray*, *roAssociativeArray*, *roInt*, *roMessagePort*, etc.), BrightScript objects are platform specific.

You can create intrinsic objects in BrightScript, but these objects are not BrightScript components. There is currently no way to create a BrightScript component in BrightScript or to create intrinsic objects that have interfaces (intrinsic objects can only contain member functions, properties, and other objects).

A BrightScript object is simply an *roAssociativeArray*: When a member function is called from an associative array, a “this” pointer is set to “m”, and “m” is accessible inside the Function code to access object keys. A “constructor” in BrightScript is simply a normal function at a global scope that creates an *roAssociativeArray* instance and fills in its member functions and properties 

See the “snake” game in the appendix for examples of creating intrinsic objects.