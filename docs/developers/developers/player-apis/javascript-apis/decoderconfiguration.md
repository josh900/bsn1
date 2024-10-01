# decoderconfiguration

The *decoderconfiguration* object allows you to configure video decoders for Mosaic Mode.

**decoderconfiguration IDL**

```
interface DecoderConfiguration {
    Promise<DecoderConfigRead> getConfig();
    Promise<void> applyConfig(DecoderConfig config);
};

interface DecoderConfigWritable {
    attribute String name;
    attribute String friendlyName;
    attribute String configuredSize;
    attribute int zIndex;
    attribute bool mosaicDeinterlace;
};

interface DecoderConfig : DecoderConfigWritable {
    attribute String maxSize;
    attribute String mode;
    attribute int usageCount;
    attribute int maxUsage;
};
```

## Object Creation

To create a *decoderconfiguration* object, first load the `brightsign/decoderconfiguration` module using the `require()` method. Then create an instance of the *decoderconfiguration* class.

```
var DecoderConfigurationClass = require("@brightsign/decoderconfiguration");
var decoderConfig = new DecoderConfigurationClass();
```

## DecoderConfiguration

Use this interface to retrieve and modify video decoder data.

##### getConfig()

```
Promise <DecoderConfigArray> getConfig() 
```

Returns an array of *DecoderConfig* interfaces. Each interface describes a video decoder.

##### applyConfig()

```
Promise <void> applyConfig(DecoderConfigArray config) 
```

Configures video decoder(s) for either standard mode or Mosaic mode. In standard mode, a single decoder is used to play a single video; in Mosaic mode, the decoder can be used to decode multiple videos from different local or remote sources. This method accepts an array of *DecoderConfig* interfaces–attributes that are read-only (e.g. `maxSize`) will be ignored.

The system software selects which video decoder to use based on the resolution probed from the video file. In standard mode, it will attempt to select the decoder that has the closest maximum supported resolution (i.e. 1920x1080 for the HD decoder and 3840x2160 for the 4K decoder), without exceeding that maximum resolution. If a decoder has been configured for Mosaic mode, it will match the video resolution against the specified `configuredSize` instead. If two decoders support the same maximum resolution, you can select a decoder manually using the `friendlyName` attribute.

To select a decoder for an HTML video, include the `decoder:[Friendlyname]` property with the  [hwz attribute](../../../developers/html-development/html-video.md):

```
<video hwz= "decoder:main-video;" > </video>
<video hwz= "decoder:sd-video;" > </video> 
```

The `maxUsage` value of a decoder determines how many video players can be assigned to the decoder using the system software algorithm described above—video players beyond the  `max_usage` limit may be assigned to another decoder or not displayed at all. On the other hand, if you manually assign video players using the `friendly_name` of the decoder, you can assign more video players to the decoder than the `max_usage` limit, but this may cause unpredictable video-display behavior.

## DecoderConfig

This interface contains the settings of a video decoder. It contains both editable and read-only attributes.

### Editable

*   `name` string: The system name of the video decoder (decoder availability differs by model):
    
    *   "4K1": The primary 4K decoder (XTx44 models only)
        
    *   "4K2": The secondary 4K decoder (XTx44 models only)
        
    *   "4K": The sole 4K decoder (HDx24, XTx43, 4Kx42, XDx34, and XDx33 models only)
        
    *   "HD1": The first HD decoder
        
    *   "HD2": The second HD decoder
        
*   `friendlyName` string: A name for referencing the decoder in HTML or BrightScript
    
*   `configuredSize` string: The maximum resolution that the decoder will accept (at framerates up to 60p). If this resolution is the same as the decoder's maximum resolution limit, the decoder will use standard mode; otherwise, it will use Mosaic mode.
    
    *   "4K": 3840x2160
        
    *   "HD": 1920x1080
        
    *   "SD": 720x576
        
    *   "CIF": 352x288
        
    *   "QCIF": 176x144
        

> [!CAUTION]
> **Important**
> Upscaling videos in Mosaic mode currently causes severe performance degradation.

*   `zIndex` int: The z-index of the video window (in standard mode) or group of video windows (in Mosaic mode) relative to the graphics plane:
    
    *   1: The video window (or group of windows) is positioned in front of the graphics plane.
        
    *   \-1: The video window (or group of windows) is positioned behind the graphics plane.
        
*   `mosaicDeinterlace` bool: A flag indicating whether Mosaic-mode videos can be interlaced or not. Enabling the deinterlacer will allow playback of interlaced videos in Mosaic mode, but will reduce the number of Mosaic-mode videos that can be decoded simultaneously as well.
    

### Read-Only

*   `maxSize` string: The maximum resolution of the decoder, as set by system software. This value can be either "4K" or "HD"
    
*   `mode` string: The current mode of the decoder, which can be either `"regular"` or `"mosaic"`
    
*   `usageCount` int:  The number of videos currently being decoded by the decoder
    
*   `maxUsage` int: The maximum number of videos that can be decoded simultaneously by the decoder (this value is always 1 in `"regular"` mode). The optimum `max_usage` limits are described below; the limit may be lower depending on a number of factors, including interlacing and frame rate.
    
    *   4K decoder:
        
        *   1 4K video
            
        *   2 HD videos
            
        *   4 SD videos
            
        *   8 CIF videos
            
        *   10 QCIF videos
            
    *   HD decoder:
        
        *   0 4K videos
            
        *   1 HD video
            
        *   3 SD videos
            
        *   4 CIF videos
            
        *   5 QCIF videos
            

## Example

This script retrieves the current video decoder configuration and modifies it so that the 4K decoder can be used to decode 2 HD videos.

```
var DecoderConfigurationClass = require("@brightsign/decoderconfiguration");
var decoderConfig = new DecoderConfigurationClass();

function findDecoder(element) {
    return element.name === "4K";
};

function setDecoder(decoderList) {
    decoder = decoderList.find(findDecoder);
    decoder.friendlyName = "main-video";
    decoder.configuredSize = "HD";
    decoder.zIndex = 1;
    decoderConfig.applyConfig(decoderList).then()
        .catch(
            function(data) {
                console.log(JSON.stringify(data));
            });
};

decoderConfig.getConfig().then(
        function(data) {
            setDecoder(data);
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        });
```