# keyboard

The *keyboard* object allows you to configure the input for a USB keyboard connected to the player.

**keyboard IDL**

```
interface Keyboard {
    Promise<bool> isAttached();
    Promise<void> setLayout(String layoutName);
    Promise<void> setNumLock(bool on_off);
};
```

## Object Creation

To create a *keyboard* object, first load the `brightsign/keyboard` module using the `require()` method. Then create an instance of the *keyboard* class.

```
var keyboardClass = require("@brightsign/keyboard");
var keyboard = new keyboardClass();
```

## Keyboard

This interface allows for detection and configuration of a USB keyboard.

##### isAttached()

```
Promise<bool> isAttached()
```

Returns `true` if a USB keyboard is connected to the player. This method counts a connected device as a keyboard if it reports having the following keys: "A", "Z", "0", "9", ".", and Enter.

##### setLayout()

```
Promise<void> setLayout(String layoutName)
```

Specifies the localized layout for the attached USB keyboard. This setting takes effect immediately and persists in the registry after a reboot. See [this table](../../../developers/brightscript/object-reference/inputoutput-objects/rokeyboard.md) for valid keymap parameters (players are set to "us" by default).

##### setNumLock()

```
Promise<void> setNumLock(bool on_off)
```

Sets the numlock state for the attached USB keyboard if passed true. Reset the state if passed false.

## Example

```
var KeyboardClass = require("@brightsign/keyboard");
var keyboard = new KeyboardClass();
keyboard.isAttached().then(
        function(data) {
            console.log("***Is Attached***");
            console.log(JSON.stringify(data));
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        });
keyboard.setLayout("gb").then(
        function(data) {
            console.log("***Layout set***");
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        }); 
```