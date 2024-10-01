# Control.BSN.cloud

Control Cloud is a solution that allows partners to automate new player set up through Device Provisioning (also known as B-Deploy), monitor networks through BrightAuthor:connected, and examine problems through a remote diagnostic web server. This page will go over the basics on how to use these new features to manage BrightSign players in your network. The Control Cloud can be accessed through [control.bsn.cloud](http://control.bsn.cloud).

# Device Provisioning (B-Deploy)

Device Provisioning is a service that allows for automated provisioning of BrightSign players over the Internet. In order to use Device Provisioning, CMS partners need to provide and maintain an application URL on an accessible HTTP file server host. The package should be contained in an *autorun.zip* file containing presentation files along with an *autozip.brs* boilerplate script. In most cases, the script will not need to be modified.

Once the package has been hosted, device setups made through BrightAuthor:connected can point players directly to the application URL. Open BrightAuthor:connected and sign into BSN.cloud to select the cloud network desired. Under **Device Setup**, two options make use of externally hosted applications. The **Custom Application URL** option requires the link to be manually input into the field. The **Partner Application** option provides a drop down menu of applications that have been officially registered with Device Provisioning servers. To get an application URL added to the drop down, contact the Partner Integration team. Add the setup file to the library when done.

![](./attachments/SetupFigure.png)

Navigate through the **Admin** tab to **Device Provisioning**. From this page, select **Add Device** and enter the serial number of all players desired. This process will register the player to currently selected BSN.cloud network. From here, check mark the boxes of all players and apply the setup. Alternatively, clicking **Download Template** will download a Microsoft Excel file that contains columns for Serial Number, Device Name, Setup File, Application URL, and Description. The Excel sheet can be used to help expedite the process by adding multiple serial numbers simultaneously and automatically assigning them setup files and application URLs.

![](./attachments/ProvisioningFigure.png)

When everything is entered correctly, the player should automatically query the Device Provisioning servers when connected to the internet and powered on. The Device Provisioning servers will then assign the players the corresponding setup files and point to any application URLs entered, and the player will automatically configure itself and play any presentation files contained in the *autorun.zip*. For more information about Device Provisioning, please see [this page](#).

## Re-provisioning vs. Factory Resetting a Player

Cloud connected players should be re-provisioned rather than factory reset, if they must be refreshed.

> [!WARNING]
> ### Note
> If the player to be re-provisioned is currently configured on a network which requires a specification configuration (security, certificates, etc.) or is a Wifi player, chose **Use Current Device Settings** in **Device Setup > Network Configuration** on the bottom left to maintain your player's current network configuration.

Factory reset should only be used if you have local access to the player since it deletes all registry sections and clears network interfaces. The factory reset may leave a remote player in an inaccessible state (it would only be possible to factory reset a player and reconnect to BSN.cloud if the user has a "Device Provisioning" entry in BrightAuthor:connected, and their network allows a rogue device to retrieve an active ip address for a B-Deploy connection).

# Remote Diagnostic Web Server

Control Cloud also offers access to a remote diagnostic web server (DWS). Administrators can use the DWS to monitor the health of players on the network, as well as view and modify settings of any players over the Internet. To access the DWS, open BrightAuthor:connected through either the application or webtop service, or go to control.bsn.cloud and sign in. Select the **Network** tab to see all registered players on the network and their health status, then click the gear icon to the right of the desired player to enter the DWS.

From the **Info** tab, the DWS can provide basic info such as a snapshot of the time on the player, the model number, MAC address, IPv6 address, OS version, and up time.

![](./attachments/InfoFigure.png)

The **Log** tab provides a way to remotely download the player log for troubleshooting purposes

![](./attachments/LogFigure.png)

The **Control** tab allows admins to reboot the player with or without a crash report, factory reset the player, change the recovery URL, disable local DWS access, and reprovision the device remotely.

![](./attachments/ControlFigure.png)

The **SD** tab allows remote uploading of files directly to the SD card; however, the file size cannot exceed 10MB. 

![](./attachments/SDFigure.png)

The **Diagnostics** tab contains various diagnostic tools:

![](./attachments/DiagFigure.png)

1.  **Network Configuration** allows admins to view the network configuration selection of the player.
    
2.  **Network Neighborhood** allows admins to view information about the network neighborhood of the player.
    
3.  **Network Diagnostics** runs network diagnostics on the player.
    
4.  **Network Packet Capture** allows admins to set up a network packet capture. The packet capture can be over ethernet, WiFi, or 3G modem. File sizes exceeding 10MB cannot be downloaded.
    
5.  **DNS Lookup** allows admins to test name resolution on a DNS hostname.
    
6.  **Disable Autorun** disables the currently run script and reboots the player.
    
7.  **Ping** pings an IP address.
    
8.  **Storage Formatting** formats the SD inserted in the player.
    
9.  **Trace Route** performs route tracing on an IP address or hostname.
    

The **Snapshot** tab can pull a real-time snapshot of the content being displayed by the player.

![](./attachments/SnapshotFigure.png)

The **Video** tab displays the current video mode and allows manual adjustment if required, as well as toggle the **Power Save** option.

![](./attachments/VideoFigure.png)

The **Advanced** tab provides a registry dump and the ability to update the OS of the player.

![](./attachments/AdvancedFigure.png)