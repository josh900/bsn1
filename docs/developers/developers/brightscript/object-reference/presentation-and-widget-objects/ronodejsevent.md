# roNodeJsEvent

If an *roMessagePort* is attached to an *roNodeJs*, it will receive *roNodeJsEvent* objects when something happens to the parent *roNodeJs* instance.

## ifUserData

`SetUserData(user_data As Object)`  
Sets the user data that will be returned when events are raised.

`GetUserData() As Object`  
Returns the user data that has previously been set via `SetUserData()`. It will return `Invalid` if no data has been set.

## ifNodeJsEvent

`GetData() As roAssociativeArray`  
Returns the event data as an associative array with the following key/value pairs:

*   `reason` string: The cause of the event, which can be one of the following:
    
    *   `process_exit`: The nodeJs instance has exited.
        
    *   `message`: The nodeJs instance has sent a message*.*
        
*   `exit_code` number:  This field is only present if the value of the `reason` field value is `process_exit`. It will return the exit code from the Node.js® process, as described at [https://nodejs.org/api/process.html#process\_exit\_codes](https://nodejs.org/api/process.html#process_exit_codes).  The `exit_code` field is only defined from OS 8.2 onwards. Note that the Node.js script could also use these codes for its own purposes. 
    
*   `message` string: If the `reason` field value is `message`, this field returns the contents of the message.
    

## Example

The following event loop waits for a nodeJs event and reports the events:

```
while true
    ev = wait(0, gaa.mp)
    print "=== BS: Received event ";type(ev)
    if type(ev) = "roNodeJsEvent" then
        eventData = ev.GetData()
        if type(eventData) = "roAssociativeArray" and type(eventData.reason) = "roString" then
            if eventData.reason = "process_exit" then
                print "=== BS: Node.js instance exited with code " ; eventData.exit_code
            else if eventData.reason = "message" then
                print "=== BS: Received message "; eventData.message
                ' To use this: msgPort.PostBSMessage({text: "my message"});
            else
                print "======= UNHANDLED NODEJS EVENT ========="
                print eventData.reason
            endif
        else
            print "=== BS: Unknown eventData: "; type(eventData)
        endif
    endif
endwhile
```