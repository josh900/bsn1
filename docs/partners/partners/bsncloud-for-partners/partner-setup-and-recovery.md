# Partner Setup and Recovery

You can use the 1.6.52 or higher version of the BrightAuthor:connected / BSN.cloud autorun to download a partner setup to your local PC and place it on an SD card. This is useful for advanced network configurations that require the player to be able to reach the internet to download the partner application. You can also set up a recovery URL if, for example, your SD card was corrupted and needs either reformatting or replacement (the player is not automatically configured for recovery in this workflow, unlike the B-Deploy workflow). If you have a lot of players, you can use the [Download Template / Upload Provisioning File](#PartnerSetupandRecovery-Provision) workflow to do this.

> [!WARNING]
> You must disable the autorun before reformatting the SD card on your device.
> To disable the autorun, use the PUT API /v1/control/reboot with body parameter { “autorun”:”disable” }, as described in [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/378831527/Remote+DWS+APIs#RemoteDWSAPIs-%2Fcontrol%2Freboot%2F). This can also be done in the local DWS Diagnostics tab.

To save your setup package to an SD card through BrightAuthor:connected:

1.  Choose the **Partner Application** setup type, and select any partner (see Image 1).
    
2.  Select **Save Setup Files** so that the package can be saved to the SD card
    
3.  Factory reset the player
    
4.  Install the SD card
    
5.  Reboot the player
    

Next, set up a recovery URL for your partner application: 

1.  In BrightAuthor:connected, go to **Admin > Device Provisioning > Add Device** 
    
2.  Add your device serial number and check the box next to your player in the list
    
3.  In the **Actions** dropdown, choose **Apply Application**
    
4.  Choose **Partner Applications** and add the partner you previously selected.
    
5.  Select **Apply**
    

![](./attachments/Screen%20Shot%202022-06-14%20at%203.55.12%20PM.png)