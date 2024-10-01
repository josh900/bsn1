# Postman Collections

[BSN%20Control%20Cloud.postman_collection.json](./attachments/BSN%20Control%20Cloud.postman_collection.json)
[bsn-control-cloud-production.postman_environment.json](./attachments/bsn-control-cloud-production.postman_environment.json)

# Control Cloud Library

The Postman library for BSN Control Cloud allows you to quickly familiarize yourself with the different APIs and processes associated with a BSN Control Cloud subscription. Follow the below steps to create a person/network, create a player setup, and provision a player on your network with the player setup.

> [!WARNING]
> This is a collection of sample endpoint calls to introduce users to our infrastructure.
> It is not a comprehensive document of our available endpoints. Please see the [BSN.cloud](../cloud-apis/bsncloud-main-apis.md), [Remote DWS](../../developers/local-and-remote-diagnostic-web-server-apis/remote-dws-apis.md), and [B-Deploy](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/378831792/B-Deploy+Device+Provisioning) endpoint documentation for a complete list of those endpoints and their usage.

## Prerequisites

*   A client ID and client secret (provided by BrightSign)
    
*   Postman
    
*   The BSN Control Cloud Library collection and bsn-control-cloud-production environment 
    
*   A BrightSign player with an active internet connection
    

## Steps

1.  Import both the Control Cloud Library collection and the bsn-control-cloud-production environment into Postman.
    
2.  Set the Postman environment to bsn-control-cloud-production using the dropdown menu in the top right.
    
3.  Select the "eye" icon and select **Edit** to edit the following variables (other variables will get their values from Postman scripts):
    
    ![Screenshot 2024-01-05 at 11.30.43 AM.png](./attachments/Screenshot%202024-01-05%20at%2011.30.43%20AM.png)
    
    *   **partnerLogin**: The email address to use for your BSN.Cloud person credentials
        
    *   **partnerEmail**: This email address, which should be the same as the Partner Login for now
        
    *   **partnerFirstName**: Your first name
        
    *   **partnerLastName**: Your last name
        
    *   **networkName**: The name of the BSN.cloud network to create. This name must be unique within the BSN.cloud database. You can change this value later if you want to create multiple networks (for example, for different customers).
        
    *   **clientId**: Provided by BrightSign
        
    *   **clientSecret**: Provided by BrightSign
        
    *   **playerSerial**: The serial number of the player to provision on your BSN.cloud network.
        
    *   **playerModel**: The model number of the player (for example, "XD1034")
        
    *   **deviceName**: The device name, which can be arbitrary
        
    *   **setupName**: The player setup name, which can be arbitrary
        
    *   **userAccessTokenLifetime**: The amount of time that a full access token for a network remains valid (the default is 15 minutes).
        
4.  Go to **BSN > User/Self > POST Self**. Select **Send** to register with BSN.cloud. This call also returns your person credentials and an auto-generated password, which Postman will store.
    
5.  Verify your email address:
    
    *   BSN.cloud will send an email to your email address. This may take a few minutes.
        
    *   Select the link in the email to verify the address.
        
    *   You don't need to follow the additional steps to create a network since these steps will be performed using APIs below.
        
6.  Select the **Token (Self)** call in the root of the library. Select **Send** to get a "Self" auth token, which Postman will store.
    
7.  Go to **BSN > User/Self > POST Self/Networks**. Select **Send** to create a BSN.cloud network with your credentials as the network owner.
    
8.  Select the **Token (Full)** call in the root of the BSN Control Cloud Library. Select **Send**.
    
    *   The server will return a "Full" auth token, stored in Postman, which will give you access to the network you created.
        
    *   To renew the "Full" access token, repeat this step. The default timeout for the token is 15 minutes.
        
9.  Select the **Token (device registration)** call in the root of the BSN Control Cloud Library. Select **Send**.
    
    *   The server will return a "device registration" auth token, which Postman will store.
        
    *   The "device registration" token is separate from a user token and allows players to provision themselves for a certain network.
        
10.  Go to **B-Deploy > POST /setup/**. Select **Send** to post a setup to the B-Deploy server and get the setup ID, which Postman will store.
    
11.  Go to **B-Deploy > POST /device/**. Select **Send**. Your device serial number is now associated with the ID of the device setup you created in the previous step.
    
12.  Power on or reboot your player. The player will reboot several times while provisioning itself for your network.
    
13.  Go to **BSN > Devices > GET Devices**. Select **Send** to get a list of the players on your network.
    
14.  Go to **Remote DWS > GET /info/**. Select **Send** to get player information.