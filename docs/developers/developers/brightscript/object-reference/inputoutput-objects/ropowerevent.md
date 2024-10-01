# roPowerEvent

The *roPowerEvent* object triggers if you switch between plugged in AC and PoE.

Object Creation: The *roPowerEvent* object is created as follows:

```
CreateObject("roPowerEvent", a As String, b As String) As Object
```

## IfPowerEvent

`GetData() As Object`

Returns current state and requested state when it has switched from the current state to the requested state.