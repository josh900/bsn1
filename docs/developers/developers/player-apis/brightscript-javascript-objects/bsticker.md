# BSTicker

For more information about available methods, refer to the *roTextWidget* entry. This object can be used to display a scrolling type ticker.

> [!NOTE]
> This object supports both right-to-left and left-to-right (for example, Arabic, Hebrew) scrolling modes, depending on the language of the first string or file added to the widget. To change the scrolling direction, first remove all strings from the ticker.

## Object Creation

`BSTicker(in unsigned long x, in unsigned long y, in unsigned long w, in unsigned long h, in long rotation);`

The `x` and `y` integers specify the position of the ticker widget (via the top-left corner), while the  `w` and `h` integers specify the size of the widget. The `rotation` parameter accepts the following values (rotation is counter-clockwise from landscape mode):

`0`: 0 degrees

`90`: 90 degrees

`180`: 180 degrees

`270`: 270 degrees

> [!NOTE]
> The `rotation` parameter only affects the text inside the ticker; it does not alter the screen coordinates of the widget itself. If you are creating a vertical ticker or rotating the ticker to match portrait-mode HTML content, you will need to use the `x, y, w, h`  coordinate parameters to match the rotation of the text.

## Methods

`boolean SetRectangle(in unsigned long x, in unsigned long y, in unsigned long w, in unsigned long h)`

