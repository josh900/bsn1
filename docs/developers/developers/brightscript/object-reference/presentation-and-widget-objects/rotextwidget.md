# roTextWidget

This object is used to display text on the screen.

Note that "Scrolling ticker" mode is limited to 10 tickers at a time. You can have 100 roTextWidgets, so long as they are in some other mode (for example, "Static text")*.*

Object Creation: This object is created using one of two variants.

**Option 1**

```
CreateObject("roTextWidget", r As roRectangle, line_count As Integer, text_mode As Integer, pause_time As Integer)
```

*   `r` : An *roRectangle* instance that contains the text
    
*   `line_count`: The number of lines of text to show within the rectangle
    
*   `text_mode`: The animation characteristics of the text:
    
    *   0: An animated view similar to teletype
        
    *   1: Static text
        
    *   2: Simple text with no queue of strings
        
    *   3: Scrolling ticker (strings are separated with a diamond by default; the separator can be modified using the `SetSeparator()` method). Note that this option is not available for LSx22, HDx20, or HDx10 models. 
        
*   `pause_time`: The length of time each string is displayed before displaying the next string. This does not apply to text mode 2 or 3 because the strings on screen are updated immediately.
    

**Option 2**

```
CreateObject("roTextWidget", r As roRectangle, line_count As Integer, text_mode As Integer, parameters As roAssociativeArray)
```

*   `r`: An *roRectangle* instance that contains the text
    
*   `line_count`: The number of lines of text to show within the rectangle
    
*   `text_mode`: The animation characteristics of the text:
    
    *   0: An animated view similar to teletype
        
    *   1: Static text
        
    *   2: Simple text with no queue of strings
        
    *   3: Scrolling ticker (strings are separated with a diamond by default; the separator can be modified using the `SetSeparator()` method). Note that this option is not available for LSx22, HDx20, or HDx10 models.
        
*   `parameters`: An associative array that can include the following values:
    
    *   `LineCount`: The number of lines of text to show within the rectangle.
        
    *   `TextMode`: The animation characteristics of the text:
        
        *   0: An animated view similar to teletype
            
        *   1: Static text
            
        *   2: Simple text with no queue of strings
            
        *   3: Scrolling ticker (strings are separated with a diamond by default; the separator can be modified using the `SetSeparator()` method). Note that this option is not available for LSx22, HDx20, or HDx10 models.
            
    *   `PauseTime`: The length of time each string is displayed before displaying the next string. This does not apply to text mode 2 or 3 because the strings on screen are updated immediately.
        
    *   `Rotation`: The rotation of the text within the widget (note that the coordinates and dimensions of the rectangle itself are not rotated):
        
        *   0: 0 degrees
            
        *   1: 90 degrees. This value can also be represented in degrees (90) or radians (.5Π).
            
        *   2: 180 degrees. This value can also be represented in degrees (180) or radians (Π).
            
        *   3: 270 degrees. This value can also be represented in degrees (270) or radians (1.5Π).
            
*   `Alignment`: The alignment of the text:
    
    *   0: Left
        
    *   1: Center
        
    *   2: Right
        

> [!TIP]
> **Tip**
> Modes 0, 1, and 3 are useful for displaying RSS feeds and ticker-type text. However, for dynamic data where immediate screen updates are required, mode 2 may be more appropriate. Mode 2 allows text to be drawn immediately to the screen.

> [!NOTE]
> Text-mode 3 (scrolling ticker) supports both right-to-left and left-to-right (e.g. Arabic, Hebrew) scrolling modes, depending on the language of the first string or file added to the widget. To change the scrolling direction, you will first need to remove all strings from the ticker.

## ifTextWidget

##### SetGlobalParameter(param As String, value as Integer) As Void

Configures parameters related to scrolling tickers (i.e. text mode 3). The following are accepted parameters: 

*   `startat`: The starting position of scrolling text, which can be any number between 0 (the left side of the screen) and the total width of the widget. To start at the right side of the screen (i.e. offscreen), specify a value of -1 or the total width of the widget. 
    
*   `autopop`: The autopop setting for the widget. If this value is set to 1, strings are automatically removed (popped from the stack) once they have scrolled offscreen. If this value is set to 0 (the default behavior), strings are not automatically removed. 
    
*   `autoaddseparator`: The separator setting for the widget. Setting this value to 0 disables string separators (useful for displaying emojis with the `PushSurface()` method), while setting this value to 1 enables string separators (the default behavior). 
    
