# HTML Video

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Streaming Video](#streaming-video)
    *   [Streaming Parameters](#streaming-parameters)
    *   [YouTube](#youtube)
    *   [Media Source Extensions](#media-source-extensions)
    *   [HLS Live Streaming](#hls-live-streaming)
*   [HDMI Input](#hdmi-input)
*   [Multiple Video Elements](#multiple-video-elements)
*   [Small Videos](#small-videos)
*   [View Mode](#view-mode)
*   [HWZ Video](#hwz-video)
    *   [Z-Ordering HWZ Video](#z-ordering-hwz-video)
    *   [Transforming HWZ Video](#transforming-hwz-video)
    *   [Fading HWZ Video Streams](#fading-hwz-video-streams)
    *   [HWZ Video Transparency Extensions](#hwz-video-transparency-extensions)
    *   [How Video Decoders are Selected for Playback](#how-video-decoders-are-selected-for-playback)
*   [Video Decryption](#video-decryption)
*   [Video Stream Parsing](#video-stream-parsing)
    *   [Video Streams](#video-streams)
    *   [Audio Streams](#audio-streams)
    *   [Subtitle and Caption Streams](#subtitle-and-caption-streams)
    *   [Pattern Matching Behavior](#pattern-matching-behavior)
    *   [Further Examples](#further-examples)
*   [Video Track Switching](#video-track-switching)
*   [Audio Routing <audio>/<video> Elements](#audio-routing-audiovideo-elements)
*   [HTML Video Timecode Playback](#html-video-timecode-playback)
*   [Chroma Keying](#chroma-keying)

> [!NOTE]
> The documentation below applies to firmware versions 7.1.x and later.

You can use `<video>` elements to play streaming video (HLS, UDP, RTP, RTSP) and local video files. You can also display HDMI® input on the XD1230, XD1132, 4K1142, or XT1143 (and RF Input on the XD1230). 

## Streaming Video

Streaming video playback is achieved using the standard HTML <video> element with an appropriate *src* attribute.  These URL schemes can be used for playback:

*   http/https
    
*   udp
    
*   rtp
    
*   rtsp
    

Note that pause/resume commands currently work for HLS streams only.

### Streaming Parameters

You can configure streaming video using a number of unique BrightSign attributes.  These attributes can be overridden by parameters that are [included in the streaming URL](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2340651034/Customize+Network+Streaming#Customize-the-Streaming-Buffer-Size).

**Example (HTML)**

```
<video src="udp://239.192.1.1:5004" x-bs-stream-timeout="0">
```

**Example (JavaScript)**

```
videoPlayer.setAttribute("x-bs-stream-low-latency", "1"); 
```

The following streaming parameters are supported:

*   `[int] x-bs-stream-timeout`: The length of time (in milliseconds) to wait for a stream to start before abandoning playback. Passing zero indicates that the video player should wait indefinitely. The default timeout value is 5000ms for HTTP streams and 3000ms for all other streams.
    
*   `[int] x-bs-stream-latency`: The amount of deviation (in milliseconds) from the default latency value: For example, a value of -500 will reduce the latency by half a second; a 500 value will increase the latency by half a second; and a 0 value will specify the default latency. Specifying a negative value will not change the buffer size; instead, it will give the buffer less time to fill up before playback begins. Usable values extend to approximately -750, though this value may differ depending on the network environment. Reducing the latency too much will result in obvious playback stutter.
    
*   `[int] x-bs-stream-fade-in`: The fade-in length (in milliseconds) for streams. By default, non-HTTP streams have a fade value of 1500ms if they contain video and 4000ms if they contain audio only. HTTP streams have a default fade value of 0ms.
    
*   `[int or boolean] x-bs-stream-low-latency`: Low-latency mode for RTSP streams. Setting this parameter to `true` (1) will achieve the lowest possible latency for a stream, but at a reduced maximum bitrate–which is often useful for IP camera streams. This parameter is set to `false` (0) by default.
    
*   `[int] x-bs-intrinsic-width`: The intrinsic width of the source video
    
*   `[int] x-bs-intrinsic-height`: The intrinsic height of the source video.
    

#### Achieving Low Latency

There are three options to reduce latency on Series 3 and 4 BrightSign players:

##### x-bs-stream-latency

The `x-bs-stream-latency` flag (buffer) described above under "Streaming Parameters". In this example, the latency is reduced by half a second (500 milliseconds):

```
<video src="udp://239.192.1.1:5004" x-bs-stream-latency="-500">
```

##### x-bs-no-force-capture

If the `x-bs-no-force-capture` flag is set to `true`, video capture will bypass frame-rate conversion and introduce the following limitations:

*   Transform values other than "identity" will not work.
    
*   Screenshots may not be correct
    
*   The encoded video frame rate and the video mode output must match
    

For example:

```
<video src="udp://239.192.1.1:5004" x-bs-no-force-capture="1">
```

##### x-bs-no-reordering

If the `x-bs-no-reordering` flag is set, it will Improve latency but disable playback of B-slices. For example:

```
<video src="udp://239.192.1.1:5004" x-bs-no-reordering="1">
```

See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2340651034/Customize+Network+Streaming) for more information about modifying the latency of audio or video streams.

#### Native Chrome Media Player

Series 5 players support selecting native Chrome for video playback with hardware acceleration or using the default BrightSign Media Player for video playback. You can pick which option is best for your use case (see [HTML Playback Options on Series 5 Players](../html-development/html-playback-options-on-series-5-players.md)).

##### WebRTC

For WebRTC, BrightSign OS always uses native Chrome video playback.

Series 5 players, running OS 9.0.115 and later, will automatically use hardware-accelerated decode in this case.

Series 4 and older players do not support hardware-accelerated decode with native Chrome video playback. As such, the decode will be done in software, and we only recommend trying this approach with XT4 players.

#### Intrinsic Video Size

The following order of precedence is used to determine the intrinsic size of a video:

1.  The `x-bs-intrinsic-width` and `x-bs-intrinsic-height` attributes
    
2.  The size of the image specified by the `poster` attribute
    
3.  The `width` and `height` attributes of the `<video>` element
    
4.  The size as reported by the WebMediaPlayer
    
5.  The CSS default size, as defined by [W3C](https://www.w3.org/TR/2011/WD-html5-20110113/video.html): 300x150
    

If only the `width` and `height` attributes of a `<video>` element are specified, the rendering engine assumes that the intrinsic size of the source video is the same as the `<video>` element size, so it will scale the video to fill the video element, ignoring the aspect ratio of the source video if necessary. Additionally, if the `width` and `height` attributes of a `<video>` are not specified and the size is not available from the sources (for example, if the stream is still loading), the video will initially default to a resolution of 300x150.

If you know the size or aspect ratio of a source video beforehand, you can use the `x-bs-intrinsic-width`/`x-bs-intrinsic-height` attributes to ensure the aspect ratio of the source video is maintained when scaled to fit a `<video>` element: For example, if the video window is oriented as portrait HD (`width=1080, height=1920`), specifying an intrinsic width and height of 1920x1080 ensures that landscape HD videos will scale to fit while maintaining their aspect ratio and letter-boxing appropriately. Likewise, videos will scale to the intrinsic width/height immediately if the `<video>` element lacks `width` and `height` parameters, rather than possibly defaulting to 300x150 for a short time

### YouTube

BrightSign players support YouTube videos and playlists.

### Media Source Extensions

As of OS 8.3, Media Source Extension (MSE) is enabled automatically on Series 4 players. However, it can still be disabled by setting the mse-support flag to 0 in the registry.

MSE support is available for series 3 but it must be specifically enabled. To do this, enter the following code at the BrightSign prompt:

```
registry write html mse-support 1
```

### HLS Live Streaming

BrightSign players support HLS live streaming, but large playlists (which usually result from the server delivering a DVR playlist rather than a LIVE playlist) will cause performance issues.

## HDMI Input

You must input the video source using the following URI: “tv:brightsign.biz/hdmi”. Note that you *cannot* substitute another host URL for “brightsign.biz”.

**Example**

```
<video width="320" height="240">
       <source src="tv:brightsign.biz/hdmi">
</video>
```

## Multiple Video Elements

By default, XT, 4K, and XD players support a maximum of two active `<video>` elements at any time (HD/LS models only support one). You can have more than this amount of `<video>` elements on a page as long as additional `<video>` elements have their `src` attribute set to an empty string. By modifying the `src` string, you can enable and disable `<video>` elements on the page.

You can enable Mosiac Mode (using the [SetDecoderMode()](../../developers/player-apis/brightscript-javascript-objects/bsvideomode.md) JavaScript method) to increase the minimum allowed number of `<video>` elements.

## Small Videos

BrightSign players do not support videos that are less than 64 pixels in width or height. However, a video can be scaled down beyond this limit by making the `<video>` element smaller than 64x64. To get the desired downscaling behavior, ensure that the `<video>` element does not have the `viewmode="scale-to-fill-and-crop"` attribute.

## View Mode

In firmware versions 7.0.x and later, HWZ video scales to fit the aspect ratio of a `<video>` element (i.e. `"scale-to-fill"`). In earlier versions of firmware, `<video>` elements maintain the aspect ratio of the source video (i.e. `"scale-to-fit"`). This default behavior can be modified using the `viewmode` attribute; however, we now recommend using standard CSS methods (e.g. `object-fit`) to modify the view mode behavior of a `<video>` element.

*   `viewmode="scale-to-fill"`: Scales the video to fill the window. The aspect ratio of the source video is ignored, so the video may appear stretched.
    
*   `viewmode="scale-to-fit"`: Letterboxes the video.
    
*   `viewmode="scale-to-fill-and-crop"`: Scales the video to fill the window. The aspect ratio of the source video is maintained, so the video may be cropped.
    

## HWZ Video

HTML `<video>` elements can have an optional “hwz” attribute, which is disabled by default. With hwz disabled, video frames are decoded by the dedicated hardware but are routed to the GPU for display. With hwz enabled, video frames are instead routed directly to the hardware compositor, bypassing the GPU. The choice of whether to enable hwz or not depends on the application and there is no single and obviously right answer. Some considerations are:

*   The GPU is limited to 8-bit color depth. If 10-bit video is in use, it must be routed to the hardware video plane in order to retain the full color depth.
    
*   In most cases, the GPU is limited to full-HD resolutions. If 4K video is in use, it must be routed to the hardware video plane to avoid loss of resolution. (Even on platforms which can be configured to support 4K graphics, it is unlikely that the GPU will achieve a high enough frame rate for full-motion video playback.)
    
*   The hardware video compositor can perform simple scaling and alpha-blending but does not support arbitrary CSS transforms. Video with complex CSS styling must be routed through the GPU in order to display correctly.  Likewise, any video which needs to be captured as a canvas for WebGL processing must be routed to the GPU. We recommend testing a manipulated hwz video thoroughly before using it in a production environment.
    
*   If video is routed to the GPU, a graphics repaint is required for every frame. This consumes a large amount of system bandwidth and may result in stuttery playback if the GPU is not able to keep up with the required frame rate at all times.
    

In general, we recommend routing video to the hardware compositor unless there is a specific need for processing by the GPU. For most applications, routing video to the hardware compositor can be achieved by setting hwz="z-index:-1" on the video element in question.  This causes the compositor to stack the video and graphics layers according to the CSS z-index property.

You can also enable hwz for all videos in an HTML widget using one of the following methods:

*   **BrightAuthor:connected**: Select the **Enable native video playback** box in the [HTML5 State](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1632600407/HTML5+State).
    
*   **BrightAuthor**: Check the **Enable native video plane playback** box in the [HTML5 state](https://docs.brightsign.biz/display/DOC/HTML5).
    
*   **BrightScript**: Call `SetHWZDefault("on")` on the [*roHtmlWidget*](https://docs.brightsign.biz/display/DOC/roHtmlWidget) instance.
    

### Z-Ordering HWZ Video

If two video elements are to be routed to the hardware compositor, one of them should be given hwz="z-index:-2".  The one with the lower (more negative) z-index will be stacked behind the other. (Note that in this specific instance the CSS stacking order is overridden.)  Alternatively, it is possible to pass a positive z-index value in the hwz attribute. If this is done, the video elements will be stacked in front of the graphics layer, again overriding the CSS stacking order, and the one with the higher positive value z-index will be in front.

To route video playback to the GPU, pass hwz="off" or hwz="z-index:0" (these are equivalent). The legacy value hwz="on" is equivalent to hwz="z-index:1" and should be avoided.

You can use the CSS z-index property to layer the elements without enabling hwz. The layer order shown below is text on top → video in the middle→ image in the back:

```
<body style="background-color:blue">
  <div style="position:absolute;color:red;font-size:100px;z-index:-1" > Hello BrightSign </div>
  <img src="poster.png" style="position:absolute;left:0px;top:0px;width:800px;height:800px;z-index:-3"></img>
  <video src="coffee2.mp4" style="position:absolute;left:0px;top:0px;width:480px;height:320px;z-index: -2;" autoplay loop muted></video>
</body>
```

If hwz is enabled, your CSS z-index property (`style="z-index:-1")` will be overridden. Add a z-index value in the hwz attribute to maintain the correct z-ordering positions for all elements:

```
<body style="background-color:blue">
  <div style="position:absolute;z-index:-1;color: red;font-size: 100px;" hwz="z-index:-1"> Hello World </div>
  <img src="poster.png" style="position:absolute;left:0px;top:0px;width:800px;height:800px;z-index:-3" hwz="z-index:-3"></img>
  <video src="coffee2.mp4" style="position:absolute;left:0px;top:0px;width:480px;height:320px;z-index: -2;" hwz="z-index:-2" autoplay loop muted></video>
</body>
```

### Transforming HWZ Video

You can add the optional "transform" parameter to the "hwz" attribute to rotate or mirror the `<video>` element. The `z-index:` parameter must also be specified for the transform to work. The "transform" parameter can be assigned the following values:

*   `identity`: No transformation (default behavior)
    
*   `rot90`: 90 degree clockwise rotation
    
*   `rot180`: 180 degree rotation
    
*   `rot270`: 270 degree clockwise rotation
    
*   `mirror`: Horizontal mirror transformation
    
*   `mirror_rot90`: Mirrored 90 degree clockwise rotation
    
*   `mirror_rot180`: Mirrored 180 degree clockwise rotation
    
*   `mirror_rot270`: Mirrored 270 degree clockwise rotation
    

> [!NOTE]
> Multiple HWZ video tag extensions are separated with a semicolon. A semicolon should also be appended to the final parameter.

**Example**

```
 // Video rotated 180 degrees and behind graphics layer.
<video src="example_movie.mp4" hwz="z-index:-1; transform:rot180;">
```

### Fading HWZ Video Streams

The "fade" parameter allows you to control the fading behavior between streaming videos in a `<video>` element (this setting does not apply to local video). The "fade" parameter allows you to control the fading behavior between decoded videos in a <video> element (this setting does not apply to HDMI in). It does not affect audio and will operate independently of [StreamFadeIn](https://docs.brightsign.biz/display/DOC/roVideoPlayer#roVideoPlayer-PlayFile(parametersAsroAssociativeArray)AsBooleanplayfile).

The "fade" parameter accepts the following values:

*   `auto`: If the video player is currently not showing anything (i.e. it hasn't played anything yet or the previous loaded video was cleared), the next video will fade in. If the video player is currently playing video, is paused, or is stopped without being cleared, the next video will not fade in. This is the default behavior.
    
*   `always` : When a video ends, the video window will go black. The new video will then fade in.
    
*   `never`: Videos transition without fade effects. 
    

### HWZ Video Transparency Extensions

If "hwz" is enabled for a `<video>` element, the video window can also support luma and chroma keys for video transparency. The `z-index:` parameter must also be specified for transparency to work. The luma and chroma keys are specified as follows: 

*   `luma-key:[HEX_VALUE]` 
    
*   `cr-key:[HEX_VALUE]` 
    
*   `cb-key:[HEX_VALUE]`  
    

**Example**

This is an example of a video on video layer, in front of graphics layer, with luma-keyed video:

```
<video src="example_movie.mp4" hwz="z-index:1; luma-key:#ff0020;">
```

### How Video Decoders are Selected for Playback

The system software selects which video decoder to use based on the resolution probed from the video file. In standard mode, it will attempt to select the decoder that has the closest maximum supported resolution (i.e. 1920x1080 for the HD decoder and 3840x2160 for the 4K decoder), without exceeding that maximum resolution. If a decoder has been configured for Mosaic mode, it will match the video resolution against the specified `timeslice_mode` instead. If both decoders support the same maximum resolution, you can select a decoder by matching the z-order of the *roVideoPlayer* instance (set using the `ToFront()` and `ToBack()` methods) with the z-order of the decoder (set using the *roVideoMode.SetDecoderMode()* method).

You can also select the decoder manually. First, configure the decoder(s) using the *roVideoMode.SetDecoderMode()* method. Then, use the `friendly_name` specified when calling the method to designate a decoder to use for video playback.

To select a decoder in BrightScript, pass an associative array to the *roVideoPlayer.PlayFile()* method containing the `decoder:[friendly_name]` parameter:

`PlayFile({filename:"text_1.mov", decoder:"main-video"})`

To select a decoder for HTML video, include the `decoder:[friendly_name]` property with the `hwz` attribute:

`<video` `hwz="decoder:main-video;"> </video>`  
`<video` `hwz="decoder:sd-video;"> </video>`

  
The `max_usage` of a decoder determines how many video players can be assigned to the decoder using the system software algorithm described above—video players beyond the  `max_usage` limit may be assigned to another decoder or not displayed at all. On the other hand, if you manually assign video players using the `friendly_name` of the decoder, you can assign more video players to the decoder than the `max_usage` limit, but this may cause unpredictable video-display behavior.

## Video Decryption

The HTML `<video>` tag can be used to decrypt video files and IP streams. Streaming decryption is currently only supported with the UDP protocol and the HTTP protocol (when HTTP is paired with an MPEG2 transport stream). If using a UDP multicast MPEG2 transport stream, one of the elemental streams should provide the PCR to the player.

The `<video>` tag supports the `EncryptionAlgorithm` and `EncryptionKey` methods:

*   `EncryptionAlgorithm`: The file-encryption algorithm. The following are the current options:
    
    *   "AesCtr": The AES algorithm in CTR mode
        
    *   "AesCtrHmac": The AES algorithm in CTR mode with HMAC
        
    *   "TsAesEcb": The AES algorithm in ECB mode (e.g. with a Harmonic Prostream). This algorithm is currently used for streaming encryption/decryption.
        
    *   "TsAesCbcRbt": The AES algorithm in CBC mode with residual block termination. This algorithm is used for streaming encryption/decryption.
        
*   `EncryptionKey`: A byte array consisting of 128 bits of key. If the encryption algorithm is AES-CTR or AES-CTR-HMAC, this is followed by 128 bits of IV.
    

**Example (HTML)**

```
<video src="udp://239.192.1.59:5000" EncryptionAlgorithm="TsAesEcb" EncryptionKey="01030507090b0d0f00020406080a0c0e">
```

> [!NOTE]
> The video player no longer accepts "{A|A}" AES encryption keys (i.e. where the top and bottom 64 bits of the key are identical).

**Example (JavaScript)**

```
var player = document.getElementById("my_video_player");
player.setAttribute("EncryptionAlgorithm", "TsAesEcb");
player.setAttribute("EncryptionKey", "01030507090b0d0f00020406080a0c0e");
```

## Video Stream Parsing

The following optional attributes can be included in an HTML `<video>` tag: "preferredvideo", "preferredaudio", and "preferredcaptions". If multiple video, audio, or data streams are encapsulated in the video input, these attributes allow you to determine which stream to use. For example, if a video may contain English and Spanish audio tracks, you can use the "preferredaudio" attribute to specify that the Spanish track should be played if it exists, with the video defaulting to English otherwise.

Preferred streams are chosen by matching the supplied text patterns against the textual description of the stream:

1.  Each attribute ("preferredvideo", "preferredaudio", or "preferredcaptions") is a semicolon-separated list of templates.
    
2.  Each template is a comma-separated list of patterns.
    
3.  Each pattern is a `[field_name]=[field_value]` pair that is matched directly against the stream description.
    

### Video Streams

Each template in a "preferredvideo" attribute can contain the following patterns:

*   `pid=[integer]`: The packet identifier (PID) of the video stream you wish to display
    
*   `program=[integer]`: The program number of the video stream
    
*   `codec=[video_codec]`: The preferred video codec, which can be any of the following:
    
    *   `MPEG1`
        
    *   `MPEG2`
        
    *   `MPEG4Part2`
        
    *   `H263`
        
    *   `H264`
        
    *   `VC1`
        
    *   `H265`
        
*   `width=[integer]`: The preferred video width
    
*   `height=[integer]`: The preferred video height
    
*   `aspect=[float(x.yy)]`: The preferred aspect ratio of the video stream as a floating-point number with two fractional digits.
    
*   `colordepth=[integer]`: The preferred color depth of the video.
    

**Example**

```
preferredvideo="pid=7680, codec=H264, width=1280, height=720, aspect=1.78, colordepth=8;;"
```

### Audio Streams

Each template in a "preferredaudio" attribute can contain the following patterns:

*   `pid=[integer]`: The packet identifier (PID) of the audio stream you wish to play
    
*   `program=[integer]`: The program number of the audio stream
    
*   `codec=[audio_codec]`: The preferred audio codec, which can be any of the following:
    
    *   `MPEG`
        
    *   `MP3`
        
    *   `AAC`
        
    *   `AAC-PLUS`
        
    *   `AC3`
        
    *   `AC3-PLUS`
        
    *   `DTS`
        
    *   `PCM`
        
    *   `FLAC`
        
    *   `Vorbis`
        
*   `channels=[integer]`: The preferred number of audio channels (from 1 to 8)
    
*   `freq=[frequency]`: The preferred sample frequency of the audio track, which can be any of the following:
    
    *   `32000`
        
    *   `44100`
        
    *   `48000`
        
*   `lang=[language]`: A code that determines the preferred language of the audio track (e.g. `eng`, `spa`). The language codes are specified in the ISO 639-2 standard.
    
*   `type=[audio_type]`: The preferred audio type, which can be one of the following:
    
    *   `Main audio`
        
    *   `Clean effects`
        
    *   `Hearing impaired`
        
    *   `Visual impaired commentary`
        

**Example**

```
preferredaudio="pid=4192, codec=AC3, channels=5, freq=48000, lang=eng, type=Main audio;;"
```

### Subtitle and Caption Streams

Each template in a "preferredcaption" attribute can contain the following patterns:

*   `pid=[integer]`: The packet identifier (PID) of the caption stream you wish to play
    
*   `type=[subtitle_type]`: The encoding standard of the subtitles. This value can be one of the following:
    
    *   `CEA708`: If the CEA-708 standard is not present, the subtitle\_type will default to CEA-608 (if it is present).
        
    *   `CEA608`
        
    *   `DVB`
        
*   `lang=[language]`: A code that determines the preferred language of the subtitles (e.g. `eng`, `spa`). The language codes are specified in the ISO 639-2 standard.
    
*   `service=[integer]`: The preferred service number of the caption stream
    

**Example**

```
preferredcaptions="pid=0, type=Cea708, lang=eng service=1;;"
```

> [!NOTE]
> Subtitles and captions are rendered on the graphics layer, and `hwz` must be set to `z-index -1` or `z-index -2` to place the video behind the graphics. Otherwise the subtitles and/or captions will be covered by the video.

### Pattern Matching Behavior

Note the following when matching templates to stream descriptions:

*   For a template to match a stream description, every pattern within the template must match.
    
*   The first listed template to match the stream description (if any) will be used.
    
*   An empty template string will match any stream description.
    
*   All value comparisons are case-insensitive.
    
*   Numerical values must match the stream description exactly (without leading zeroes). For example, the pattern `pid=016` will never match the stream PID value of 16.
    
*   To indicate logical negation, apply the "!" exclamation mark to the beginning of a pattern. For example, specifying `preferredvideo="!codec=H265"` will match only streams that are not encoded using H.265.
    
*   Apply the ">" greater-than symbol before an integer to indicate that, for a successful match, the value in the stream description must be *greater than* the value following the symbol. For example, specifying `preferredvideo="width=<1921,height=<1081"` will match only videos that are no larger than full-HD.
    
*   Apply the "<" less-than symbol before an integer to indicate that, for a successful match, the value in the stream description must be *less than* the value following the symbol.
    

### Further Examples

The following template list contains three patterns: `lang=eng`, `lang=spa`, and an empty string. The first pattern specifies an English language channel; if the English channel does not exist, the second pattern specifies a Spanish language channel. The third pattern specifies any other channel if the first two don't exist (the empty string matches anything).

```
preferredaudio="lang=eng;lang=spa;;"
```

Since the following template list is empty, no captions are specified. This can be used to disable captions altogether.

```
preferredcaptions=""
```

The following template list contains an empty string template. Since an empty template matches anything, the first video stream encountered will be played. This is the default behavior of all attributes.

```
preferredvideo=";"
```

The following template list specifies a 48KHz audio stream if there is one; otherwise, no audio stream will be played. Observe that the list is not terminated with a semicolon; in this case, the semi-colon is implicitly supplied.

```
preferredaudio="freq=48000"
```

The following template list contains two templates. Note that all patterns within a template must match the stream description for the entire template to match. In this example, an AAC-encoded English track is preferred; an MP3-encoded English track is designated as the second option; and any track will be chosen if neither template is matched.

```
preferredaudio="codec=aac,lang=eng;codec=mp3,lang=eng;;"
```

## Video Track Switching

The BrightSign media playback framework does not support dynamic switching among tracks via HTML5 video/audio. However, it does support querying track information using the [Tracklist API](https://www.w3.org/TR/html5/embedded-content-0.html#audiotracklist-and-videotracklist-objects). The following steps outline how to select tracks using this API.

1.  Create a video element in JavaScript that is not attached to the DOM (i.e. that is invisible).
    
2.  Set the `onloadedmetadata` event listener.
    
3.  Set the `src` of the media URL.
    
4.  Call `load()` on the HTML5 video element. This will trigger the `loadedmetadata` event.
    
5.  Read the track information from the event.
    
6.  Create a new HTML5 video player and use the track information to set the `preferredAudio`, `preferredVideo`, and `preferredSubtitle` parameters (described above).
    
7.  Call `load()`/`play()` on the video element.
    
8.  Append the video element to the DOM.
    

> [!NOTE]
> When switching from one video to another, it is important to set the video source to be blank to release the video element, otherwise the first video(s) will continue to use memory while subsequent videos are playing. See line 12 in the code example below.

**Example**

```
<!DOCTYPE html>
<head>
  <script>
var video;

function playTrackNext()
{
  // Switch to audio/video 1
  var pid = video.videoTracks[1].id;
  var audiopid = video.audioTracks[1].id;
  // release the video element
  video.src = "";                            
  // create a new video element
  video = document.createElement('video');   
  video.src = "http://brightsign.biz/example.ts";
  video.hwz = "on";
  video.preferredvideo = "pid=" + pid;       
  // use the params we gathered from previous video load
  video.preferredaudio = "pid=" + audiopid;
  video.load();
  video.play();
  document.getElementById("videoarea").appendChild(video);
}


function runTest()
{
  // Initialize testing bs/javascript bridge.
  bs.start();
  // Initial load of media to gather track information
  video = document.createElement('video');
  video.onloadedmetadata = playTrackNext; // play track 0
  video.src = "http://brightsign.biz/example.ts";
  video.hwz = "on";
  video.load(); // will trigger loadedmetadata event once the video is loaded.
}
  </script>
</head>
<html>
  <body bgcolor="#E6E6FA" onload="runTest()">
    <h1>Video Audio Tracks Test Page</h1>
    <div id="videoarea"></div>
</html>
```

## Audio Routing <audio>/<video> Elements

BrightSign players have unique audio attributes for `<audio>/<video>` elements. These allow you to control how the audio is routed through the player outputs:

*   `Pcmaudio`: PCM audio
    
*   `Compaudio`: Compressed audio
    
*   `Multiaudio`: Multi-channel audio
    

Each attribute can be passed the following values, which determine where the audio will be routed:

*   `“none”`
    
*   `"hdmi”` or `"hdmi-1"`, `"hdmi-2"`, `"hdmi-3"`, or `"hdmi-4`" for Series 5 players with multiple outputs
    
*   `“usb”`
    
*   `“spdif”`
    
*   `"analog"`
    
*   `“analog:N”` (N specifies the port enumeration, which is useful for models with multiple analog-audio ports; you can also use `"analog:1"` to specify the analog output on a model with a single analog-audio port)
    

> [!NOTE]
> If you don’t assign any audio attributes to an `<audio>/<video>` element, then the audio will be routed to all audio outputs, along with any other audio that is currently playing.

**Example 1**

```
<video src="example_movie.mp4" width="512" height="400" pcmaudio="hdmi" autoplay>
  Your browser does not support the video tag.
</video>
```

**Example 2**

```
<video src="example_movie.mp4" width="512" height="400" compaudio="hdmi;usb"autoplay>
  Your browser does not support the video tag.
</video>
```

## HTML Video Timecode Playback

BrightSign precision for HTML video timecode playback is 200ms.

## Chroma Keying

BrightSign chroma key settings consist of a mask, and a minimum and maximum value. The minimum and maximum are the most important values since the mask is really only useful for “special effects”. Each pixel of every frame is checked to see if it is between the minimum and maximum values and if it is, the pixel is set to fully transparent. If it is outside the range, the pixel is fully opaque. This means you will have a hard edge, not a gradual fade, where the video goes from opaque to transparent.

#### Chroma Key Tips

*   To get better chroma keying, do not anti-alias any pixels that should be transparent. You will then be able to target a single transparency color rather than a range.
    
*   If your video is compressed, the chroma is sub-sampled, so there will be edges where the chroma will end up as an intermediate value between green and the frame color. CGI animations with green holes often have anti-aliasing which will result in a fade of green around edges. You may be able to chroma keyed out these edges with the values shown in the examples below (in these examples, v is an [roVideoPlayer](../../developers/brightscript/object-reference/presentation-and-widget-objects/rovideoplayer.md) object).
    
*   The easiest color to remove from content is black which has a luma value of 0, because the video has sub-sampled chroma (4:2:0 rather than 4:4:4). Using luma keying means that every pixel can be accurately keyed.
    
*   White is luma 240 (it's not quite a full range 8 bit value), but the chroma can mean that it contains many other bright colors, so it's hard to just remove white.
    
*   Arbitrary colors are hard to deal with, as they involve specifying a small range of chroma values which must be calculated. The color to be removed has to be calculated in YCbCr, and the Cb and Cr values are used for the chroma keying. If the source is CGI then the range used can be very tight since a single color is made transparent. If the video source was live footage shot against a green screen, then the range needs to be much wider to accommodate the range of green colors in the video.
    

#### Examples

##### Lower Chroma Key Values

Here the Cr range is 0-32 and the Cb range is 0-48. This may leave a green halo around areas that were blended to give a smoother look since chroma keying can't do smooth transitions.

```
v.SetKeyingValue({cr:&hff2000, cb:&hff3000})
```

##### Higher Chroma Key Values

This example covers a much larger range of colors:

```
v.SetKeyingValue({cr:&hff7000, cb:&hff7000})  
```