# configurednetworks

The *configurednetworks* object provides an array of persistent configuration names, even if they are not active at present. The configurations may be accessed using *@brightsign/networkconfiguration* objects.

**configurednetworks IDL**

```
interface ConfiguredNetworks {
    Promise<Array<String>> getConfigurationNames();
};
```

## Object Creation

To create a *configurednetworks* object, load the *@brightsign/configurednetworks* module using the `require()` method:

```
var configurednetworksClass = require("@brightsign/configurednetworks");
var configurednetworks = new configurednetworksClass();
```

## ConfiguredNetworks

##### getConfigurationNames()

```
Promise<Array<String>> getConfigurationNames()
```

This method returns an array of persistent configuration names, even if they are not active at present.