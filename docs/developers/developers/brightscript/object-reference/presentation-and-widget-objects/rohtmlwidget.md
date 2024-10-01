# roHtmlWidget

This object embeds the Chromium HTML rendering engine, which can be rendered at full screen or as a widget. You can display multiple *roHtmlWidget* instances at the same time. The JavaScript equivalent is [htmlwidget](../../../../developers/player-apis/javascript-apis/htmlwidget.md).

> [!TIP]
> **Tip**
> Use the [*roKeyStore*](../../object-reference/networking-objects/rokeystore.md) object to provide client certificates for websites. Use the [*roVirtualMemory*](../../object-reference/hashing-and-storage-objects/rovirtualmemory.md) object to set up a virtual memory repository for Chromium.

## Object Creation 

The *roHtmlWidget* object is initialized with an *roRectangle* object, which specifies the size and positioning of the widget on the screen, and an optional associative array, which defines properties for the widget. 

```
CreateObject("roHtmlWidget", rect As roRectangle, properties As roAssociativeArray)
```

The properties of an *roHtmlWidget* instance can be set with an associative array at initialization or with equivalent methods after initialization. Because many *roHtmlWidget* properties cannot be changed without reloading the page (and can produce unpredictable results if changed while the page is running), we recommend setting properties at initialization when possible, rather than using the equivalent methods.

> [!CAUTION]
> **Important**
> Defining initialization properties for an *roHtmlWidget* instance disables some methods for that instance (e.g. `SetTransform()`, `AddFont()`, `SetUserStylesheet()`). See the “Available Methods with Initialization” section below for a list of available methods.

## Initialization Parameters

The associative array passed during initialization can have the following parameters: 

`nodejs_enabled` bool: Enables [Node.js®](../../../../developers/html-development/nodejs.md) on the widget. This value is `false` by default.

> [!NOTE]
> Reloading a page which has Node.js enabled can be classified as an undefined behavior. The recommended method for restarting a Node instance is to destroy and rebuild the *roHtmlWidget*

`focus_enabled` bool: Enables focus for mouse/touchscreen events. This value is `true` by default.

`mouse_enabled` bool: Enables mouse/touchscreen events. This value is `false` by default.

`scrollbar_enabled` bool: Enables automatic scrollbars for content that does not fit into the viewport. This value is `false` by default.

The browser defaults to desktop-style scrollbars, but they can be [configured for mobile style](../../../../developers/html-development/displaying-html-without-brightauthor.md) as well.

`pinch_to_zoom_enabled` bool: Enables pinch-to-zoom functionality. This value is `false` by default.

