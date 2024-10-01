# HTML Playback Options on Series 5 Players

There are two ways to playback HTML audio and video from Series 5 players:

*   On Series 5 and older players, video decode is handed off by default to the BrightSign application which deals with decode and display.
    

*   On Series 5 players, there is now an option to set a registry value to enable the built-in Chromium video player. The resulting Chromium plays back video similarly to desktop Chromium. Series 5 players will automatically use hardware-accelerated decode if the Chromium video player is enabled. This option is not available on Series 4 and earlier players, regardless of OS version. 
    

BrightSign video and audio features are only provided by the BrightSign video player, so if you chose to use Chrome, BrightSign [HTML video](../html-development/html-video.md) features will not be supported (it is like running Chrome in a browser on a PC). Chromium has much poorer streaming support than our application, and fewer hardware accelerated video decode levels and profiles are supported.

Only customers who do not want to take advantage of our unique capabilities should use native Chrome in their CMS.

To switch from the BrightSign video player to the Chrome Media Player:

```
registrySection = CreateObject("roRegistrySection", "html")
registrySection.Write("use-brightsign-media-player", "0") ' to switch to Chromium for media playback
```

To switch from the Chrome Media Player to the BrightSign video player:

```
registrySection = CreateObject("roRegistrySection", "html")
registrySection.Delete("use-brightsign-media-player") ' to switch to back to the default (BrightSign) for media playback
```

or:

```
registrySection = CreateObject("roRegistrySection", "html")
registrySection.Write("use-brightsign-media-player", "1") ' to switch to back to BrightSign for media playback
```