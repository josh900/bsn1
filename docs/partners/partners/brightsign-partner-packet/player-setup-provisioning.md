# Player Setup / Provisioning

> [!INFO]
> bsn.Control and bsn.Content were formerly named Control Cloud and Content Cloud, respectively.

## Player Setup

As covered in the [Start Here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1968472149/Start+Here) section, new players must first be set up before they can do much of anything. This process involves applying a **Setup** to the player. The Setup applies various settings to the player (network settings, Publishing Mode, logging, etc.) and includes a **Player App** which provides instructions for what the player should do upon startup.

![image-20240404-165839.png](./attachments/image-20240404-165839.png)

## Player Provisioning

As was also mentioned in the [Start Here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1968472149/Start+Here) section*,* the term *provisioning* refers to using BSN.cloud to set up a player, and given that BSN.cloud (either the bsn.Control or bsn.Content tiers) is used the vast majority of time to set up players, the term provision is often used when referring to player setup.

The primary cases where a player can be properly set up instead of provisioned (i.e., BSN.cloud is not used to apply the Setup to the player) are:

*   Standalone player configurations where the Setup is manually copied to a storage device and then the storage device is connected to a player.
    
*   Uncommon situations where a partner chooses to set up players without using BSN.cloud.
    

With BSN.cloud, provisioning a new player can be nearly automatic - if things are properly set up beforehand, new players can be automatically provisioned just by plugging them in! For customers who can’t or don’t want to connect their players to the internet, offline provisioning options are also available.

> [!INFO]
> Provisioning of players can be done for free using either BrightAuthor:connected or the unbranded bsn.Control interface at control.bsn.cloud. However, since control.bsn.cloud is the interface preferred by most partners, this guide will largely focus on using control.bsn.cloud.

## Setup

Setups can be created using the free and unbranded bsn.Control interface at control.bsn.cloud. Setups can be saved to the [Setup Library](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/395313604/Setup+Library) to be used or modified in the future.

Once created, Setups can be applied to a player or group of players using control.bsn.cloud. Alternatively, the information contained in a Setup can be directly incorporated into the Player App (described below) and manually copied to the player’s storage device.

### Player Settings

The Setup establishes various player settings which include things like [Publishing Mode](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1968078934/Player+Setup+Provisioning#Publishing-Mode), network settings (Ethernet, WiFi, etc.), player identification (name and description), logging, and more.

### Player App

The set of files and folders that instruct the player what to do upon boot up is collectively known as the Player App. At a minimum, the Player App must contain an *autorun.brs* file (the .brs extension denotes a BrightScript file) which instructs the player what to do upon startup.

When a Setup is applied to a player via BSN.cloud, an autorun.brs file is automatically created on the player.

Partners can write custom Player Apps according to their specific needs. For example, the Player App may be designed to connect to the partner CMS to download content from the CMS for the player to display.

> [!INFO]
> The term Partner App may sometimes be used when referring to the partner’s Player App.

More info about Setups can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/395313598/Setup) and more info about provisioning can be found [here](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/395313614/Provision).

[Next - Player Provisioning and Recovery System Requirements >](./player-setup-provisioning/player-provisioning-and-recovery-system-requirements.md)