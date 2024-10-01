# roRectangle

This object is passed to various video and graphics widgets (*roVideoPlayer*, *roImageWidget*, *roHtmlWidget*, etc.) to specify their size and positioning.

Object Creation: This object is created with coordinate and dimension parameters.

```
CreateObject("roRectangle", x As Integer, y As Integer, width As Integer, height As Integer)
```

`SetRectangle()` calls made by widget objects (e.g. *roImageWidget.SetRectangle()*) honor the view-mode or aspect-ratio conversion mode set by the user. If the user has set the video player for letterboxing, it will occur if the video does not fit in the new rectangle exactly.

### Rectangles with 4K Video Modes 

When the player is using a 4K video mode (e.g. 3840x2160x60p), rectangles still operate as if the total screen area is 1920x1080 (unless [full-resolution graphics](../presentation-and-widget-objects/rovideomode.md) is enabled). They are then scaled by a factor of 2 when the video is output. For example, to display a full-screen 4K video, set the *roRectangle* instance to `0,0,1920,1080`; to display an additional HD video in the top-right quadrant of the screen, set another *roRectangle* instance to `960,0,960,540`.

![](./attachments/4K%20Coordinates.png)

Note that, while 4K video is output at a 1:1 pixel ratio, graphics elements (*roImageWidget*, *roCanvasWidget*, etc.) are upscaled to match the size of the 4K video output. This occurs irrespective of the size of the original image and widget rectangle: For example, an image in a 960x540 rectangle will first be downscaled to 960x540, then upscaled to 1920x1080. If you want to display images without upscaling on 4K video modes, display them in a video window using the *roVideoPlayer.PlayStaticImage()* method (or enable [full-resolution graphics](../presentation-and-widget-objects/rovideomode.md)).

## ifRectangle

##### SetX(x As Integer) As Void

Specifies a new x coordinate for the rectangle

##### SetY(y As Integer) As Void

Specifies a new y coordinate for the rectangle

##### SetWidth(width As Integer) As Void

Specifies a new width value for the rectangle

##### SetHeight(height As Integer) As Void

Specifies a new height value for the rectangle

##### GetX() As Integer

Returns the x coordinate of the rectangle

##### GetY() As Integer

Returns the y coordinate of the rectangle

##### GetWidth() As Integer

Returns the width of the rectangle

##### GetHeight() As Integer

Returns the height of the rectangle