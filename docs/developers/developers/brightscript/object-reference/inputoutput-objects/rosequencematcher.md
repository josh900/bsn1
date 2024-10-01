# roSequenceMatcher

This object is used to send *roSequenceMatchEvent* events when the specified byte sequence patterns are matched. Once a pattern has been matched and the event has been posted, all contributing bytes are discarded. As a result, if one pattern is a prefix of another pattern, then the second, longer pattern will never be matched by the object.

This object provides both a standard interface and an overloaded interface for sending events to a message port.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roSequenceMatchEvent* to the attached message port.

## ifSequenceMatcher

##### SetPort(a As Object)

Specifies the message port where *roSequenceMatchEvent* objects will be posted.

##### Add(pattern As Object, user\_data As Object) As Boolean

Adds a pattern to be matched by the *roSequenceMatcher* object instance. The pattern should be specified as an object that is convertible to a byte sequence (e.g. *roByteArray*, *roString*). For the user data, pass the object that should be returned if the specified pattern is matched.

## Example

```
Function FromHex(hex as String) as Object
    bytes = CreateObject("roByteArray")
    bytes.FromHexString(hex)
    return bytes
End Function
 
Sub Main()
    serial = CreateObject("roSerialPort", 1, 115200)
    mp = CreateObject("roMessagePort")
 
    button1_seq = FromHex("080a01040001e000")
    button2_seq = FromHex("080e01040001e000")
 
    matcher = CreateObject("roSequenceMatcher")
    matcher.SetMessagePort(mp)
    matcher.Add(button1_seq, { name: "button1" })
    matcher.Add(button2_seq, { name: "button2" })
    matcher.Add("flibbet", { name: "flibbet" })
    matcher.Add("flobbet", { name: "flobbet" })
 
    if not serial.SetMatcher(matcher) then
       stop
    end if
 
    finished = false
    while not finished
       ev = mp.WaitMessage(10000)
       if ev = invalid then
           finished = true
       else if type(ev) = "roSequenceMatchEvent" then
           print "Got button: "; ev.GetUserData().name
       else
           print "Unexpected event: "; type(ev)
       end if
    end while
End Sub
```