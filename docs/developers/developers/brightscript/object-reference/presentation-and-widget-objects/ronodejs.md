# roNodeJs

*roNodeJs* is a BrightScript object that allows the launching of a Node.js® instance. These Node.js instances will have access to all BrightSign Node.js modules as built in modules. roNodeJs also provides mechanisms to communicate between JavaScript and BrightScript environments for more complex applications.

## Object Creation

*roNodeJs* is instantiated with a filename and optional parameters. 

```
node = CreateObject("roNodeJs", "index.js", {message_port:my_message_port, arguments: ["arg1", "arg2"]})
```

In OS 8.2.17 and later versions, you can also pass an optional *node\_arguments* parameter which provides arguments to the node interpreter itself (as opposed to *arguments* which provides arguments to the JavaScript application being run inside Node):

```
node = CreateObject("roNodeJs", "index.js", {message_port:my_message_port, node_arguments: ["arg"], arguments: ["arg1", "arg2"]})
```

*   `message_port:` Optional. Allows communication with JavaScript applications. 
    
*   `arguments:` Optional. Passes arguments to the node instance. 
    
*   `node_arguments:` Optional. Passes arguments to the node.js executable, for example, to enable remote inspector for node.js. *Node\_arguments* can take multiple arguments.
    
*   `env_vars:` Optional. Passes environment variables (supplied as an associative array) to the node.js application. **Note:** Environment variable names are case-sensitive, but *roAssociativeArray* is case-insensitive by default and the BrightScript literal syntax for associative arrays forces all key names to lower case. To ensure correct behavior, call `SetModeCaseSensitive()` and use the `AddReplace()` method to add variables to the array. Or you can use the following example, which is slightly less verbose than `AddReplace():`
    

```
a={}
a.SetModeCaseSensitive()
a["KeY"] = 1
a["key"] = 2
print a  ' returns both key and KeY
```

## PostJsMessage()

`PostJsMessage (data as AssociativeArray) As Boolean`  
Posts a collection of key:value pairs to the BrightScript *MessagePort* JavaScript class. This method takes an associative array but it doesn't support nested associative arrays. See [JavaScript to BrightScript](https://docs.brightsign.biz/display/DOC/messageport) for more details.

## roNodeJs Events

See this [page](https://docs.brightsign.biz/display/DOC/roNodeJsEvent) for information about roNodeJs events.

## Examples

To enable inspector using node\_arguments:

```
node_js = CreateObject("roNodeJs", "main.js", {message_port: msgPort, node_arguments: ["--inspect=0.0.0.0:2999"], arguments:["node_application_argument1", "node_application_argument2"})
```

To change a directory to the directory of the current JavaScript file:

```
proc.chdir(__dirname)
```

To set a timer to stop node from exiting:

```
setInterval(function(){console.log("ping"}, 10000)
```

To pass arguments to roNodeJs:

```
node = CreateObject("roNodeJs", "index.js",
{node_arguments: ["-r", "dotenv/config"], arguments: ["dotenv_config_path=/storage/sd/.env"]})
```

Note that "node\_arguments" are arguments that come before the filename, while "arguments" come after the filename.