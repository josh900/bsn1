# HTML Caching

This page covers how to use caching techniques to display HTML content. BrightSign players offer novel solutions through BrightAuthor and BrightScript, as well as support for common Node.js® and JavaScript caching solutions.

## Storage and Memory

Before discussing HTML caching techniques, it is important to understand the storage and memory limitations of the players. All BrightSign players run HTML content on a Chromium engine. By default, Chromium reserves 1GB plus 10% of the total size of the player's storage device for memory. Players also have limited memory to run HTML graphics and JavaScript. This amount varies between player models; consult [this list](https://docs.brightsign.biz/display/DOC/HTML+Best+Practices#HTMLBestPractices-MemoryandPerformance) for more detail.

To change the storage values through BrightAuthor:

1.  Navigate to **Edit > Preferences > Storage**
    
2.  Check **Limit Storage Space by Function**
    
3.  Now space can be allocated for both HTML graphics and JavaScript. Make sure that:
    
    1.  When using **Specify absolute size**, the specified segments should be neither larger nor smaller than the absolute size of your storage device
        
    2.  When using **Specify percentages**, the percentages must add up to 100%.
        

These limitations are shared across all *roHtmlWidget* instances, where [*roHtmlWidget*](https://docs.brightsign.biz/display/DOC/roHtmlWidget) is the BrightScript object that handles all HTML processes.

## Caching Capabilities

BrightSign players offer a flexible toolset for caching HTML content. The sections below discuss novel BrightSign solutions and how to enable and use more common methods through Node.js and JavaScript.

### BrightSign solutions

BrightSign players offer two HTML caching solutions:

*   **Local Storage**: The SD card for each player can store HTML content for playback. This method eliminates any connectivity or latency issues that may arise from networked solutions, but it must be done on a player by player basis. This can make local storage unattractive when dealing with a large fleet of devices.
    
*   **The AssetPool BrightScript object:** The AssetPool is a sharded hash directory and is recommended for large file count applications. The AssetPool is filled by AssetFetcher objects that can acquire content online and store it for later playback in either sha1, besha1, or MD5 hash protocols. Consult [this page](https://docs.brightsign.biz/display/DOC/Content+Management+Objects) for more information about AssetPool.
    

### Node.js and JavaScript solutions

BrightSign players also support Node.js and JavaScript caching techniques. To use Node.js:

*   If you are using BrightAuthor, Node.js must first be enabled through a [BrightScript *roHtmlWidget* object](https://docs.brightsign.biz/display/DOC/roHtmlWidget#roHtmlWidget-%5Bboolean%5Dnodejs_enabled)
    
*   If you are using BrightAuthor:connected, Node.js can be initialized through the [Presentation State Properties](https://docs.brightsign.biz/display/DOC/State+Properties#StateProperties-Options) user interface.
    

Once Node.js is running on the player, users can use any JavaScript API or caching method to cache content. Recommended content acquisition methods are XmlHttpRequest and Fetch with Service Worker. Keep the memory limitations in mind - for example, XmlHttpRequest will cause some player models to crash if it is used to download files larger than 100-200MB. If XmlHttpRequest's storage reservation will exceed your memory limitation, we recommend using the Fetch API. 

You cannot use Service Workers to cache video content. BrightSign players use our media player infrastructure for later video playback, not the Chromium network. BrightSign recommends [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB) for storage: use it to cache content playback according to [these instructions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage#storing_complex_data_via_indexeddb). 

See an HTML/JavaScript test download example [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370677153/Node.js#Downloading-Large-Files). 

> [!NOTE]
> Our HTML widget cannot cache videos listed in the AppCache manifest because of differences between the Chrome desktop and BrightSign device video playback architecture. Please use Service Worker and IndexedDB to cache content instead of AppCache, which is now deprecated.

### Using Blobs

BrightSign video players can play blob URLs referring to items in IndexedDB and Html5 FileSystem API. However it cannot play blob URLs referring to JavaScript objects in memory.

See this video-browser-storage.html example:

[indexdb_playback_example.zip](./attachments/indexdb_playback_example.zip)