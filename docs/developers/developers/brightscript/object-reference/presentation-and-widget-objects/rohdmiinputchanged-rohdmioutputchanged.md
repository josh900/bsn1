# roHdmiInputChanged, roHdmiOutputChanged

The *roVideoMode* object generates an *roHdmiInputChanged* or *roHdmiOutputChanged* event object whenever the hotplug status of the HDMI® input or output changes. The JavaScript equivalent is *videoinput.VideoInputConfiguration.hdmiinputchanged* or *videooutput.VideoOutputConfiguration.hotplugevent.*

At least one *roHdmiOutputChanged* event object will always be generated for a hotplug event, even for very quick disconnect/connect hotplug events. In most cases, a disconnect/connect hotplug event will generate two event objects.

## ifInt

##### GetInt() As Integer

Returns the event ID. 

##### SetInt(value As Integer) As Void

Sets the value of the event. 

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.