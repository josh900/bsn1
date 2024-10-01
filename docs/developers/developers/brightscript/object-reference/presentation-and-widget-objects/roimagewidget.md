# roImageWidget

This object can be used in place of *roImagePlayer* in cases where the image is displayed within a rectangle. Using an *roImageWidget* can result in more pleasing aesthetics for image player creation; it can also be used to display images in a multi-screen array. Beyond this, *roImageWidget* behaves identically to *roImagePlayer*. The JavaScript equivalent is the [<img> tag in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img).

Object Creation: The image widget area is generated using an *roRectangle* object.

```
rectangle = CreateObject("roRectangle", 0, 0, 1024, 768)
i = CreateObject("roImageWidget", rectangle)
```

## ifImageControl 

##### DisplayFile(image\_filename As String) As Boolean

Displays the image with the specified filename. The image\_filename string must point to a *.png*, *.jpeg*, or 8-bit, 24-bit, or 32-bit *.bmp* file. Note that *.jpeg* image files with CMYK color profiles are not supported.

##### DisplayFile(parameters As roAssociativeArray) As Boolean

Displays an image using an associative array of display parameters:

*   `Filename`: The name of the image file
    
*   `Mode`: The image mode. See the entry for SetDefaultMode() below for more details.
    
*   `Transition`: The image transition setting. See the entry for SetDefaultTransition() below for more details.
    
*   `EncryptionAlgorithm`: The file-encryption algorithm. Currently the options are "AesCtr" and "AesCtrHmac".
    
*   `EncryptionKey`: The key to decrypt the image file. This is a byte array consisting of 128 bits of key, followed by 128 bits of IV.
    

See the [Image Decryption](../presentation-and-widget-objects/roimageplayer.md) descrption in the *roImagePlayer* entry for details on displaying encrypted images.

##### PreloadFile(image\_filename As String) As Boolean

Loads the specified image file into an offscreen memory buffer.

##### PreloadFile(parameters As roAssociativeArray) As Boolean

Loads an image file into an offscreen memory buffer. Image display properties are determined by an associative array of parameters:

*   `Filename`: The name of the image file
    
*   `Mode`: See the entry for SetDefaultMode() below for more details.
    
*   `Transition`: See the entry for SetDefaultTransition() below for more details.
    

##### DisplayPreload() As Boolean

Uses the on-screen memory buffer to display the image stored in the offscreen memory buffer using `PreloadFile()`. There are only two memory buffers: one is displayed on screen; and the other is used for preloading images. `PreloadFile()`can be called multiple times before `DisplayPreload()` is called, and will keep loading into the same off-screen buffer. The `DisplayFile()` method calls `PreloadFile()` followed immediately by `DisplayPreload()`, so any previously preloaded image will be lost. If no image is preloaded, `DisplayPreload()` will have no effect.

##### StopDisplay() As Boolean

Removes an image from the display.

##### DisplayFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean  
 

##### PreloadFileEx(filename As String, mode As Integer, x As Integer, y As Integer) As Boolean

##### SetDefaultMode(mode As Integer) As Boolean

Sets the default image display mode for DisplayFile() and PreloadFile(). If SetDefaultMode() is not called, then the default mode is set to 0 (equivalent to the image being centered without scaling). The supported display mode are listed below:

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
    
*   26-29: Expands a new image onto the screen from right, left, bottom, or top
    

##### SetTransform(transform As String) As Boolean

Applies one of eight transforms to the image. Calls to this method only take effect when the next file is displayed. Note that the image rectangle itself does not change to accommodate the new height and width ratio of a transformed image. This method can be called separately on multiple *roImagePlayer* or *roImageWidget* instances.

*   `identity`: No transformation (default behavior)
    
*   `rot90`: 90 degree clockwise rotation
    
*   `rot180`: 180 degree rotation
    
*   `rot270`: 270 degree clockwise rotation
    
*   `mirror`: Horizontal mirror transformation
    
*   `mirror_rot90`: Mirrored 90 degree clockwise rotation
    
*   `mirror_rot180`: Mirrored 180 degree clockwise rotation
    
*   `mirror_rot270`: Mirrored 270 degree clockwise rotation
    

##### OverlayImage(image\_filename As String, x As Integer, y As Integer) As Boolean

Composites the image with the specified filename on top of the primary `DisplayFile()` image. Use the `x` and `y` integers to specify its location within the image widget.

##### SetRectangle(r As roRectangle) As Boolean

Changes the size and positioning of the image rectangle using the passed *roRectangle* object.

##### GetRectangle() As roRectangle

Returns an *roRectangle* object that has the same location and dimensions as the *roRectangle* object used to define the image window.

##### CreateTestHole(hole As roRectangle) As Boolean

Creates a hole in the image with the location and dimensions specified in the passed *roRectangle* instance. Any video windows located directly beneath the image will show through. This method will disrupt image playback and should be used for test purposes only.

##### SetTransitionDuration(duration As Integer) As Boolean

Sets the amount of time it takes (in milliseconds) for a specified transition effect to take place. The default transition duration is 1000 milliseconds.

##### DisplayBuffer(a As Object, b As Integer, c As Integer) As Boolean

##### Hide() As Boolean

Hides the image currently being displayed by the *roImageWidget* instance.

##### Show() As Boolean

Shows the image currently being displayed by the *roImageWidget* instance.

## Multiscreen Images

This object includes overloaded `PreloadFile()` and `DisplayFile()` methods. These methods receive an [*roAssociativeArray*](#) object that stores various options to be passed. They must be used when displaying images across multiple screens in an array, or displaying a portion of an image—though they can also be used in place of the original method calls in all cases.

The following code uses the `PreloadFile()` method for a multiscreen display:

```
i=CreateObject("roImageWidget")
a=CreateObject("roAssociativeArray")
a["Filename"] = "test.jpg"
a["Mode"] = 1
a["Transition"] = 14
a["MultiscreenWidth"] = 3
a["MultiscreenHeight"] = 2
a["MultiscreenX"] = 0
a["MultiscreenY"] = 0
i.PreloadFile(a)
i.DisplayPreload
```

The `filename`, `mode`, and `transition` values are the same as those documented for the `DisplayFile()` and `PreloadFile()` methods above. The `MultiscreenWidth` and `MultiscreenHeight` parameters specify the width and height of the multi-screen matrix. For example, 3x2 would be three screens wide and two screens high. The `MultiscreenX` and `MultiscreenY` specify the position of the current screen within that matrix.

In the above case, on average only 1/6 of the image is drawn on each screen, though the image mode still applies so that, depending on the shape of the image, it may have black bars on the side screens. It is relatively simple, therefore, for an image widget to display part of an image based on its position in the multiscreen array. The following are default values for the parameters:

*   Mode = 0
    
*   Transition = 0
    
*   MultiscreenWidth = 1
    
*   MultiscreenHeight = 1
    
*   MultiscreenX = 0
    
*   MultiscreenY = 0
    

This code uses `DisplayFile()` to display a portion of an image:

```
i=CreateObject("roImageWidget")
a=CreateObject("roAssociativeArray")
a["Filename"] = "test.JPG"
a["Mode"] = 0
a["SourceX"] = 600
a["SourceY"] = 600
a["SourceWidth"] = 400
a["SourceHeight"] = 400
i.DisplayFile(a)
```

This displays just a portion of the image test JPG starting at coordinates `SourceX`, `SourceY`, and `SourceWidth` by `SourceHeight` in size. The `viewmode` is still honored as if it were displaying the whole file.