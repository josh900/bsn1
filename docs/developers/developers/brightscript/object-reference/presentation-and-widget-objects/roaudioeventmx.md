# roAudioEventMx

The *roAudioPlayerMx* object can generate *roAudioEventMx* messages with the following values:

*   8 EVENT\_MEDIAENDED
    
*   14 EVENT\_OVERLAY\_MEDIAENDED
    
*   16 EVENT\_MEDIAERROR
    
*   17 EVENT\_OVERLAY\_MEDIAERROR
    

"Media ended" events are sent when a track finishes and there are no more queued tracks for the player, while "Media error" events are sent when a queued file is not found (e.g. when it does not exist). 

## ifInt

##### GetInt() As Integer

Returns the event ID 

##### SetInt(value As Integer) As Void

Sets the value of the event

## ifAudioUserData

##### SetUserData(user\_data As String)

Sets the user data.

##### GetUserData() As String

Returns the user data that has previously been set via `SetUserData()` (either on the source or event object). It will return Invalid if no data has been set.

## ifSourceIdentity

##### GetSourceIdentity() As Integer  
 

##### SetSourceIdentity() As Integer

> [!NOTE]
> The *ifSourceIdentity* interface has been deprecated. We recommend using the *ifAudioUserData* interface instead.