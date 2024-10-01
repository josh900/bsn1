# roJRE

This object allows you to load Java applications using the Java Runtime Environment (JRE) on the player. Java Runtime is no longer built into the firmware and roJRE is not invokable unless you run a BSFW file extension to add JRE to the player. After you install JRE, you must then invoke it to use roJRE. Contact BrightSign customer support to get the BSFW file extension.

The JRE uses OpenJDK 8 and is available on XTx44/43, XDx34/33, HDx24/23, LS424/423, and 4Kx42 models.

Object Creation: The *roJRE* object is instantiated with the Java package filename and an optional associative array that specifies JVM system properties and program arguments. You can use the `Type()` global function to determine if the package was successfully loaded.

```
CreateObject("roJRE", filename As String, options As roAssociativeArray)
```

The associative array can contain two entries:

*   `defines`: An associative array specifying system properties.
    
*   `arguments` : An array specifying command-line arguments.
    

All property/argument values must be passed as strings. Note that associative-array keys are case insensitive (i.e. converted to all lowercase) by default; use the *roAssociativeArray.SetModeCaseSensitive()* method to enable case-sensitive keys.

##### **Example**

```
props = {}
props.SetModeCaseSensitive()
props["SYS_PROP_1"] = "system prop 1"
props["SYS_PROP_2"] = "system prop 2"
props["java.io.tmpdir"] = "/var/tmp"
 
jre = CreateObject("roJRE", "app.jar", { defines: props, arguments: [ "arg 1", "arg 2" ] })
if type(jre)="roJRE" then
	print "Successfully started Java runtime"
else
	print "Unable to start Java runtime"
end if
```