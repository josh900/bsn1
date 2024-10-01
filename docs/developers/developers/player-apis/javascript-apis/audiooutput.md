# audiooutput

This object allows individual control of audio outputs on the player.

**audiooutput IDL**

```
    constructor(String output_name)
] interface AudioOutput {
            attribute float volumeLinear;
            attribute float volumeDb;
            attribute long delay;   
            attribute float treble; 
            attribute float bass;   
            attribute boolean mute;
   readonly attribute string name;
};
```

## Object Creation

To create an *audiooutput* object, use the `require()` method.

You must also enter an `AudioOutputClass` (in the example below, "analog" is used). The `AudioOutputClass` parameter can take the following strings:

*   `“none”`
    
*   `"hdmi”` or `"hdmi-1"`, `"hdmi-2"`, `"hdmi-3"`, or `"hdmi-4`" for Series 5 players with multiple outputs
    
*   `“usb”`
    
*   `“spdif”`
    
*   `"analog"` 
    
*   `“analog:N”`
    
*   `"earc"` (AU335 only)
    
*   Support for multiple USB outputs using the USB port naming terminology. See [roDeviceInfo-getusbtopology](../../../developers/brightscript/object-reference/system-objects/rodeviceinfo.md)
    

```
var AudioOutputClass = require("@brightsign/audiooutput");
var audiooutput = new AudioOutputClass("analog");
```

## AudioOutput

Use this interface to create *audiooutput* objects.

*   `volumeLinear` float: Sets the linear volume of the specified output as a percentage represented by a floating point number between 0 and 1 (1.0 is 100%).
    
*   `volumeDb` float: Sets the volume in decibels of the specified output as a percentage represented by a floating point number where 0.0 is 100%
    
*   `delay` long: On Series 3 and 4 players, delays the audio for a specific audio output by lagging decoded samples before they reach that output. Delays are in milliseconds.
    
*   `treble` float: On Series 3 and 4 players, sets the treble of the specified output in decibels. The treble floating point numbers can range from -10 to 10, with 0 indicating no modification to the audio signal. 
    
*   `bass` float: On Series 3 and 4 players, sets the bass of the specified output in decibels. The bass floating point numbers can range from -10 to 10, with 0 indicating no modification to the audio signal. 
    
*   `mute` boolean: Mutes the specified output if True. This method is set to False by default.
    
*   `name` string: The name of the output.
    
*   `plugState` boolean: Has a value of `true` if the corresponding output has a plug in it, `false` if it does not, or `undefined` if the plug state cannot be determined on the current hardware or OS version. This is supported by BOS 9.0.163 onwards.