# roDiskMonitor

This object provides access to low-level information about disk errors. It provides an event-based interface that delivers *roDiskErrorEvent* objects via *roMessageport*. Error messages are held for five seconds before delivery to minimize the chance of spurious error reports. Errors are not reported if the disk is removed during this five second interval because disk-removal detection takes several seconds. This allows for long-term monitoring of occasional media errors.

Object Creation: The *roDiskMonitor* object is created with no parameters.

```
CreateObject("roDiskMonitor")
```

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roDiskErrorEvent* to the attached message port. 

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

##### **Example**

```
diskmon=CreateObject("roDiskMonitor")
 
msgp=CreateObject("roMessagePort")
diskmon.Setport(msgp)
```