`force_gpu_rasterization_enabled` bool: Enables GPU rasterization for HTML graphics. By default, the decision to use GPU rasterization is based on [internal Chromium logic](https://www.chromium.org/developers/design-documents/chromium-graphics/how-to-get-gpu-rasterization).

> [!NOTE]
> This setting has been deprecated. As of OS8, GPU rasterization is enabled by default and setting this property has no effect.

`canvas_2d_acceleration_enabled` bool: Enables 2D canvas acceleration. This will improve the framerate of most HTML pages that use 2D animations, but can cause out-of-memory issues with pages that use a large number of off-screen canvas surfaces.

> [!NOTE]
> This setting has been deprecated. As of OS8, Canvas acceleration is enabled by default and can be disabled by setting this flag to `false`.

`javascript_enabled` bool: Enables JavaScript on the widget. This value is `true` by default.

`brightsign_js_objects_enabled` bool: Enables [BrightScript-JavaScript objects](../../../../developers/player-apis/brightscript-javascript-objects.md). This value is `false` by default.

In OS 8.2.55.4 and later, html widgets that are loaded from HTTP/HTTPS protocols do not share the same local storage database (html widgets that are loaded via file protocol act as they did in previous releases). These flags allow you to change the default behavior of widgets loaded through HTTP/HTTPS from "unshared" to "shared", or to change the default behavior of widgets with locally loaded files to "unshared" from "shared":

`force_shared_storage` bool: Allows HTML widgets loaded via HTTP/HTTPS protocol to share local storage if they are loaded from the same domain.

`force_unshared_storage` bool: Prevents HTML widgets loaded via FILE protocol from sharing storage.

`transform` string: Sets the screen orientation of content in the widget (note that the coordinates and dimensions of the *roRectangle* containing the widget are not affected by rotation). The following values are accepted:

*   `"identity"`: There is no transform (i.e. the widget content is oriented as landscape). This is the default setting.
    
*   `"rot90"`: The widget content is rotated to portrait at 90 degrees (clockwise).
    
*   `"rot180"`: The widget content is rotated to portrait at 180 degrees (clockwise).
    
*   `"rot270"`: The widget content is rotated to portrait at 270 degrees (clockwise).
    

`user_agent` string: Modifies the default user-agent string for the *roHtmlWidget* instance.

`url` string: The URL to use for display. See the [SetUrl()](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-SetURL(URLAsString)AsBooleanseturl()) entry below for more information on using URIs to access files from local storage.

`language` string: Specifies the language to load the web page in.

`user_stylesheet` string: Applies the specified user stylesheet to pages in the widget. The parameter is a [URI](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-SetURL(URLAsString)AsBooleanseturl()) specifying any `file:` resource in the storage. The stylesheet can also be specified as inline data.

`hwz_default` string: Specifies the default [HWZ](../../../../developers/html-development/html-video.md) behavior. This value is `off` by default. To enable it, set it to `on`.

`storage_path` string: Creates a "Local Storage" subfolder in the specified directory. This folder is used by local storage applications such as the JavaScript *storage* class. 

`storage_quota` string or double: Sets the total size (in bytes) allotted to all local storage applications (including IndexedDB). A BrightScript integer is only guaranteed to be able to represent a count of bytes up to 2GB so avoid using integers when calculating the size: Use float or double instead since they can represent values over 2GB (string can also be used but is not recommended). If the storage path is specified without a storage quota, Chromium defaults to reserving 1GB plus 10% of the total size of the storage device.

`port` roMessagePort: Configures the message port to which the *roHtmlWidget* instance will send events. When using initialization parameters, the `port` parameter should be used instead of the `SetPort()` method to ensure the script can catch `load-started`, `load-finished`, and `load-error` events.

`fonts` roArray: Specifies a list of font files that can be accessed by the webpage. Font files are specified as an array of string filenames. Supported font types include TrueType Font files (*.ttf*) and Web Open Font files (*.woff*, *.woff2*).

`pcm_audio_outputs` roArray: Configures the PCM audio output for the HTML widget. Outputs are specified as an array of strings, each string being the name of an output. (See [*roAudioOutput* documentation](../presentation-and-widget-objects/roaudiooutput.md) for a list of acceptable names.)

`compressed_audio_outputs` roArray: Configures compressed audio output (e.g. Dolby AC3 encoded audio) for the HTML widget. Outputs are specified as an array of *roAudioOutput* instances. 

`multi_channel_audio_outputs` roArray: Configures multi-channel audio output for the HTML widget. Outputs are specified as an array of *roAudioOutput* instances.

`inspector_server` roAssociativeArray: Configures the [Chromium Inspector](../../../../developers/html-development/html-best-practices.md) for the widget.Starting in BrightSign OS 8.5.31 you will need to also set the enable\_web\_inspector registry key (in the "html" section) to enable the JavaScript console. In “enable\_web\_inspector”, "1" will allow the inspector and "0" or not present will disable it.  A reboot will be needed for these changes to take effect (if you enable/disable this through the LDWS UI it may trigger a reboot to apply the changes).

*   `ip_addr` string: The Inspector IP address. This value is useful if the player is assigned more than one IP address (i.e. there are multiple network interfaces) and you wish to limit the Inspector server to one. The default value is `"0.0.0.0"`, which allows the Inspector to accept connections using either IP address.
    
*   `port` int: The port for the Inspector server
    

> [!CAUTION]
> **Important**
> For security reasons, **enable\_web\_inspector** should only be used in non-production presentations. Make sure to disable JavaScript console before publishing to a production environment. In the Chromium version found in BOS 8.5.31 and beyond, the JavaScript console will log information in memory even when you are not connected to the inspector. This will consume memory until the player runs out, which will result in a crash.

  

  

`security_params` roAssociativeArray: Enables or disables Chromium security checks for cross-origin requests, local video playback from HTTP, etc. 

*   `websecurity` bool: Enables Chromium security checks for cross-origin requests. 
    
*   `camera_enabled` bool: Enables webpage access to USB cameras connected to the player (access is disabled by default). This allows support for WebRTC applications.
    
*   `insecure_https_enabled` bool: Instructs the widget to ignore security errors when connecting to insecure HTTPS hosts (insecure HTTPS is disabled by default). Enabling this feature makes the player insecure; it is not suitable for production environments and should only be used for testing.\]
    
