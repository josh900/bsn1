# Copy to Player

In this example, we will maintain the player’s default Setup (the BrightSign Default Setup) and manually copy an *autorun.zip* file to the player’s storage device. The *autorun.zip* file will install the Player App.

## autorun.zip

At a minimum, the *autorun.zip* file should include the following files:

*   *autorun.brs*
    
*   *autozip.brs*
    

While not required, *autorun.zip* files can also include the presentation/content (e.g., an HTML file and associated media files that the player will display) that the *autorun.brs* file invokes. In this way, everything the player needs is contained in a single package for delivery. We will utilize this approach in this example, and we will use an HTML file as our sample presentation.

![](./attachments/image-20230327-234103.png)

The *autorun.zip* file will include the following files:

*   *autorun.brs* (this is the script [shown](https://brightsign.atlassian.net/wiki/spaces/PID/pages/1490124837/Autorun#Sample-autorun.brs) in the previous section; recall that this file instructs the player to render *index.html*)
    
*   *autozip.brs* (this is the script [shown](https://brightsign.atlassian.net/wiki/spaces/PID/pages/1490124837/Autorun#Sample-autozip.brs) in the previous section which instructs the player to unzip the *autorun.zip* file)
    
*   *index.html* (this is our HTML presentation)
    
*   *snowy\_river.mp4* (this is a sample video that is displayed by the index.html presentation)
    

You can create your own versions of the files above and compress them into an *autorun.zip* file, or you can use the *autorun.zip* file attached here:

[autorun.zip](./attachments/autorun.zip)

## Local + Remote Content

Although we are including a video file in the *autorun.zip* file, our presentation will also display the following:

*   A streaming video from YouTube.
    
*   A picture slideshow where the pictures are retrieved from an external web server.
    
*   The local weather displayed by a weather widget that retrieves data from an external URL.
    

BrightSign players are capable of displaying any combination of local and remote content.

## Copy to Card

Next, we will manually copy the *autorun.zip* to an empty microSD card and insert the card into a player.

![](./attachments/image-20230623-164334.png)

1.  Copy the *autorun.zip* file to the *root* directory of a blank, properly formatted microSD card.
    
2.  Insert the microSD card into the player.
    
3.  Power up the player.
    

Shortly after the player boots up, you should see something like this on your display:

![](./attachments/image-20230328-161412.png)

## Folders

![](./attachments/image-20230526-015203.png)

When the *autorun.zip* file is unpacked, the *autozip.brs* file instructs the player to create several folders in the root directory of the microSD card. These folders and their functions are as follows:

### brightsign-dumps

If a player crashes, dumps are created and stored in this folder. Dumps are numbered incrementally and can be useful for troubleshooting. They may be requested by BrightSign Support when diagnosing problems. Note that only the 10 most recent crash dumps are retained.

### pool

Media files, especially video files, can be quite large. To help players better manage such large files, players apply a cryptographic [hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function) to each media file. Hash functions are well beyond the scope of this document, but at a high-level, when a hash algorithm is applied to any file, a unique hash, or alphanumerical representation, of that file can be generated. If that file is changed in any way, the new file will result in a completely different hash.

Hashes are typically many times smaller in size compared with the original file. Whereas a large video file can easily run into the gigabytes, a hash of that video will only be at most a few dozen bytes (the exact size of the hash depends on the algorithm used).

Hashes are therefore much more manageable representations of the actual media files, and the pool (more formally, the Asset Pool) is where these hashes are stored. System efficiency is greatly improved through the use of hashes. The system can, for example, quickly determine if a file has changed simply based on whether the hash has changed instead of having to compare two large files. More detail about the Asset Pool can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/411436363/BrightSign+Asset+Pool).

### feedPool

The feedPool contains transient / non-static assets like RSS feeds and [dynamic playlists](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/384958989/Content#Dynamic-Playlists-%5BinlineExtension%5D), both of which can be used with BrightSign presentations.

### feed\_cache

The feed\_cache stores the metadata for the transient assets in the feedPool. For example, the feed\_cache would store the URL for an RSS feed, identifiers for particular items in the feed, and which items have been read and which ones are new.

[Next - Considerations >](../example-manual-setup/considerations.md)