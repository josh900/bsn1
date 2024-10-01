# BSControlPort

This object provides support for the BP200/BP900 USB button boards and GPIO ports. Button presses are returned as `oncontroldown` and `oncontrolup` events. The object is used to configure output levels on the I/O connector and monitor inputs. Typically, LEDs and buttons are attached to the GPIO connector on the BrightSign player or the BrightSign Expansion Module.

The JavaScript equivalent is [controlport](../../player-apis/javascript-apis/controlport.md).

## Object Creation

The *roControlPort* object is created with a single parameter that specifies the port being used.

```
BSControlPort(in DOMString PortName)
```

The port parameter can be one of the following:

*   `BrightSign`: Specifies the onboard GPIO connector (including the SVC (GPIO12) button).
    
*   `Expander-GPIO`: Specifies the DB-25 connector on the BrightSign Expansion Module. If no BrightSign Expansion module is attached, then object creation will fail and Invalid will be returned.
    
*   `Expander-<n>-GPIO`: Specifies a [USB-to-GPIO device](https://www.brightsign.biz/digital-signage-products/accessories/USB-C-Cables) connected to the player. Multiple USB-to-GPIO devices can be controlled using separate *roControlPort* instances: The first device corresponds to `"Expander-0-GPIO"`, the second to `"Expander-1-GPIO"`, etc.
    
*   `Expander-DIP`: Specifies the eight DIP switches on the BrightSign Expansion Module. If no BrightSign Expansion module is attached, then object creation will fail and Invalid will be returned.
    

> [!NOTE]
> Hot-plugging the BrightSign Expansion Module is not supported.

*   `Touchboard-<n>-GPIO`: Retrieves events from the specified BP200/BP900 button board. Events are handled in the same manner as events from the BrightSign port.
    
*   `Touchboard-<n>-LED-SETUP`: Sets various LED output options for the specified BP200/BP900 button board.
    
*   `Touchboard-<n>-LED`: Sets the bits for each button on the specified BP200/BP900 button board. The bits indicate whether the associated LED should be on or off.
    

> [!NOTE]
> Since multiple BP200/BP900 button boards can be connected to a player simultaneously, the <n> value specifies the port enumeration of each board. This value corresponds to the `<raw>` or `<fid>` value returned by the [*roDeviceInfo.GetUSBTopology()*](../../../developers/brightscript/object-reference/system-objects/rodeviceinfo.md) method. An unspecified enumeration value is synonymous with a button board with an enumeration value of 0 (e.g. Touchboard-GPIO and Touchboard-0-GPIO are identical).

## Methods

> [!TIP]
> See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/375390705/XTx44+Hardware+Interfaces) for a table of pins and corresponding buttons for the onboard GPIO connector.

`boolean ConfigureAsInput (unsigned Button)`

Marks the specified button as an input. If an invalid button number is passed, `false` will be returned. If successful, the function returns `true`. Input buttons are tri-stated and can be driven high or low externally.

`boolean ConfigureAsOutput (unsigned Button)`

Marks the specified button as an output. If an invalid button number is passed, `false` will be returned. If successful, the function returns `true`. The output will be driven high or low depending on the current output state of the pin.

`boolean SetPinValue(unsigned Button, unsigned Output)`

Configures the output of the specified button, which can be either low (0) or high (1). If the button is not configured as an output, the resulting level is undefined. This method can also be used to configure LED output behavior on [BP200/B900 button boards](../../../developers/brightscript/object-reference/inputoutput-objects/rocontrolport.md).

`boolean GetPinValue(unsigned Button)`

Returns the output of the specified button.

`void Close()`

Shuts down the *BSControlPort* instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

`boolean SetOutputValue(unsigned Param)`

Specifies the desired state of all outputs attached to the control port as bits in an integer. The individual buttons can be set using binary operations.

The parameter is an 8-bit integer and each bit represents an output.

`boolean SetOutputValues(unsigned Param1, unsigned Param2, unsigned Param3, unsigned Param4)`

Configures buttons on a BP200/BP900 button board. This method can only be used when the *BSControlPort* object is instantiated with the `Touchboard-<n>-LED-SETUP` or `Touchboard-<n>-LED` parameter. The parameters are integer values.

## Events

The following events are available on the *BSControlPort* object. Each event can receive a *ControlPortEvent* event.

*   `oncontroldown`
    
*   `oncontrolup`
    
*   `oncontrolevent`
    

### ControlPortEvent – Attributes

