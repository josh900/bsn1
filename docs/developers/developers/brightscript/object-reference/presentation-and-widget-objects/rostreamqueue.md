# roStreamQueue

This object allows you to play a list of video files seamlessly (i.e. without any blank frames or interrupts between one video and the next). You can link *roStreamQueue* to an *roVideoPlayer* instance for seamless video playback or to an *roMediaStreamer* instance for seamless video streaming. 

Object Creation: This object is created with no parameters.

```
CreateObject("roStreamQueue")
```

## File Requirements

Video files must meet the following requirements to work with the *roStreamQueue* object:

*   Files must be Transport Stream (*.ts*) formatted.
    
*   All files in a queue should have identical PIDs.
    
*   Files must begin and end with a closed GOP.
    
*   Files must have regular PCRs at intervals of 100ms or shorter. Note that the default interval for FFMPEG is 1000ms unless it is configured for CBR muxing (in which case the interval is set to 20ms). The following is an example of an appropriate command-line tp remux:
    

```
avconv -i clip_short.ts -vcodec copy -acodec copy -muxrate 15M clip_short2.ts
```

## ifStreamQueue

##### QueueFile(filename As String) As Boolean

Adds the specified video file to the queue.

##### Loop(loop As Boolean) As Boolean

Specifies that playback/streaming should return to the beginning of the queue once it reaches the end. If `Loop(false)` and `LoopLast(false)` are both called, playback/streaming will stop once the end of the queue is reached. This is also the default behavior.

##### LoopLast(loop\_last As Boolean) As Boolean

Specifies that playback/streaming should loop the last file in the queue once it reaches the end. This method has no effect if `Loop(true)` is called as well.

##### SetPreferredAudio(description As String) As Boolean

Chooses a video stream from the video input based on the [parameters](http://docs.brightsign.biz/display/DOC/roVideoPlayer#roVideoPlayer-preferred_streams) in the passed string.

##### SetPreferredVideo(description As String) As Boolean

Chooses an audio stream from the video input based on the [parameters](http://docs.brightsign.biz/display/DOC/roVideoPlayer#roVideoPlayer-preferred_streams) in the passed string.

##### KeepPadding(enabled As Boolean)

If `enabled=true`, all PIDs in the input stream (including padding packets) are passed through to the output. This allows the CBR bitstream profile to be preserved when re-streaming to the network. It cannot be used when feeding a local decoder.

##### NextFile(a As Boolean) As Boolean  
 

##### Start() As Boolean

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roStreamQueueEvent* to the attached message port. An event is raised whenever the end of the queue is reached.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifIdentity

##### GetIdentity() As Integer

Returns a unique number that can be used to identify when events originate from this object.

> [!NOTE]
> The *ifIdentity* interface has been deprecated. We recommend using the *ifUserData* interface instead.

## Playing and Streaming Queues

To use *roStreamQueue* as a streaming playlist, include it as the source component in an *roMediaStreamer.SetPipeline()* call. For video playback, use an *roVideoPlayer* instance as the destination component in the `SetPipeline()` call.

##### **Example (roVideoPlayer)**

```
q=createobject("rostreamqueue")
q.queuefile("sd:/Test_Count_Up_Blue_Frames.ts")
q.queuefile("sd:/Test_Count_Up_Green_Frames.ts")
q.loop(true)
c=createobject("romediastreamer")
r=createobject("rorectangle",0,0,1920,1080)
v=createobject("rovideoplayer")
v.setrectangle(r)
c.setpipeline([q, v])
c.start()
```

##### **Example (roMediaStreamer)**

```
queue = CreateObject("roStreamQueue")
queue.queueFile("file1.ts")
queue.queueFile("file2.ts")
queue.loop(true)
m = CreateObject("roMediaStreamer")
m.setpipeline([queue, "udp://239.0.156.101:5000/?maxbitrate=0"])
m.Start()
```

> [!CAUTION]
> **Important**
> We strongly suggest appending the "maxbitrate=0" parameter to UDP streams when using *roStreamQueue.* This prevents the *roMediaStreamer* instance from rate-limiting an *roStreamQueue* stream that is already running at a precise, correct rate.