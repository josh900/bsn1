# Node.js Versions

As of BrightSignOS 8.2, two versions of Node are shipped with the player:

*   A Node.js version that is integrated into Chromium
    
*   The standalone Node.js that is used by [roNodeJs](https://docs.brightsign.biz/display/DOC/roNodeJs) and similar objects
    

The version numbers of these are not identical although BrightSign tries to ensure that they are at least the same major version.

Note that the embedded Node.js is associated with [roHtmlWidget](../../developers/brightscript/object-reference/presentation-and-widget-objects/rohtmlwidget.md) and standalone Node.js is associated with [roNodeJs](../../developers/brightscript/object-reference/presentation-and-widget-objects/ronodejs.md).

## Determining Version Numbers

Inspecting `process.version` in each environment is the most reliable way to determine the exact version number for any given version of the OS. For standalone Node.js, enter `process.version` at the prompt:

```
BrightSign> node
> process.version
'v10.15.3'
> 
BrightSign>
```

  
For embedded Node.js, run a script to print the version number to the log and inspect the output (there is no way to type directly in the console):

```
BrightSign> htmlplay data:text/html,<script>console.log(process.version);</script>
BrightSign> log
[...]
<12>[173535.688] [INFO]   [source data:text/html,%3Cscript%3Econsole.log(process.version);%3C/script%3E:1]: v10.11.0 
BrightSign>
```

## OS/Chromium Version Compatibility

| BrightSignOS version | Chromium version | Embedded Node.js version | Standalone Node.js version |
| --- | --- | --- | --- |
| OS 7.1.x, 7.0.x | Chromium 45 | 5.1.1 | 5.1.1 |
| OS 8.0.x | Chromium 65 | 10.0.0 | 8.9.4 |
| OS 8.1.x, 8.2.x, 8.3.x | Chromium 69 | 10.11.0 | 10.15.3 |
| OS 8.5.x, OS 9.0.x | Chromium 87 | 14.17.6 | 14.17.6 |