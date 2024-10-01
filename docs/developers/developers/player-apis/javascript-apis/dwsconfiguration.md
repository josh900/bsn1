# dwsconfiguration

The *dwsconfiguration* object allows you to configure the [Diagnostic Web Server](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server) (DWS) on the player. By default, the Diagnostic Web Server is enabled on port 80, with the player serial number as password. The username is always "admin".

**dwsconfiguration IDL**

```
[
   GarbageCollected,
] interface DWS {
    DWSConfig defaultConfig();
    Promise<DWSConfig> getConfig();
    Promise<DWSResult> applyConfig(DWSConfigWritable config);
};

interface DWSConfig {
    attribute int port;
    attribute Password password;
    attribute Array<String> authenticationList;
};

interface DWSConfigWritable : DWSConfig {
    attribute Password password;
};

interface Password {
    attribute String value;
    attribute bool obfuscated;
};

interface DWSResult {
    attribute bool restartRequired;
};
```

## Object Creation

To create a *dwsconfiguration* object, first load the `brightsign/dwsconfiguration` module using the `require()` method. Then create an instance of the *dwsconfiguration* class.

```
var DWSConfigurationClass = require("@brightsign/dwsconfiguration");
var dwsConfig = new DWSConfigurationClass();
```

## DWS

Use this interface to retrieve and modify the DWS configuration.

##### getConfig()

```
Promise <DWSConfig> getConfig() 
```

Returns a `DWSConfig` interface containing current DWS-configuration information. If there is a set password, `getConfig()` will return True for the `password` parameter. If there isn't a set password, If there is a set password, `getConfig()` will return False for the `password` parameter.

##### applyConfig()

```
Promise <DWSResult> applyConfig(DWSConfigWritable config) 
```

Applies DWS-configuration settings to the player. This method accepts a `DWSConfig` interface. It returns a `DWSResult` interface that indicates whether or not a reboot is required for the changes to take effect (the caller is responsible for requesting the reboot). The `restartRequired` property of the `DWSResult` indicates whether the reboot is required.

The `config` parameter should contain the complete desired configuration. Any previous configuration is overwritten. If you wish to change one item while keeping the rest of the configuration the same, then call `getConfig` and modify the returned object (see the example in the Examples section).

## DWSConfig

This interface contains DWS configuration parameters:

*   `port` int: The port number of the DWS, located at the IP address of the player. The default for the DWS is port 80. Setting this value to 0 will disable the DWS. 
    
*   `password` Password: A `Password` interface containing password settings for the DWS. To enable the DWS without password protection, set `value` to an empty string and `obfuscated` to false.
    
*   `authenticationList` Array<String>: The authentication scheme for the DWS password. This entry currently accepts a single value only. The following are accepted values:
    
    *   `"basic"`: The password will be validated using basic authentication.
        
    *   `"digest"`: The password will be validated using digest access authentication.
        

> [!NOTE]
> **Note**
> To enable the DWS without password authentication, set the `password.value` to be an empty string and `password.obfuscated` to be false, when calling the `applyConfig()` method.

## DWSConfigWritable

*   `password` Password: A `Password` interface containing password settings for the DWS
    

## Password

This interface contains password settings for the DWS:

*   `value` String: The DWS password
    
*   `obfuscated` bool: A flag indicating whether the password string is obfuscated. Contact [support@brightsign.biz](mailto:support@brightsign.biz) to learn more about generating a key for obfuscation and storing it on the player.
    

## DWSResult

This interface contains results from an `applyConfig()` operation.

*   `restartRequired` bool: A flag indicating whether a reboot is required for changes to go into effect (the script must perform the reboot)
    

## Examples

```
var DWSConfigurationClass = require("@brightsign/dwsconfiguration");
var dwsConfig = new DWSConfigurationClass();

var configData = {};
var pw = {};

configData.port = 1010;
configData.password = pw;
configData.authenticationList = ["basic"];

pw.value = "password";
pw.obfuscated = false;

dwsConfig.applyConfig(configData).then(
        function(data) {
            console.log(JSON.stringify(data));
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        });
dwsConfig.getConfig().then(
        function(data) {
            console.log(JSON.stringify(data));
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        });
```

To change one item while keeping the rest of the configuration the same, then call `getConfig` and modify the returned object:

```
  var DWSConfigurationClass = require("@brightsign/dwsconfiguration");
  var dwsConfig = new DWSConfigurationClass();
  var pw = {};
  dwsConfig.getConfig()
  .then(function(config) {
    pw.value = "password";
    pw.obfuscated = false;
    config.password = pw;
    dwsConfig.applyConfig(config);
  })
  .then(function() {
    console.log("Success");
  })
  .catch(function(error) {
    console.log(JSON.stringify(error));
  });
```