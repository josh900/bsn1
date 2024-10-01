# Considerations

While BrightSign players are highly versatile in the content sources they are able to utilize, there are some important factors that should be considered when making decisions about content sources.

Displaying web and streaming content hosted on an external website requires a persistent internet connection and performance is subject to the whims of network connectivity - if there are internet issues, the players will not be able to reliably display content.

Further, a common use case for digital signage is for players to loop the same content over and over. Having to repeatedly retrieve the same content from a server, particularly if there are multiple players where each player requires an individual stream, is a highly inefficient, and potentially expensive, use of bandwidth and server resources.

Content that resides locally on the player is much preferred. Quality of service can be much more tightly controlled as it is not dependent on a persistent network connection. BrightSign offers tools that enable remote content delivery directly to players as well as solutions for caching external web content (refer to the [Resources](https://brightsign-sandbox-694.atlassian.net/wiki/spaces/DOC/pages/6688342) section of this guide) on the player.

BrightSign players also have the capability of directly running Node.js applications, and if streaming content is desired, players have the ability to run a streaming server.

For most use cases, the preferred content source(s) will be Local Content, cached Web Content, or a mixture of both.

[Next - Integrating with BrightSign >](../../brightsign-partner-packet/integrating-with-brightsign.md)