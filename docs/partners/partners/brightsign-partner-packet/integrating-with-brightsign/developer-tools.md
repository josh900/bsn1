# Developer Tools

BrightSign offers an extensive array of developer tools. These are listed here in alphabetical order.

## BrightSign Shell & BrightScript Debugger

The BrightSign Shell is the CLI (command-line interface) that enables interaction with the BrightSignOS through a serial cable or Telnet/SSH. The BrightScript Debugger is a tool that facilitates debugging of BrightScript code. More info about these tools can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1988100153/BrightSign+Shell).

## Crash Dumps

If a player encounters a non-deliberate shutdown (aka a crash), “crash dumps” are generated upon reboot. These files contain useful information that BrightSign Support can analyze and use for troubleshooting. These files can be found in the *brightsign-dumps* folder located in the root folder of the player’s storage device.

## Diagnostic Web Server

The Diagnostic Web Server (DWS) is a powerful tool that enables inspection of various player settings and diagnostic details. Both a Local Diagnostic Web Server (LDWS, accessible over the local network via the player’s IP address or by typing `http://BrightSign-NNNNNNNNNN.local` into a browser where `NNNNNNNNNN` is the serial number) and Remote Diagnostic Web Server (RDWS, accessible via either the bsn.Control or bsn.Content at bsn.cloud) are available. General info about the DWS can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server) and more specific info about the RDWS can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404620688/Remote+Diagnostic+Web+Server).

### Media Analyzer

The DWS includes a useful tool that can analyze media files for playability. More info can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404620688/Remote+Diagnostic+Web+Server#SD%2FMicroSD%2FMSATA%2FUSB).

## HTML

HTML is a common format for displaying presentations on BrightSign players. The [HTML Best Practices](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices) document will likely be very useful to developers. Specific sub-sections from that document worth noting individually are listed below.

### Web Inspector

Web pages can be debugged over the local network using the [Web Inspector](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices#Web-Inspector).

### Chromium Version

The Chromium version that BrightSign players use is likely several versions behind that version that most users are using in their web browsers. Find the Chromium version for the specific firmware version of your player [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2303000608/Chromium+Downloads+for+Current+Older+OS+Versions).

During development and testing, it is useful to have the correct version of Chromium on your Mac or PC. More information about this can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2303000608/Chromium+Downloads+for+Current+Older+OS+Versions).

## Logs / Diagnostics

Logs contain important diagnostic information about players. System logs (sometimes referred to as player logs) from the player are available and can be gathered via a syslog server, telnet or SSH, or a serial cable. More info about accessing logs via these means can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1988100153/BrightSign+Shell#Accessing-Logs).

Refer to [this article](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2350972929/Get+Player+and+DWS+Logs) on obtaining player logs and [this one](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2216034305/Interpret+Player+Logs) for interpreting player logs. Logs can easily be accessed via the RDWS as described [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404620688/Remote+Diagnostic+Web+Server#Log).

## Node

The node prompt is a command-line interface (CLI) that allows you to interact with Node.js. It is used to run JavaScript code and execute Node.js commands. Information about the Node prompt as well as the Node Inspector/Debugger can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices#Web-Inspector).

## Registry

The *registry* object allows you to read from and write to the player registry (the player’s persistent memory). More info about the registry can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370678545/registry).

## Serial Ports

Brightsign players have serial ports for diagnostic purposes as well as to provide interactive capabilities. More info about the hardware details of player serial ports can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/388434643/Serial+Port+Configuration) and how to use the serial port to access the BrightSign Shell and BrightScript Debugger can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1988100153/BrightSign+Shell).

## Telnet and SSH

Telnet and SSH can be used to communicate with BrightSign players. More info can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1988100153/BrightSign+Shell#Telnet).

## VSCode Extension for BrightScript

The popular [BrightScript Language Extension](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript) for [VSCode](https://code.visualstudio.com/) facilitates writing BrightScript and is used by thousands of developers around the world. Note that Brightsign’s BrightScript is a fork of Roku’s BrightScript. The forks have diverged and while they are similar, they are technically not the same. The value add is mainly the BrightScript syntax highlighting.

Next, we provide a recommended developer setup to help maximize efficiency in developing for the BrightSign platform.

[Next - Developer Setup >](../integrating-with-brightsign/developer-setup.md)