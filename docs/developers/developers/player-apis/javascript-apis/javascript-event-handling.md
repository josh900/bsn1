# JavaScript Event Handling

## AddEventListener

`addEventListener()` is a common BrightSign method that is used to listen for an event.

#### Syntax:

```
target.addEventListener(type, listener);
```

*   `type` string: Specifies the type of event to listen for
    
*   `listener` function: The object to be notified when the event (of the specified `type`) happens 
    

## RemoveEventListener

`removeEventListener()`is a common BrightSign method that is used to remove an event listener.

#### Syntax:

```
target.removeEventListener(type, listener);
```

*   `type` string: Specifies the type of event to listen for
    
*   `listener` function:  The object to be notified when the event (of the specified `type`) happens 
    

## Example

```
function GPIOcontrolDown(msg){

    console.log(JSON.stringify(msg)); 
    console.log(" GPIO : " + msg.detail)
}

// to add an event listener for the "controldown" GPIO event

control_port.addEventListener("controldown", GPIOcontrolDown);

// to remove the "controldown" GPIO event listener

control_port.removeEventListener("controldown", GPIOcontrolDown);
```