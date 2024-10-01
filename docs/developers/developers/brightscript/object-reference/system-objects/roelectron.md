# roElectron

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This BrightScript object launches an Electron instance from a BrightScript runtime. 

All BrightSign JavaScript objects are available to use with Electron, and BrightSign mechanisms allow communication between JavaScript (Electron main processes) and BrightScript (BrightSign processes).

> [!NOTE]
> This object is only available on Series 5 players.

## Object Creation

roElectron takes two parameters: a filename and an options parameter.

```
aa = CreateObject("roAssociativeArray")
aa.message_port = my_message_port
aa.arguments = CreateObject("roArray")
aa.arguments[0] = "arg1"
aa.arguments[1] = "arg2"
aa.node_arguments = CreateObject("roArray")
aa.node_arguments = {"node_arg1", "node_arg2")
aa.env_vars = CreateObject("roAssociativeArray")
aa.env_vars.AddReplace("ENV_VAR_1", "test")
aa.env_vars.AddReplace("ENV_VAR_2", "true")
node = CreateObject("roElectron", "path/to/my/application", aa)
```

*   `message_port` optional: A message port to bridge the Electron and BrightScript applications.
    
*   `arguments` optional: An roArray of arguments for Electron
    
*   `node_arguments` optional: An roArray of arguments for the Electron application itself to consume.
    
*   `env_vars` optional: An roAssociativeArray of environment variables for Electron application.
    

BrightScript associative arrays are case insensitive when object-literal syntax (for example, `aa={bright:"Sign"}`) is used. Environment variables are generally considered as case sensitive. Use the `AddReplace` method with an associative array, or call `SetModeCaseSensitive()` before assigning object-literal syntax variables into an env\_vars associative array.

## Methods

##### PostJSMessage(data as AssociativeArray) as Boolean

Posts a collection of key:value pairs to the BrightScript MessagePort JavaScript class. This method takes an associative array but it doesn't support nested associative arrays. See [JavaScript to BrightScript](https://docs.brightsign.biz/display/DOC/messageport) for more details.  

## Events

See [roElectronEvent](../system-objects/roelectronevent.md) for information about roElectron events.