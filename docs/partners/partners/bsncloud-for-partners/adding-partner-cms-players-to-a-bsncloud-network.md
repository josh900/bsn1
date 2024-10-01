# Adding Partner CMS Players to a BSN.cloud Network

Players that are configured for a partner CMS application can also use a BSN.cloud network connection to access players for configuration and maintenance. To do this, temporary replace the partner CMS autorun with an *autorun*.*brs* that can make the changes needed to connect to BSN.cloud. This process is described below.

## Prerequisites

1.  You must be able to access the player on the local DWS through a browser.
    
2.  You must know the name of the target BSN.cloud network.
    
3.  You will need a registration token. See the Appendix for instructions.
    
4.  After getting the token, you must download the *cloudParameters.json* file from the Appendix and customize it:
    
    1.  Edit line 9 to add the registration token.
        
    2.  Edit line 10 to add the target network name, then save the file.
        

## Replace the Autorun and Reboot the Player

1.  Open the local DWS for the player you are adding to BSN.cloud and go to the **SD** tab.
    
    1.  Upload the *cloudParameters.json* file to the SD card.
        
    2.  Download and open the *standalone-autorun.brs* file in the Appendix. If you saved the *cloudParameters.json* file under a different name on the SD card, make sure that line 4 of *standalone-autorun.brs* references the correct name.
        
    3.  Upload the *standalone-autorun.brs* to the SD card.
        
2.  Go to the **SD** tab in the local DWS and locate the *autorun.brs* file.  
    
3.  Select the cogs icon, shown in Image 1, to go to the **Rename** section:
    
    1.  Rename *autorun.brs* to *autorun.backup*
        
    2.  Rename *standalone-autorun.brs* to *autorun.brs.*
        
4.  Go to the **Control** tab in the local DWS and reboot the player.
    
5.  The player will appear in the BrightAuthor:connected **Network** tab when it has rebooted, and the *autorun.brs* will again reference the partner CMS application.
    

![image-20240305-163734.png](./attachments/image-20240305-163734.png)

## Appendix

### BRS and JSON Files

[cloudParameters.json](./attachments/cloudParameters.json)
[standalone-autorun.brs](./attachments/standalone-autorun.brs)

### Getting a Registration Token through BSN.cloud

1.  Create a new setup package with BSN.cloud.
    
2.  Select **Save Setup** and choose a location to save the package on your computer.
    
3.  Open the folder where you saved the package and open the *current-sync.json* file.
    
    1.  At the top of the file you will find similar script to Image 2. The long string after `"bsnRegistrationToken"`, is your registration token. The string after “account” should match your target network name inserted in step 4c.
        

![Screenshot 2024-03-05 at 8.28.20 AM.png](./attachments/Screenshot%202024-03-05%20at%208.28.20%20AM.png)

### Getting a Registration Token through an API

First get your OAuth token correctly issued for the target network, then see [Token Entity (v3)](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1427013681/Token+Entity+v3).