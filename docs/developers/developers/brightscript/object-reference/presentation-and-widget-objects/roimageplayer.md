# roImagePlayer

This object displays static bitmap images on the video display. The simplest way to use *roImagePlayer* is to make calls to `DisplayFile()` with the filename as a String. Alternatively, you can use `PreloadFile()` in conjunction with `DisplayPreload()` to have more control. For more pleasing aesthetics when generating an image player, use the *roImageWidget* object. The JavaScript equivalent is the [<img> tag in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img).

Object Creation: The image player is displayed by first creating *roRectangle* and *roImagePlayer* instances, then calling `SetRectangle()` using the *roRectangle* instance as the argument.

```
rectangle = CreateObject("roRectangle", 0, 0, 1024, 768)
i = CreateObject("roImagePlayer")
i.SetRectangle(rectangle)
```

## ifImageControl 

##### DisplayFile(image\_filename As String) As Boolean

Displays the image with the specified filename. The image\_filename string must point to a *.png*, *.jpeg*, or 8-bit, 24-bit, or 32-bit *.bmp* file. Note that *.jpeg* image files with CMYK color profiles are not supported.

##### DisplayFile(parameters As roAssociativeArray) As Boolean

Displays an image using an associative array of display parameters:

*   `Filename`: The name of the image file
    
*   `Mode`: The image mode. See the entry for SetDefaultMode() below for more details.
    
*   `Transition`: The image transition setting. See the entry for SetDefaultTransition() below for more details.
    
*   `EncryptionAlgorithm`: The file-encryption algorithm. Currently the options are "AesCtr" and "AesCtrHmac".
    
*   `EncryptionKey`: The key to decrypt the image file. This is a byte array consisting of 128 bits of key, followed by 128 bits of IV.
    

