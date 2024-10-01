# Displaying HTML with BrightAuthor:connected

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [HTML Guidelines](#html-guidelines)
    *   [Zones](#zones)
    *   [Z-Ordering](#z-ordering)
    *   [Content Sourcing](#content-sourcing)
    *   [Using Custom Fonts](#using-custom-fonts)
    *   [Exporting an HTML5 Presentation](#exporting-an-html5-presentation)
    *   [Chromium Video Playback](#chromium-video-playback)
*   [Caching and Storage](#caching-and-storage)
*   [Using HTML with Portrait Orientation](#using-html-with-portrait-orientation)
*   [Integrating Touchscreen Content](#integrating-touchscreen-content)
*   [Disguising Network Latency](#disguising-network-latency)
*   [Displaying Scrollbars](#displaying-scrollbars)

This page covers how to integrate HTML pages into BrightAuthor:connected presentations. To add an HTML page to a presentation, select the HTML5 widget in the bottom of the **Content** window and drag it into the content panel above. [This page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1632600407/HTML5+State) describes how to use that widget.

## HTML Guidelines

### Zones

*   You can have multiple zones containing HTML content in a BrightAuthor:connected presentation.
    
*   HTML content can be inserted into a **Video or Image** zone or an **Image** zone.
    

### Z-Ordering

*   HTML content will show at the highest Z-level of graphics zones, meaning that an HTML zone will cover all other zones that contain images and text. This behavior does not extend to touch screens.
    
*   HTML content can be placed in front of or behind zones containing video content, if you drag the **Graphics** zone(s) before or after the **Video** zone(s) (under the Zone menu in the **Zone Properties** panel). See Image 1 below.
    
*   If the HTML page contains video and the **Enable native video playback** option is enabled in the HTML5 state, the HTML page will *always* display over other video zones.
    

![](./attachments/Screenshot%202023-09-07%20at%2010.47.42%20AM.png)

### Content Sourcing

HTML content can originate from a remote server, a local server, or the local storage (SD card) of the player. Presentations containing HTML content can also be downloaded onto the local storage from the BrightSign Network.

### Using Custom Fonts

To use custom fonts, specify the font in your script. If the font file is in the same directory as your JS and CSS files, it will be used in BrightAuthor:connected. 

### Exporting an HTML5 Presentation

Exporting a presentation that contains multiple HTML pages also exports in full all asset folders associated with those pages. If your pages share common asset folders, the entire contents will be duplicated multiple times. This can become problematic if your asset folders contain large content files, so you may need to prune and/or rearrange asset folders that are duplicated after export.

### Chromium Video Playback

The HTML5 widget has an **Enable Native Chromium video playback** option in versions 1.19.2 and later of BrightAuthor:connected. This feature is only available for XC5 players and is explained on [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1632600407/HTML5+State).

> [!NOTE]
> Partners using a custom CMS can use [HTML Playback Options on Series 5 Players](../html-development/html-playback-options-on-series-5-players.md) for more guidance on setting this option in their CMS.

## Caching and Storage

BrightAuthor:connected allows you to configure common browser caching and storage functions on the player. To enable these functions in your BrightAuthor:connected presentation, select **Enable Limit Storage** under **Admin > Application Preferences**, allocate the space as you wish, and select **Apply**. You can allocate space for the following functions:

*   **HTML Data**: The amount of space dedicated to the HTML application cache
    
*   **HTML Local Storage**: The amount of space dedicated to JavaScript variables and data
    
*   **HTML Indexed DB**: The amount of space dedicated to IndexedDB content
    

![](./attachments/HTMLLimitOptions.png)

## Using HTML with Portrait Orientation

To create a digital-signage canvas that is portrait oriented, simply create a portrait presentation and then insert an HTML5 widget.

## Integrating Touchscreen Content

You can enable touch-screen events for an HTML page by checking the **Enable mouse and touch events** box when creating an HTML5 state .

## Disguising Network Latency

When the BrightSign player loads HTML content from a URL, there may be a delay based on network latency. You can add a preload image to sidestep this issue. Note that this solution is not necessary if all HTML assets are located on the local storage of the player.

1.  Set BrightAuthor:connected to **Interactive**
    
2.  Drag and drop an image file into the main panel
    
3.  Set the **Initial State** box while editing the [**Image State**](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1632632833/Image+State).
    
4.  Specify the timeout for three seconds (or more if desired) in a [**Timeout** **Event**](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1636106748/Timeout+Event)**.**
    
5.  Set the **Timeout** **Event** to transition to the HTML5 state.
    

## Displaying Scrollbars

Browser scrollbars are disabled by default in BrightAuthor:connected. To display scrollbars, reference this simple CSS file from your HTML page:

[ForceScrollbars.css](./attachments/ForceScrollbars.css)