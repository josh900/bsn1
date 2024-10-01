# htmlwidget

The *htmlwidget object* allows you to instantiate additional HTML browsers. 

**htmlwidget IDL**

```
[
    Constructor(HtmlWidgetParams params)
] interface HtmlWidget {
    void postMessage(Object data);
    void close();
};
  
interface HtmlWidgetParams {
    attribute HtmlWidgetRect rect;
    attribute String url;
    [optional] attribute NodeParams node;
    [optional] attribute JavascriptInjection javascriptInjection;
    [optional] attribute bool bsObjects;
    [optional] attribute Storage storage;
    [optional] attribute String inspectorServer;
    [optional] attribute bool inputEnabled;
    [optional] attribute Security security;
    [optional] attribute String transform;
    [optional] attribute String hwzDefault;
    [optional] attribute bool interceptReloads;
};
  
interface HtmlWidgetRect {
    attribute long x;
    attribute long y;
    attribute long width;
    attribute long height;
};
  
interface NodeParams {
    attribute bool enabled;
    [optional] attribute Array<String> arguments;
};
  
interface JavascriptInjection {
    [optional] attribute JavascriptInjectionDetailList documentCreation;
    [optional] attribute JavascriptInjectionDetailList documentReady;
    [optional] attribute JavascriptInjectionDetailList deferred;
};
  
interface JavascriptInjectionDetail {
    [optional] attribute String world;
    [optional] attribute String source;
    [optional] attribute String uri;
    [optional] attribute String code;
};
  
interface Storage {
    attribute String path;
    attribute long quota;
    attribute bool forceSharedStorage;
    attribute bool forceUnsharedStorage;
};
  
interface Security {
    [optional] attribute bool insecureOriginEnabled;
    [optional] attribute bool cameraEnabled;
    [optional] attribute bool desktopCaptureEnabled;
    [optional] attribute bool audioCaptureEnabled;
    [optional] attribute bool insecureHttpsEnabled;
};
```

## Object Creation

To create a *htmlwidget* object first load the `brightsign/htmlwidget` module using the `require()` method. Then create an instance of the *htmlwidget* class. 

```
var HtmlWidgetClass = require("@brightsign/htmlwidget");
var htmlwidget = new HtmlWidgetClass({ rect:{x: 0, y:0, w: 640, h: 480 }, url: "https://brightsign.biz" });
```

## HtmlWidget

##### postMessage()

```
void postMessage(Object data)
```

Sends an asynchronous message to the child browser process. If the child process has an @brightsign/messageport object open, this message will generate a "bsmessage" event on that object. The payload can be any JavaScript object but must be only one level deep (that is, it cannot include other nested objects).

##### close()

```
void close()
```

Shuts down the child browser process. This is equivalent to calling *window.close()* from inside the child browser.  Node.js® parent processes won't exit automatically and the HTML widget can't be garbage collected until the widget is closed.

## HtmlWidgetParams

This interface contains the HTML widget parameters.

*   `rect` HtmlWidgetRect: Contains the set parameters of the size and positioning of the widget. 
    
*   `url` String: The URL to use for display. 
    
*   `node` NodeParams optional: Contains the parameters used to specify added Node.js functionality. 
    
*   `javascriptInjection` JavascriptInjection optional: Contains the parameters that specify JavaScript code to inject at different initialization points.
    
