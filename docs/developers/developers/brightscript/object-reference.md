# Object Reference

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Interfaces and Methods](#interfaces-and-methods)
    *   [Example](#example)
*   [Classes](#classes)
    *   [Example](#example)
*   [Object and Class Name Syntax](#object-and-class-name-syntax)
*   [Zones](#zones)
*   [Event Loops](#event-loops)
    *   [Example](#example)

BrightSign players use a standardized library of BrightScript objects to expose functionality for software development. To publish a new API for interacting with BrightSign hardware, we create a new BrightScript object. 

The pages in this section provide definitions for objects that can be used in BrightScript. A brief description, a list of interfaces, and the member functions of the interfaces are provided for each object class. While most BrightScript objects have self-contained pages, some objects are grouped on the same page if they are closely related or depend on one another for functionality.

Here is a sample of objects that are used frequently when creating applications in BrightScript:

|     |     |
| --- | --- |
| [*roVideoMode*](./object-reference/presentation-and-widget-objects/rovideomode.md) | Configures video output and interacts with displays using CEC/EDID. |
| [*roRectangle*](./object-reference/presentation-and-widget-objects/rorectangle.md) | Used to define zones/widgets on the screen. This object is passed to many other objects to define their screen area, including *roVideoPlayer*, *roImagePlayer, roImageWidget*, *roHtmlWidget*, *roClockWidget*, and *roCanvasWidget.* |
| [*roVideoPlayer*](./object-reference/presentation-and-widget-objects/rovideoplayer.md) | Plays video files, streams, and HDMI® input. |
| [*roImagePlayer*](./object-reference/presentation-and-widget-objects/roimageplayer.md) | Displays images. |
| [*roHtmlWidget*](./object-reference/presentation-and-widget-objects/rohtmlwidget.md) | Displays local or remote HTML content using the Chromium rendering engine. |
| [*roNetworkConfiguration*](./object-reference/networking-objects/ronetworkconfiguration.md) | Used to configure Ethernet, WiFi, and local network parameters. |
| [*roDeviceInfo*](./object-reference/system-objects/rodeviceinfo.md) | Used to retrieve a wide array of system information, including model type, device serial number, and firmware version. |

## Interfaces and Methods

Every BrightScript object consists of one or more "interfaces." An interface consists of one or more "methods." For example, the *roVideoPlayer* object has several interfaces, including *ifMessagePort*. The interface *ifMessagePort* has one method: `SetPort()`. 

The abstract interface *ifMessagePort* is exposed and implemented by both the *roControlPort* and the *roVideoPlayer* objects. Once the SetPort() method is called, these objects will send their events to the supplied message port. This is discussed more in the Event Loops section below.

##### **Example**

```
p = CreateObject("roMessagePort")
video = CreateObject("roVideoPlayer") 
gpio = CreateObject("roControlPort", "BrightSign")
gpio.SetPort(p)
video.SetPort(p)  
```

The above syntax makes use of a shortcut provided by the language: The interface name is optional, unless it is needed to resolve name conflicts. For example, the following two lines of code carry out the exact same function:

```
gpio.SetPort(p)
gpio.ifMessagePort.SetPort(p)
```

BrightScript Objects consist *only* of interfaces, and interfaces define *only* methods. There is no concept of a "property" or variable at the object or interface level. These must be implemented as "set" or "get" methods in an interface.

## Classes

A *class name* is used to create a BrightScript object. For example, the class name for a video playback instance is *roVideoPlayer*, so, to initialize a video playback instance, you would use code similar to the following:

##### **Example**

```
video = CreateObject("roVideoPlayer")
```

Note that "video" can be any name that follows the syntax outlined in the next section.

## Object and Class Name Syntax

Class names have the following characteristics:

*   Must start with an alphabetic character (a – z).
    
*   May consist of alphabetic characters, numbers, or the "\_" (i.e. underscore) symbol.
    
*   Are not case sensitive.
    
*   May be of any reasonable length.
    

## Zones

With the BrightSign Zones feature, you can divide the screen into rectangles and play different content in each rectangle.

Depending on the BrightSign model, zones can contain video, images, HTML content, audio, a clock, or text. 4Kx42, XDx32, and XDx30 models can display two video zones on screen, while the HDx22, HDx20, and LSx22 models can only display one. There can be multiple zones of other types on the screen. A text zone can contain simple text strings or can be configured to display an RSS feed in a ticker-type display. 

As of firmware 6.0.x, zone support is enabled by default. When zones are enabled, the image layer is on top of the video layer by default. The default behavior can be modified using the*roVideoMode.SetGraphicsZOrder()* method. 

Zone support can be disabled by calling `EnableZoneSupport(false)`. When zones are not enabled, the image layer is hidden whenever video is played, and the video layer is hidden whenever images are played.

## Event Loops 

When writing anything more than a very simple script, an "event loop" will need to be created. Event loops typically have the following structure:

1.  Wait for an event.
    
2.  Process the event.
    
3.  Return to step 1.
    

An event can be any number occurrences: a button has been pressed; a timer has been triggered; a UDP message has been received; a video has finished playing back; etc. By convention, event scripting for BrightScript objects follows this work flow:

1.  An object of the type *roMessagePort* is created by the script.
    
2.  Objects that can send events (i.e. those that support the *ifMessagePort/ifSetMessagePort* interface) are instructed to send their events to this message port using the `SetPort()` method. You can set up multiple message ports and have each event go to its own message port, but it is usually simpler to create one message port and have all the events sent to this one port.
    
3.  The script waits for an event using the built-in `Wait()` statement (or the *ifMessagePort.WaitMessage()* method).
    
4.  If multiple object instances are assigned to the same message port, the script determines from which instance the event originated, then processes it. The script then jumps back to the `Wait()` statement.
    

##### **Example**

```
'Listens for UDP messages on two different ports and displays the image file requested in the UDP message body.
mp = CreateObject("roMessagePort")

udp1 = CreateObject("roDatagramReceiver", 3000)
udp1.SetPort(mp)
udp1.SetUserData("port 3000")
 
udp2 = CreateObject("roDatagramReceiver", 5000)
udp2.SetPort(mp)
udp2.SetUserData("port 5000")
 
r = CreateObject("rorectangle",0, 0, 1920, 1080)
img = CreateObject("roImagePlayer")
img.SetRectangle(r)

loop:
event = Wait(0, mp)
if type(event) = "roDatagramEvent"
	print "Image play command received on " + event.GetUserData() + "."
	img = DisplayFile("SD:/" + event.GetString())
	endif
endif
goto loop
```