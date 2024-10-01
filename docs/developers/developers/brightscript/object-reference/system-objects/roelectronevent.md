# roElectronEvent

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

If an *roMessagePort* is attached to an *roElectron* object, it will receive *roElectronEvent* objects when something happens to the parent *roElectron* instance.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return `Invalid` if no data has been set.

## ifElectronEvent

##### GetData() As roAssociativeArray

Returns the event data as an associative array with the following key/value pairs:

*   `reason` string: The cause of the event, which can be one of the following:
    
    *   `process_exit`: The Electron instance has exited.
        
    *   `message`: The Electron instance has sent a message*.*
        

*   `exit_code` number:  The value of this field is set by the Electron application when it exits ([www.electronjs.org/docs/api/app#appexitexitcode](https://www.electronjs.org/docs/api/app#appexitexitcode)). The Electron process exit code is only defined in OS 8.2 and later OS versions. Note that the Electron script can also use these codes for its own purposes. 
    
*   `message` string: If the `reason` field value is `message`, this field returns the contents of the message.
    

## Example

The following event loop waits for an Electron event and reports the events:

```
while true
    ev = wait(0, gaa.mp)
    print "=== BS: Received event ";type(ev)
    if type(ev) = "roElectronEvent" then
        eventData = ev.GetData()
        if type(eventData) = "roAssociativeArray" and type(eventData.reason) = "roString" then
            if eventData.reason = "process_exit" then
                print "=== BS: Electron instance exited with code " ; eventData.exit_code
            else if eventData.reason = "message" then
                print "=== BS: Received message "; eventData.message
                ' To use this: msgPort.PostBSMessage({text: "my message"});
            else
                print "======= UNHANDLED ELECTRON EVENT ========="
                print eventData.reason
            endif
        else
            print "=== BS: Unknown eventData: "; type(eventData)
        endif
    endif
endwhile
```