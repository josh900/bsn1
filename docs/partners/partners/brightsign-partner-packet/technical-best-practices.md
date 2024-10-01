# Technical Best Practices

To assist partners in getting up and running as efficiently as possible, we’ve compiled a list of technical best practices to maximize your chances of success.

## brightsign-dumps Folder

When developing your own autoruns, do not forget to include instructions for the autorun to create a *brightsign-dumps* folder on the player. The *brightsign-dumps* folder is used to store crash information and is very useful to BrightSign support when troubleshooting.

## Free Tools

BrightSign offers a plethora of free tools and services that greatly ease provisioning and diagnostics. These include the powerful tools available via bsn.Control for player provisioning as well as the many tools described in the [Developer Tools](../brightsign-partner-packet/integrating-with-brightsign/developer-tools.md) section of this guide. Partners are highly encouraged to take as much advantage of these tools as possible as it accelerates development and also makes support and troubleshooting much easier.

## Memory Management

BrightSign players are purpose-built for digital signage. Players are not general-purpose devices and they do not have, nor do they require, as much memory as a typical Mac or PC. When developing for the BrightSign platform, developers should be cognizant of potential memory limitations that they may not be accustomed to.

## OS Updates

Partners should try to use the latest BrightSignOS builds in order to take advantage of the latest bug fixes and newest features. Keeping up to date with the latest OS build also enables partners to more easily expand their deployments with our latest hardware.

We are continuously improving the firmware on our players, but as is often the case with software, problems are sometimes inadvertently introduced. A stable player is paramount to any BrightSign integration, so we strongly encourage partners to thoroughly test any BrightSign firmware releases prior to upgrading any players being used in a production environment.

## HTML <video> Elements & Memory

It is fairly common for a presentation to include switching from one video to another. In many BrightSign players, including the Series 4 line, if a video element is not explicitly released, that element will continue to use memory even if it is no longer actively displaying. It is therefore important to reset the source to blank prior to switching videos. If this is not done, the first video(s) will continue to use memory while subsequent videos are playing, potentially resulting in the following log message:

`Failed to find a video decoder`

To release the video element, the `src` attribute of the `<video>` should be set to blank:

`video.src = "";`

Additional detail on this topic can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370672326/HTML+Video#Multiple-Video-Elements).

## Smooth Video Transitions

If multiple videos are being displayed sequentially, it is generally desired for one video to transition smoothly into the other one. To help ensure this, make sure that both the first and last frames of the videos do not consist of a blank frame. The presence of even one blank frame between videos can result in a noticeably jarring transition between videos.

## Upgradeability

Change is inevitable so partners are recommended to design their apps with the ability to push updates to players remotely. This applies not only to the partner app itself, but also to diagnostic scripts which can be very useful for troubleshooting.

[Next - Operational Best Practices >](../brightsign-partner-packet/operational-best-practices.md)