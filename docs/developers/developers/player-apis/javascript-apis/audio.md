# audio .

The *audio* object is a JavaScript object for use with *roNodeJs* that allows the playback of audio by replicating functionality from the HTML5 audio element.

**audio IDL**

```
interface Audio {
  // error state
  readonly attribute MediaError error;
 
  // network state
           attribute String src;
  readonly attribute String currentSrc;
  readonly attribute unsigned short networkState;
  const unsigned short NETWORK_EMPTY = 0;
  const unsigned short NETWORK_IDLE = 1;
  const unsigned short NETWORK_LOADING = 2;
  const unsigned short NETWORK_NO_SOURCE = 3;
 
  void load();
  String canPlayType(String type);
 
  // ready state
  readonly attribute unsigned short readyState;
  const unsigned short HAVE_NOTHING = 0;
  const unsigned short HAVE_METADATA = 1;
  const unsigned short HAVE_CURRENT_DATA = 2;
  const unsigned short HAVE_FUTURE_DATA = 3;
  const unsigned short HAVE_ENOUGH_DATA = 4;
 
  readonly attribute boolean seeking;
 
  // playback state
           attribute double currentTime;
  readonly attribute double duration;
  readonly attribute boolean paused;
           attribute double defaultPlaybackRate;
           attribute double playbackRate;
  readonly attribute boolean ended;
           attribute boolean autoplay;
           attribute boolean loop;
  void play();
  void pause();
 
  void setSyncParams(String domain, String sync_id, String iso_timestamp);
 
  // controls
           attribute double volume;
           attribute boolean muted;
 
  // BrightSign extensions
           attribute String pcmaudio;
           attribute String compaudio;
 
           attribute int x-bs-stream-timeout;
           attribute String x-bs-audio-mode;
 
  // Present but unimplemented
           attribute String preload;
  readonly attribute TimeRanges buffered;
  readonly attribute double initialTime;
  readonly attribute Date startOffsetTime;
           attribute boolean controls;
  readonly attribute TimeRanges played;
  readonly attribute TimeRanges seekable;
 
  readonly attribute TextTrack[] tracks;
  MutableTextTrack addTrack(String kind, optional String label, optional String language);
 
};
```

## Object Creation

To create an *audio* object, first load the *brightsign/audio* module using the require() method. Then create an instance of the audio class using the following example:

```
var audio_class = require("@brightsign/audio");
var audio_player = new audio_class();
```

## Audio

Use this interface to create *audio* objects.

### Event

`seeked:` This event is fired when media loops back to the start.

### Methods

##### load() 

```
void load()
```

Triggers processing of the `src`. `load` starts up playback to the point of being ready to play the first frame. If `autoplay` is set, then it also starts playback. `readyState` and `networkState` are altered, and multiple events fire as playback starts.

##### canPlayType() 

```
 String canPlayType(String type)
```

Returns whether the passed MIME type can be displayed on the BrightSign player.

##### play() 

```
void play()
```

Starts or resumes playback.

##### pause() 

```
void pause()
```

Pauses playback.

##### setSyncParams()

```
 void setSyncParams(String domain, String sync_id, String iso_timestamp)
```

This BrightSign extension is documented [here.](https://docs.brightsign.biz/display/DOC/BSSyncManager)

## Audio Parameters

*   `src` string: Contains the URL of a media resource to use in the element. Only file URLs are supported currently, including relative URLs to the current script and a file:/// URI with an absolute filesystem path on the player. The URL returned when reading this value back is always absolute with file: protocol on the front.
    
*   `currentSrc` string: Contains the URL of the media resource in use by the element.
    
*   `networkState` unsigned short: An enum that indicates the current state of the fetching of media. This attribute moves through the states as `src` is selected and playback begins, but because support is currently for files only, it is not as dynamic as when used with HTTP. Possible values are:
    
    *   `NETWORK_EMPTY = 0,`
        
    *   `NETWORK_IDLE,`
        
    *   `NETWORK_LOADING,`
        
    *   `NETWORK_NO_SOURCE` 
        
*   `readyState` unsigned short: Indicates the readiness state of media. This attribute moves through the states as `src` is selected and playback begins. Possible values are:
    
    *   `HAVE_NOTHING = 0,`
        
    *   `HAVE_METADATA,`
        
    *   `HAVE_CURRENT_DATA,`
        
    *   `HAVE_FUTURE_DATA,`
        
    *   `HAVE_ENOUGH_DATA`
        
*   `seeking` boolean:  Indicates if the media is seeking to a new position.
    
*   `currentTime` double: Specifies the current playback time in seconds as a floating point. Currently seeking is not supported, and setting this attribute has no effect. If playback is completed, this returns the same value as duration.
    
*   `duration` double: Specifies the current duration of the media in seconds as a floating point.
    
*   `paused` boolean: Reflects whether the media playback is currently paused.
    
*   `defaultPlaybackRate` double: This cannot be set to anything other than 1.0, and always returns 1.0 (only normal speed playback is supported).
    
*   `playbackRate` double: This cannot be set to anything other than 1.0, and always returns 1.0 (only normal speed playback is supported).
    
*   `ended`  boolean: Reflects where the media playback has reached the end of the media.
    
*   `autoplay` boolean: Indicates whether playback should automatically begin when media is available to play without interruption.
    
*   `loop` boolean: Sets whether the playback should loop or not. The value is used when load is called. Setting it once playback has started will have no effect.
    
*   `volume` double: Controls the volume of playback
    
*   `muted` boolean: Controls the muting and unmuting of the audio
    
*   `pcmaudio` string: Route decoded PCM audio to the outputs in the string. Outputs available are `analog`, `earc`, or a USB output (for example, `usb:A.0`). Multiple outputs can be specified by using a semi-colon delimeter (for example, `earc; analog`)
    
*   `compaudio` string: Routes compressed audio direct to eARC without decoding. Can be set to `earc` only.
    
*   `x-bs-stream-timeout` int*:* Controls timeouts when streaming.
    
*   `x-bs-audio-mode` string: Controls the downmix of audio to mono. Possible values are `MonoLeftMixdown`, `MonoRightMixdown`, and the default which is `Stereo`. Using this, two audio players can output to a single stereo output, one to the left channel, and the other to the right channel.
    

## Unimplemented Methods and Properties

*   `preload`
    
*   `buffered`
    
*   `initialTime`
    
*   `startOffsetTime`
    
*   `controls`
    
*   `played`
    
*   `seekable`
    
*   `tracks`
    

## Examples

```
const audio_class = require("@brightsign/audio");
let audio_player = new audio_class();
audio_player.src = "/storage/sd/file.mp4"
audio_player.volume = .5;
audio_player.load();
audio_player.play();
```

```
let setupAudio = (audio, setupObj) => {
   for (let [key, val] of Object.entries(setupObj)) {
      audio[key] = val;
   }
}

let interval = setInterval(()=>{}, 10000);
const audio_class = require("@brightsign/audio");
let audio = new audio_class();
let settings = {
   src: '/storage/sd/file.mp4',
   autoplay: true,
   loop: false,
   volume: .5,
   pcmaudio: "analog"
};
setupAudio(audio, settings);
audio.load();
audio.addEventListener("ended", () => {
   audio.src = '';
   audio = null;
   clearInterval(interval);
   process.exit(0);
});
```