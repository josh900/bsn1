# roTouchScreen

This object accepts inputs from touchscreen panels or mice. For each recognized input, the object will generate an *roTouchEvent* object. See the "roTouchScreen" section of the [BrightScript-JavaScript Migration Guide](../../../../developers/player-apis/brightscript-javascript-migration-guide.md) for the equivalent methods in JavaScript.

Not all touchscreens are supported. Please see [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2320728065/Supported+Touchscreens) for a full list of supported touchscreens. The *roTouchScreen* object responds to the clicks of a USB mouse in the same way it responds to touch events on a touchscreen.

To set up touchscreen/mouse interactivity, follow this outline:

1.  Create an *roTouchScreen* instance.
    
2.  Use `SetPort()` to specify an *roMessagePort* instance to receive the *roTouchScreen* events.
    
3.  Define one or more touch regions.
    
    1.  A touch region may be rectangular or circular.
        
    2.  When a touch or click occurs anywhere inside the area of a touch region, an event will be sent to the message port.
        
    3.  If touch regions overlap such that a click or touch hits multiple regions, an event for each affected region will be sent.
        
4.  Process the events.
    

The *roTouchScreen* object supports rollover regions. Rollovers are based around touch regions. When a rectangular or circular region is added, it defaults to having no rollover. You can use the `EnableRollover()` method to add an *on* and *off* image for a region. Whenever the mouse cursor is within that region, the *on* image is displayed. In all other cases, the *off* image is displayed. This allows buttons to be highlighted as the mouse cursor moves over them.

## ifTouchScreen

##### SetResolution(x As Integer, y As Integer) As Void  
 

##### AddRectangleRegion(x As Integer, y As Integer, w As Integer, h As Integer, region\_id As Integer) As Void

Adds a rectangular touch region to the screen. The region\_id is used to associate the touch region with *roTouchEvent* events and to link the region with rollover images.

##### AddCircleRegion(x As Integer, y As Integer, radius As Integer, region\_id As Integer) As Void

Adds a circular touch region to the screen. The `region_id` is used to associate the touch region with *roTouchEvent* events and to link the region with rollover images.

##### ClearRegions() As Void

Clears the list of regions added using `AddRectangleRegion()` or `AddCircleRegion()` so that any contacts in those regions no longer generate events. This call has no effect on the rollover graphics.

##### GetDeviceName() As String  
 

##### SetCursorPosition(x As Integer, y As Integer) As Void  
 

##### SetCursorBitmap(filename As String, x As Integer, y As Integer) As Void 

Specifies a BMP or PNG file as the mouse cursor icon. This method also accepts a "hot spot" (i.e. the point within the icon rectangle that will trigger events when the mouse is clicked) as a set of **x,y** coordinates. The icon can be a rectangle of any width or height.

##### EnableCursor(enable As Boolean) As Void

Displays a cursor on screen if passed True.

##### EnableRollover(region\_id As Integer, on\_image As String, off\_image As String, cache\_image As Boolean, image\_player As Object) As Void

Enables a rollover for a touch region. This method accepts the ID of the touch region, as well as two strings specifying the names of the *on* and *off* bitmap images, a cache setting, and the image player that draws the rollover. The `cache_image` parameter simply tells the script whether to keep the bitmaps loaded in memory or not. This setting uses up memory very quickly, so we recommend that `cache_image` normally be set to 0.

##### SetRollOverOrigin(region\_id As Integer, x As Integer, y As Integer) As Void

Changes the origin so that more (or less) of the screen changes when the mouse rolls in and out of the region. This means that bitmaps that are larger than the region can be drawn. The default requirement is that rollover bitmaps be the same size and position as the touch region. Note that the bitmap is square for circular regions. The default origin for circular regions is \[x - r\]**,** \[y – r\], where x**,** y is the center of the circle, and r is the radius.

> [!CAUTION]
> **Important**
> The `EnableRollover()` and `SetRollOverOrigin()` methods have been deprecated. As of OS8, the end points exist but do not perform any function.

##### EnableRegion(region\_id As Integer, enabled As Boolean) As Void

Enables or disables a rollover region. This method accepts the ID of the touch region, as well as a Boolean value (True or False). The rollover regions default to "enabled" when created, but you can set up all of the regions at the start of your script and then enable regions as required.

