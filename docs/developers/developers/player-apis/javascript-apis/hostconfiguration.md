# hostconfiguration

The *hostconfiguration* object allows you to retrieve information about network interfaces and Internet connectivity.

**hostconfiguration IDL**

```
interface NetworkHost {
    HostConfig defaultConfig();
    Promise<HostConfig> getConfig();
    Promise<void> applyConfig(HostConfigWritable config);
};

interface HostConfig {
    [optional] attribute String proxy;
    [optional] attribute Array<String> proxyBypassList;
    [optional] attribute Array<String> timeServerList;
    [optional] attribute String timeServerInterval;
    [optional] attribute String hostName;
	[optional] attribute bool loginPassword;
    [optional] attribute bool forwardingEnabled;
    [optional] attribute bool masqueradingEnabled;
	[optional] attribute Array<NatRule> natList;
};

interface HostConfigWritable : HostConfig {
    [optional] attribute String[or bool] loginPassword;
    [optional] attribute String[or bool] obfuscatedLoginPassword;
};

interface NatRule {
    attribute NatRuleMatch match;
    attribute NatRuleReplacement replace;
};

interface NatRuleMatch {
    attribute String protocol;
    [optional] attribute String sourceAddressRange;
    attribute String destinationAddressRange;
    attribute unsigned short destinationPort;
};

interface NatRuleReplacement {
    attribute String destinationAddress;
    attribute unsigned short destinationPort;
};
```

## Object Creation

To create a *hostconfiguration* object, first load the `brightsign/hostconfiguration` module using the `require()` method. Then create an instance of the *hostconfiguration* class.

```
var HostConfigurationClass = require("@brightsign/hostconfiguration");
var hc = new HostConfigurationClass();
```

## NetworkHost

Use this interface to retrieve and modify host configuration.

##### getConfig()

```
Promise<HostConfig> getConfig() 
```

Returns a `HostConfig` interface containing current host-configuration information.

##### applyConfig()

```
Promise<void> applyConfig(HostConfigWritable config)
```

Applies host-configuration settings to the player. This method accepts a `HostConfigWritable` interface.

The `config` parameter should contain the complete desired configuration. Any previous configuration is overwritten. If you wish to change one item while keeping the rest of the configuration the same, then call `getConfig` and modify the returned object (see the example in the Examples section).

## HostConfig

This interface contains host configuration parameters:

*   `proxy` String:  The name or address of the proxy server used for HTTP and FTP requests. The proxy string should be formatted as "[http://user:password@hostname:port](http://user:password@hostnameport)". The hostname can contain up to four "\*" characters; each "\*" character can be used to replace one octet from the current IP address. For example, if the IP address is currently 192.168.1.2, and the proxy is set to "proxy-\*-\*", then the player will attempt to use a proxy named "proxy-192-168".
    
*   `proxyBypassList` Array<String>: A list of hostnames exempted from the proxy setting. The player will attempt to reach the specified hosts directly rather than using the proxy specified in the `proxy` attribute. For example, the hostname "[example.com](http://example.com)" would exempt "[example.com](http://example.com)", "[example.com](http://example.com):80", and "[www.example.com](http://www.example.com)" from the proxy setting.
    
