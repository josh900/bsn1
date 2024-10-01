# BSVideoMode

For more information about available methods, refer to the *roVideoMode* page.  If you’d like to change the video mode of the player, you will need to use BrightScript instead of this JavaScript class. 

The JavaScript equivalent is [videomodeconfiguration](../../player-apis/javascript-apis/videomodeconfiguration.md).

## Attributes

`readonly attribute int resX`

`readonly attribute int resY`

`readonly attribute int safeX`

`readonly attribute int safeY`

`readonly attribute int safeWidth`

`readonly attribute int safeHeight` 

`readonly attribute DOMString mode`

`readonly attribute BSDecoderModeList decoderModeList`

## Methods

> [!WARNING]
> The methods used by this object are obsolete and can be found in the [videooutput](../../player-apis/javascript-apis/videooutput.md) and [videomodeconfiguration](../../player-apis/javascript-apis/videomodeconfiguration.md) JavaScript API documentation. The HdmiAudioDisable() method can be found in the *roVideoMode* BrightScript API documentation.

```
boolean IsAttached(in DOMString connector)

DOMString GetBestMode(in DOMString connector)

boolean SetBackgroundColour(in unsigned long rgb)

boolean SetBackgroundColour(in unsigned long r,
	in unsigned long g,
	in unsigned long b)

boolean SetPowerSaveMode(in boolean disable)

boolean HdmiAudioDisable(in boolean disable)
 
boolean SetDecoderMode(in DOMString decoder,
	in DOMString timeslice_mode,
	in int z_order,
	in DOMString friendly_name,
	in boolean enable_mosaic_deinterlacer)


boolean SetSyncManager(in BSSyncManager sync); //See the roVideoMode.SetSyncDomain() entry for more details.
```

## BSDecoderMode

The `decoderModeList` attribute contains an array of *BSDecoderMode* objects, each containing information about a configured decoder on the player.

See the `SetDecoderMode()` and `GetDecoderMode()` entries on the [*roVideoMode*](../../../developers/brightscript/object-reference/presentation-and-widget-objects/rovideomode.md) page for more information about decoder parameters.

```
interface BSDecoderMode {
    readonly attribute DOMString decoderName;
    readonly attribute DOMString friendlyName;
    readonly attribute DOMString maxSize;
    readonly attribute DOMString configuredSize;
    readonly attribute unsigned long currentUsage;
    readonly attribute unsigned long maxUsage;
    readonly attribute boolean mosaic;
    readonly attribute boolean enableDeinterlacer;
};
```

## Example

The following JavaScript example illustrates how to retrieve information about the current video mode:

```
function fillInVideoData()
    {
        var videomode_info = new BSVideoMode();
        document.getElementById("resX").innerHTML = videomode_info.resX;
        document.getElementById("resY").innerHTML = videomode_info.resY;
        document.getElementById("safeX").innerHTML = videomode_info.safeX;
        document.getElementById("safeY").innerHTML = videomode_info.safeY;
        document.getElementById("safeWidth").innerHTML = videomode_info.safeWidth;
        document.getElementById("safeHeight").innerHTML = videomode_info.safeHeight;
        document.getElementById("videoMode").innerHTML = videomode_info.mode;
        document.getElementById("bestMode").innerHTML = videomode_info.GetBestMode("hdmi");
        document.getElementById("connectedFlag").innerHTML = videomode_info.IsAttached("vga");
    }

function changeBackground()
    {
        var videomode_info = new BSVideoMode();
        videomode_info.SetBackgroundColour(0xFF0000);
    }
```