##### IsMousePresent() As Boolean

Returns True if a relative pointing device is attached to the player. This does not work for absolute devices like touchscreens.

##### SetMouseRotation(rotation As Integer) As Boolean

Transforms mouse-movement inputs to account for screen rotation. This method can accept the following integers:

*   0: Inputs are unchanged (i.e. landscape orientation).
    
*   1, 90: Rotated 90 degrees (i.e. clockwise portrait orientation).
    
*   2, 180: Rotated 180 degrees.
    
*   3, 270: Rotated 270 degrees (i.e. counter-clockwise portrait orientation).
    

##### EnableSerialTouchscreen(a As Integer) As Boolean  
 

##### SetSerialTouchscreenConfiguration(a As String) As Boolean

##### GetDiagnosticInfo() As String

Returns an HTML string with captured information describing hardware that was connected and events that occurred during the calibration process. This method is used by the calibration script to diagnose touchscreen issues.

## ifSetMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roTouchEvent* and *roTouchCalibrationEvent* to the attached message port.

## ifTouchScreenCalibration

##### StartCalibration() As Boolean  
 

##### GetCalibrationStatus() As Integer  
 

##### GetDiagnosticInfo() As String  
 

##### ClearStoredCalibration() As Boolean  
 

##### StartEventLogging() As Boolean  
 

##### StopEventLogging() As Boolean  
 

##### ClearEventLogs() As Boolean

##### SetCalibrationRanges(x-min As Integer, x-max As Integer, y-min As Integer, y-max As Integer) As Boolean

Overrides the screen range values provided by the touchscreen. This method is useful when the entirety of the video output is not being displayed on the touch surface. Practical use of this method usually requires a custom calibration script, appropriate images, and a calibration setting matched to a particular setup.

## ifSerialControl

##### SetBaudRate(baud\_rate As Integer) As Boolean

Sets the baud rate of the device. The supported baud rates are as follows: 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400.

##### NotUsed1(a As String)  
 

##### SetMode(a As String) As Boolean  
 

##### NotUsed2(a As Boolean) As Boolean

## Examples

This script loops a video and waits for a mouse click or touchscreen input. It outputs the coordinates of the click or touch to the shell if it is located within the defined region.

```
v=CreateObject("roVideoPlayer")
t=CreateObject("roTouchScreen")
p=CreateObject("roMessagePort")

v.SetPort(p)
t.SetPort(p)
v.SetLoopMode(True)
v.PlayFile("testclip.mp2v")

t.AddRectangleRegion(0,0,100,100,2)

loop:
    msg=Wait(0, p)
    print "type: ";type(msg)
    print "msg=";msg
    if type(msg)="roTouchEvent" then
        print "x,y=";msg.GetX();msg.GetY()
    endif
    goto loop:
```

This script includes mouse support:

```
t=CreateObject("roTouchScreen")
t.SetPort(p)
REM Puts up a cursor if a mouse is attached
REM The cursor must be a 16 x 16 BMP
REM The x,y position is the "hot spot" point
t.SetCursorBitmap("cursor.bmp", 16, 16)
t.SetResolution(1024, 768)
t.SetCursorPosition(512, 389)
REM
REM Pass enable cursor display:  TRUE for on, and FALSE for off
REM The cursor will only enable if there is a mouse attached
REM
t.EnableCursor(true)
```

This script includes a rollover region and mouse support:

```
img=CreateObject("roImagePlayer")
t=CreateObject("roTouchScreen")
p=CreateObject("roMessagePort")
t.SetPort(p)


t.SetCursorBitmap("cursor.bmp", 16, 16)
t.SetResolution(1024, 768)
t.SetCursorPosition(512, 389)
t.EnableCursor(true)


img.DisplayFile("\menu.bmp")


REM Adds a rectangular touch region
REM Enables rollover support for that region
REM Sets the rollover origin to the same position as the touch region REM
t.AddRectangleRegion(0, 0, 100, 100, 1)
t.EnableRollOver(1, "on.bmp", "off.bmp", true, img)
t.SetRollOverOrigin(1, 0, 0)
```

#####