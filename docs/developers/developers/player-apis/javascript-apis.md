# JavaScript APIs

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [JavaScript APIs Replace Previous “BrightScript-JavaScript Objects”](#javascript-apis-replace-previous-brightscript-javascript-objects)
*   [Enabling the JavaScript API](#enabling-the-javascript-api)
*   [Loading BrightSign Modules](#loading-brightsign-modules)
*   [Synchronous and Asynchronous Methods](#synchronous-and-asynchronous-methods)

The BrightSign API for JavaScript allows you to interface with the BrightSign player firmware to configure the player, retrieve system data, and interface with peripheral devices. This API allows for operation of a digital signage platform–including playback, scheduling, diagnostics, and network configuration–using HTML/JavaScript, without the need for extensive coding in BrightScript.

## JavaScript APIs Replace Previous “BrightScript-JavaScript Objects”

This API replaces the [BrightScript-JavaScript objects](../player-apis/brightscript-javascript-objects.md). Those older JavaScript objects are still offered for backwards-compatibility purposes. See the [BrightScript-JavaScript Migration Guide](../player-apis/brightscript-javascript-migration-guide.md) for the mapping between BrightScript and JavaScript APIs.

JavaScript objects are embedded into the browser runtime. They only exist in the global JavaScript namespace, and can only be used with *roHtmlWidget*.

Thus JavaScript API uses node modules. It works seamlessly with [*roHtmlWidget*](../../developers/brightscript/object-reference/presentation-and-widget-objects/rohtmlwidget.md), [*roNodeJs*](../../developers/brightscript/object-reference/presentation-and-widget-objects/ronodejs.md)*,* and on *roElectron*. It is a superset of legacy JavaScript objects.

BrightSign has not added new features to the legacy BrightScript-JavaScript objects for several years, and all of our current development efforts go into JavaScript APIs. The legacy BrightScript-Javascript objects exist to support customers who use them in deployed software, and to maintain that support during OS upgrades. 

Unlike the legacy BrightScript-JavaScript objects, there is no one-to-one relationship between BrightScript objects and objects in the new JavaScript API. Many BrightScript functions (e.g. HTTP server and file storage capabilities) are not exposed in the new API because JavaScript and Node.js® expose standardized, popular equivalents.

## Enabling the JavaScript API

The BrightSign API for JavaScript is implemented with the Node.js module, which is included with the Chromium engine on the player. To use the BrightSign API with an *roHtmlWidget* instance, you must enable Node.js when creating the widget:

##### **Example**

```
r=createobject("rorectangle",0,0,1920,1080)
aa=createobject("roassociativearray")

aa.url="http://test-server/index.html"
aa.nodejs_enabled=true

bb=createobject("roassociativearray")
bb.port=3000
aa.inspector_server=bb

h=createobject("rohtmlwidget",r,aa)
h.show()
```

In the above example, Node.js is enabled by including the `nodejs_enabled:true` entry in the associative array that is passed during creation of the *roHtmlWidget* instance.

## Loading BrightSign Modules

The BrightSign API does not exist in the global (window) namespace of the JavaScript runtime. Instead, like Node.js objects, BrightSign modules are loaded using the `require()` function (i.e. `require("@brightsign/<module_name>")`). BrightSign modules are actually part of the firmware, but in terms of usage, they are identical to other Node.js modules.

##### **Example**

```
var NetworkConfigClass = require("@brightsign/networkconfiguration");   // Call the class constructor for the networkconfiguration object.
var wifi = new NetworkConfigClass("ethernet"); 							// Create an instance of the networkconfiguration class.
```

## Synchronous and Asynchronous Methods

BrightSign modules contain both synchronous and asynchronous methods. Synchronous methods return an object that can be used immediately, while asynchronous methods return a Promise object, which will itself return the object data when the operation is resolved. Scripts must handle these delayed returns (typically using the `.then()` and `.catch()` methods available on the Promise object).

##### **Example**

```
var NetworkConfigClass = require("@brightsign/networkconfiguration");
var wifi = new NetworkConfigClass("wlan0"); 
wifi.scan().then(											 // Call the Scan() method, which returns a promise.
		function(data){console.log(JSON.stringify(data));}) // The resolve/success case, which prints the scan results 
	.catch(
		function(data){console.log(JSON.stringify(data));}) // The reject/failure case, which prints the failure reason
```