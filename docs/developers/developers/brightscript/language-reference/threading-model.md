# Threading Model

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

BrightScript runs in a single thread. In general, BrightScript object calls are synchronous if they return quickly, and asynchronous if they take a substantial amount of time to complete. For example, methods belonging to the *roArray* object are all synchronous, while the `Play()` method that is part of the *roVideoPlayer* object will return immediately (it is asynchronous). As a video plays, the *roVideoPlayer* object will post messages to the message port, indicating such events as “media playback finished” or “frame x reached”.                                  

The object implementer decides whether a BrightScript object should launch a background thread to perform a synchronous operation. Sometimes, an object will feature synchronous and asynchronous versions of the same method.

This threading model ensures that the script writer does not have to deal with mutexes and other synchronization objects. The script is always single threaded, and the message port is polled or waited on to receive events into the thread. On the other hand, those implementing BrightScript objects have to consider threading issues: For example, the *roList* and *roMessagePort* objects are thread-safe internally, allowing them to be used by multiple threads.