*   `timeServerList` Array<String>: An array containing zero or one time servers to be used by the player. An empty array disables automatic setting of the player's clock. A single entry indicates the time server and protocol that should be used as a URL. Supported protocols are HTTP, HTTPS and NTP. For backward-compatibility the use of just a host name is supported and indicates that NTP should be used. Note that when using HTTPS, host and peer verification are disabled since the player clock may not be correct. The following are valid time server addresses:
    
    *   [http://time.brightsignnetwork.com/](http://time.brightsignnetwork.com/)
        
    *   [https://time.brightsignnetwork.com/](https://time.brightsignnetwork.com/)
        
    *   [ntp://time.brightsignnetwork.com/](#)
        
    *   [time.brightsignnetwork.com](http://time.brightsignnetwork.com/)
        
*   `timeServerInterval` String: A value specifying how often (in seconds) the player should communicate with the time server to adjust its clock. The default interval is 12 hours. The minimum interval allowed is 120 seconds.
    
*   `hostName` String: The player host name. If no host name has been explicitly set, then a host name is automatically generated based on the device serial number. Passing an empty string to this method resets the device host name to its automatically generated value.
    
*   `loginPassword` bool: A value of true means that the password exists, false means that there is no password.
    
*   `forwardingEnabled`  bool: A flag that enables or disables IP forwarding. IP forwarding is disabled (false) by default.
    
*   `masqueradingEnabled` bool: A flag that enables or disables source address translation with IP forwarding. If `forwardingEnabled` is true, `masqueradingEnabled` must be specified as true or false:
    
    *   If `masqueradingEnabled` is false, IP datagrams are forwarded between all interfaces and no address translation is done. 
        
    *   If `masqueradingEnabled` is true, IP datagrams are forwarded between all interfaces, but [SNAT](https://ipwithease.com/snat-vs-dnat/) is applied to any datagrams which are sent out of an "upstream" interface (any interface or interfaces on which a default route is set). Datagrams destined for an interface that has no default route are forwarded without [NAT](https://ipwithease.com/snat-vs-dnat/). 
        
*   `natList` Array<NatRule>:  A list of [DNAT](https://ipwithease.com/snat-vs-dnat/) rules which lets users change the destination address and port of a packet.
    

## HostConfigWritable

This interface contains password settings for SSH. When writing settings using the `applyConfig()` method, some members of the `HostConfig` interface have special behavior.

*   `loginPassword` String or bool :
    
    *   If a string is supplied, sets a plain-text login password for the SSH connection (note that SSH must also be enabled separately in the registry for this to be useful).
        
    *   If boolean `True` is supplied, the existing password (if any) is left unchanged.
        
    *   if boolean `False` is supplied, any existing password is removed.
        
*   `obfuscatedLoginPassword` String or bool :
    
    *   As above, except that the password should previously have been obfuscated using a shared secret. Contact [support@brightsign.biz](mailto:support@brightsign.biz)![](https://jira.brightsign.biz/images/icons/mail_small.gif)
        
         to learn more about generating a key for obfuscation and storing it on the player.
        

This behavior ensures that code such as `getConfig().then((c) => { applyConfig(c); })` preserves any existing password, even though the password itself is not returned by `getConfig()`.

## NatRuleMatch

The rules in this interface are compared to destinations in the TCP or UDP packets that enter the player. If the packet fields match the properties established in `NatRuleMatch`, the destination IP and port will be overwritten with the desired values in the `NatRulesReplacement` interface.

*   `protocol` String: Filter for "udp" or "tcp" (the entry must be lower case).
    
*   `sourceAddressRange` String optional:  Filter for this range of source IP addresses (in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20introduced%20a%20new%20method,db8%3A%3A%2F32%20for%20IPv6.) format). Traffic from all source IP addresses will be included if this optional attribute is not specified. 
    
*   `destinationAddressRange` String: The range of destination IP addresses (in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20introduced%20a%20new%20method,db8%3A%3A%2F32%20for%20IPv6.) format) to be overwritten.
    
*   `destinationPort` unsigned short: The destination port to be overwritten.
    

## NatRuleReplacement

The address and port properties specified in `NatRuleReplacement` are written to the packet to replace selected IP address and port properties. 

*   `destinationAddress` String : The IP address that will replace the previous IP address in the destination.
    
*   `destinationPort` unsigned short:  The port that will replace the previous port in the destination.
    

## Examples

The following script uses the `applyConfig()` method to set the hostname, time server, and time-server refresh interval:

```
var HostConfigurationClass = require("@brightsign/hostconfiguration");
var hc = new HostConfigurationClass();

var configData = {};
configData.hostName = "myplayer";
configData.proxy = "";
configData.proxyBypassList = [];
configData.timeServerInterval = 1200;
configData.timeServerList = ["time.brightsignnetwork.com"];

console.log("***Configuring Host***")
hc.applyConfig(configData).then(
        function() {
            console.log("Success");
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        }); 
```

To change one item while keeping the rest of the configuration the same, call `getConfig` and modify the returned object:

```
  var HostConfiguration = require('@brightsign/hostconfiguration');
  var hostConfiguration = new HostConfiguration;
  hostConfiguration.getConfig()
  .then(function(config) {
    config.hostName = "host-brightsign";
    hostConfiguration.applyConfig(config);
  })
  .then(function() {
    console.log("Success");
  })
  .catch(function(error) {
    console.log(`${JSON.stringify(error)}`);
  });
```