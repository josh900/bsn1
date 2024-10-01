# roVideoEvent, roAudioEvent

Video and audio events are declared as separate classes. Events can have one of the following values, which are retrieved using the `GetInt()` method:

|     |     |     |
| --- | --- | --- |
| 3   | `Playing` | The current media item has started playing. |
| 8   | `MediaEnded` | The media item has completed playback. |
| 12  | `TimeHit` | A particular timecode has been reached. See the entry on [Timecode Events](../presentation-and-widget-objects/rovideoplayer.md) for more details. |
| 13  | `Overlay_Playing` | An *roAudioPlayerMx* instance has begun playback of an audio file. |
| 14  | `Overlay_MediaEnded` | An *roAudioPlayerMx* instance has completed playback of an audio file. |
| 15  | `Overlay_TimeHit` | The EventTimeStamp of an *roAudioPlayerMx* instance has been been reached. |
| 16  | `MediaError` | A media error has been detected. As opposed to code 30, this event usually indicates transient errors (e.g. low buffer levels). |
| 17  | `Overlay_MediaError` | A media error has been detected during *roAudioPlayerMx* playback. |
| 18  | `FadingOut` | The current media item has completed fading out. See the *roVideoPlayer.SetFade()* entry for more details. |
| 19  | `DecoderEOS` |     |
| 20  | `Overlay_FadingOut` | The FadeOutLocation of an *roAudioPlayerMx* instance has been reached. |
| 21  | `Overlay_DecoderEOS` |     |
| 26  | `Underflow` | The stream seems to be underflowing. This event usually indicates that the streaming latency is set too low. It will be generated every few seconds as long as underflow is detected. |
| 30  | `MediaError_NotStarted` | A fatal error has been encountered while attempting to start playback (e.g. the video format is not supported). |
|     | `ResourceShortage` | You are trying to play more video simultaneously than is allowed. If you are playing a single video by creating new video tags, reuse the existing video tag when possible to avoid race conditions when a video tag might hold onto a hardware video resource or take too long to disassociate a video player from the video tag. |

  

> [!NOTE]
> The [Diagnostic Web Server](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server#DiagnosticWebServer-log) [log](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server#DiagnosticWebServer-log) may return more specific information about media error states.

## ifInt

##### GetInt() As Integer

Returns the event ID as an integer value. 

##### SetInt(value As Integer) As Void

Sets the integer value. 

## ifUserData

##### SetUserData(user\_data As Object) As Void

Sets the user data.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()` (on either the event or source object). It will return Invalid if no data has been set.

## ifSourceIdentity

##### GetSourceIdentity() As Integer  
 

##### SetSourceIdentity() As Integer 

> [!NOTE]
> The *ifSourceIdentity* interface has been deprecated. We recommend using the *ifUserData* interface instead.

## ifData    

##### GetData() As Integer

##### SetData(a As Integer) 

## Example

```
vp_msg_loop:
    msg=Wait(tiut, p)    
    if type(msg)="roVideoEvent" then
        if debug then print "Video Event";msg.GetInt()
        if msg.GetInt() = 8 then
            if debug then print "VideoFinished"
            retcode=5
            return
        endif
    else if type(msg)="roGpioButton" then
        if debug then print "Button Press";msg
        if escm and msg=BM then retcode=1:return
        if esc1 and msg=B1 then retcode=2:return
        if esc2 and msg=B2 then retcode=3:return
        if esc3 and msg=B3 then retcode=4:return
    else if type(msg)="rotINT32" then
        if debug then print "TimeOut"
        retcode=6
        return
    endif

    goto vp_msg_loop
```