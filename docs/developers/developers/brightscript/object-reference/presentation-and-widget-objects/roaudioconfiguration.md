# roAudioConfiguration

This object allows for mixing and leveling of audio streams before they are passed to audio outputs.

Object Creation: The *roAudioConfiguration* object is created with no parameters.

```
CreateObject("roAudioConfiguration")
```

## ifAudioConfiguration

##### ConfigureAudio(audio\_routing As roAssociativeArray) As Boolean

Configures the audio routing. This method will fail if called when audio resources are in use (i.e. there are active *roVideoPlayer* or *roAudioPlayer* instances). It returns `true` on success and `false` on failure. The passed associative array can have the following parameters:

*   `mode` string: Sets the audio routing mode:
    
    *   `"dynamic"`: The default mode. Mixing audio streams with differing sampling rates will cause playback to fail; differing volume levels will not be normalized; and audio streams cannot be added to an output that currently has audio playing on it. Other parameters in the associative array are ignored.
        
    *   `"prerouted"`: This setting was implemented in firmware 7.0. You can add and remove audio streams on an output that currently has audio playing on it; additional audio routing behavior is determined with the `autolevel`, `pcmonly`, and `srcrate` parameters. 
        
*   `autolevel` string: Enables (`"on"`) or disables (`"off"`) volume leveling for audio outputs in the `"prerouted"` audio mode. When this setting is enabled, all PCM audio streams on a particular output will play at a similar volume.
    
*   `pcmonly` string: Enables (`"true"`) or disables (`"false"`) compressed audio support in the `"prerouted"` audio mode.
    
*   `srcrate` int: Sets the sample rate to which all PCM audio streams are converted in the the `"prerouted"` audio mode. This value can be either 44100 or 48000.
    

##### GetConfiguration() As roAssociativeArray

Returns audio configuration information as an associative array:

*   `mode` string: The audio routing mode (`"dynamic"` or `"prerouted"`)
    
*   `decoder_count` int: The number of available decoders
    
*   `compressed_capable_count` int: The number of decoders that can route compressed audio
    
*   `autolevel` boolean: A flag indicating whether the volume leveling setting is enabled
    
*   `pcmonly` boolean: A flag indicating whether the compressed audio support setting is enabled
    
*   `srcrate` int: The sample rate to which all PCM audio streams are converted
    

> [!NOTE]
> If the mode is `"dynamic"`, the associative array will contain the `mode` and `decoder_count` parameter only.

##### GetClockStatus() As roAssociativeArray

Returns audio clock information about the I2C, SPDIF, and HDMI® outputs.