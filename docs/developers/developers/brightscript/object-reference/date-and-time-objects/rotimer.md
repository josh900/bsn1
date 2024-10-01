# roTimer

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This object allows the script to trigger events at a specific date/time or during specified intervals. Events are triggered by delivering *roTimerEvent* objects to the specified message port. The JavaScript equivalent is .setTimeout()/.setInterval().

## ifTimer

##### SetTime(hour As Integer, minute As Integer, second As Integer, millisecond As Integer) As Void

Sets the time for the event to trigger. In general, if a value is -1, then it is a wildcard and will cause the event to trigger every time the rest of the specification matches. If there are no wildcards, then the timer will trigger only once when the specified time occurs.

> [!NOTE]
> Periodic timers that fire every second are not supported. The seconds and milliseconds parameters must be zero if there are any wildcards elsewhere.

##### SetTime(a As Integer, b As Integer, c As Integer)  
 

##### SetDate(year As Integer, month As Integer, day As Integer) As Void

Sets the date for the event to trigger. In general, if a value is -1, then it is a wildcard and will cause the event to trigger every time the rest of the specification matches. If there are no wildcards, then the timer will trigger only once when the specified date/time occurs.

##### SetDayOfWeek(day\_of\_week As Integer) As Void

Sets the day of week for the event to trigger. In general, if a value is -1, then it is a wildcard and will cause the event to trigger every time the rest of the specification matches. If there are no wildcards, then the timer will trigger only once when the specified date/time occurs.

> [!NOTE]
> It is possible, using a combination of SetDate() and SetDayOfWeek() calls, to specify invalid combinations that will never occur. If specifications include any wildcard, then the second and millisecond specifications must be zero; events will be raised at most once per minute near the whole minute.

##### SetDateTime(date\_time As roDateTime) As Void

Sets the time when you wish the event to trigger from an *roDateTime* object. It is not possible to set wildcards using this method.

##### Start() As Boolean

Starts the timer based on the current values specified using the above functions.

##### Stop() As Void

Stops the timer.

##### SetElapsed(seconds As Integer, milliseconds As Integer)

Configures a timer to trigger once the specified time period has elapsed. Unlike the absolute timer methods above, changes to the system clock will not affect the period of the SetElapsed() timer.

## ifMessagePort

##### SetPort(port As roMessagePort) As Void

Posts messages of type *roTimerEvent* to the attached message port.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifIdentity

##### GetIdentity() As Integer

Returns a unique number that can be used to identify when events originate from this object.

> [!NOTE]
> The *ifIdentity* interface has been deprecated. We recommend using the *ifUserData* interface instead.

## Examples

This script uses the `SetElapsed()` method to create a timer that triggers every 30 seconds:

```
Sub Main()
    mp = CreateObject("roMessagePort")
    timer = CreateObject("roTimer")
    timer.SetPort(mp)

    timer.SetElapsed(30, 0)

    print "Start at "; Uptime(0)
    timer.Start()

    while true
       ev = mp.WaitMessage(0)
       if type(ev) = "roTimerEvent" then
           print "Timer event received at "; Uptime(0)
           timer.Start()
       else
           print "Another event arrived: "; type(ev)
       end if
    end while
End Sub
```

This script creates a timer that triggers every minute using wildcards in the timer spec:

```
st=CreateObject("roSystemTime")
timer=CreateObject("roTimer")
mp=CreateObject("roMessagePort")
timer.SetPort(mp)

timer.SetDate(-1, -1, -1)
timer.SetTime(-1, -1, 0, 0)
timer.Start()

while true
       ev = Wait(0, mp)
       if (type(ev) = "roTimerEvent") then
             print "timer event received"
       else
             print "unexpected event received"
       endif
endwhile
```

This script creates a timer that triggers once at a specific date/time.

```
timer=CreateObject("roTimer")
mp=CreateObject("roMessagePort")
timer.SetPort(mp)

timer.SetDate(2008, 11, 1)
timer.SetTime(0, 0, 0, 0)

timer.Start()

while true
       ev = Wait(0, mp)
       if (type(ev) = "roTimerEvent") then
             print "timer event received"
       else
             print "unexpected event received"
       endif
endwhile
```