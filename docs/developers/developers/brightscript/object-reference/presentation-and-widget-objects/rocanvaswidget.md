# roCanvasWidget

This object composites background color, text, and images into a single rectangle, allowing you to layer images on a z-axis.

Object Creation: Like other widgets, *roCanvasWidget* is created with an *roRectangle* to set its size and position on the screen.

```
CreateObject ("roCanvasWidget", r As roRectangle) As Object
```

## ifCanvasWidget

##### Hide() As Boolean

Hides the widget.

##### Show() As Boolean

Shows the widget.

##### Raise() As Void

Sends the widget to the top of the z-order on the graphics plane (i.e. in front of all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

> [!NOTE]
> Some surfaces are always drawn at the top of the graphics z-order, including the mouse cursor, closed captions, and [scrolling tickers](../presentation-and-widget-objects/rotextwidget.md).

> [!TIP]
> **Tip**
> You can use the `PauseGraphics()`/ `ResumeGraphics()` methods on the [*roVideoMode*](../presentation-and-widget-objects/rovideomode.md) object to ensure multiple changes to the graphics z-order occur simultaneously.

##### Lower() As Void

Sends the widget to the bottom of the z-order on the graphics plane (i.e. behind all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

##### SetRectangle(r As roRectangle) As Boolean

Changes the size and positioning of the widget rectangle using the passed *roRectangle* object.

##### SetLayer(content As Object, z-level As Integer) As Boolean

Sets the contents of a layer within the widget. The lowest z-level is drawn first, and the highest z-level is drawn last. The object content is described below.

##### ClearLayer(z-level As Integer) As Boolean

Clears the specified layer.

##### Clear() As Boolean

Clears all of the layers

##### EnableAutoRedraw(enable As Boolean) As Boolean

Enables or disables the automatic redrawing of the widget.

*   When this function is enabled, each call to SetLayer, ClearLayer, or Clear results in a redraw. If you need to change multiple layers, then you should disable auto redraw while calling the SetLayer function.
    
*   SetLayer enables or disables redrawing of the widget when layer content is changed. When auto-redraw is enabled, each call to SetLayer, ClearLayer, or Clear results in a redraw. To batch multiple updates together, you should first suspend drawing using EnableAutoRedraw(false), then make the changes to the content, and finally re-enable drawing using EnableAutoRedraw(true). The redraw happens in a separate thread, so EnableAutoRedraw returns almost immediately.
    

## Object Content

The content specified in each layer can consist of one or more objects. Each object is defined by an [*roAssociativeArray*](#) . If there is more than one object, then each is placed into an [*roArray*](#) prior to passing to the `SetLayer()` method. Currently, there are four object types. 

### Background color

*   `color`: The #\[aa\]rrggbb hex value of the background color
    
*   `targetRect`: A target rectangle, which is another *roAssociativeArray* consisting of x, y, w, and h values. These values are relative to the top left corner of the widget.
    

### Text

*   `text`: A string of text to display
    
*   `targetRect`: The rectangle in which the text is displayed
    
*   `textAttrs`: An *roAssociativeArray* containing attributes to be applied to the text. The attributes can be any of the following:
    
    *   `font`: A string indicating whether the text should be displayed as "small"/"medium"/"large"/"huge"
        
    *   `fontSize`: A point size that is used directly when creating the font. If the value is set to 0, then the font automatically resizes to fit the targetRect.
        
    *   `fontfile`: The filename for a non-system font to use
        
    *   `hAlign`: A string indicating the "left"/"center"/"right" alignment of the text on a line
        
    *   `vAlign`: A string indicating the "top"/"center"/"bottom" alignment of the text perpendicular to the line
        
    *   `rotation`: A string indicating the "0"/'90"/"180"/"270" degree rotation of the text
        
    *   `color`: The #\[aa\]rrggbb hex value of the text
        

### Image

*   `filename`: The filename of the image
    
*   `encryptionalgorithm`: The file-encryption algorithm. Currently the options are "AesCtr" and "AesCtrHmac".
    
*   `encryptionkey`: The key to decrypt the image file. This is a byte array consisting of 128 bits of key, followed by 128 bits of IV.
    

> [!NOTE]
> See the [Image Decryption](../presentation-and-widget-objects/roimageplayer.md) section in the *roImagePlayer* entry for details on displaying encrypted images.

*   `targetRect`: The rectangle in which the image is displayed. The image will be automatically resized to fit into the target area.
    
*   `sourceRect`: The source rectangle to clip from a source image
    
*   `compositionMode`: Enter either source or source\_over. The latter alpha blends with underlying objects. The former replaces the underlying values completely.
    
*   `imgAttrs`: An *roAssociativeArray* containing attributes to be applied to the image:
    
    *   `rotation`: A string indicating the "0"/'90"/"180"/"270" degree rotation of the image
        

### QR Codes

QR (quick response) codes appear as squares of black dots on a white background. They are used to encode URLs, email addresses, etc, and they can be scanned using readily available software for smart phones. Although the codes usually appear as black on white, you can, in theory, use any two contrasting colors.

*   `targetRect`: The rectangle in which the QR code is displayed. Regardless of the aspect ratio of this rectangle, the QR code itself will always be squared with the background color that fills the gaps.
    
*   `QrCode` (simple form): Contains the string to encode into the QR code.
    
*   `QrCode` (complex form): Contains an array of parameters for the QR code. The parameters can be any of the following:
    
    *   `color`: The foreground color in the QR code (the default is black)
        
    *   `backgroundColor`: The background color in the QR code (the default is white)
        
    *   `rotation`: A string indicating the "0"/'90"/"180"/"270" degree rotation of the code. The code will scan regardless of rotation.
        
    *   `qrText`: Contains the text to encode into the QR code.
        

## Example

This code contains most of the *roCanvasWidget* features outlined above:

```
rect=CreateObject("roRectangle", 0, 0, 1920, 1080)
cw=CreateObject("roCanvasWidget", rect)

aa=CreateObject("roAssociativeArray")
aa["text"] = "Primal Scream"
aa["targetRect"] = { x: 280, y: 180, w: 500, h: 30 }
aa["textAttrs"] = { Color:"#AAAAAA", font:"Medium", HAlign:"Left", VAlign:"Top"}

aa1=CreateObject("roAssociativeArray")
aa1["text"] = "Movin' on up, followed by something else, followed by something else, followed by something else, followed by something else"
aa1["targetRect"] = { x: 282, y: 215, w: 80, h: 500 }
aa1["textAttrs"] = { Color:"#ffffff", font:"Large", fontfile:"usb1:/GiddyupStd.otf", HAlign:"Left", VAlign:"Top", rotation:"90"}

array=CreateObject("roArray", 10, false)
array.Push({ color: "5c5d5f" })
array.Push({ filename: "transparent-balls.png" })
array.Push(aa)

aa2=CreateObject("roAssociativeArray")
aa2["filename"] = "transparent-balls.png"
aa2["CompositionMode"] = "source_over"
aa2["targetRect"] = { x: 400, y: 200, w: 200, h: 200 }

aa3=CreateObject("roAssociativeArray")
aa3["QrCode"] = "www.brightsign.biz"
aa3["targetRect"] = { x: 100,  y: 100,  w: 400, h: 400  }

aa4=CreateObject("roAssociativeArray")
aa4["QrCode"] = { qrText:"www.brightsign.biz", rotation:"90" }
aa4["targetRect"] = { x: 1200,  y: 100,  w: 400, h: 600  }

aa5=CreateObject("roAssociativeArray")
aa5["QrCode"] = { color:"#964969", backgroundColor:"#FFFF77", qrText:"www.brightsign.biz", rotation:"180" }
aa5["targetRect"] = { x: 100,  y: 600,  w: 400, h: 400  }

cw.Show()
cw.EnableAutoRedraw(0)
cw.SetLayer(array, 0)
cw.SetLayer(aa1, 1)
cw.SetLayer(aa1, 2)
cw.SetLayer(aa3, 3)
cw.SetLayer(aa4, 4)
cw.SetLayer(aa5, 5)
cw.EnableAutoRedraw(1)

cw.ClearLayer(0) 
```

##