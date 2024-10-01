# IGMP Behavior

In OS version 8.0.84, players accept a `force_igmp_version` registry entry in the networking section. This entry allows for customization of the player response to the IGMP network environment. It can have the following values:

*   0: The default behavior. The player will use IGMPv3 unless a querier with an older version is present, in which case the player will fall back to v2 or v1.
    
*   1: The player will always use IGMPv1.
    
*   2 : The player will use IGMPv2 if possible, but will fall back to v1 if an older querier is present.
    
*   3 : The player will only use IGMPv3 and will not fall back to v1 or v2.
    

### Example

This is a simple example which sets the value to 1. You will have to reboot the player to see registry changes. See BrightScript [roRegistry](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673016) or JavaScript [registry](../../developers/player-apis/javascript-apis/registry.md) for more details.

```
var registryClass = require("@brightsign/registry");
var registry = new registryClass();
 
//Writes to the registry, forcing the player to always use IGMPv1
registry.write({networking:{force_igmp_version:"1"}}).then(
	function(){console.log("Write Successful");});
```