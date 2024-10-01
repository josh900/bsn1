# roChannelManager

You can use this object to manage RF channel scanning and tuning. The *roVideoPlayer* method also has channel scanning capabilities.

Object Creation: The *roChannelManager* object is created with no parameters.

```
CreateObject("roChannelManager")
```

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifMessagePort

##### SetPort(port As roMessagePort)

## ifChannelManager

The *ifChannelManager* interface provides both a Synchronous and Asynchronous API:

### Synchronous API

##### Scan(parameters As roAssociativeArray) As Boolean

Performs a channel scan on the RF input for both ATSC and QAM frequencies and builds a channel map based on what it finds. The *roChannelManager* object stores a list of all channels that are obtained using the `CreateChannelDescriptor()` method (described below). The list is cleared on each call to `Scan()` by default, but this behavior can be overridden.

Each channel takes approximately one second to scan; you can limit the scope of the channel scan with the following parameters:

*   \["ChannelMap"\] = "ATSC" or "QAM": Limits the frequency scan to either QAM or ATSC.
    
*   \["ModulationType"\] = "QAM64" or "QAM256": Limits the modulation type of the scan to QAM64 or QAM256.
    
*   \["FirstRfChannel"\] = Integer and/or \["LastRfChannel"\] = Integer: Limits the scan to the specified range of channels. The high end of the channel range is an optional parameter.
    
*   \["ChannelStore"\] = "DISCARD ALL" or "MERGE": Controls how the script handles previous channel scan information. The default setting is DISCARD ALL, which clears all channel data prior to scanning. On the other hand, MERGE overwrites the data only for channels specified in the scan.
    

##### GetChannelCount() As Integer

Returns the number of found channels.

##### ClearChannelData() As Boolean

Clears all stored channel scanning data, including that which persists in the registry. This method also cancels any `AsyncScan()` calls that are currently running.

##### GetCurrentSnr() As Integer

Returns the SNR (in centibels) of the currently tuned channel.

##### ExporttoXML() As String

Serializes the contents of RF channels into XML. You can write the XML to a file that can be used at a later point on the same or other units. See below for an example of XML output.

##### ImportFromXML(a As String) As Boolean

Retrieves the RF channel contents stored as XML. The formatting of the XML is controlled using version tags.

Example:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="7">
<ChannelList class_id="0" tracking_level="0" version="0">
<ChannelCount>2</ChannelCount>
<Channel class_id="1" tracking_level="0" version="0">
<RfChannel>42</RfChannel>
<ModulationType>7</ModulationType>
<SpectralInversion>0</SpectralInversion>
<MajorChannelNumber>1</MajorChannelNumber>
<MinorChannelNumber>1</MinorChannelNumber>
</Channel>
<Channel>
<RfChannel>42</RfChannel>
<ModulationType>7</ModulationType>
<SpectralInversion>0</SpectralInversion>
<MajorChannelNumber>1</MajorChannelNumber>
<MinorChannelNumber>2</MinorChannelNumber>
</Channel>
</ChannelList> 
```

##### EnableScanDebug(filename As String) As Boolean

Allows all scan debugging to be written to a text file. By default, there is no debug output from a scan. You can close the debug file by passing an empty string.

Example:

```
c=CreateObject("roChannelManager")
c.EnableScanDebug("tmp:/scandebug.txt")

v = CreateObject("roVideoPlayer")
aa = CreateObject("roAssociativeArray")
aa["RfChannel"] = 12
aa["VirtualChannel"] = "24.1"
print v.PlayFile(aa)

c.EnableScanDebug("")
```

##### CreateChannelDescriptor(a As Object) As Object

Creates an associative array that can either be passed to the *roVideoPlayer.PlayFile()* method (to tune to a channel) or parsed for metadata. The generated channel object can be based on one of the following:

*   Index:
    

```
["ChannelIndex"] = 0
```

*   Virtual channel number as a string in an associative array:
    

```
["VirtualChannel"] = "12.1"
```

*   Channel name as a string:
    

```
["ChannelName"] = "KCBS"
```

> [!NOTE]
> Channels are sorted internally by virtual channel, so you could use a Channel Index script to implement standard channel up/down behavior.

These are the entries generated in the array:

*   VirtualChannel
    
*   ChannelName
    
*   CentreFrequency
    
*   ModulationType
    
*   VideoPid
    
*   VideoCodec
    
*   AudioPid
    
*   AudioCodec
    
*   SpectralInversion
    
*   ChannelMap
    
*   FirstRfChannel
    
*   LastRfChannel
    

The last three entries in this array allow you to use the same *roArray* as a parameter for `Scan()` and `PlayFile()`. The first and last RF channel values are set to the same value so that only one RF channel will be scanned. This kind of scan can be performed at the same time as playing the channel because it doesn’t require retuning.

Example:

```
c=CreateObject("roChannelManager")
aa=CreateObject("roAssociativeArray")
aa["ChannelMap"] = "QAM"
aa["FirstRfChannel"] = 10
aa["LastRfChannel"] = 15
c.Scan(aa)

cinfo  = CreateObject("roAssociativeArray")
cinfo["ChannelIndex"] = 0
desc = c.CreateChannelDescriptor(cinfo)
print desc

v = CreateObject("roVideoPlayer")
v.PlayFile(desc)
c.Scan(desc) 
```

### Asynchronous API

##### AsyncScan(parameters As roAssociativeArray) As Boolean

Begins a channel scan on the RF input and returns the results immediately. Otherwise, the behavior and parameters of this method are identical to `Scan()`. When completed or cancelled, `AsyncScan()` generates an *roChannelManagerEvent*, which supports *ifUserData* and outputs two types of event:

*   0 – Scan Complete: Generated upon the completion of a scan. No extra data is supplied.
    
*   1 – Scan Progress: Generated upon every tune that is performed during the scan. `GetData()` returns the percentage complete of the scan.
    

##### CancelScan() As Boolean

Cancels any asynchronous scans that are currently running. This method does not generate an *roChannelManagerEvent*.

Synchronous Example:

```
 c = CreateObject("roChannelManager")

' Scan the channels
aa  = CreateObject("roAssociativeArray")
aa["ChannelMap"] = "ATSC"
aa["FirstRfChannel"] = 12
aa["LastRfChannel"] = 50
c.Scan(aa)

' Start at the first channel
index = 0
cinfo  = CreateObject("roAssociativeArray")
cinfo["ChannelIndex"] = index
desc = c.CreateChannelDescriptor(cinfo)

' Play the first channel
v = CreateObject("roVideoPlayer")
v.PlayFile(desc)

' Play the second channel
index = index + 1
cinfo["ChannelIndex"] = index
desc = c.CreateChannelDescriptor(cinfo)
v.PlayFile(desc)
```

  
Asynchronous Example:

```
 c = CreateObject("roChannelManager")
p = CreateObject("roMessagePort")
c.SetPort(p)

' Scan the channels
aa  = CreateObject("roAssociativeArray")
aa["ChannelMap"] = "ATSC"
aa["FirstRfChannel"] = 12
aa["LastRfChannel"] = 50
c.AsyncScan(aa)

loop:
  msg = Wait(2000,p)
  if msg = 0 then goto scan_complete
  goto loop

scan_complete:
' Start at the first channel
index = 0
cinfo  = CreateObject("roAssociativeArray")
cinfo["ChannelIndex"] = index
desc = c.CreateChannelDescriptor(cinfo)

' Play the first channel
v = CreateObject("roVideoPlayer")
v.PlayFile(desc)

' Rescan the current channel, and update the
desc["ChannelStore"] = MERGE
c.Scan(desc)
```