*   `audio_capture_enabled` bool: Gives access to audio input devices and lets Chromium enumerate all audio input and output devices
    

With BOS 8.2 and later (Chromium69 and later), several new CORS checks have been added: `security_params.websecurity` or `enableSecurity(false)` do not disable all these checks. Use the following registry setting instead:

`registry write html disable-web-security 1`

To write this to the registry using [roRegistrySection](../../object-reference/hashing-and-storage-objects/roregistrysection.md):

```
RegHtml = CreateObject("roRegistrySection", "html")
RegHtml.Write("disable-web-security", "1")
RegHtml.Flush()
```

This flag will take effect on all `roHtmlWidget` instances, as opposed to previous flags which are only effective on the instance they are called on.

> [!NOTE]
> The `camera_enabled` parameter is currently supported on the XTx44/43, XDx34/33, HDx24/23, LS424/LS423, and 4Kx42 models.

`javascript_injection` roAssociativeArray: Specifies JavaScript code to inject at different initialization points (JavaScript code can also be injected during runtime using the `InjectJavaScript()` method). The associative array can contain three parameters (described below). Each parameter value is an array of associative arrays, each containing a single key/value pair. The array must contain a `source` key. The `source` value is a string that can contain any of the following: pure JavaScript code, a path to a JavaScript file, or a base64-encoded string (i.e. beginning with  `data:text/javascript;charset=utf-8;base64,` ). Mutliple `source` keys can be included, but the load order will be unpredictable. The array can also contain the optional `world` key, which can be assigned one of the following values: `"application"`, `"user"`, or `"main"`(see [this page](http://doc.qt.io/archives/qt-5.6/qwebenginescript.html#ScriptWorldId-enum) for more details); if the `world` parameter is not included in the array, `"application"` is selected by default.

*   `document_creation`: The script will run as soon as the document is created. This behavior is not suitable for any DOM operation.
    
*   `document_ready`: The script will run as soon as the DOM is ready. This behavior is equivalent to the `DOMContentLoaded` event firing in JavaScript. 
    
*   `deferred`: The script will run when the page load finishes.
    

```
config = {
      javascript_injection: { 
         document_creation: [{source: "0.js" }], 
         document_ready: [{source: "1a.js" }, {source: "1b.js" }], 
         deferred: [{source: "2.js" }] 
      },
      url: "..."
   }
```

`assets` roArray: Allows the *roHtmlWidget* instance to [access one or more asset pools](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-MapFilesFromAssetPool(asset_poolAsroAssetPool,asset_collectionAsroAssetCollection,pool_prefixAsString,uri_prefixAsString)AsBooleanmapfilesfromassetpool). If a file exists in multiple specified asset pools, the asset pool with the lowest index in the array has precedence. Each array entry is an associative array containing information about an asset pool:

*   `pool` roAssetPool: An asset pool containing files 
    
*   `collection` roAssetCollection: A manifest identifying the files in the pool
    
*   `uri_prefix` string: The URI prefix of the webpage resources to retrieve from the pool
    
*   `pool_prefix` string: The pool prefix that will replace the URI prefix when looking up the resource in the pool
    

## ifHtmlWidget

##### GetFailureReason() As String

Gives more information when a member function returns `false`.

##### Hide() As Boolean

Hides the widget.

##### Show() As Boolean

Shows the widget.

##### raise()

Raises the html widget above all other graphical elements on screen (including other html widgets).

##### lower()

Lowers the html widget below all graphical elements on screen.

##### SetRectangle(r As roRectangle) As Boolean

Changes the size and positioning of the widget rectangle using the passed *roRectangle* object.

##### SetURL(URL As String) As Boolean 

Displays content from the specified URL. When using this method to retrieve content from local storage, specify the file location as follows: `"file:/<drive>:/<directory>/<filename>"`. For example, an *index.html* file in the "Content" folder on the SD card can be selected with the string `"file:/SD:/Content/index.html"`. You can also omit the drive specification to select the currently active drive (i.e. whichever drive the current autorun as loaded from).

##### AddAuthenticationCredentials (url As String, username As String, password As String) As Boolean

Tells Chromium to use  the specified username and password when retrieving the given URL.

##### MapFilesFromAssetPool(asset\_pool As roAssetPool, asset\_collection As roAssetCollection, pool\_prefix As String, uri\_prefix As String) As Boolean 

Sets the mapping between the URL space and the pool files. HTML content that has been deployed via BrightAuthor will typically reside in the pool and have encrypted SHA1-based filenames. A mapping mechanism is required to allow any relative URIs contained in the HTML content to continue working and to locate the appropriate resources in their respective pool locations.

You can use this method to bind part of the resource URI space onto pool locations. This method accepts the following arguments: an *roAssetPool* object containing assets, an *roAssetCollection* object identifying the assets, and two semi-arbitrary strings (URI\_PREFIX and POOL\_PREFIX).

Any URI in the form `"file:/[URI_PREFIX][RESOURCE_ID]"` will be rewritten into the form `"[POOL_PREFIX][RESOURCE_ID]"`. It will then be located in the pool as if that name had been passed to the *roAssetPoolFiles.GetPoolFilePath()* method. This binding occurs for every instance of *roHtmlWidget*, so different mappings can be used for different bundles of content.

##### SetZoomLevel(scale\_factor as Float) As Boolean

Adjusts the scale factor for the displayed page (the default equals 1.0).

##### EnablePinchToZoom(enable as Boolean) As Boolean

Enables or disables pinch-to-zoom functionality, which is disabled by default.

##### EnableSecurity(enable As Dynamic) As Boolean 

Deprecated. Use [security\_params](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5BroAssociativeArray%5Dsecurity_params) in initialization parameters instead.

##### EnableMouseEvents(enable As Boolean) As Boolean

Deprecated. Use [mouse\_enabled](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bboolean%5Dmouse_enabled) in initialization parameters instead.

##### SetPortrait(portrait\_mode As Boolean) As Boolean

Deprecated. Use [transform](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bstring%5Dtransformtransform) in initialization parameters instead.

##### SetTransform(transform As String) As Boolean

Sets the screen orientation of content in the widget (note that the coordinates and dimensions of the *roRectangle* containing the widget are not affected by rotation). This method accepts the following strings:

*   `"identity"`: There is no transform (i.e. the widget content is oriented as landscape). This is the default setting.
    
*   `"rot90"`: The widget content is rotated to portrait at 90 degrees (clockwise).
    
*   `"rot270"`: The widget content is rotated to portrait at 270 degrees (counter-clockwise).
    

> [!NOTE]
> The JavaScript `onload` event will report landscape dimensions for a window that is rotated with the `SetPortrait()` or `SetTransform()` method. If your application relies on the `onload` event to retrieve window dimensions, we recommend instead using the [roHtmlWidget#transform](https://brightsign.atlassian.net/wiki/pages/resumedraft.action?draftId=370672896#roHtmlWidget-transform) initialization parameter, which ensures the HTML window is initialized with portrait dimensions.

##### SetAlpha(alpha As Integer) As Boolean

Sets the overall alpha level for the widget (the default equals 255).

##### EnableScrollbars(scrollbars As Boolean) As Boolean

Deprecated. Use [scrollbar\_enabled](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bboolean%5Dscrollbar_enabled) in initialization parameters instead.

##### AddFont(filename As String) As Boolean

Deprecated. Use [fonts](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5BroArray%5Dfonts) in initialization parameters instead.

##### SetPcmAudioOutputs(outputs As roArray) As Boolean

Deprecated. Use [pcm\_audio\_outputs](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5BroArray%5Dpcm_audio_outputs) in initialization parameters instead.

##### SetCompressedAudioOutputs(outputs As roArray) As Boolean

Deprecated. Use [compressed\_audio\_outputs](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5BroArray%5Dcompressed_audio_outputs) in initialization parameters instead.

##### SetMultichannelAudioOutputs(outputs As roArray) As Boolean

Deprecated. Use [multi\_channel\_audio\_outputs](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5BroArray%5Dmulti_channel_audio_outputs) in initialization parameters instead. 

##### SetHWZDefault(default As String) As Void 

Deprecated. Use [hwz\_default](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bstring%5Dhwz_default) in initialization parameters instead.

##### SetVideoPlayerDefaults(defaults As roAssociativeArray) As Boolean

Sets default playback settings for `<video>` elements in the widget. Available parameters are identical to the [*roVideoPlayer.PlayFile()*](../presentation-and-widget-objects/rovideoplayer.md) method. Default settings will be overwritten by parameters specified in individual `<video>` elements.

##### ForceGpuRasterization(enable As Boolean) As Boolean

Deprecated. As of OS8, GPU rasterization is enabled by default and calling this method has no effect.

##### EnableCanvas2dAcceleration(enable As Boolean) As Boolean

Deprecated. Use [canvas\_2d\_acceleration\_enabled](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bboolean%5Dcanvas_2d_acceleration_enabled) in initialization parameters instead.

##### SetUserStylesheet(URI As String) As Boolean 

Deprecated. Use [user\_stylesheet](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bstring%5Duser_stylesheet) in initialization parameters instead.

##### FlushCachedResources() As Boolean

Discards any resources that Chromium has cached in memory.

> [!CAUTION]
> Changing the storage path after an URL is loaded can cause the storage database to be irretrievably lost and/or damaged. Users should avoid using SetLocalStorageDir, SetWebDatabaseDir and SetAppCacheDir APIs when writing BrightScript applications.
> Since the BOS 6.0 release, BrightSign uses a single storage path for WebDatabase, LocalStorage and AppCache. This should be set by the `storage_path` parameter in roHtmlWidget static initialization parameters.
> With the BOS 8.2.35.4 release, if SetLocalStorageDir, SetWebDatabaseDir, or SetAppCacheDir are called, roHtmlWidget will use the path as the first one that is set. This directory will only set once and will be used for the subsequent use of roHtmlWidget as well.

##### SetLocalStorageDir(file\_path As String) As Boolean

Configures the HTML storage path. This method takes effect when a new *roHtmlWidget* instance is created; it doesn't apply to the *roHtmlWidget* instance on which it is called.

> [!NOTE]
> As of OS8, the `SetLocalStorageDir()`, `SetWebDatabaseDir()`, and `SetAppCacheDir()` methods all configure the same HTML database. See the [HTML Best Practices](../../../../developers/html-development/html-best-practices.md) page for more details.

##### SetWebDatabaseDir(file\_path As String) As Boolean

Configures the HTML storage path. See the `SetLocalStorageDir()` entry above for details.

This method takes effect when a new *roHtmlWidget* instance is created; it doesn't apply to the *roHtmlWidget* instance on which it is called.

##### SetAppCacheDir(file\_path As String) As Boolean 

Configures the HTML storage path. See the `SetLocalStorageDir()` entry above for details.

This method takes effect when a new *roHtmlWidget* instance is created; it doesn't apply to the *roHtmlWidget* instance on which it is called.

##### SetLocalStorageQuota(maximum As Dynamic) As Boolean

Sets the total size (in bytes) for all persistent HTML storage on the player. This method can accept a string, double, or integer. A number literal can only represent byte numbers up to 2GB; use a string to specify larger amounts. If the storage path is specified without a storage quota, Chromium defaults to reserving 1GB plus 10% of the total size of the storage device.

This method takes effect when a new *roHtmlWidget* instance is created; it doesn't apply to the *roHtmlWidget* instance on which it is called.

> [!NOTE]
> As of OS8, the `SetLocalStorageQuota()`, `SetWebStorageQuota()`, and `SetAppCacheQuota()` methods all configure a single storage quota, which applies to all persistent HTML storage on the player. See the [HTML Best Practices](../../../../developers/html-development/html-best-practices.md) page for more details.

##### SetWebDatabaseQuota(maximum As Dynamic) As Boolean

Sets the total size (in bytes) for all persistent HTML storage on the player. See the `SetLocalStorageQuota()` entry above for details.

This method takes effect when a new *roHtmlWidget* instance is created; it doesn't apply to the *roHtmlWidget* instance on which it is called.

##### SetAppCacheSize(maximum As Integer) As Boolean

Sets the maximum size (in bytes) for the application cache. Changing the storage size of the application cache will clear the cache and rebuild the cache storage. Depending on database-specific attributes, you will only be able to set the size in units that are equal to the page size of the database, which is established at creation. These storage units will occur only in the following increments: 512, 1024, 2048, 4096, 8192, 16384, 32768.

##### EnableJavaScript(enable As Boolean) As Boolean

Deprecated. Use [javascript\_enabled](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bboolean%5Djavascript_enabled) in initialization parameters instead.

##### AllowJavaScriptURLs(url\_collection As roAssociativeArray)

Deprecated.  If `javascript_enabled` is set to `true` in the initialization parameters, JavaScript objects are enabled for all sites.

##### PostJSMessage(data As roAssociativeArray) As Boolean

Posts a collection of key:value pairs to the *BSMessagePort* JavaScript class (see the [JavaScript Objects for BrightScript tech note](https://docs.brightsign.biz/display/DOC/BSMessagePort) for more details). This method does not support passing nested associative arrays.

##### InjectJavaScript(code As String) As Boolean

Immediately injects a user script into the JavaScript engine. The passed string can contain any of the following: pure JavaScript code, a path to a JavaScript file, or a base64-encoded string (i.e. beginning with  `data:text/javascript;charset=utf-8;base64,` ). 

This method can be used to simulate the `bind_ready` option:

```
if type(event) = "roHtmlWidgetEvent" then               
   if event.GetData().reason = "load-finished" then
      h.InjectJavascript("fillPasswordFields()")      
  end if
end if
```

> [!NOTE]
> Changing the DOM is only possible at `bind_dom_loaded` and `bind_ready`. Also, since JavaScript is only guaranteed to be ready at `bind_ready`, your callbacks must use this event if they invoke any global functions.

##### StartInspectorServer(port As Integer) As Boolean

Deprecated. Use [inspector\_server](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5BroAssociativeArray%5Dinspector_server) in initialization parameters instead.

##### SetUserAgent(user\_agent As String) As Boolean

Deprecated. Use [user\_agent](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bstring%5Duser_agent) in initialization parameters instead.

##### GetUserAgent() As String

Returns the currently active user-agent string for the *roHtmlWidget* instance.

##### SetUserAgentSuffix(suffix As String) As Boolean

Deprecated. Use [user\_agent](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bstring%5Duser_agent) in initialization parameters instead.

##### SetProxy(proxy as String) As Boolean

Sets the name or address of the proxy server that the *roHtmlWidget* instance will use to make HTTP requests. This method takes effect immediately. It does not affect network operations performed by other components in the firmware. The string can be used to specify either the proxy URL or the location of a *.pac* proxy file:

*   **Proxy URL**: The proxy address should be formatted as "[http://user:password@hostname:port](http://user:password@hostnameport)". The hostname can contain up to four "\*" characters; each "\*" character can be used to replace one octet from the current IP address. For example, if the IP address is currently 192.168.1.2, and the proxy is set to "proxy-\*-\*", then the player will attempt to use a proxy named "proxy-192.168".
    
*   **Proxy File**: The *.pac* proxy file can be located on either the local file system or the network. If the file is local, there are no file-name restrictions; if the file is located on the network, the file name should have a *.pac* extension. If the URL is a hostname only, it will be considered a proxy-server address rather than a file URL.
    

> [!TIP]
> **Example**
>  The following are examples of valid location formats for *.pac* files:
> *   [file:///storage/sd/asset\_pool/a/b/ababababababa](#)
>     
> *   [http://example:8080/setup/proxy.pac](http://example:8080/setup/proxy.pac)
>     
> *   [https://example/encrypted/proxy.pac](https://example/encrypted/proxy.pac)
>     
> *   [https://example:433/encrypted/proxy.pac](https://example:433/encrypted/proxy.pac)
>     
> *   [ftp://example/files/proxy.pac](ftp://example/files/proxy.pac)
>     
> *   [file:///storage/sd/myproxypac.txt](#)

##### SetProxyBypass(hostnames As String) As Boolean

Exempts the specified hosts from the proxy configuration on the *roHtmlWidget* instance. The passed array should consist of one or more hostnames. The player will attempt to reach the specified hosts directly rather than using the proxy that has been specified with the `SetProxy()` method. For example, the hostname "[example.com](http://example.com)" would exempt "[example.com](http://example.com)", "[example.com](http://example.com):80", and "[www.example.com](http://www.example.com)" from the proxy setting.

##### AddProxyAuthenticationCredentials(hostname As String, username As String, password As String)

Allows the user to set up one or more proxies. If proxy pac files are included, this method must be used to specify authentication parameters.

##### roHtmlWidget.acceptdialog(response as String) 

Accept any dialog request with the given string, if there is any such request. This parameter was added in BOS 8.5.16.

##### roHtmlWidget.rejectdialog()

Reject any dialog request. This parameter was added in BOS 8.5.16.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roHtmlWidgetEvent* to the attached message port.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## Available Methods with Initialization 

If the properties of an *roHtmlWidget* object are configured at initialization, most *ifHtmlWidget* methods will be disabled. However, the following methods are still functional:

*   `Hide()`
    
*   `Show()`
    
*   `EnablePinchToZoom()`
    
*   `FlushCachedResources()`
    
*   `SetUserAgent()`
    
*   `GetUserAgent()`
    
*   `SetUserAgentSuffix()`
    
*   `PostJSMessages()`
    

## Examples 

The following examples show how to use either an associative array or object methods to configure an *roHtmlWidget* instance using local storage to cache the files.

Note that these techniques are mutually exclusive.

Example (with initialization properties):

```
x = 0
y = 0
width = 1920
height = 1080
url = "http://www.brightsign.biz"
 
rect = CreateObject("roRectangle", x, y, width, height)
 
config = {
url: url,
mouse_enabled: true,
storage_path: "/local/",
}
 
html = CreateObject("roHtmlWidget", rect, config)
 
html.Show()
```

Example (with methods):

```
x = 0
y = 0
width = 1920
height = 1080
url = "http://www.brightsign.biz"

rect = CreateObject("roRectangle", x, y, width, height)
html = CreateObject("roHtmlWidget", rect)


html.SetUrl(url)
html.EnableMouseEvents(true)
html.SetLocalStorageDir("/local/")
html.Show()
```