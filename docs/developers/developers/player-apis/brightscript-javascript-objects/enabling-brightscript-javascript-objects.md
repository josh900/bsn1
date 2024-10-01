# Enabling BrightScript-JavaScript Objects

For security reasons, all BrightScript JavaScript objects are disabled by default. As a result, you will encounter DOM errors like those shown below if you do not enable first enable them (to view a console log of BrightScript/JavaScript events, go to the [Diagnostic Web Server](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server) or use the JavaScript console).

![](./attachments/DOM%20Exception%20--%20Console%20Output.png)

Follow the below steps to enable BrightScript JavaScript objects.

## Enabling with BrightAuthor

Make sure that you are using BrightAuthor version 4.1 or later. Earlier versions do not have the code that enables BrightScript objects for JavaScript.

Also, ensure that the **Enable external data** box is checked within the HTML5 state that is displaying your page.

![](./attachments/BA%20--%20Enable%20External%20Data.png)

## Enabling with BrightScript

Include the `brightsign_js_objects_enabled:true` entry with the associative array that is passed during creation of the [*roHtmlWidget*](../../../developers/brightscript/object-reference/presentation-and-widget-objects/rohtmlwidget.md) instance:

**Example:**

```
r=createobject("rorectangle",0,0,1920,1080)
aa=createobject("roassociativearray")

aa.url="http://test-server/index.html"
aa.brightsign_js_objects_enabled=true

bb=createobject("roassociativearray")
bb.port=3000
aa.inspector_server=bb

h=createobject("rohtmlwidget",r,aa)
h.show()
```

The above method enables all BrightScript-JavaScript objects on an *roHtmWidget* instance. To enable only a subset of BrightScript-JavaScript objects, or to restrict the objects to certain URLs, use the `AllowJavaScriptUrls()` method on a *roHtmlWidget* instance. This method accepts an associative array that maps BrightScript-JavaScript classes to the URL(s) that are allowed to use them.

*   An `all` key indicates that all classes are authorized for the associated URL(s).
    
*   An asterisk `"*"` value indicates that all URLs are authorized for the associated BrightScript-JavaScript class.
    
*   A `"local"` value indicates that all local pages are authorized for the associated BrightScript-JavaScript class.
    

This will enable all BrightScript classes for all URLs:

```
html.AllowJavaScriptUrls({ all: "*" })
```

This call will enable all BrightScript-JavaScript classes for local pages and the BrightSign homepage:

```
html.AllowJavaScriptUrls({ all: ["local", "http://www.brightsign.biz"]})
```