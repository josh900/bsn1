# Events

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

Events in BrightScript center around an event loop and the *roMessagePort* object. Most BrightScript objects can post to a message port in the form of an event object: For example, the *roTimer* object posts events of the type *roTimerEvent* when configured intervals are reached.

The following script sets the destination message port using the `SetPort()` method, waits for an event in the form of an *roGpioButton* object, and then processes the event.

```
print "BrightSign Button-LED Test Running"
p =   CreateObject("roMessagePort")
gpio =  CreateObject("roGpioControlPort") 
gpio.SetPort(p)
 
while true
   msg=wait(0, p)
   if type(msg)="roGpioButton" then
       butn = msg.GetInt()
       if butn <=5 then
           gpio.SetOutputState(butn+17,1)
           print "Button Pressed: ";butn
           sleep(500)
           gpio.SetOutputState(butn+17,0)
        end if
    end if
 
   REM ignore buttons pressed while flashing led above
   while p.GetMessage()<>invalid
         end while
end while
```

Note that lines 6-7 can be replaced using the following (and substituting `end while` with `end for`):

```
For each msg in p
```