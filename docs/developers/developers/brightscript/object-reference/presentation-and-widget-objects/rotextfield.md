# roTextField

A text field represents an area of the screen that can contain arbitrary text. This feature is intended for presenting diagnostic and usage information. Use the *roTextWidget* object to generate text for user interfaces and signage.

Object Creation: The object is created with several parameters:

```
CreateObject("roTextField", xpos As Integer, ypos As Integer, width_in_chars As Integer, height_in_chars As Integer, metadata As Object)
```

*   `xpos`: The horizontal coordinate for the top left of the text field.
    
*   `ypos`: The vertical coordinate for the top left of the text field. The top of the screen is equivalent to zero.
    
*   `width_in_chars`: The width of the text field in character cells.
    
*   `height_in_chars`: The height of the text field in character cells.
    
*   `metadata`: An optional *roAssociativeArray* containing extra parameters for the text field. You can pass zero if you do not require this.
    

The metadata associative array supports the following extra parameters:

*   "CharWidth": The width of each character cell in pixels.
    
*   "CharLength": The height of each character cell in pixels.
    
*   "BackgroundColor": The background color of the text field as an integer specifying eight bits (for each) for red, green and blue in the form &Hrrggbb.
    
*   "TextColor": The color of the text as an integer specifying eight bits (for each) for red, green and blue in the form &Hrrggbb.
    
*   "Size": An alternative to "CharWidth" and "CharLength" for specifying either normal size text (0) or double-sized text (1).
    

> [!NOTE]
> In TV modes, a border around the screen may not be displayed due to overscanning. You may want to use the *roVideoMode* object functions `GetSafeX()` and `GetSafeY()` to ensure that the coordinates you use will be visible.

## ifTextField

##### Cls() As Void

Clears the text field.

##### GetWidth() As Integer

Returns the width of the text field

##### GetHeight() As Integer

Returns the height of the text field.

##### SetCursorPos(x As Integer, y As Integer) As Void

Moves the cursor to the specified position. Subsequent output will appear at this position.

##### GetValue() As Integer

Returns the value of the character currently under the cursor

##### Raise() As Void

Sends the widget to the top of the z-order on the graphics plane (i.e. in front of all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

> [!NOTE]
> Some surfaces are always drawn at the top of the graphics z-order, including the mouse cursor, closed captions, and [scrolling tickers](../presentation-and-widget-objects/rotextwidget.md).

> [!TIP]
> **Tip**
> You can use the `PauseGraphics()`/ `ResumeGraphics()` methods on the [*roVideoMode*](../presentation-and-widget-objects/rovideomode.md) object to ensure multiple changes to the graphics z-order occur simultaneously.

##### Lower() As Void

Sends the widget to the bottom of the z-order on the graphics plane (i.e. behind all other surfaces that implement the *ifWidget* interface). By default, new widgets are placed at the top of the graphics z-order.

## ifStreamSend

##### SendByte(byte As Integer) As Void

Writes the character indicated by the specified number at the current cursor position within the text field. It then advances the cursor.

##### SendLine(string As String) As Void

Writes the characters specified at the current cursor position followed by the end-of-line sequence.

##### SendBlock(string As Dynamic) As Void

Writes the characters specified at the current cursor position and advances the cursor to one position beyond the last character. This method can support either a string or an [*roByteArray*](#) . If the block is a string, any null bytes will terminate the block.

##### SetSendEol(string As String) As Void

Sets the sequence sent at the end of a SendLine() value. You should leave this at the default ASCII value of 13 (Carriage Return) for normal use. If you need to change this value to another non-printing character, use the `chr` [global function](../../object-reference/global-functions.md).

> [!NOTE]
> The ifStreamSend interface is also described in the section documenting the various file objects. The interface is described again here in a manner more specific to the roTextField object.

## Printing a Text Field 

As with any object that implements the *ifStreamSend* interface, a text field can be written to using the PRINT #textfield syntax. See the example below for more details.

It is also possible to write to a text field using the syntax PRINT #textfield, @pos, where *pos* is the character position in the *textfield*. For example, if your *textfield* object has 8 columns and 3 rows, writing to position 17 writes to row 3, column 2 (positions 0-7 are in row 1; positions 8-15 are in row 2; and positions 16-23 are in the last row).

When output reaches the bottom of the text field, it will automatically scroll.

##### **Example**

```
meta = CreateObject("roAssociativeArray")
meta.AddReplace("CharWidth", 20)
meta.AddReplace("CharLength", 32)
meta.AddReplace("BackgroundColor", &H101010) ' Dark grey
meta.AddReplace("TextColor", &Hffff00) ' Yellow
vm = CreateObject("roVideoMode")
tf = CreateObject("roTextField", vm.GetSafeX(), vm.GetSafeY(), 20, 20, meta)
print #tf, "Hello World"
tf.SetCursorPos(4, 10)
print #tf, "World Hello"
```