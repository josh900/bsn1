# Updating BOS from HTML/JavaScript Applications

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Accessing the BOS](#accessing-the-bos)
*   [Installing the Update](#installing-the-update)
    *   [Code Requirements](#code-requirements)
    *   [Selecting a Download Location](#selecting-a-download-location)
*   [Example](#example)
*   [Checking the BOS](#checking-the-bos)

BrightSign partners who use HTML/JavaScript applications (and do not use the BrightAuthor:connected interface) can follow the steps outlined below to update to the latest BOS. 

## Accessing the BOS

1.  Go to the [Downloads](http://www.brightsign.biz/downloads/overview/) section of our website or to [Previous-BOS-Releases](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2165178386/Previous+BOS+Releases) to download the BOS version you want. 
    
2.  Click the **Download** button on the download page that corresponds with the model number of your BrightSign player. Note that BOS versions for different model families are often designated with the same number, but they are different files. Make sure to use only the update file that corresponds to the model number of your BrightSign player.
    
3.  Unzip the downloaded file.
    
4.  Put the *.bsfw* file in your known URL location.
    

Contact [support@brightsign.biz](mailto:support@brightsign.biz) if you need help creating an URL for the correct BOS release.

## Installing the Update

To install the update, your code must download the BOS update into the root directory of an attached storage device (where the OS will look for it during a reboot) and reboot the player after the download. You may also want to add a check to see if the BOS has been downloaded correctly.

### Code Requirements

1.  Specify the correct OS version and *.bsfw*  from the downloaded URL.
    
2.  If you know where to download the update, specify that location in your code. If not, the code must "decide" where to write the BOS update file. See "Selecting a Download Location" for more guidance.
    
3.  Download the BOS. You can use the `downloadFile()` function and and the `node-fetch` module or your own preferred method.
    
4.  To call the reboot function after download, use the [*@brightsign/system*](https://docs.brightsign.biz/display/DOC/system) API.
    
5.  You can use the [*@brightsign/deviceinfo*](https://docs.brightsign.biz/display/DOC/deviceinfo) API to make sure the BOS was downloaded correctly on the device.
    

### Selecting a Download Location

You can use any writable storage device with sufficient space, but we recommend that you implement a search order which prefers a faster or more durable device (prioritize a plugged in USB stick over other storage, while the primary SD should take precedence over the secondary SD, and an SD card the user plugs in should take precedence over an SSD). For example:

1.  */storage/usb1* (the drive for USB storage devices connected to the player)
    
2.  */storage/sd* (the primary SD or microSD drive on the player)
    
3.  */storage/sd2* (the internal microSD drive on the player for 4Kx42, XDx32 models)
    
4.  */storage/ssd* (the internal SSD on the player for XTx44, XTx43, XDx34, and XDx33 models)
    

Have your script iterate over all the mountpoints in */storage* (skipping anything that's not a mountpoint, or is a tmpfs, or is read-only) looking for a drive with enough space.

## Example

This code is for illustration purposes only. A production implementation should also contain steps to handle errors, data overflow, write-protected storage devices, etc.

If you want to run it, you'll need to have Node.js enabled in your browser runtime. You should also edit it to point to the correct:

*   `osYouWant:` The correct OS version
    
*   `fwName:` The *.bsfw* filename of the OS
    
*   `URL:` The OS URL ([https://bsncloud.s3.amazonaws.com/public](https://bsncloud.s3.amazonaws.com/public/) is the public URL that stores BrightSign .bsfw files).
    
*   `devicePath:` Write the OS update to this storage device  
    

```
// Fetch the BOS url.
let fs = require("fs")
let path = require("path")
let fetch = require("node-fetch");

const systemClass = require("@brightsign/system");
let system = new systemClass();
const diClass = require("@brightsign/deviceinfo");
let di = new diClass();

// Use the information in the hardcoded URL to specify the osYouWant and fwName variables.
let osYouWant = '8.2.82'
let fwName = 'malibu-8.2.82-update.bsfw'
let url = 'https://bsncloud.s3.amazonaws.com/public/malibu-8.2.82-update.bsfw';
let devicePath = '/storage/sd/'+fwName;


const downloadFile = (async (url, path) => {
  const res = await fetch(url);
  const fileStream = fs.createWriteStream(path);
  await new Promise((resolve, reject) => {
      res.body.pipe(fileStream);
      res.body.on("error", (err) => {
        reject(err);
      });
      fileStream.on("finish", function() {
        resolve('success');
      });
    });
});

 
function main(){
  if (di.osVersionCompare(osYouWant) != 0) {
    downloadFile(url, devicePath).then(() => {
        console.log(`${osYouWant} has been downloaded successfully!`)
        system.reboot();
    })
    .catch((err) => {
        console.log(err)
    })
  }
  else{
    console.log(`You have gotten the right OS ${osYouWant} you want!`)
  }
}

main();
```

## Checking the BOS

After the player reboots, check the BrightSign BOS version in the [BrightAuthor:connected DWS](https://docs.brightsign.biz/display/DOC/Diagnostic+Web+Server#DiagnosticWebServer-Infoinfo) to make sure that it is updated to the correct version.