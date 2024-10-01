# Autorun Files

As was covered, player provisioning consists of applying a Setup to the player which includes the installation of a Player App. The Player App must contain an *autorun.brs* file which, as an example, may instruct the player to display a specific .html file, either local on the player or on an external website. Alternatively, the autorun may instruct the player to check a particular URL for updated presentations and/or content and, if new files are available, download them and play them.

There are three autorun-related files:

*   autorun.brs (may also be referred to as “the autorun” or “autorun file”)
    
*   autorun.zip
    
*   autozip.brs
    

These have similar-sounding names, but each term has a different function so it’s important to not conflate the terms.

Upon bootup, the player searches for certain files. The player’s search follows a prescribed sequence as shown below.

![](./attachments/image-20230413-155338.png)

Players will search for storage devices in a [predefined order](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1967783990/Player+Storage#Storage-Device-Priority).

1.  The player first looks for an *autorun.brs* file in the root directory of the first storage device it encounters.
    
    1.  If found, *autorun.brs* is executed.
        
2.  If an *autorun.brs* file is not found, the player looks for an *autorun.zip* file in the same root directory.
    
    1.  If an *autorun.zip* file is found and it also contains within it an *autozip.brs* file, the player will unzip the *autorun.zip* file, in the process overwriting any existing files on the storage device.
        
    2.  The player will then reboot.
        
3.  If these files are not found on the first storage device, the player will repeat these steps on the next storage device, if available.
    

If an *autorun.zip* is not found on any of the storage devices, the player will query the BSN.cloud provisioning service to see if the player has previously been provisioned with BSN.cloud.

Both *autorun.brs* and *autozip.brs* must be written in BrightScript and be given the specific filenames indicated.

Additional information about these files can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673002/roBrightPackage#Using-roBrightPackage-for-Content-Updates).

Below are sample *autorun.brs* and *autozip.brs* files for reference.

## Sample autorun.brs

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

This autorun.brs file instructs the player to display a local HTML file, specifically, index.html:

```
Sub Main()
    'Create the BrightSign event handler.
    msgPort = CreateObject("roMessagePort")
    
    'Define the screen viewing area.
    r = CreateObject("roRectangle", 0, 0, 1920, 1080)
  
    'Set the URL where the presentation resides. This can be either local or external.
    config = {
      url: "file:///index.html",
    }

    'Create an HTML event since our presentation is an HTML file.
    h = CreateObject("roHtmlWidget", r, config)
    h.SetPort(msgPort)
    sleep(10000)
    h.Show()

    'Event loop to ensure that the script runs indefinitely
    while true
        msg = wait(0, msgPort)
        print "type(msg)=";type(msg)
        if type(msg) = "roHtmlWidgetEvent" then
            eventData = msg.GetData()
            if type(eventData) = "roAssociativeArray" and type(eventData.reason) = "roString" then
                print "reason = ";eventData.reason
                if eventData.reason = "load-error" then
                    print "message = ";eventData.message
                endif
            endif
        endif
    end while

End Sub
```

## Sample autozip.brs

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

This autozip.brs file instructs the player to unzip the autorun.zip file:

```
'name file autorun.zip
' Content update application

Sub Main()
    path$= FindDestPath()
    source$= FindSourcePath()
    package = CreateObject("roBrightPackage", source$+"autorun.zip")
    package.SetPassword("test")
    package.Unpack(path$)
    package = 0
    CreateDirectory(path$+"brightsign-dumps")
    CreateDirectory(path$+"pool")
    CreateDirectory(path$+"feed_cache")
    CreateDirectory(path$+"feedPool")

    DeleteFile(path$+"autozip.brs")
    DeleteFile(source$+"autorun.zip")
    a=RebootSystem()
End Sub

Function FindDestPath()
    if not IsFirmwareValid() then
        return "SD:/"
    end if

    destinationPaths = ["SSD:", "SD:", "USB1:"]
    for each destination in destinationPaths
        if IsMounted(destination) then
            return destination+"/"
        end if
    next
    return "unknown"
End Function

Function FindSourcePath()
    if not IsFirmwareValid() then
        return "SD:/"
    end if

    sourcePaths = ["USB1:", "SD:", "SSD:"]
    for each source in sourcePaths
        if IsMounted(source) and CheckFile(source+"/autorun.zip") then
            return source+"/"
        end if
    next
    return "unknown"
End Function

Function IsMounted(path as String)
    if CreateObject("roStorageHotplug").GetStorageStatus(path).mounted then
        return true
    end if

    return false
End Function

Function IsFirmwareValid()
    di = CreateObject("roDeviceInfo")
    return di.FirmwareIsAtLeast("7.0.60")
End Function

Function CheckFile(path as String)
    file = CreateObject("roReadFile", path)
    if type(file) = "roReadFile" then
        return true
    end if

    return false
End Function
```

[Next - Content Sources >](../brightsign-partner-packet/content-sources.md)