*   `gap`: The gap (in pixels) between the string and the string separator (at both the beginning and end of strings). The default value is 0. This parameter may not be reliable if the ticker contains strings in its memory. 
    

> [!NOTE]
> Global parameters can be altered after `Show()` is called, but in some cases (e.g. the `startat` parameter) their results are undefined. The parameters `autopop` and `autoaddseparator` are intended to be used once `Show()` has been called.

##### GetGlobalParameter(param as String) As Integer

Returns the value of a parameter set using the `SetGlobalParameter()` method. This method also returns a value for the read-only "`last_string_id`" parameter, which is a unique identifier for the string most recently added to the list-list value that is identical to the integer returned by the `PushString()` and `PushSurface()` methods. 

##### PushString(str As String) As Boolean

Adds the string to the list of elements to display in modes 0, 1, and 3. Strings are displayed in order, and when the end is reached, the object loops, returning to the beginning of the list. In mode 2, the string is displayed immediately. This method returns a unique identifier, which can be used with *roTextWidgetEvent* messages to determine when the string has moved offscreen. A failure to add an element to the list returns "0". 

> [!NOTE]
> Adding too many strings without popping them from the stack will cause PushString() to return False (the exact number depends on the font size for each string). The maximum recommended number of stored strings is 64.

##### PushSurface(image as roImageBuffer) As Integer

Adds a bitmap image to the list of elements to display in modes 0, 1, and 3. Images are scaled to match the height of the ticker. This method returns a unique identifier. which can be used with *roTextWidgetEvent* messages to determine when the image/surface has moved offscreen. A failure to add an element to the list returns "0". 

> [!NOTE]
> There are currently no restrictions on formatting, but it is recommended to use the same color format as the main screen.

##### PopStrings(number\_of\_string\_to\_pop As Integer) As Boolean

Pops elements off the front of the list (using "last in, first out" ordering) in modes 0, 1, and 3. This occurs the next time the widget wraps so that elements can be added to and removed from the widget seamlessly. In mode 2, the element is cleared from the widget immediately.

##### GetStringCount() As Integer

Returns the number of elements that will exist once any pending pops have taken place.

##### Clear() As Boolean

Clears the list of elements, leaving the widget blank and able to accept more `PushString()` calls.

##### SetStringSource(file\_path As String) As Boolean

Displays the text file at the specified path as a single, continuous string. This method is only applicable to text mode 3 (scrolling ticker). When the end of the file is reached, the text widget loops to the beginning, using a diamond symbol as the separator.

##### SetAnimationSpeed(speed As Integer) As Boolean

Sets the speed at which animated text displays. This method is applicable to text modes 0 and 3 only:

*   Mode 0: The default speed value is 10000. Setting an integer above this value decreases the speed of the teletype-style ticker: For example, specifying a value of 20000 will decrease the default speed at which text displays by half, while a value of 5000 will double the default speed.
    
*   Mode 3: The default speed value is 10000. Because the speed of a scrolling ticker is measured in pixels per second (PPS), the speed must be a multiple of the current framerate, or else it will be rounded down to the nearest multiple (for example, a framerate of 60p will honor PPS values of 60, 120, 180, etc.). The software determines the speed of the scrolling ticker by performing the following calculation on the passed `speed` parameter:  
    `PPS = (speed * 60) / 10000`
    

##### SetSeparator(separator As String) As Boolean

Changes the separator between strings. The default diamond separator will be replaced by the contents of the passed string. This method applies to Text Mode 3 (smooth scrolling ticker) only. The following strings indicate special symbols: ":diamond:", ":circle:", ":square:".

##### SetSyncManager(domain As String) As Boolean

Specifies a [*roSyncManager*](../../object-reference/networking-objects/rosyncmanager.md) domain to use when executing the `SetMultiscreen()` call. When this method is called, it creates an internal domain that is based on the existing *roSyncManager* domain and uses the same network parameters. We recommend using this method instead of passing a multicast IP address and port to the `SetMultiscreen()` method itself.

##### SetMultiscreen(offset As Integer, size As Integer, ip\_address As String, port As Integer) As Boolean

Displays a smooth scrolling ticker across multiple screens. To specify network synchronization parameters, you can either call the `SetSyncManager()` method first or pass the optional `ip_address` and `port` values to the `SetMultiscreen()` method (calling `SetSyncManager()` is preferred). If you use `SetSyncManager()`, do not specify the `ip_address`/`port`; doing so may lead to unexpected behavior.

