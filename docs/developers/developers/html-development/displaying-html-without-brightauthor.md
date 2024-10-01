# Displaying HTML without BrightAuthor

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Simple Webpage Script](#simple-webpage-script)
*   [Portrait Orientation](#portrait-orientation)
*   [Displaying Scrollbars](#displaying-scrollbars)
*   [Mobile Scrollbars](#mobile-scrollbars)

There are two methods to display HTML without BrightAuthor. 

*   You can play an HTML page from the local storage without an autorun script by placing the  *index.html* file (along with other files and folders containing the page content) into the root folder of the player storage.
    
*   You can use BrightScript to display local or remote HTML content. The sections below pertain to using the [*roHtmlWidget*](../../developers/brightscript/object-reference/presentation-and-widget-objects/rohtmlwidget.md) BrightScript object to display HTML. To learn more about BrightScript, see the [BrightScript](../../developers/brightscript.md) section.
    

## Simple Webpage Script

The simple script outlined below displays a webpage stored on a remote server. Save this script as an *autorun.brs* file, place it on an SD card, and publish it to the player.

If you want to display a webpage located on local storage, replace the "http://www.brightsign.biz" URL on line 4 with the filename of the .html file: `"file:///mytestpage.html"`

Notice that the script has a `Sleep(10000)` line. This line delays loading of the web URL–this is necessary to compensate for connection delays that may occur on your network. If you don’t use this script, the BrightSign player may not connect in time to load the page, resulting in a “cannot resolve host” error, which indicates that the player does not have an Internet connection. In certain network configurations, especially when the player utilizes DHCP, you may need to increase the sleep amount (in milliseconds) to give the player more time to establish a connection before loading the page.

Parameters for the *roHtmlWidget* are defined in an associative array, which is then passed during object creation. See the [*roHtmlWidget* page](../../developers/brightscript/object-reference/presentation-and-widget-objects/rohtmlwidget.md) for more information on creating and configuring an HTML widget. 

```
Sub Main()
msgPort = CreateObject("roMessagePort")
r = CreateObject("roRectangle", 0, 0, 1920, 1080)
 
config = {
url: "http://www.brightsign.biz",
}
h = CreateObject("roHtmlWidget", r, config)
h.SetPort(msgPort)
sleep(10000)
h.Show()
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

## Portrait Orientation

To rotate the contents of an HTML page, include the `transform` parameter when creating the *roHtmlWidget* object: For clockwise portrait orientation, use `transform:"rot90"`; for counter-clockwise portrait orientation, use `transform:"rot270"`. If you're using the above simple webpage script, you can add this parameter to the `config` associative array on line 7.

## Displaying Scrollbars

Browser scrollbars are disabled by default. They can be enabled by including the `scrollbar_enabled:true` parameter when creating the *roHtmlWidget* object. If you're using the above simple webpage script, you can add `scrollbar_enabled:true` to the `config` associative array on line 7.

You can also enable scrollbars using CSS (for example, by referencing the simple CSS file below).

[ForceScrollbars.css](./attachments/ForceScrollbars.css)

## Mobile Scrollbars

Browser scrollbars default to desktop style (i.e. more prominent and visible at all times). You can configure the Chromium instance for mobile-style scrollbars (i.e. less prominent and only visible when scrolling) by writing the `overlay-scrollbar` entry to the `html` section of the registry.

```
htmlRegistry = CreateObject("roRegistrySection", "html")
htmlRegistry.Write("overlay-scrollbar", "1")
```