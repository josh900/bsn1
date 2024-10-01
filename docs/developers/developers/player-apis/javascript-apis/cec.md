# cec

The *cec* object lets you send messages over CEC (Consumer Electronics Control).

**cec IDL**

```
interface ReceiveEvent {
    attribute String type;
    attribute Array<byte> data;
};

callback ReceiveEventCallback = void (ReceiveEvent event);

interface Cec {
    Promise<void> send(Array<byte> data);
    void addEventListener(String type, ReceiveEventCallback callback);
    void removeEventListener(String type, ReceiveEventCallback callback);
};
```

## Object Creation

To create a *cec* object, load the *@brightsign/cec* module using the `require()` method. 

```
const CecClass = require('@brightsign/cec');
const cec = new CecClass();
```

Set the specific HDMI port for players with more than one output as follows:

```
const CecClass = require("@brightsign/cec");
const cec = new CecClass("HDMI-2"); //Modify this to be 'HDMI-1', 'HDMI-2', 'HDMI-3', and 'HDMI-4' as needed
```

## Cec

### Event

*   `ReceiveEvent`:  The CEC reception path is implemented as a receive event. The receive message has two generic fields:
    
    *   `type`:  The event type "receive"
        
    *   `data`:  Array<byte> CEC frame
        

### Method

##### send()

```
    Promise<void> send(Array<byte> data)
```

Sends messages over *cec.*

*   `data` Array<byte> : The CEC frame
    

##### port\_name ()

```
    Promise<void>
```

The parameters for this optional argument are:

*   `default`: The default output for the platform, normally `HDMI-1`
    
*   `HDMI-X`: X is a number from 1 up to the number of HDMI**®** outputs on the platform
    
*   `eARC`: The default for the AU335   
    

> [!NOTE]
> **Note**
> As of BrightSignOS 8.2.55, the CEC implementation for AU series 5 products will reply to these messages with the correct data, without involving the script:
> *   CEC\_MSG\_GET\_CEC\_VERSION
>     
> *   CEC\_MSG\_ABORT
>     
> *   CEC\_MSG\_GIVE\_DEVICE\_POWER\_STATUS
>     
> *   CEC\_MSG\_GIVE\_OSD\_NAME
>     
> *   CEC\_MSG\_GIVE\_DEVICE\_VENDOR\_ID
>     
> *   CEC\_MSG\_GIVE\_FEATURES
>     
> *   CEC\_MSG\_GIVE\_PHYSICAL\_ADDR
>     
> *   CEC\_MSG\_USER\_CONTROL\_PRESSED
>     
> *   CEC\_MSG\_USER\_CONTROL\_RELEASED
>     
> *   CEC\_MSG\_REPORT\_PHYSICAL\_ADDR

## Example

See the following example to send or receive CEC messages. See [BSCECTransmitter](../../player-apis/brightscript-javascript-objects/bscectransmitter.md) for an example that turns a display on and off.

```
const CecClass = require('@brightsign/cec');
const cec = new CecClass();

var initiatorAddress = 0x40;
var opcodeGetVersion = 0x9f;
var opcodeVersion = 0x9e;
var version = "";

function onRxEvent(packet) {
    let frame = packet.data;
    let opcode = frame[1];
    console.log("Frame Opcode: " + opcode);
    console.log(JSON.stringify(frame));
    if (opcode == opcodeVersion) {
        version = frame[2].toString(16);
        console.log("Version: " + version);
    }
}

function cecVersion() {
    return new Promise(async (resolve) => {
        version = "";
        let buffer =[];
        buffer[0] = initiatorAddress;
        buffer[1] = opcodeGetVersion;
        cec.send(buffer)
            .then(async function() {
                await (async () => new Promise(resolve => setTimeout(resolve, 1000)))();
                console.log("Version received: " + version);
                resolve();
            })
            .catch (function(error) {
                console.log("Ooops: " + error);
                resolve();
            });
    });
}

async function runtest() {
    cec.addEventListener("receive", onRxEvent);
    await cecVersion();
}
```