The master screen is designated as the instance with the rightmost offset of all the players in the multiscreen array; all `PushString()` and `Show()` calls (as well as any other changes) must be made on the master instance. Follower instances of the text widget will remain blank until the leader starts. This method requires the following parameters:

*   `offset`: The offset (in pixels) of the display in the multiscreen array. For example, using an offset of 1920 in a two-screen array of 1920x1080 screens would specify this player as the right-hand (master) display.
    
*   `size`: The total width (in pixels) of the multiscreen array. For example, defining a size of 3840 would specify a two-screen array of 1920x1080 screens.
    
*   `ip_address`: A string specifying the multicast IP address for the [roSyncManager](../../object-reference/networking-objects/rosyncmanager.md) network traffic (e.g. "239.192.0.0")
    
*   `port`: A string specifying the multicast port for the PTP synchronization process (e.g. 1234).
    

> [!NOTE]
> Players can support more than one multiscreen ticker at a time.

## ifWidget

##### Show() As Boolean

Displays the widget. After creation, the widget is hidden until Show() is called.

##### Hide() As Boolean

Hides the widget.

##### Raise() As Void

Sends the widget to the top of the z-order on the graphics plane (i.e. in front of all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

> [!NOTE]
> Some surfaces are always drawn at the top of the graphics z-order, including the mouse cursor, closed captions, and scrolling tickers.

> [!TIP]
> **Tip**
> You can use the `PauseGraphics()`/ `ResumeGraphics()` methods on the [*roVideoMode*](../presentation-and-widget-objects/rovideomode.md) object to ensure multiple changes to the graphics z-order occur simultaneously.

##### Lower() As Void

Sends the widget to the bottom of the z-order on the graphics plane (i.e. behind all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

##### SetForegroundColor(color As Integer) As Boolean

Sets the foreground color in ARGB format. The top 8 bits are "alpha" parameters. Zero is equivalent to fully transparent and 255 to fully non-transparent.

> [!NOTE]
> Foreground alpha values are currently unsupported with ticker mode 3 (scrolling ticker) and will be ignored by this method. This behavior may change in future firmware versions.

Hex color values should be converted to integers before being passed to this method (e.g. the value `&hFFFFFFFF` should be passed as 4294967295). You can use the `HexToInteger()` method (available in the [core library extension](../../../brightscript/language-reference/core-library-extension.md)) to convert a hex string to an integer.

##### SetBackgroundColor(color As Integer) As Boolean

Sets the background color in ARGB format. The top 8 bits are "alpha" parameters. Zero is equivalent to fully transparent and 255 to fully non-transparent. This feature allows for effects similar to subtitles. For example, you can create a semi-transparent black box containing text over video.

Hex color values should be converted to integers before being passed to this method (e.g. the value `&hFFFFFFFF` should be passed as 4294967295). You can use the `HexToInteger()` method (available in the [core library extension](../../../brightscript/language-reference/core-library-extension.md)) to convert a hex string to an integer.

##### SetFont(font\_filename As String) As Boolean

Specifies a custom font for the widget using a TrueType font file from local storage (e.g. "SD:/ComicSans.ttf").

##### SetBackgroundBitmap(bitmap\_filename As String, stretch As Boolean) As Boolean

Sets the background bitmap image. If stretch is True, then the image is stretched to the size of the widget.

##### SetBackgroundBitmap(parameters As roAssociativeArray, stretch As Boolean) As Boolean

Sets the background bitmap image. If *stretch* is True, then the image is stretched to the size of the widget. The associative array can contain the following parameters:

*   `Filename`: The name of the image file
    
*   `EncryptionAlgorithm`: The file-encryption algorithm. Currently the options are "AesCtr" and "AesCtrHmac".
    
*   `EncryptionKey`: The key to decrypt the image file. This is a byte array consisting of 128 bits of key, followed by 128 bits of IV.
    

> [!NOTE]
> See the [Image Decryption](../presentation-and-widget-objects/roimageplayer.md) section in the *roImagePlayer* entry for details on displaying encrypted images.

##### SetSafeTextRegion(region As roRectangle) As Boolean

Specifies the rectangle within the widget where the text can be drawn safely.

##### SetRectangle(r As roRectangle) As Boolean

Changes the size and positioning of the widget rectangle using the passed *roRectangle* object.

##### GetFailureReason() As String

Yields additional useful information if a function return indicates an error.