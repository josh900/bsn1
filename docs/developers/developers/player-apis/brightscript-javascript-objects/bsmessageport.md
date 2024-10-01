# BSMessagePort

This object allows for an associative array to be passed from JavaScript to BrightScript (or vice versa). Only one *BSMessagePort* instance may be created per *roHtmlWidget* instance.

The JavaScript equivalent is [messageport](../../player-apis/javascript-apis/messageport.md).

## Methods

`boolean PostBSMessage(in Dictionary message)`

> [!NOTE]
> The PostBSMessage() method does not accept nested dictionaries. The same is true for the PostJSMessage() BrightScript method.

## Events

The following event occurs when a message is sent from BrightScript to JavaScript. It will appear as a *MessagePortEvent* event.

`onbsmessage`

### MessagePortEvent

This event contains a single field:

`readonly attribute any data;`

The following script will iterate over all the fields received in the event:

```
var bsMessage = new BSMessagePort();

bsMessage.onbsmessage = function(msg)
{
    for(name in msg.data)
    {
    	console.log('### ' + name + ': ' + msg.data[name]);
    }
}
```

In BrightScript, the *roHtmlWidget.PostJSMessage()* method can be used to post a message to JavaScript:

`widget.PostJSMessage({ Param1: "Data1", Param2: "Data2", Param3: "Data3" })`

## Examples

The following script will send a collection of properties to BrightScript:

```
function myFunction()
{
    var bsMessage = new BSMessagePort();
    bsMessage.PostBSMessage({complete: true, result: "PASS"});
}
```

The message will appear in BrightScript as an *roHtmlWidgetEvent*. In this case, the GetData().reason equals "message" and GetData().message contains the *roAssociativeArray*.

```
while not finished
    ev = mp.WaitMessage(30000)
    if type(ev) <> "roHtmlWidgetEvent" then
        print type(ev)
        stop
    end if
    payload = ev.GetData()
    print payload
    print "Reason: "; payload.reason
    if payload.reason = "message" then
        print "Message: "; payload.message
        if payload.message.complete = invalid then
            stop
        else if payload.message.complete = "true" then
            finished = true
            if payload.message.result = "PASS" then
                print "Test passed"
            else
                print "Test failed: "; payload.message.err
                stop
            end if
        end if
    end if
end while
```