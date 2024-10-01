# roKeyboard

This object is used to wait for events from a USB keyboard. It can also be used to configure the localization of the keyboard. The JavaScript equivalent is [keyboard](https://docs.brightsign.biz/display/DOC/keyboard).

Object Creation: The *roKeyboard* object is created with no parameters.

```
CreateObject("roKeyboard")
```

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roKeyboardPress* to the attached message port.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifKeyboardConfig

##### IsPresent() As Boolean

Returns True if a USB keyboard is connected to the player. This method counts a connected device as a keyboard if it reports having the following keys: "A", "Z", "0", "9", ".", and Enter.

##### SetNumLock(on\_off As Boolean) As Boolean

Sets the numlock state for the attached USB keyboard if passed true. Resets the state if passed false.

##### SetLayout(layout As String) As Boolean

Specifies the localized layout for the attached USB keyboard. This setting takes effect immediately and persists in the registry after a reboot. The following table lists valid keymap parameters (players are set to "us" by default): 

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| af  | Afghanistan | es  | Spain | kh  | Cambodia | pk  | Pakistan |
| al  | Albania | et  | Ethiopia | kr  | Korea, Republic of | pl  | Poland |
| am  | Armenia | fi  | Finland | kz  | Kazakhstan | pt  | Portugal |
| at  | Austria | fo  | Faroe Islands | la  | Laos | ro  | Romania |
| az  | Azerbaijan | fr  | France\* | lk  | Sri Lanka | rs  | Serbia |
| ba  | Bosnia and Herzegovina | gb  | United Kingdom | lt  | Lithuania | ru  | Russia |
| bd  | Bangladesh | ge  | Georgia | lv  | Latvia | se  | Sweden |
| be  | Belgium | gh  | Ghana | ma  | Morocco | si  | Slovenia |
| bg  | Bulgaria | gn  | Guinea | md  | Moldova | sk  | Slovakia |
| br  | Brazil | gr  | Greece | me  | Montenegro | sn  | Senegal |
| bt  | Bhutan | hr  | Croatia | mk  | Macedonia | sy  | Syria |
| bw  | Botswana | hu  | Hungary | ml  | Mali | th  | Thailand |
| by  | Belarus | ie  | Ireland | mm  | Myanmar | tj  | Tajikistan |
| ca  | Canada | il  | Israel | mn  | Mongolia | tm  | Turkmenistan |
| cd  | Congo (DRC) | in  | India | mt  | Macao | tr  | Turkey |
| ch  | Switzerland | iq  | Iraq | mv  | Maldives | tw  | Taiwan |
| cm  | Cameroon | ir  | Iran | ng  | Nigeria | tz  | Tanzania |
| cn  | China | is  | Iceland | nl  | Netherlands | ua  | Ukraine |
| cz  | Czech Republic | it  | Italy | no  | Norway | us  | United States\*\* |
| de  | Germany | jp  | Japan | np  | Nepal | uz  | Uzbekistan |
| dk  | Denmark | ke  | Kenya | pc  | Pitcairn | vn  | Vietnam |
| ee  | Estonia | kg  | Kyrgyzstan | ph  | Philippines | za  | South Africa |

\*Equivalent to the AZERTY keyboard layout

\*\*The default setting