*   `readonly attribute unsigned long code`
    

## Examples

The following example code configures four GPIO outputs:

```
var gpio = new BSControlPort("BrightSign");
 
// set outputs
gpio.ConfigureAsOutput(0);
gpio.ConfigureAsOutput(1);
gpio.ConfigureAsOutput(2);
gpio.ConfigureAsOutput(3);
 
// set desired states
gpio.SetPinValue(0, 1);
gpio.SetPinValue(1, 1);
gpio.SetPinValue(2, 0);
gpio.SetPinValue(3, 0);
```

The following example causes the LEDs on a BP900 button board to twinkle:

```
var bp900_gpio;
function myFunction()
{
    var bp900_setup = new BSControlPort("TouchBoard-0-LED-SETUP");
    bp900_setup.SetPinValue(0, 11)

    var bp900 = new BSControlPort("TouchBoard-0-LED");
    bp900.SetPinValue(0, 0x07fe)
    bp900.SetPinValue(1, 0x07fd)
    bp900.SetPinValue(2, 0x07fb)
    bp900.SetPinValue(3, 0x07f7)
    bp900.SetPinValue(4, 0x07ef)
    bp900.SetPinValue(5, 0x07df)
    bp900.SetPinValue(6, 0x07bf)
    bp900.SetPinValue(7, 0x077f)
    bp900.SetPinValue(8, 0x06ff)
    bp900.SetPinValue(9, 0x05ff)
    bp900.SetPinValue(10, 0x03ff)

    bp900_gpio = new BSControlPort("TouchBoard-0-GPIO");
    bp900_gpio.oncontroldown = function(e)
    {
        console.log('###### oncontroldown' + e.code);
    }
}
```

The following example displays events from a GPIO expander board. Note that using the equivalent *roGpioControlPort* object in BrightScript at the same time will result in unpredictable I/O behavior.

```
<html>
    <head>
    <script>
        var bp900_gpio = new BSControlPort("BrightSign");

        bp900_gpio.oncontroldown = function(e){
            console.log('### oncontroldown ' + e.code);
            newtext = " DOWN: " + e.code + "\n";
            document.myform.outputtext.value += newtext;
            document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
        }

        bp900_gpio.oncontrolup = function(e){
            console.log('### oncontrolup ' + e.code);
            newtext = "   UP: " + e.code + "\n";
            document.myform.outputtext.value += newtext;
            document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
        }

        bp900_gpio.oncontrolevent = function(e){
            console.log('### oncontrolevent ' + e.code);
            newtext = "EVENT: " + e.code + "\n";
            document.myform.outputtext.value += newtext;
            document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
        }

        function ledOn(output_index)
        {
            bp900_gpio.ConfigureAsOutput(output_index);
            newtext = "  LED: " + output_index + "\n";
            document.myform.outputtext.value += newtext;
            document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
        }

        function buttonOn(output_index)
        {
            bp900_gpio.ConfigureAsInput(output_index);
            newtext = "INPUT: " + output_index + "\n";
            document.myform.outputtext.value += newtext;
            document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
        }
    </script>
    </head>

    <body bgcolor="#E6E6FA">

    <h1>GPIO/Expander Test Page</h1>
    Note this does NOT play well with <em>roGpioControlPort</em>!!<br><br>
    <input type="button" onclick="ledOn(0)" value="led0">
    <input type="button" onclick="ledOn(1)" value="led1">
    <input type="button" onclick="ledOn(2)" value="led2">
    <input type="button" onclick="ledOn(3)" value="led3">
    <input type="button" onclick="ledOn(4)" value="led4">
    <input type="button" onclick="ledOn(5)" value="led5">
    <input type="button" onclick="ledOn(6)" value="led6">
    <input type="button" onclick="ledOn(7)" value="led7">
    <br>
    <input type="button" onclick="buttonOn(0)" value="button0">
    <input type="button" onclick="buttonOn(1)" value="button1">
    <input type="button" onclick="buttonOn(2)" value="button2">
    <input type="button" onclick="buttonOn(3)" value="button3">
    <input type="button" onclick="buttonOn(4)" value="button4">
    <input type="button" onclick="buttonOn(5)" value="button5">
    <input type="button" onclick="buttonOn(6)" value="button6">
    <input type="button" onclick="buttonOn(7)" value="button7">
    <br>

    <form name="myform">
        <textarea readonly rows="50" cols="100" name="outputtext" style="font-family:monospace"></textarea>
    </form>

</body>
</html>
```