Modifies the (`x,y)` position and (`w,h)` size of the ticker widget. Changing the size of the widget will reset the ticker animation. As long as the size of the widget remains unchanged, modifying the position will not interrupt the ticker animation. This method returns `True` on success, or `False` on failure.

`int AddString(in DOMString str)`

Adds a string to the queue. This method returns a `string_id` integer that can be used to identify which string was removed when the `ontickerstringremoved` event is generated; a zero return indicates that the method failed to add the string. Adding too many strings without popping them from the stack will cause `AddString()` to return a non-zero value (the exact number depends on the font size for each string). The maximum recommended number of stored strings is 64.

`int AddSurface(in ImageData image)`

Adds a bitmap image to the list of strings to display. The image must be of type `ImageData`. This method returns a `string_id` integer that can be used to identify which surface is removed when the `ontickerstringremoved` event is generated. See the code at the bottom of this page for an example of using a canvas/image with this method.

`boolean PopStrings(in unsigned long count)`

Removes designated number of strings from the queue. This method returns `True` on success, or `False` on failure.

`boolean SetAutoPop(in boolean)`

If this method is set to `True`, strings are automatically removed (popped from the stack) once they have scrolled offscreen.

`boolean SetForegroundColor(in unsigned long argb)`

Specifies the foreground color as a 32-bit number in ARGB (Alpha, Red, Green, Blue) format. This method returns `True` on success, or `False` on failure.

`boolean SetForegroundColor(in unsigned long a, in unsigned long r, in unsigned long g, in unsigned long b)`

Sets the foreground color in red, green, and blue (foreground alpha values are currently unsupported and are ignored by this method, though this may change in future firmware versions). `a, r, g` and `b` are integer values between 0 and 255. This method returns `True` on success, or `False` on failure.

`boolean SetBackgroundColor(in unsigned long argb)`

Specifies the background color as a 32-bit number in ARGB (Alpha, Red, Green, Blue) format. This method returns `True` on success, or `False` on failure.

`boolean SetBackgroundColor(in unsigned long a, in unsigned long r, in unsigned long g, in unsigned long b)`

Sets the background color in alpha, red, green, and blue. While standard alpha values are between 0.0 and 1.0, the values in BSTicker are `unsigned long` (or the upper 8 bits of an `unsigned long`). The values are mapped between 0x00 and 0xff to correspond to 0.0 to 1.0. This method returns `True` on success, or `False` on failure.

`boolean SetSeparatorString(in DOMString str)`

Use a text string to separate individual messages. This method returns `True` on success, or `False` on failure.

`boolean SetSeparatorCircle()`

Use a circle to separate individual messages. This method returns `True` on success, or `False` on failure.

`boolean SetSeparatorDiamond()`

Use a diamond to separate individual messages. This method returns `True` on success, or `False` on failure.

`boolean SetSeparatorSquare()`

Use a square to separate individual messages. This method returns `True` on success, or `False` on failure.

`unsigned long SetPixelsPerSecond(in unsigned long pps)`

Sets the speed of the ticker.

`boolean SetFont(in DOMString font)`

Specifies a font for the BSTicker (as well as the roTextWidget BrightScript object). This method accepts a list of font-family names (similar to the CSS <font-family> property). The string can also have a `font-face:` prefix to indicate that this is a font description (for example, `font-face:DejaVu Serif,Serif Italic Bold`). Fonts must be added to the HTML widget using the `roHtmlWidget.AddFont()` method before they can be used in a BSTicker instance. This method returns `True` on success, or `False` on failure.

`boolean SetSyncManager(in DOMString domain)`

Specifies a BSSyncManager domain to use when executing the `SetMultiscreen()` call. When this method is called, it creates an internal domain based on the existing BSSyncManager domain and uses the same network parameters. We recommend using this method instead of passing a multicast IP address and port to the `SetMultiscreen()` method itself. This method returns `True` on success, or `False` on failure.

`boolean SetMultiscreen(in unsigned long offset, in unsigned long size, in DOMString ip_address, in unsigned long port)`

Call the `SetMultiscreen()` method to create a ticker that smoothly scrolls across multiple screens. This method returns `True` on success, or `False` on failure.

*   `offset:` Determines the left starting point (in pixels) in the multiscreen array. The parameter value will always be 0 for the leftmost display. This parameter should be calculated using the length of the multiscreen ticker, *not the total length of the multiscreen display*. For example, using an offset of 1920 in a two-screen array of 1920x1080 screens would specify this player as the right-hand (master) display.To create a ticker that smoothly scrolls across multiple screens, call the `SetMultiscreen()` method on each page. 
    
*   `size:` The total width (in pixels) of the multiscreen array across all displays. This parameter should be the same value for each `SetMultiscreen()` call. Note that the size of a multiscreen ticker can be different from the total width of a multiscreen display (for example, if the width of a BSTicker widget is smaller than the width of the screen). Defining a size of 3840 would specify a two-screen array of 1920x1080 screens.
    
*   `ip_address:` A string specifying the multicast IP address for the PTP synchronization process (for example, "239.192.0.0")
    
*   `port:` A string specifying the multicast port for the PTP synchronization process (for example, "1234").
    

The following example diagram and code snippets specify a multiscreen display with two monitors. The width of each monitor is 1024 pixels, while the width of each ticker is 768 pixels:

![](./attachments/SetMultiScreen()%20Diagram.png)

## Events

`bsTicker.ontickerstringremoved`

This event handler is triggered when a string has been removed and is no longer visible. The event contains the `string_id` property, which is returned by a successful `AddString()` call.

## Examples

The following script shows how to use many of the available *BSTicker* methods:

```
var bsTicker = new BSTicker(10, 110, 600, 30);
 
function addText1()
{
    console.log('############ addText1');
    bsTicker.AddString("addText1");
}
function addText2()
{
    console.log('############ addText2');
    bsTicker.AddString("addText2");
}
function addText3()
{
    console.log('############ addText3');
    bsTicker.AddString("addText3");
}

function setBackground1()
{
    console.log('############ setBackground1');
    bsTicker.SetBackgroundColor(0xFFFF0000);
}
function setBackground2()
{
    console.log('############ setBackground2');
    bsTicker.SetBackgroundColor(0xFF00FF00);
}

function setForeground1()
{
    console.log('############ setForeground1');
    bsTicker.SetForegroundColor(0xFF007700);
}
function setForeground2()
{
    console.log('############ setForeground2');
    bsTicker.SetForegroundColor(0xFF000077);
}

function setSeparatorString()
{
    console.log('############ setSeparatorString');
    bsTicker.SetSeparatorString(" ### ");
}
function setSeparatorCircle()
{
    console.log('############ setSeparatorCircle');
    bsTicker.SetSeparatorCircle();
}
function setSeparatorDiamond()
{
    console.log('############ setSeparatorDiamond');
    bsTicker.SetSeparatorDiamond();
}
function setSeparatorSquare()
{
    console.log('############ setSeparatorSquare');
    bsTicker.SetSeparatorSquare();
}

function setTickerSpeed()
{
    console.log('############ setTickerSpeed');
    var speed = bsTicker.SetPixelsPerSecond(180);
    console.log('############ SetPixelsPerSecond(180), Resulting speed: ' + speed);
}
```

The following examples allow for adding a canvas or image to the ticker with the `AddSurface()` method:

```
//Loading a canvas
var ctx = canvas.getContext("2d");
var img = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);

ticker.AddSurface(img); 

//Loading an image
var imageObj = new Image();
imageObj.onload = function() {
	canvas.width = this.width;
	canvas.height = this.height;

	var ctx = canvas.getContext("2d");
	ctx.drawImage(this, 0, 0); // Use getImage Data as above
 };
 imageObj.src = "filename.jpg";
```