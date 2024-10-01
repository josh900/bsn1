# controlport

This *controlport* object is used to configure output levels on the I/O connector and monitor inputs and provides support for the BP200/BP900 USB button boards and GPIO ports. Typically, LEDs and buttons are attached to the GPIO connector on the BrightSign player or the BrightSign Expansion Module.

**controlport IDL**

```
    Constructor(String port)
] interface ControlPort {
    bool SetOutputValue(unsigned param);
    bool SetOutputValues(unsigned p1, unsigned p2, unsigned p3, unsigned p4);
    bool SetPinValue(unsigned pin, unsigned param);
    bool GetPinValue(unsigned pin);
    bool ConfigureAsInput(unsigned pin);
    bool ConfigureAsOutput(unsigned pin);
    void Close()
};
```

## Object Creation

To create an *controlport* object, use the `require()` method:

```
let control_port_class = require("@brightsign/legacy/controlport")
let control_port = new control_port_class("TouchBoard-0-GPIO");
```

The c*ontrolport* object is created with a parameter that specifies the port being used (`TouchBoard-0-GPIO` in the example above). The port parameter can be one of the following:

*   `BrightSign`: Specifies the onboard GPIO connector (including the SVC (GPIO12) button).
    
*   `Expander-GPIO`: Specifies the DB-25 connector on the BrightSign Expansion Module. If no BrightSign Expansion module is attached, then object creation will fail and Invalid will be returned.
    
*   `Expander-<n>-GPIO`: Specifies a [USB-to-GPIO device](https://www.brightsign.biz/digital-signage-products/accessories/USB-C-Cables) connected to the player. Multiple USB-to-GPIO devices can be controlled using separate *roControlPort* instances: The first device corresponds to `"Expander-0-GPIO"`, the second to `"Expander-1-GPIO"`, etc.
    
*   `Expander-DIP`: Specifies the eight DIP switches on the BrightSign Expansion Module. If no BrightSign Expansion module is attached, then object creation will fail and Invalid will be returned. Note that hot plugging the BrightSign Expansion Module is not supported.
    
*   `Touchboard-<n>-GPIO`: Retrieves events from the specified BP200/BP900 button board. Events are handled in the same manner as events from the BrightSign port.
    
*   `Touchboard-<n>-LED-SETUP`: Sets various LED output options for the specified BP200/BP900 button board.
    
*   `Touchboard-<n>-LED`: Sets the bits for each button on the specified BP200/BP900 button board. The bits indicate whether the associated LED should be on or off.
    

> [!NOTE]
> Since multiple BP200/BP900 button boards can be connected to a player simultaneously, the <n> value specifies the port enumeration of each board. The ordering of multiple attached boards is dependent on the order they appear in the data structure returned by [*roDeviceInfo.GetUSBTopology()*](../../../developers/brightscript/object-reference/system-objects/rodeviceinfo.md). An unspecified enumeration value is synonymous with a button board with an enumeration value of 0 (e.g. Touchboard-GPIO and Touchboard-0-GPIO are identical).

## ControlPort

##### SetOutputValue()

```
bool SetOutputValue(unsigned param)
```

Specifies the desired state of all outputs attached to the control port as bits in an integer. 

##### SetOutputValues()

```
bool SetOutputValues(unsigned p1, unsigned p2, unsigned p3, unsigned p4)
```

Configures buttons on a BP200/BP900 button board. This method can only be used when the c*ontrolport* object is instantiated with the `Touchboard-<n>-LED-SETUP` or `Touchboard-<n>-LED` parameter. See [BP200/BP900 Setup](https://docs.brightsign.biz/display/DOC/roControlPort#roControlPort-bp_setup) for more details.

The parameters are integer values.

##### SetPinValue()

```
bool SetPinValue(unsigned pin, unsigned param)
```

Returns a bool and configures either:

*   The output of the specified GPIO button and the value (either 0 or 1). If the button is not configured as an output, the resulting level is undefined. For example, `SetPinValue(0,1), SetPinValue(1,1), SetPinValue(2,1), SetPinValue(3,1) ... etc ...`
    
*   The LED output behavior on [BP200/B900 button boards](https://docs.brightsign.biz/display/DOC/roControlPort#roControlPort-bp_setup). In this case, the offset is the pin value and the bit-mask is the unsigned parameter.
    

##### bool GetPinValue()

Returns `true` if the specified input pin is active (low). Returns `false` if the pin is inactive (not connected or high).

##### bool ConfigureAsInput()

```
bool ConfigureAsInput(unsigned pin)
```

Marks the specified button as an input. If an invalid button number is passed, `false` will be returned. If successful, the function returns `true`. Input buttons are tri-stated and can be driven high or low externally.

##### bool ConfigureAsOutput()

```
bool ConfigureAsOutput(unsigned pin)
```

Marks the specified button as an output. If an invalid button number is passed, `false` will be returned. If successful, the function returns `true`. The output will be driven high or low depending on the current output state of the pin. See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370676258/XTx43+Hardware+Interfaces#XTx43HardwareInterfaces-gpio_table) for a table of pins and corresponding buttons for the onboard GPIO connector.

##### Close()

```
void Close()
```

Shuts down the c*ontrolport* instance

## Events

Use [addEventListener](../javascript-apis/javascript-event-handling.md) to listen for controldown, controlup, and controlevent.

## Example

This example script sets a BP900 to “twinkle” by turning off each button LED at a different point in the cycle:

```
const control_port_class = require('@brightsign/legacy/controlport');
const led = new control_port_class("TouchBoard-0-LED");
const led_setup = new control_port_class("TouchBoard-0-LED-SETUP");

led_setup.SetPinValue(0, 0x000B00A0);

led.SetPinValue(0, 0x07fe);
led.SetPinValue(1, 0x07fd);
led.SetPinValue(2, 0x07fb);
led.SetPinValue(3, 0x07f7);
led.SetPinValue(4, 0x07ef);
led.SetPinValue(5, 0x07df);
led.SetPinValue(6, 0x07bf);
led.SetPinValue(7, 0x077f);
led.SetPinValue(8, 0x06ff);
led.SetPinValue(9, 0x05ff);
led.SetPinValue(10, 0x03ff);
```