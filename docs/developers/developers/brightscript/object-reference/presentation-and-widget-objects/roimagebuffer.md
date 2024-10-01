# roImageBuffer

This object allows you to access decoded image-file data. You can then copy or manipulate that data.

Object Creation: An *roImageBuffer* object is instantiated with an *roImagePlayer* object and a string specifying the file path of an image file. If an *roImagePlayer* object is not needed, `Invalid` can be substituted for it.

```
CreateObject("roImageBuffer", image_player As Object, file_path As String)
```

Example:

```
imgBuffer = CreateObject("roImageBuffer", Invalid, "SD:/content/image.png")
```

## ifImageBufferControl

##### DisplayBuffer(x As Integer, y As Integer) As Boolean

Displays the image on screen. The `x` and `y` integers specify the coordinates of the top-left corner of the image.

> [!CAUTION]
> **Important**
> The `DisplayBuffer`() method has been deprecated. As of OS8, the end point exists but does not perform any function.

##### GetBufferByteArray() As roByteArray

Returns the decoded image-file data as an *roByteArray*.

##### GetBufferMetadata() As roAssociativeArray

Returns an associative array containing information about the image file. The associative array contains the following keys:

*   `width`: The width of the image file
    
*   `height`: The height of the image file
    
*   `acceptable`: A Boolean integer value indicating whether the image can be displayed by the *roImagePlayer* instance
    
*   `format`: The color space (ARGB/CMYK) of the image file
    

##### ConvertFormat(a As String) As Object

#####