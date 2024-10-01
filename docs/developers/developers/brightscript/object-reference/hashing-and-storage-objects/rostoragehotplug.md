# roStorageHotplug

This object provides *roStorageAttached* messages when storage devices appear and *roStorageDetached* messages when storage devices disappear. An *roStorageAttached* event is not delivered until the filesystem is mounted. The JavaScript equivalent is Node.js `fs.watch()`. 

There is currently no way to poll for media. 

Object Creation: The *roStorageHotplug* object is created with no parameters.

```
CreateObject("roStorageHotplug")
```

## ifStorageHotplug

##### GetStorageStatus(drive As String) As roAssociativeArray

Returns the current status of a storage device ("SD:", "SSD:", "USB:"), even if it is not mounted. This method returns an associative array containing the following:

| Key | Value Type | Description |
| --- | --- | --- |
| `present` | Boolean | Indicates whether the specified device is present. |
| `mounted` | Boolean | Indicates whether the specified device is mounted. |
| `corrupt` | Boolean | Indicates whether the specified device is believed to be corrupt. |
| `checking` | Boolean | Indicates whether the specified device is currently being checked. |

> [!NOTE]
> The results of the `GetStorageStatus()` method are unreliable when called with a "USBn:" parameter, where "n" is a positive integer indicating a USB storage device when multiple USB devices are connected to the player.

Example:

```
 status = CreateObject("roStorageHotplug").GetStorageStatus("SSD:")
 if not status.mounted and not status.checking and status.present then
    ' Should ask for confirmation here
    FormatDrive("SSD:")
 end if 
```

## ifFailureReason

##### GetFailureReason() As String

Returns additional diagnostic information if a method returns False.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via SetUserData(). It will return Invalid if no data has been set.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roStorageAttached* and *roStorageDetached*  to the attached message port.

> [!NOTE]
> In order to avoid race conditions at startup, you should check for any storage devices that might have existed prior to the message port being set. We recommend doing this after the object is created and the message port is set, but before instructing the script to wait for any events.

## Example

```
Sub Main()
    mp = CreateObject("roMessagePort")
    sh = CreateObject("roStorageHotplug")
    gpio = CreateObject("roControlPort", "brightsign")

    sh.SetPort(mp)
    gpio.SetPort(mp)

    finished = false
    while not finished
    ev = mp.WaitMessage(0)
    if type(ev) = "roControlDown"
        finished = true
    else if type(ev) = "roStorageAttached"
        print "ATTACHED "; ev.GetString()
    else if type(ev) = "roStorageDetached"
        print "DETACHED "; ev.GetString()
    else
        print type(ev)
        stop
    end if
    end while
End Sub 
```