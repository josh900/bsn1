# Node.js

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [BrightSign Node.js Implementation](#brightsign-nodejs-implementation)
*   [Enabling Node.js](#enabling-nodejs)
    *   [Cross-Domain Security](#cross-domain-security)
    *   [Web Storage](#web-storage)
    *   [JQuery](#jquery)
    *   [Node SerialPort](#node-serialport)
    *   [Reloading Node.js Enabled Web Applications](#reloading-nodejs-enabled-web-applications)
*   [Packaging and Delivering Node.js Applications](#packaging-and-delivering-nodejs-applications)
    *   [WebPack](#webpack)
*   [Device Storage Paths](#device-storage-paths)
*   [Debugging Applications](#debugging-applications)
*   [Downloading Large Files](#downloading-large-files)
*   [Node.js Examples](#nodejs-examples)

Our customers often need to communicate between applications on a BrightSign player, or between a BrightSign player and the outside world. This can be done using various protocols: HTTP, serial, and UDP are the most popular. You can write applications in either BrightScript or JavaScript to create this functionality. If you choose to write your application in JavaScript, you will need Node.js® to implement features such as hosting a web server in JavaScript.

BrightSign makes a Node.js endpoint available so that our partners can use Node.js modules and features. 

## BrightSign Node.js Implementation

BrightSign players support the Node.js runtime environment, which runs on the same V8 JavaScript engine used by Chromium. The Node.js® and Chromium instances share a single JavaScript execution context, so JavaScript applications can access both Node.js modules and DOM objects at the same time. BrightSign firmware pushes Node.js events to the Chromium event loop, ensuring that JavaScript applications receive Node.js and DOM events seamlessly.

The BrightSign Node.js implementation is based on the [NW.js](https://github.com/nwjs/nw.js) and [Electron](https://github.com/electron/electron) projects and shares many characteristics with them. Whereas Electron uses a JavaScript file as the entry point (i.e. the JavaScript file creates a webview, which also has access to the Node.js runtime), NW.js and BrightSign use an HTML file as the entry point: On a BrightSign player, BrightScript creates a Node.js-enabled *roHtmlWidget* instance; the initial URL, which is passed when *roHtmlWidget* is initialized, acts as the entry point for Node.js applications.

Like NW.js and Electron, BrightSign does not use sandboxing. Instead, it launches the render process with a Node.js user and storage group, which has write permissions for local storage and read permissions for the entire file system. It also can access networking interfaces and use privileged ports.  

![](./attachments/nodejs_combined_diagrams.png)

The integrated Node.js implementation in OS 8.2.x and OS 8.3.x is based on Node v10. For further documentation and usage information, consult the [Node.js 10.0.0 API documentation](https://nodejs.org/dist/v10.0.0/docs/api/). 

> [!NOTE]
> Node.js is not enabled for iframes or Web Workers.

## Enabling Node.js

Node.js object functionality is available in BrightAuthor:connected when users specify Node.js items in [Presentation Settings](https://docs.brightsign.biz/display/DOC/Presentation+Settings#PresentationSettings-Node.js). Node.js objects are not available in BrightAuthor.

Node.js is enabled for individual *roHtmlWidget* instances by including the `nodejs_enabled:true` entry in the [initialization parameters](../../developers/brightscript/object-reference/presentation-and-widget-objects/rohtmlwidget.md) of the *roHtmlWidget* object.

**Example:**

```
r=CreateObject("roRectangle", 0,0,1920,1080)
is = {
	port: 3000
}
config = {
	nodejs_enabled: true
	inspector_server: is
	brightsign_js_objects_enabled: true
	url: "file:///sd:/nodehello.html"
}
h=CreateObject("roHtmlWidget", r, config)
h.Show()
```

> [!WARNING]
> We do not recommend loading arbitrary websites with Node.js enabled. Some JavaScript libraries assume that Node.js is running on an instance with server-side capabilities, and they will attempt to load dependencies, causing playback to fail.

> [!NOTE]
> If you are using a BrightAuthor plugin to enable Node.js, you will need to set other desired parameters in the plugin, rather than with an HTML5 state. For example, if you want to enable the mouse cursor, you will need to set `mouse_enabled:true` during the *roHtmlWidget* initialization, rather than checking the box in the HTML5 state.

### Cross-Domain Security

Chromium has default security measures for preventing cross-site scripting attacks: If the URL for the *roHtmlWidget* instance is a remote domain, JavaScript applications from that domain cannot make HTTP requests to other domains; on the other hand, if the URL points to local storage, requests to other, remote domains are acceptable.

If you want to reference other domains in remote applications, set the `websecurity` parameter to `false` when initalizing the *roHtmlWidget*, as shown below:

**Example:**

```
r=CreateObject("roRectangle", 0,0,1920,1080)
is = {
	port: 3000
}
config = {
	nodejs_enabled: true
	inspector_server: is
	brightsign_js_objects_enabled: true
	url: "http://www.mysitehere.com"
	security_params: {websecurity: false} 
}
h=CreateObject("roHtmlWidget", r, config)
h.Show()
```

### Web Storage

If you want to use JavaScript storage applications, you will need to specify a `storage_path` and `storage_quota` when initializaing the *roHtmlWidget*:

**Example:**

```
r=CreateObject("roRectangle", 0,0,1920,1080)
is = {
	port: 3000
}
config = {
	nodejs_enabled: true
	inspector_server: is
	brightsign_js_objects_enabled: true
	url: "file:///sd:/nodehello.html"
	storage_path: "SD:"
	storage_quota: 1073741824
}
h=CreateObject("roHtmlWidget", r, config)
h.Show()
```

### JQuery

JQuery® requires a workaround to operate correctly with Node.js (see [this page](https://stackoverflow.com/questions/4299363/how-to-use-jquery-selectors-in-node-js) for an example). This workaround requires modifying the content, so if you don't have control over the webpage enabling node in your HTML widget, this can cause an intractable problem. You should only enable Node.js if you are planning to use it (for example with our [JavaScript API](../../developers/player-apis/javascript-apis.md)s).

See also [HTML Best Practices](../html-development/html-best-practices.md).

### Node SerialPort

The BrightSign player provides JavaScript serial port bindings for the Node SerialPort package. These bindings can be used using with the *@brightsign/serialport* API:

```
const SerialPort = require('@serialport/stream');
const BrightSignBinding = require('@brightsign/serialport');
SerialPort.Binding = BrightSignBinding;
```

Also see our [reference implementation](https://github.com/brightsign/bs-node-serialport) on GitHub.

### Reloading Node.js Enabled Web Applications

Any customer application that uses *@brightsign* objects, and some of the "BS" objects, will throw a JavaScript exception when reloaded in BrightSignOS 8.0 to 8.4 (even though it may have worked in OS 7.x and earlier) due to limitations with native modules in Node 10. This problem will be fixed in OS 8.5 and above, which ships with Node 14.x. You can also disable Node.js (and *@brightsign* objects) if you don’t need it.

## Packaging and Delivering Node.js Applications

> [!WARNING]
> If you are using Electron/Chromium 110 or a later version, BrightSign no longer supports any BrightScript/JavaScript objects in iframes for security reasons. iframes requests should be sent to [parent](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow%2Fparent&data=05%7C02%7Csmulqueen%40brightsign.biz%7Cc0b4df4b1a374212f14308dc95fa4ac2%7C8fbcdf641ab847cebdc743e23b04fb3c%7C0%7C0%7C638550149459230214%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=%2BBc0ofFac7LaEWddOehvXi7WJyxDFMvLPhPV6YNKl1g%3D&reserved=0) and then the parent page should call BrightSign/JavaScript objects.

To deploy your Node.js application to a BrightSign player, run "npm install" on your computer. This will create the `node_modules` directory. Copy this directory to the SD card along with the rest of the application.

When initialized, the BrightSign Node.js implementation seeks to the `node_modules` directory relative to the loaded HTML file. Like a standard Node.js application, it then loads all modules contained in the `node_modules` directory.

> [!NOTE]
> The majority of Node.js modules contain JavaScript code only. However, some modules contain binary code. When a module containing binary parts is installed using "npm install", the binary parts are compiled for the local platform (usually Intel x64), and this code will not run on a BrightSign player. Currently, the BrightSign Node.js implementation is limited to JavaScript code only.

### WebPack

The *node\_modules* directory associated with a Node.js application may contain hundreds or thousands of unnecessary files. The [webpack](https://webpack.js.org/)® bundler allows you to reduce the *node\_modules* directory to a manageable size.

To use webpack®, you will need to place your Node.js entry-point function in a separate file (e.g. "index.js"), rather than as inline HTML. This file will contain the references to other JavaScript files and Node.js modules:

**Example index.js:**

```
var myutils = require('./utilities'); // My utilities.js
var moment = require('moment'); // A node module
 
function main() {
 
  myutils.foo();
  moment.now();
  //...
}
```

The JavaScript file containing the Node.js entry point can then be referenced in the HTML file:

**Example HTML:**

```
<script src='./index.js'></script>
```

To use webpack®, attach `main()` to the window object so that it can be found from the HTML file:

```
var myutils = require('./utilities'); // My utilities.js
var moment = require('moment'); // A node module
 
function main() {
 
  myutils.foo();
  moment.now();
  //...
}
window.main = main;
```

Change the HTML file so that it points to the bundled JavaScript and to `window.main()`:

```
<script src='./bundle.js'></script>
 
<body onload="window.main()">
```

To build your bundle, run the following npm steps on your computer:

```
npm i -D webpack webpack-cli
npx webpack --mode production
```

Now you can publish the index.html and bundle.js files; there's no need to publish the `node_modules` directory. See the sample webpack® configuration below for more information.

[webpack.config.js](./attachments/webpack.config.js)

## Device Storage Paths

To load Node.js modules and read/write files, you must first define the root directory of the device storage. The following are common root directories:

*   microSD: `"storage/sd/"`
    
*   SSD: `"storage/ssd/"`
    
*   USB: `"storage/usb1/"`
    

We recommend using the `process.chdir()` call at the beginning of the script to change the process path:

**Example:**

```
var process = require("process");
process.chdir("/storage/sd");
```

  
Alternatively, if you have modules located on multiple storage drives, you can append multiple search paths to a module:

**Example:**

```
module.paths.push("/storage/sd/")
module.paths.push("/storage/ssd/")
module.paths.push("/storage/usb1/")
```

## Debugging Applications

When Node.js modules are enabled, they become visible from the [Chromium remote inspector](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices#Debugging-Webpages), allowing you to debug applications. The console.log works like a normal web application: Output is redirected to both stderr and the remote inspector.

## Downloading Large Files

If your application uses the XMLHttpRequest object to download a large file (100-200MB, depending on the player model), the player will run out of memory and the download operation will fail. The XMLHttpRequest object first downloads the whole file into memory, then creates a blob object of equal size, so memory requirements for a download are effectively double that of the file size.

For large-file downloads, we recommend using the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), which has callbacks that are fired when fragments are downloaded. Data can be appended to the disk as it arrives, so the player won't run out of memory, no matter the file size. The "download-test" HTML/JavaScript example below uses the Fetch API and the Node.js File Service module to download a file in fragments.

[download-test.zip](./attachments/download-test.zip)

> [!NOTE]
> This example is specific to BrightSign players and requires node.js runtime, enabled by use of the *roHtmlWidget* `nodejs_enabled` flag, to write files to disk.

## Node.js Examples

GitHub contains a [Node.js-starter-project](https://github.com/brightsign/node.js-starter-project). This project was originally created for BrightAuthor but can also be used with BrightAuthor:connected.

Another example is the script below, which initializes an HTTP server on the BrightSign player at port 8000. When a client (for example, a desktop browser) connects to the server, it will send the model number and boot version of the player to the client. The script also displays the IP address of the connected client on the screen attached to the player. 

**Example:**

```
<html>
<script>
function displayMessage()
{
  // Load the http module to create an http server.
  var http = require('http');

  // Configure our HTTP server to respond with Hello World to all requests.
  var server = http.createServer(function (request, response) {
    var device_info = new BSDeviceInfo();
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.end("Device Information:\n" + device_info.model + "\n" + device_info.bootVersion + "\n");
    var ip = request.connection.remoteAddress;
    document.getElementById("Ip").innerHTML+="Server responded to: "+ ip + "<br>";
    console.log("Server responded to request from " + ip);
  });

  // Listen on port 8000, IP defaults to 127.0.0.1
  server.listen(8000);

  // Display it on brightsign browser
  var os = require('os');
  var interfaces = os.networkInterfaces();
  var addresses = [];
  for (var k in interfaces) {
      for (var k2 in interfaces[k]) {
          var address = interfaces[k][k2];
          if (address.family === 'IPv4' && !address.internal) {
              addresses.push(address.address);
          }
      }
  }
  var message = "Server running at: " + addresses[0] + ":8000<br>";
  document.getElementById("Ip").innerHTML+= message;

  // Print message on console
  console.log(message);

}
</script>
<body style="background-color:red" onload="displayMessage()">
  <div id = "Ip" style="font-size:60px; text-align:center;">
  </div>
</body>
</html>
```

  
Built-in modules, such as "os" and "http", can be initialized using the `require()` method. If the `nodejs_enabled:true` entry is not included when initializing the *roHtmlWidget* object (as shown above), the `require()` method will not be available.