See the [Image Decryption](https://docs.brightsign.biz/display/DOC/roImagePlayer#roImagePlayer-ImageDecryptionimage_decryption) section below for details on displaying encrypted images.

> [!CAUTION]
> **Important**
> The image player no longer accepts "{A|A}" AES encryption keys (i.e. where the top and bottom 64 bits of the key are identical).

##### PreloadFile(image\_filename As String) As Boolean

Loads the specified image file into an offscreen memory buffer.

##### PreloadFile(parameters As roAssociativeArray) As Boolean

Loads an image file into an offscreen memory buffer. Image display properties are determined by an associative array of parameters:

*   `Filename`: The name of the image file
    
*   `Mode`: See the entry for SetDefaultMode() below for more details.
    
*   `Transition`: See the entry for SetDefaultTransition() below for more details.
    

##### DisplayPreload() As Boolean

Uses the on-screen memory buffer to display the image stored in the offscreen memory buffer using `PreloadFile()`. There are only two memory buffers: one is displayed on screen; and the other is used for preloading images. `PreloadFile()`can be called multiple times before `DisplayPreload()` is called, and will keep loading into the same off-screen buffer. The `DisplayFile()` method calls `PreloadFile()` followed immediately by `DisplayPreload()`, so any previously preloaded image will be lost. If no image is preloaded, `DisplayPreload()` will have no effect.

##### StopDisplay() As Boolean

Removes an image from the display.

##### DisplayFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean  
 

##### PreloadFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean

##### SetDefaultMode(mode As Integer) As Boolean

Sets the default image display mode for DisplayFile() and PreloadFile(). If SetDefaultMode() is not called, then the default mode is set to 0 (equivalent to the image being centered without scaling). The supported display mode are listed below:

*   **0 – Center image**: No scaling takes place. Cropping only occurs if the image is bigger than the window.
    
*   **1 – Scale to fit**: The image is scaled so that it is fully viewable, with its aspect ratio maintained.
    
*   **2 – Scale to fill and crop**: The image is scaled so that it completely fills the window, with its aspect ratio maintained.
    
*   **3 – Scale to fill**: The image is stretched so that it fills the window and the whole image is viewable. The aspect ratio will not be maintained if it is different from the window.
    

##### SetDefaultTransition(transition As Integer) As Boolean

Sets the transition to be used when the next image is displayed. The following are available transitions:

*   0: No transition: immediate blit
    
*   1-4: Wipes from top, bottom, left, or right.
    
*   5-8: Explodes from centre, top left, top right, bottom left, or bottom right.
    
*   10-11: Uses vertical or horizontal venetian-blind effect.
    
*   12-13: Combs vertical or horizontal.
    
*   14: Fades out to background color, then back in.
    
*   15: Fades between current image and new image.
    
*   16-19: Slides from top, bottom, left or right.
    
*   20-23: Slides entire screen from top, bottom, left, or right.
    
*   24-25: Scales old image in, then the new one out again (this works as a pseudo rotation around a vertical or horizontal axis).
    
*   26-29: Expands a new image onto the screen from right, left, bottom, or top.
    

##### SetTransform(transform As String) As Boolean

Applies one of eight transforms to the image. Calls to this method only take effect when the next file is displayed. Note that the image rectangle itself does not change to accommodate the new height and width ratio of a transformed image. This method can be called separately on multiple *roImagePlayer* or *roImageWidget* instances.

*   `identity`: No transformation (default behavior)
    
*   `rot90`: 90 degree clockwise rotation
    
*   `rot180`: 180 degree rotation
    
*   `rot270`: 270 degree clockwise rotation
    
*   `mirror`: Horizontal mirror transformation
    
*   `mirror_rot90`: Mirrored 90 degree clockwise rotation
    
*   `mirror_rot180`: Mirrored 180 degree clockwise rotation
    
*   `mirror_rot270`: Mirrored 270 degree clockwise rotation
    

##### OverlayImage(image\_filename As String, x As Integer, y As Integer) As Boolean

Composites the image with the specified filename on top of the primary `DisplayFile()` image. Use the `x` and `y` integers to specify its location within the image widget.

##### SetRectangle(r As roRectangle) As Boolean

Changes the size and positioning of the image rectangle using the passed *roRectangle* object.

##### GetRectangle() As roRectangle

Returns an *roRectangle* object that has the same location and dimensions as the *roRectangle* object used to define the image window.

##### CreateTestHole(hole As roRectangle) As Boolean

Creates a hole in the image with the location and dimensions specified in the passed *roRectangle* instance. Any video windows located directly beneath the image will show through. This method will disrupt image playback and should be used for test purposes only.

##### SetTransitionDuration(duration As Integer) As Boolean

Sets the amount of time it takes (in milliseconds) for a specified transition effect to take place. The default transition duration is 1000 milliseconds.

##### DisplayBuffer(a As Object, b As Integer, c As Integer) As Boolean  
 

##### Hide() As Boolean

Hides the image currently being displayed by the *roImagePlayer* widget.

##### Show() As Boolean

Shows the image currently being displayed by the *roImagePlayer* widget.

##### Raise() As Void

Sends the widget to the top of the z-order on the graphics plane (i.e. in front of all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

> [!NOTE]
> Some surfaces are always drawn at the top of the graphics z-order, including the mouse cursor, closed captions, and [scrolling tickers](../presentation-and-widget-objects/rotextwidget.md).

> [!TIP]
> **Tip**
> You can use the `PauseGraphics()`/ `ResumeGraphics()` methods on the [*roVideoMode*](../presentation-and-widget-objects/rovideomode.md) object to ensure multiple changes to the graphics z-order occur simultaneously.

##### Lower() As Void

Sends the widget to the bottom of the z-order on the graphics plane (i.e. behind all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

## X, Y

The x and y values indicate which position of the image to center as near as possible, or both x and y can be set to -1, which uses the center of the image as the point to position nearest to the center.

To display images in a zone, `SetRectangle()` must be called, and `EnableZoneSupport()` must be included in a script to use the zones functionality.

## Testing Display Modes

Here are some example shell commands you can use to test the different display modes:

```
BrightSign> image filename.bmp 0
BrightSign> image filename.bmp 1
BrightSign> image filename.bmp 2
BrightSign> image filename.bmp 3

BrightSign> image filename.bmp 0 0 0
BrightSign> image filename.bmp 2 0 0
```

## Preloading Images

The following example script uses preloaded images to improve the UI speed when the user hits a key on the keyboard. As soon as a key is struck, the display switches to the new image, which has already been preloaded. The only possible delay occurs if the key is hit while the image is preloading. In this case, the image will display as soon as it is loaded.

```
i = CreateObject("roImagePlayer")
p = CreateObject("roMessagePort")
k = CreateObject("roKeyboard")
k.SetPort(p)

i.PreloadFile("one.bmp")

loop:
i.DisplayPreload
i.PreloadFile("two.bmp")
Wait(0,p)
i.DisplayPreload
i.PreloadFile("one.bmp")
Wait(0,p)
goto loop
```

## Image Decryption 

The *roImagePlayer*, *roImageWidget*, *roClockWidget*, *roTextWidget*, and *roCanvasWidget* objects can be used to display encrypted images. Each object has an image playback method that accepts an associative array, which can include the `EncryptionAlgorithm` and `EncryptionKey` decryption parameters.

> [!NOTE]
> Contact [support@brightsign.biz](mailto:support@brightsign.biz) to learn more about generating a key for obfuscation and storing it on the player.

You can call `roDeviceInfo.HasFeature("media_decryption")`  to determine if a player model and firmware version supports image decryption.

Example:

```
print "Play ENCRYPTED image in an image widget"

imagePlayer = CreateObject("roImageWidget", r1)

aa=CreateObject("roAssociativeArray")
aa.filename = "sd:/images_enc.jpg"
aa.encryptionalgorithm = "AesCtr"
aa.encryptionkey = CreateObject("roByteArray")
aa.encryptionkey.fromhexstring("01030507090b0d0f00020406080a0c0e00000000000000000000000000000000")

imagePlayer.DisplayFile(aa)
sleep(10000)
imagePlayer.Hide()

print "Play ENCRYPTED image with PlayStaticImage"

videoPlayer = CreateObject("roVideoPlayer")

aa=CreateObject("roAssociativeArray")
aa.filename = "sd:/images_enc.jpg"
aa.encryptionalgorithm = "AesCtr"
aa.encryptionkey = CreateObject("roByteArray")
aa.encryptionkey.fromhexstring("01030507090b0d0f00020406080a0c0e00000000000000000000000000000000")

videoPlayer.PlayStaticImage(aa)
sleep(10000)
videoPlayer = invalid

print "Show CLOCK image"

resourceManager = CreateObject("roResourceManager", "sd:/resources.txt")

clockWidget = CreateObject("roClockWidget", r1, resourceManager, {})

aa=CreateObject("roAssociativeArray")
aa.filename = "sd:/images_enc.jpg"
aa.encryptionalgorithm = "AesCtr"
aa.encryptionkey = CreateObject("roByteArray")
aa.encryptionkey.fromhexstring("01030507090b0d0f00020406080a0c0e00000000000000000000000000000000")

clockWidget.SetBackgroundBitmap(aa, True)
clockWidget.Show()
sleep(10000)
clockWidget.Hide()

print "Text widget with encrypted background image"

twParams = CreateObject("roAssociativeArray")
twParams.LineCount = 1
twParams.TextMode = 1
twParams.Rotation = 0
twParams.Alignment = 1

tw=CreateObject("roTextWidget",r1,1,2,twParams)
tw.SetBackgroundColor(&h00ff0000)
tw.SetForegroundColor(&hff00ff00)
tw.PushString("Encrypted Background")
'tw.SetRectangle(r)

aa=CreateObject("roAssociativeArray")
aa.filename = "sd:/images_enc.jpg"
aa.encryptionalgorithm = "AesCtr"
aa.encryptionkey = CreateObject("roByteArray")
aa.encryptionkey.fromhexstring("01030507090b0d0f00020406080a0c0e00000000000000000000000000000000")

tw.SetBackgroundBitmap(aa, True)
tw.Show()
sleep(10000)
tw.Hide()

cw=CreateObject("roCanvasWidget", rect)
canvas_aa=CreateObject("roAssociativeArray")
canvas_aa.Filename = "sd:/images_enc.jpg"
canvas_aa.Encryptionalgorithm = "AesCtr"
canvas_aa.EncryptionKey = CreateObject("roByteArray")
canvas_aa.EncryptionKey.FromHexString("01030507090b0d0f00020406080a0c0e00000000000000000000000000000000")
cw.SetLayer(canvas_aa, 1)
cw.Show() 
```