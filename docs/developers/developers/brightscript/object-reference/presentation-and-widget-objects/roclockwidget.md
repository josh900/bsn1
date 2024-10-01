# roClockWidget

This object places a clock on the screen. It has construction arguments only.

Object Creation: The *roClockWidget* object is created with several parameters.

```
CreateObject("roClockWidget", rect As roRectangle, res As roResourceManager, display_type As Integer)
```

*   `rect`: The rectangle in which the clock is displayed. The widget picks a font based on the size of the rectangle.
    
*   `res`: A *resources.txt* file that allows localization via the *roResourceManager* object (see below for further details).
    
*   `display_type`: Use 0 for date only, and 1 for clock only. To show both on the screen, you need to create two widgets.
    

**Example**

```
rect=CreateObject("roRectangle", 0, 0, 300, 60)
res=CreateObject("roResourceManager", "resources.txt")
c=CreateObject("roClockWidget", rect, res, 1)
c.Show()
```

The resource manager is passed into the widget, which uses the following resources within the *resources.txt* file to display the time and date correctly. Here are the "eng" entries:

```
[CLOCK_DATE_FORMAT]
eng "%A, %B %e, %Y"
[CLOCK_TIME_FORMAT]
eng "%l:%M"
[CLOCK_TIME_AM]
eng "AM"
[CLOCK_TIME_PM]
eng "PM"
[CLOCK_DATE_SHORT_MONTH]
eng "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
[CLOCK_DATE_LONG_MONTH]
eng
"January|February|March|April|May|June|July|August|September|October|November|December"
[CLOCK_DATE_SHORT_DAY]
eng "Sun|Mon|Tue|Wed|Thu|Fri|Sat"
[CLOCK_DATE_LONG_DAY]
eng "Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday"
```

## Control Characters

The following are the control characters for the date/time format strings:

```
// Date format
//
// %a Abbreviated weekday name
// %A Long weekday name
// %b Abbreviated month name
// %B Full month name
// %d Day of the month as decimal 01 to 31
// %e Like %d, the day of the month as a decimal number, but without leading zero
// %m Month name as a decimal 01 to 12
// %n Like %m, the month as a decimal number, but without leading zero
// %y Two digit year
// %Y Four digit year

// Time format
//
// %H The hour using 24-hour clock (00 to 23)
// %I The hour using 12-hour clock (01 to 12)
// %k The hour using 24-hour clock (0 to 23); single digits are preceded by a blank.
// %l The hour using 12-hour clock (1 to 12); single digits are preceded by a blank.
// %M Minutes (00 to 59)
// %S Seconds (00 to 59)
```

## ifWidget

##### SetForegroundColor(color As Integer) As Boolean

Sets the foreground color in ARGB format. Hex color values should be converted to integers before being passed to this method (e.g. the value `&hFFFFFFFF` should be passed as 4294967295). You can use the `HexToInteger()` method (available in the [core library extension](../../../brightscript/language-reference/core-library-extension.md)) to convert a hex string to an integer.

##### SetBackgroundColor(color As Integer) As Boolean

Sets the background color in ARGB format. Hex color values should be converted to integers before being passed to this method (e.g. the value `&hFFFFFFFF` should be passed as 4294967295). You can use the `HexToInteger()` method (available in the [core library extension](../../../brightscript/language-reference/core-library-extension.md)) to convert a hex string to an integer.

> [!NOTE]
> The top 8 bits of the `SetForegroundColor()` and `SetBGackgroundColor()` values are "alpha" parameters. Zero is equivalent to fully transparent and 255 to fully non-transparent. This feature allows for effects similar to subtitles. For example, you can create a semi-transparent black box containing text over video.

##### SetFont(font\_filename As String) As Boolean

Sets the *font\_filename* using a TrueType font (for example, `SD:/Arial.ttf`).

##### SetBackgroundBitmap(bitmap\_filename As String, stretch As Boolean) As Boolean

Sets the background bitmap image. If stretch is True, then the image is stretched to the size of the window.

##### SetBackgroundBitmap(parameters As roAssociativeArray, stretch As Boolean) As Boolean

Sets the background bitmap image. If *stretch* is True, then the image is stretched to the size of the window. The associative array can contain the following parameters:

*   `Filename`: The name of the image file
    
*   `EncryptionAlgorithm`: The file-encryption algorithm. Currently the options are "AesCtr" and "AesCtrHmac".
    
*   `EncryptionKey`: The key to decrypt the image file. This is a byte array consisting of 128 bits of key, followed by 128 bits of IV.
    

> [!NOTE]
> See the [Image Decryption](../presentation-and-widget-objects/roimageplayer.md) section in the *roImagePlayer* entry for details on displaying encrypted images.

##### SetSafeTextRegion(region As roRectangle) As Boolean

Specifies the rectangle within the widget where the text can be drawn safely.

##### Show() As Boolean

Displays the widget. After creation, the widget is hidden until `Show()` is called.

##### Hide() As Boolean

Hides the widget.

##### Raise() As Void

Sends the widget to the top of the z-order on the graphics plane (i.e. in front of all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

> [!NOTE]
> Some surfaces are always drawn at the top of the graphics z-order, including the mouse cursor, closed captions, and [scrolling tickers](../presentation-and-widget-objects/rotextwidget.md).

> [!TIP]
> **Tip**
> You can use the `PauseGraphics()`/ `ResumeGraphics()` methods on the [*roVideoMode*](../presentation-and-widget-objects/rovideomode.md) object to ensure multiple changes to the graphics z-order occur simultaneously.

##### Lower() As Void

Sends the widget to the bottom of the z-order on the graphics plane (i.e. behind all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

##### GetFailureReason() As String

Yields additional useful information if a function return indicates an error.

##### SetRectangle(r As roRectangle) As Boolean

Changes the size and positioning of the widget rectangle using the passed *roRectangle* object.