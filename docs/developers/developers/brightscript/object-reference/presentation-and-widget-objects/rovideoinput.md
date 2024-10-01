# roVideoInput

This object allows playback of HDMI**®** input or video provided by a video capture dongle. Note that the *ifVideoInput* methods do not apply to HDMI input, which can be achieved by passing an unmodified *roVideoInput* instance to the *roVideoPlayer.PlayFile()* method (see below for examples). The JavaScript equivalent is `MediaDevices.getUserMedia()`.

Object Creation: *roVideoInput* is created with no parameters:

```
CreateObject("roVideoInput")
```

## ifVideoInput

##### GetStandards() As roArray

##### GetInputs() As roArray

These return an array of strings describing the various inputs and video standards that the video capture device supports. The following are the possible standards that can be returned: PAL-D/K, PAL-G, PAL-H, PAL-I, PAL-D, PAL-D1, PAL-K, PAL-M, PAL-N, PAL-Nc, PAL-60, SECAM-B/G, ECAM-B, SECAM-D, SECAM-G, SECAM-H, SECAM-K, SECAM-K1, SECAM-L, SECAM-LC, SECAM-D/K, NTSC-M, NTSC-Mj, NTSC-443, NTSC-Mk, PAL-B and PAL-B1. Inputs returned are s-video and composite.

##### SetStandard(standard As String) As Boolean  
 

##### GetCurrentStandard() As String  
 

##### SetInput(input As String) As Boolean  
 

##### GetCurrentInput() As String

Use the above to get and set the input and video standard.

##### GetControls() As roArray

Returns the possible controls on the input. These include "Brightness," "Contrast," "Saturation," "Hue," and others.

##### SetControlValue(control\_name As String, value As Integer) As Boolean

Sets the value of the specified control.

##### GetCurrentControlValue(control\_name As String) As roAssociativeArray

Returns an associative array with 3 members: "Value," "Minimum," and "Maximum." "Value" is the current value, and the possible range is specified by "Minimum" and "Maximum."

##### GetFormats() As Object  
 

##### SetFormat(a As String, b As Integer, c As Integer) As Boolean  
 

##### GetCurrentFormat() As String

## Examples

This script uses the HDMI Input as the video source to create a full-screen display.

```
v = CreateObject("roVideoPlayer")
i = CreateObject("roVideoInput")
p = CreateObject("roMessagePort")


vm = CreateObject("roVideoMode")
vm.SetMode("1920x1080x60p")


r = CreateObject("roRectangle", 0, 0, 1920, 1080)
v.SetRectangle(r)


v.PlayFile(i)
```

This script uses the video capture dongle as the video source to create a full-screen display.

```
v=CreateObject("roVideoPlayer")
i=CreateObject("roVideoInput")
p=CreateObject("roMessagePort")


vm=CreateObject("roVideoMode")
vm.SetMode("1280x720x60p")


r = CreateObject("roRectangle", 0, 0, 1280, 720)
v.SetRectangle(r)


i.SetInput("s-video")
i.SetStandard("ntsc-m")


v.PlayFile(i) 
```

#####