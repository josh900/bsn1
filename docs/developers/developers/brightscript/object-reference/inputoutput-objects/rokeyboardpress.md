# roKeyboardPress

This is an event object resulting from the user pressing a key on a USB keyboard. The returned integer value is equivalent to the ASCII code of the key that was pressed.

## ifInt

##### GetInt() As Integer

Returns the ASCII value of the key press. 

##### SetInt(a As Integer)

Sets the value returned by the `GetInt()` method.

The returned *roInt32* can have one of the following values:

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Letter Keys** |     | **Number Keys** | **Function Keys** | **Misc Keys** | **Special Keys** |     |     |     |
| A - 97 | R  - 114 | 0 - 48 | F1 - 32826 | Del  - 127 | "-" | 45  | :   | 58  |
| B  - 98 | S  - 115 | 1 - 49 | F2 - 32827 | Backspace - 8 | "=" | 61  | "   | 34  |
| C  - 99 | T  - 116 | 2 - 50 | F3 - 32828 | Tab - 9 | \\  | 92  | <   | 60  |
| D  - 100 | U  - 117 | 3 - 51 | F4 - 32829 | Enter - 13 | \`  | 96  | \>  | 62  |
| E  - 101 | V  - 118 | 4 - 52 | F5 - 32830 | Print Scrn - 32838 | \[  | 91  | ?   | 63  |
| F  - 102 | W  - 119 | 5 - 53 | F6 - 32831 | Scrl Lock - 32839 | \]  | 93  | !   | 33  |
| G  - 103 | X  - 120 | 6 - 54 | F7 - 32832 | Pause/Brk - 32840 | ;   | 59  | @   | 64  |
| H  - 104 | Y  - 121 | 7 - 55 | F8 - 32833 | INS - 32841 | " ' " | 39  | #   | 35  |
| I  - 105 | Z  - 122 | 8 - 56 | F9 - 32834 | Home - 32842 | ,   | 44  | $   | 36  |
| J  - 106 |     | 9 - 57 | F11 - 32836 | Page Up - 32843 | .   | 46  | %   | 37  |
| K  - 107 |     |     | F12 - 32837 | Page Down - 32846 | /   | 47  | ^   | 94  |
| L  - 108 |     |     |     | End - 32845 | \_  | 95  | &   | 38  |
| M  - 109 |     |     |     | Caps - 32811 | "+" | 43  | \*  | 42  |
| N  - 110 |     |     |     | Left Arrow - 32848 | \|  | 124 | (   | 40  |
| O  - 111 |     |     |     | Right Arrow  - 32847 | ~   | 126 | )   | 41  |
| P  - 112 |     |     |     | Up Arrow - 32850 | {   | 123 |     |     |
| Q  - 113 |     |     |     | Down Arrow - 32849 | }   | 125 |     |     |