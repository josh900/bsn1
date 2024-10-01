# audioconfig

This object allows for mixing and leveling of audio streams before they are passed to audio outputs. 

**audioconfig IDL**

```
interface AudioConfiguration {
    Promise<AudioConfig> getConfig();
    Promise<void> applyConfig(AudioConfig config);
};

interface AudioConfig {
    attribute String modeName;
    [optional] attribute int srcRate;
    [optional] attribute bool pcmOnly;
    [optional] attribute bool autoLevel;
};
```

## Object Creation

To create an *audioconfig* object, load the `brightsign/audioconfiguration` module using the `require()` method.

```
var AudioConfigurationClass = require("@brightsign/audioconfiguration");
var audioconfig = new AudioConfigurationClass();
```

## AudioConfiguration

Use this interface to create *audioconfig* objects.

##### getConfig()

```
Promise<AudioConfig> getConfig()
```

Returns the audio configuration information.

##### applyConfig()

```
Promise<void> applyConfig(AudioConfig config)
```

Configures the audio mode to switch between dynamic and pre-routed.

## AudioConfig

This interface contains the audio configuration parameters for all but the AU series 5 product line. See the note below for more information about those products.

*   `modeName` string: Sets the audio routing mode:
    
    *   `"dynamic"`: The default mode. Mixing audio streams with differing sampling rates will cause playback to fail; differing volume levels will not be normalized; and audio streams cannot be added to an output that currently has audio playing on it. Other parameters in the associative array are ignored. However, in the AU product line, only a single audio stream can be played to an output at any one time. All other parameters in the associative array are ignored.
        
    *   `"prerouted"`: Add and remove audio streams on an output that currently has audio playing on it; additional audio routing behavior is determined with the `srcrate,  pcmonly`, and `autolevel` parameters. 
        
*   `srcRate` int optional: Sets the sample rate to which all PCM audio streams are converted in the the "pre-routed" audio mode. This value can be either 44100 or 48000.
    
*   `pcmOnly` bool optional: Enables ("true") or disables ("false") compressed audio support in the "pre-routed" audio mode. 
    
*   `autoLevel` bool optional: Enables ("on") or disables ("off") volume leveling for audio outputs in the "pre-routed" audio mode. When this setting is enabled, all PCM audio streams on a particular output will play at a similar volume. 
    

> [!NOTE]
> These audio configuration parameter definitions are specific to AU series 5 products:
> *   `modeName` string: Sets the audio routing mode:
>     
>     *   `"dynamic"`: The default mode. Only a single audio stream can be played to an output at any one time. All other parameters in the associative array are ignored.
>         
>     *   `"prerouted"`:  Multiple audio streams can be played simultaneously to analog or eARC outputs (not USB). Audio is always the sample rate converted to the value set in *srcRate*. Streams can be started and stopped without affecting other playing streams.
>         
> *   `srcRate` int optional: Sets the sample rate to which all PCM audio streams are converted in the the "pre-routed" audio mode. This value can be from 32000 to 96000.
>     
> *   `pcmOnly` bool optional: This feature is not available on the AU series 5 product line.
>     
> *   `autoLevel` bool optional: This feature is not available on the AU series 5 product line.

## Example

In this example, the code gets the current audio configuration, alters it (though it doesn't check that the values are changing), and writes it back:

```
var AudioConfigurationClass = require("@brightsign/audioconfiguration");
var audioconfig = new AudioConfigurationClass();
var config_state = await audioconfig.getConfig();
config_state.mode = "prerouted"
config_state.srcRate = 48000;
await audioconfig.applyConfig(config_state);
```