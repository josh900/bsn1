# roMessagePort

A message port is the destination where messages (events) are sent. See the explanation of [Event Loops](../../object-reference.md) for more details. You do not call these functions directly when using BrightScript. Instead, use the `Wait()` [global function](../../object-reference/global-functions.md).

## ifMessagePort

##### GetMessage() As Object

Returns the event object if available. Otherwise, Invalid is returned. In either case, this method returns immediately without waiting.

##### WaitMessage(timeout As Integer) As Object

Waits until an event object is available or the specified amount of milliseconds have passed. When an event object becomes available, it will be returned. If the timeout is reached, Invalid will be returned. Passing a zero timeout value instructs this method to wait indefinitely for a message.

You can also use the `Wait()` global function to retrieve event objects over a specified interval. The following two statements have the same effect:

```
msg = port.WaitMessage(timeout)
msg = wait(timeout, port)
```

##### PostMessage(msg As Object) As Void  
 

##### PeekMessage() As Object

Returns the event object if available (or Invalid if otherwise), but does not remove the event object from the message queue; a later call to `GetMessage()`, `WaitMessage()`, or `PeekMessage()` will return the same event object. 

##### SetWatchdogTimeout(seconds As Integer) As Integer

Enables a watchdog timeout on the *roMessagePort* instance if passed a positive integer. The watchdog will crash and reboot the player if the script does not call `GetMessage()` or `WaitMessage()` after the specified number of seconds (the timeout is blocked while the script waits on the message port). Passing zero to this method disables the watchdog.

Some BrightScript operations (e.g. *roAssetRealizer.Realize()*) can take a long time to return. In these cases, it may be better to use a short watchdog timeout in general but switch to a longer timeout before calling such operations.

The watchdog timeout only applies to its associated *roMessagePort* instance, so enabling the watchdog on one *roMessagePort* instance, then calling `WaitMessage()` on another, may cause the watchdog to trigger unexpectedly. The watchdog will not trigger while waiting on the BrightScript debugger prompt. 

##### DeferWatchdog(seconds As Integer)

Defers the watchdog timeout set by the `SetWatchdogTimeout()` method. Passing an integer to this method defers the timeout for the specified number of seconds.

##### DeferWatchdog()

Defers the watchdog timeout by the amount of seconds set in the `SetWatchdogTimeout()` method.

> [!NOTE]
> Calls to either `DeferWatchdog()` method cannot cause the watchdog to trigger earlier than it already will. For example, calling `DeferWatchdog(100)` followed by `DeferWatchdog(10)` will still cause the watchdog to trigger after 100 seconds.

## ifEnum

##### Reset()

Resets the position to the first element of enumeration.

##### Next() As Dynamic

Returns the typed value at the current position and increment position.

##### IsNext() As Boolean

Returns True if there is a next element.

##### IsEmpty() As Boolean

Returns True if there is not a next element.