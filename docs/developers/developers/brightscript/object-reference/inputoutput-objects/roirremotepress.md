# roIRRemotePress

Messages of the type *roIRRemotePress* are generated upon key presses from a Roku Soundbridge remote.

## ifInt

##### GetInt() As Integer

Returns the event ID. 

##### SetInt(value As Integer) As Void

Sets the value of the event. 

For the Roku SoundBridge remote control, the Integer returned can have one of the following values:

|     |     |     |     |
| --- | --- | --- | --- |
| **Integer** | **Command** | **Integer** | **Command** |
| 0   | West | 8   | Search |
| 1   | East | 9   | Play |
| 2   | North | 10  | Next |
| 3   | South | 11  | Previous |
| 4   | Select | 12  | Pause |
| 5   | Exit | 13  | Add |
| 6   | Power | 14  | Shuffle |
| 7   | Menu | 15  | Repeat |
| 8   | Search | 16  | Volume up |
| 9   | Play | 17  | Volume down |
| 10  | Next | 18  | Brightness |