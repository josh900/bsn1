# Partner Glossary

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [autorun.brs](#autorunbrs)
*   [autorun.zip and autozip.brs](#autorunzip-and-autozipbrs)

*   [BrightAuthor:connected](#PartnerGlossary-BrightAuthor:connected)
*   [BrightScript Debug Console](#PartnerGlossary-BrightScriptDebugConsole)
*   [BrightSign Shell / Console](#PartnerGlossary-BrightSignShell/Console)
*   [BSN.cloud](#PartnerGlossary-BSN.cloud)
    *   [bsn.Control](#bsncontrol)
    *   [bsn.Content](#bsncontent)
*   [Chromium](#PartnerGlossary-Chromium)
*   [Console](#PartnerGlossary-Console)
*   [CMS](#PartnerGlossary-CMS)
*   [Content Delivery](#PartnerGlossary-ContentDelivery)
*   [Content / Presentation](#PartnerGlossary-Content/Presentation)
*   [Crash Dumps](#PartnerGlossary-CrashDumps)
*   [Diagnostic Web Server](#PartnerGlossary-DiagnosticWebServer)
    *   [Media Analyzer](#media-analyzer)
*   [HTML](#PartnerGlossary-HTML)
    *   [Web Inspector](#web-inspector)
    *   [Chromium Version](#chromium-version)
*   [Logs / Diagnostics](#PartnerGlossary-Logs/Diagnostics)
*   [Node](#PartnerGlossary-Node)
*   [Partner App](#PartnerGlossary-PartnerApp)
*   [Player](#PartnerGlossary-Player)
*   [Provisioning](#PartnerGlossary-Provisioning)
*   [Registry](#PartnerGlossary-Registry)
*   [Serial Ports](#PartnerGlossary-SerialPorts)
*   [Setup](#PartnerGlossary-Setup)
*   [Storage Device](#PartnerGlossary-StorageDevice)
*   [Swivel](#PartnerGlossary-Swivel)
*   [Telnet and SSH](#PartnerGlossary-TelnetandSSH)
*   [Visual Studio Code](#PartnerGlossary-VisualStudioCode)
*   [VS Code Extension for BrightScript](#PartnerGlossary-VSCodeExtensionforBrightScript)

## autorun.brs

Upon bootup, players look for an *autorun.brs* file which instructs the player what to do upon startup. This file is required for all players.

## autorun.zip and autozip.brs

Players also look for *autorun.zip* files that contain the script *autozip.brs*. If found, the player will execute *autozip.brs* which unpacks the contents of the *autorun.zip* file to the root directory of the storage device and reboots the player.

# BrightAuthor:connected

This software, available for Mac and PC, provides an easy-to-use interface for creating presentations, create and assign player schedules, and monitor player status and health of players. The software also enables users to setup, activate, and provision new players as well as manage user roles and permissions.

# BrightScript Debug Console

The BrightScript Debug Console is a tool that facilitates debugging of BrightScript code. It is available through the BrightSign Shell (see below). To turn the BrightScript Debug Console on, type `script debug on` at the console. More info can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672795/BrightScript+Debug+Console).

# BrightSign Shell / Console

The BrightSign Shell, also referred to as the BrightSign Console, is the command line interface that enables interaction with the BrightSign OS through a serial cable or telnet/SSH.

From the BrightSign Shell, the `script` command can be used to access the BrightScript Debug Console, and the `node` command can be used to access Node related functions.

Commands for the BrightSign Shell can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404621543/BrightSign+Shell+Commands).

# BSN.cloud

BrightSign’s robust cloud-based platform that provides a myriad of tools and services to help customers and partners easily use a single player or manage an expansive network of players. BSN.cloud consists of two different options: the free bsn.Control and the paid bsn.Content.

## bsn.Control

Free solution the enables viewing of player information, player provisioning, remote diagnostics, and access to REST APIs.

## bsn.Content

Paid solution that includes all the features of bsn.Control plus content hosting; the ability to create, schedule, and publish content; advanced network management tools; and user groups, roles, and privileges.

# Chromium

Chromium is the free and open-source web browser project primarily developed and maintained by Google. It is the underlying engine for the ubiquitous Chrome browser. BrightSign players use the same Chromium software to render and display web content.

# Console

The informal name for BrightSign’s command line interface.

# CMS

As might be surmised, a Content Management System, or CMS, is used to manage content. CMSs are also often used to manage player setup, activation, provisioning, scheduling, and diagnostics.

While separate apps may be used to author and publish presentations, this guide will use the term CMS as a catch-all term to refer to software that enables authoring, publishing, and management of presentations, content, and players.

# Content Delivery

This term is used to describe the process of getting content onto the player’s storage device.

# Content / Presentation

Strictly speaking, a presentation refers to the file that controls the layout and behavior of the items that the player will display.

Content refers to the visual item(s) being displayed by the presentation. Content thus refers to media files associated with the presentation such as videos, images, and audio files.

Since the presentation and content depend on each other to render properly (one cannot be displayed without the other), the term “content” is generally be used to represent *both* the presentation *and* its content.

# Crash Dumps

When a player encounters a non-deliberate shutdown (aka a crash), “crash dumps” are generated upon reboot. These files contain useful information that BrightSign Support can analyze and use to help troubleshoot. These files can be found in the *brightsign-dumps* folder located in the root folder of the player’s storage device.

Further details about crash reports can be found [https://brightsign.atlassian.net/wiki/spaces/IKB/pages/519144363](https://brightsign.atlassian.net/wiki/spaces/IKB/pages/519144363).

# Diagnostic Web Server

The Diagnostic Web Server (DWS) is a powerful tool that enables inspection of various player settings and diagnostic details. Both a Local Diagnostic Web Server (LDWS, accessible over the local network via the player’s IP address) and Remote Diagnostic Web Server (RDWS, accessible via either the Control Cloud or Content Cloud at bsn.cloud) are available. General info about the DWS can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server) and more specific info about the RDWS can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404620688/Remote+Diagnostic+Web+Server).

## Media Analyzer

The DWS includes a useful tool that can analyze media files for playability. More info can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404620688/Remote+Diagnostic+Web+Server#SD%2FMicroSD%2FMSATA%2FUSB).

# HTML

HTML stands for HyperText Markup Language. It is a standard markup language for web page creation and is also a common format for displaying presentations on BrightSign players. The [HTML Best Practices](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices) document will likely be very useful to developers. Specific sub-sections from that document worth noting individually are listed below.

## Web Inspector

Web pages can be debugged over the local network using the [Web Inspector](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices#Web-Inspector).

## Chromium Version

The Chromium version that BrightSign players use is likely several versions behind that version that most users are using in their web browsers. Find the Chromium version for the specific firmware version of your player [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672286/HTML+Best+Practices#Renderer-Versions-and-Support).

During development and testing, it is useful to have the correct version of Chromium on your Mac or PC. More information about this can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2303000608/Chromium+Downloads+for+Current+Older+OS+Versions).

# Logs / Diagnostics

Logs contain important diagnostic information about players. System logs (sometimes referred to as player logs) from the player are available and can be gathered via a syslog server, telnet or SSH, or an RS-232 serial cable. More info can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673311/roSystemLog).

Refer to [this article](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2350972929/Get+Player+and+DWS+Logs) on obtaining player logs and [this one](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2216034305/Interpret+Player+Logs) for interpreting player logs. Logs can easily be accessed via the RDWS as described [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404620688/Remote+Diagnostic+Web+Server#SD/MicroSD/MSATA/USB).

# Node

The node prompt is a command-line interface (CLI) that allows you to interact with Node.js. It is used to run JavaScript code and execute Node.js commands.

# Partner App

A “partner application” or “partner app” refers to the partner software that resides on the player’s storage device. In most cases, the partner app consists of the presentation that the partner wishes the player to display. Upon bootup, the player runs the *autorun.brs* file which can be configured to invoke the partner app.

# Player

BrightSign’s extensive line of hardware devices specifically designed for digital signage.

# Provisioning

This term generally refers to the process of activating a player and getting an *autorun.brs* file onto the player’s storage device.

# Registry

The *registry* object allows you to read from and write to the player registry (the player’s persistent memory). More info about the registry can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370678545/registry).

# Serial Ports

Brightsign players have serial ports for diagnostic purposes as well as to provide interactive capabilities. More info about serial ports can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/388434643/Serial+Port+Configuration).

# Setup

Setups are files containing information such as the intended publishing configuration and various player settings. Setups can be applied to one or many players and different Setups can be saved to the Setup Library.

# Storage Device

BrightSign players lack onboard storage and require a separate storage device. Storage devices include microSD (µSD) cards as well as USB drives such as thumb drives, external hard drives, and external solid-state drives (SSDs). Many BrightSign players also support internal SSDs in the common M.2 form factor.

# Swivel

While not an official term, the word “swivel” is sometimes used to describe a partner integration in which users interact with the partner’s CMS using one browser tab while interacting with the Control Cloud interface in another browser tab.

# Telnet and SSH

Telnet and SSH are both network protocols that allow you to connect to remote computers over the internet. Telnet is an older protocol that is used for remote access to servers and networking devices. It sends data in plain text without any encryption or authentication, which makes it insecure. SSH (Secure Shell) is a newer protocol that provides secure remote access to servers and networking devices. It encrypts all data sent between the client and server, making it much more secure than Telnet. [SSH also uses public key authentication for added security](https://infraexam.com/how-is-ssh-different-from-telnet/).

Telnet and SSH can be used to communicate with BrightSign players. More info can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673607/Telnet+and+SSH).

# Visual Studio Code

Visual Studio Code (VS Code) is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux and macOS. It is used for editing text and managing your entire codebase like an integrated development environment (IDE). [It supports debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git](https://opensource.com/article/20/6/open-source-alternatives-vs-code).

# VS Code Extension for BrightScript

The popular [BrightScript Language](https://marketplace.visualstudio.com/items?itemName=RokuCommunity.brightscript) extension for [VSCode](https://code.visualstudio.com/) facilitates coding in BrightScript and is used by thousands of developers around the world. Note that Brightsign’s BrightScript is a fork of Roku’s BrightScript. The forks have diverged and while they are similar, they are technically not the same. Nevertheless, developers may find value in this extension.