*   `bsObjects` bool optional: Enables or disables [BrightScript-Javascript Objects](https://docs.brightsign.biz/display/DOC/BrightScript-JavaScript+Objects). This value is disabled by default. 
    
*   `storage` Storage optional:  Used to configure HTML storage.
    
*   `inspectorServer` String optional: Enables the [Chromium Inspector](https://docs.brightsign.biz/display/DOC/HTML+Best+Practices#HTMLBestPractices-debugging_webpages), which allows you to debug JavaScript applications while a webpage is running. Starting in BOS 8.5.31 you will need to also set the enable\_web\_inspector registry key (in the "html" section) to enable the JavaScript console. 
    
    *   To access the console, navigate to the player IP address at the specified port number. See [this page](https://trac.webkit.org/wiki/WebInspector) for documentation relating to the JavaScript console.
        
    *   In “enable\_web\_inspector”, "1" will allow the inspector and "0" or not present will disable it.  A reboot will be needed for these changes to take effect (if you enable/disable this through the LDWS UI, it may trigger a reboot to apply the change)
        

> [!CAUTION]
> For security reasons, **enable\_web\_inspector** should only be used in non-production presentations. Make sure to disable JavaScript console before publishing to a production environment. In the Chromium version found in BOS 8.5.31 and beyond, the JavaScript console will log information in memory even when you are not connected to the inspector. This will consume memory until the player runs out, which will result in a crash.

*   `inputEnabled` bool optional: Enables mouse/touchscreen events. This value is false by default.
    
*   `security` Security optional:  Override Chromium security checks.
    
*   `transform` String optional: Sets the screen orientation of content in the widget (note that the coordinates and dimensions of the *roRectangle* containing the widget are not affected by rotation). The following values are accepted:
    
    *   `"identity"`: There is no transform (i.e. the widget content is oriented as landscape). This is the default setting.
        
    *   `"rot90"`: The widget content is rotated to portrait at 90 degrees (clockwise).
        
    *   `"rot180"`: The widget content is rotated to portrait at 180 degrees (clockwise).
        
    *   `"rot270"`: The widget content is rotated to portrait at 270 degrees (clockwise).
        
*   `hwzDefault` String optional: Specifies the default [HWZ](https://docs.brightsign.biz/space/DOC/370672326#HTMLVideo-hwz_video) behavior. This value is `off` by default. To enable it, set it to `on`.
    
*   `interceptReloads` bool optional: Prevents `window.location.reload()` or similar constructs from taking effect in the browser. Instead the parent will receive a `reloadRequested` event.
    

## HtmlWidgetRect

This interface allows you to set the size and positioning of the widget rectangle. 

*   `x` long: Specifies the x coordinate for the widget.
    
*   `y` long: Specifies the y coordinate for the widget. 
    
*   `width` long: Sets the width of the widget in pixels.
    
*   `height` long: Sets the height of the widget in pixels. 
    

## NodeParams

This interface allows you to enable Node.js and define the parameters of the Node.js command-line arguments. 

*   `enabled` bool: Enables [Node.js](../../../developers/html-development/nodejs.md) on the widget. The value is `false` by default. 
    
*   `arguments` Array<String> optional:  An array specifying command-line arguments. 
    

##   
JavascriptInjection 

Use this interface to inject user scripts into the JavaScript engine. 

*   `documentCreation` JavascriptInjectionDetailList optional: The script will run as soon as the document is created. This behavior is not suitable for any DOM operation. 
    
*   `documentReady` JavascriptInjectionDetailList optional: The script will run as soon as the DOM is ready. This behavior is equivalent to the `DOMContentLoaded` event firing in JavaScript. 
    
*   `deferred` JavascriptInjectionDetailList optional: The script will run when the page load finishes. 
    

## JavascriptInjectionDetail

This interface defines the user scripts that are used by the JavascriptInjection interface. Exactly one of the `source`, `uri`, or `code` fields must be defined.

*   `world` String optional: Isolates user scripts into different worlds. This string can be assigned one of the following values: `application`, `user`, or `main` (see [this page](https://doc.qt.io/archives/qt-5.6/qwebenginescript.html#ScriptWorldId-enum) for more details); if the `world` parameter is not included in the array, "`application`" is selected by default. 
    
*   `source` String optional: Deprecated. Use `uri` or `code` instead.  
    
*   `uri` String optional: If defined, this must contain either a "file" URI, or a "data" URI with one of the following supported formats:
    
    *   "data:text/javascript;charset=utf-8;"
        
    *   "data:text/javascript;charset=utf-8;base64,"
        
    *   "data:text/javascript;charset=us-ascii;"
        
    *   "data:text/javascript;charset=us-ascii;base64,"
        
*   `code` String optional: If defined, the content will be executed as JavaScript code.
    

## Storage

This interface allows you to define the following HTML storage parameters:

*   `path` String: The folder used by local storage applications such as the JavaScript storage class. 
    
*   `quota` long:  The size (in bytes) allotted to all local storage applications (including IndexedDB). If the storage path is specified without a storage quota, Chromium defaults to reserving 1GB plus 10% of the total size of the storage device.
    
*   `forceSharedStorage` bool:  Allows HTTP/HTTPS loaded URLs to share local storage if they are loaded from the same domain. 
    
*   `forceUnsharedStorage` bool:  Prevents file loaded URLs from sharing storage.
    

> [!NOTE]
> Data can be corrupted if two HTML widgets access the database at the same time, but some applications rely on this type of access. Use the `force_unshared_storage` flag to avoid sharing on local URLs if you experience data problems, or use the `force_shared_storage` flag to allow sharing on HTTP/HTTPS sites.
> (If both flags are set, file storage is separated and HTTP storage is not.)

## Security 

Overrides Chromium security checks for these parameters:

*   `insecureOriginEnabled`  bool optional: Ignore insecure origins and treat them as enabled.
    
*   `cameraEnabled` bool optional: Enables webpage access to USB cameras connected to the player (access is disabled by default). This allows support for WebRTC applications. 
    
*   `desktopCaptureEnabled` bool optional: Enables desktop capture.
    
*   `audioCaptureEnabled` bool optional: Enables audio capture.
    
*   `insecureHttpsEnabled` bool optional: Ignore security errors when connecting to insecure HTTPS hosts (insecure HTTPS is disabled by default). Enabling this feature makes the player insecure; it is not suitable for production environments and should only be used for testing.
    

With BOS 8.2 and later (Chromium69 and later), several new CORS checks have been added. `security_params.websecurity` or `enableSecurity(false)` do not disable all these checks. Use the following registry setting instead:

`registry write html disable-web-security 1`

This flag will take effect on all `htmlwidget` instances, as opposed to previous flags which are only effective on the instance they are called on.

To write this to the registry using [roRegistrySection](../../../developers/brightscript/object-reference/hashing-and-storage-objects/roregistrysection.md):

```
RegHtml = CreateObject("roRegistrySection", "html")
RegHtml.Write("disable-web-security", "1")
RegHtml.Flush()
```