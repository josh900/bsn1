# Example Script

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

The following code uses GPIO buttons 1, 2, 3, 4 for controls. It will work on any BrightSign model that has a video output and a GPIO port.

```
REM
REM The game of Snake
REM demonstrates BrightScript programming concepts
REM June 22, 2008
 
REM
REM Every BrightScript program must have a single Main()
REM
 
Sub Main()
 
    game_board=newGameBoard()
 
    While true
        game_board.SetSnake(newSnake(game_board.StartX(), game_board.StartY()))
        game_board.Draw()
        game_board.EventLoop()
        if game_board.GameOver() then ExitWhile
    End While
End Sub
 
 
REM *******************************************************
REM *******************************************************
REM ***************                   *********************
REM *************** GAME BOARD OBJECT *********************
REM ***************                   *********************
REM *******************************************************
REM *******************************************************
 
 
REM
REM An example BrightScript constructor.   "newGameBoard()" is regular Function of module scope
REM BrightScript Objects are "dynamic" and created at runtime.  They have no "class". 
REM The object container is a BrightScript Component of type roAssocitiveArray (AA).  
REM The AA is used to hold member data and member functions.
REM
 
Function newGameBoard() As Object
    game_board=CreateObject("roAssociativeArray")       ' Create a BrightScript Component of type/class roAssociativeArray
    game_board.Init=gbInit                         ' Add an entry to the AA of type roFunction with value gbDraw (a sub defined in this module)
    game_board.Draw=gbDraw
    game_board.SetSnake=gbSetSnake
    game_board.EventLoop=gbEventLoop
    game_board.GameOver=gbGameOver
    game_board.StartX=gbStartX
    game_board.StartY=gbStartY
    game_board.Init()                                   ' Call the Init member function (which is gbInit)
 
    return game_board
 
End Function
 
 
REM
REM gbInit() is a member function of the game_board BrightScript Object.
REM When it is called, the "this" pointer "m" is set to the appropriate instance by
REM the BrightScript bytecode interpreter
REM   
Function gbInit() As Void
    REM
    REM button presses go to this message port
    REM
    m.buttons = CreateObject("roMessagePort")
    m.gpio =  CreateObject("roGpioControlPort") 
    m.gpio.SetPort(m.buttons)
 
    REM
    REM determine optimal size and position for the snake gameboard
    REM
    CELLWID=16     ' each cell on game in pixels width
    CELLHI=16      ' each cell in pix height
    MAXWIDE=30    ' max width (in cells) of game board
    MAXHI=30      ' max height (in cells) of game board
    vidmode=CreateObject("roVideoMode")
    w=cint(vidmode.GetResX()/CELLWID)
    if w>MAXWIDE then w = MAXWIDE
    h=cint(vidmode.GetResY()/CELLHI)
    if h>MAXHI then h=MAXHI
 
    xpix = cint((vidmode.GetResX() - w*CELLWID)/2)     ' center game board on screen
    ypix = cint((vidmode.GetResY() - h*CELLHI)/2)      ' center game board on screen
 
    REM
    REM Create Text Field with square char cell size
    REM
    meta=CreateObject("roAssociativeArray")
    meta.AddReplace("CharWidth",CELLWID)
    meta.AddReplace("CharHeight",CELLHI)
    meta.AddReplace("BackgroundColor",&H202020)   'very dark grey
    meta.AddReplace("TextColor",&H00FF00)   ' Green
    m.text_field=CreateObject("roTextField",xpix,ypix,w,h,meta)
    if type(m.text_field)<>"roTextField" then
        print "unable to create roTextField 1"
        stop
    endif
End Function
 
REM
REM As Object refers to type BrightScript Component
REM m the "this" pointer
REM
Sub gbSetSnake(snake As Object)
    m.snake=snake
End Sub
 
 
Function gbStartX() As Integer
    return cint(m.text_field.GetWidth()/2)
End Function
 
 
Function gbStartY() As Integer
    return cint(m.text_field.GetHeight()/2)
End Function
 
 
Function gbEventLoop() As Void
 
    tick_count=0
 
    while true
        msg=wait(250, m.buttons)   ' wait for a button, or 250ms (1/4 a second) timeout
        if type(msg)="roGpioButton" then
            if msg.GetInt()=1 m.snake.TurnNorth()
            if msg.GetInt()=2 m.snake.TurnSouth()
            if msg.GetInt()=3 m.snake.TurnEast()
            if msg.GetInt()=4 m.snake.TurnWest()
        else  'here if time out happened, move snake forward
            tick_count=tick_count+1
            if tick_count=6 then
                tick_count=0
                if m.snake.MakeLonger(m.text_field) then return
            else
                if m.snake.MoveForward(m.text_field) then return
            endif
        endif
    end while
 
End Function
 
 
Sub gbDraw()
    REM
    REM given a roTextField Object in "m.text_field", draw a box around its edge
    REM
 
    solid=191   ' use asc("*") if graphics not enabled
    m.text_field.Cls()
 
    for w=0 to m.text_field.GetWidth()-1
        print #m.text_field,@w,chr(solid);
        print #m.text_field,@m.text_field.GetWidth()*(m.text_field.GetHeight()-1)+w,chr(solid);
    end for
 
    for h=1 to m.text_field.GetHeight()-2
        print #m.text_field,@h*m.text_field.GetWidth(),chr(solid);
        print #m.text_field,@h*m.text_field.GetWidth()+m.text_field.GetWidth()-1,chr(solid);
    end for
 
    m.snake.Draw(m.text_field)
 
End Sub
 
Function gbGameOver() As Boolean
    msg$= " G A M E    O V E R "
    msg0$="                    "
    width = m.text_field.GetWidth()
    height = m.text_field.GetHeight()
 
    while true
        print #m.text_field,@width*(height/2-1)+(width-len(msg$))/2,msg$;
        sleep(300)
        print #m.text_field,@width*(height/2-1)+(width-len(msg$))/2,msg0$;
        sleep(150)
        REM  GetMessage returns the message object, or an int 0 if no message available
        If m.buttons.GetMessage() <> invalid Then Return False
    endwhile
 
End Function
 
 
REM *******************************************************
REM *******************************************************
REM ******************              ***********************
REM ****************** SNAKE OBJECT ***********************
REM ******************              ***********************
REM *******************************************************
REM *******************************************************
 
REM
REM construct a new snake BrightScript object
REM
Function newSnake(x As Integer, y As Integer) As Object
 
' Create AA BrightScript Component; the container for a "BrightScript Object"
    snake=CreateObject("roAssociativeArray")   
    snake.Draw=snkDraw
    snake.TurnNorth=snkTurnNorth
    snake.TurnSouth=snkTurnSouth
    snake.TurnEast=snkTurnEast
    snake.TurnWest=snkTurnWest
    snake.MoveForward=snkMoveForward
    snake.MakeLonger=snkMakeLonger
    snake.AddSegment=snkAddSegment
    snake.EraseEndBit=snkEraseEndBit
 
    REM
    REM a "snake" is a list of line segments
    REM a line segment is an roAssociativeArray that conains a length and direction (given by the x,y delta needed to move as it is drawn)
    REM
 
    snake.seg_list = CreateObject("roList")
    snake.AddSegment(1,0,3)
 
    REM
    REM The X,Y pos is the position of the head of the snake
    REM
    snake.snake_X=x
    snake.snake_Y=y
    snake.body=191   ' use asc("*") if graphics not enabled.
    snake.dx=1      ' default snake direction / move offset
    snake.dy=0      ' default snake direction / move offset
 
    return snake
 
End Function
 
 
Sub snkDraw(text_field As Object)
    x=m.snake_X
    y=m.snake_Y
    for each seg in m.seg_list
        xdelta=seg.xDelta
        ydelta=seg.yDelta
        for j=1 to seg.Len
            text_field.SetCursorPos(x, y)
            text_field.SendByte(m.body)
            x=x+xdelta
            y=y+ydelta
        end for
    end for
End Sub
 
 
Sub snkEraseEndBit(text_field As Object)
    x=m.snake_X
    y=m.snake_Y
    for each seg in m.seg_list
        x=x+seg.Len*seg.xDelta
        y=y+seg.Len*seg.yDelta
    end for
 
    text_field.SetCursorPos(x, y)
    text_field.SendByte(32)    ' 32 is ascii space, could use asc(" ")
 
End Sub
 
 
Function snkMoveForward(text_field As Object)As Boolean
    m.EraseEndBit(text_field)
    tail=m.seg_list.GetTail()
    REM
    REM the following shows how you can use an AA's member functions to perform the same
    REM functions the BrightScript . operator does behind the scenes for you (when used on an AA).
    REM there is not point to this longer method other than illustration
    REM
    len=tail.Lookup("Len")          ' same as len = tail.Len (or tail.len, BrightScript syntax is not case sensative)
    len = len-1
    if len=0 then
        m.seg_list.RemoveTail()
    else
        tail.AddReplace("Len",len)  ' same as tail.Len=len
    endif
 
    return m.MakeLonger(text_field)
 
End Function
 
Function snkMakeLonger(text_field As Object) As Boolean
    m.snake_X=m.snake_X+m.dx
    m.snake_Y=m.snake_Y+m.dy
    text_field.SetCursorPos(m.snake_X, m.snake_Y)
    if text_field.GetValue()=m.body then return true
    text_field.SendByte(m.body)
    head = m.seg_list.GetHead()
    head.Len=head.Len+1
    return false
End Function
 
Sub snkAddSegment(dx As Integer, dy As Integer, len as Integer)
 
    aa=CreateObject("roAssociativeArray")
    aa.AddReplace("xDelta",-dx)  ' line segments draw from head to tail
    aa.AddReplace("yDelta",-dy)
    aa.AddReplace("Len",len)
    m.seg_list.AddHead(aa)
 
End Sub
 
 
Sub snkTurnNorth()
    if m.dx<>0 or m.dy<>-1 then m.dx=0:m.dy=-1:m.AddSegment(m.dx, m.dy, 0)      'north
End Sub
 
Sub snkTurnSouth()
     if m.dx<>0 or m.dy<>1 then m.dx=0:m.dy=1:m.AddSegment(m.dx, m.dy, 0)       'south
End Sub
 
Sub snkTurnEast()
     if m.dx<>-1 or m.dy<>0 then m.dx=-1:m.dy=0:m.AddSegment(m.dx, m.dy, 0)     'east
End Sub
 
Sub snkTurnWest()
     if m.dx<>1 or m.dy<>0 then m.dx=1:m.dy=0:m.AddSegment(m.dx, m.dy, 0)       'west
End Sub
```