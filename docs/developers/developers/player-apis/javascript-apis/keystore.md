# keystore

The *keystore* object allows you to register client certificates with the player.

While CA packages (added using the `AddCAPackage()` method) are persistent, individual certificates (added using the `AddCACertificate()` and `AddClientCertificate()` methods) are not; individual certificates must be registered with the certificate database after each reboot.

**keystore IDL**

```
interface KeyStore {
    Promise<void> addCaCertificate(String filename);
    Promise<void> addCaPackage(String filename);
    Promise<void> removeCaPackage(String filename);
    Promise<PackageList> getCaPackagesInstalled();
    Promise<void> addClientCertificate(ClientCertificateObject object);
};

interface ClientCertificateObject {
    attribute String certificateFile;
    attribute String passphrase;
    attribute String obfuscatedPassphrase;
};

```

## Object Creation

To create a *keystore* object, first load the `brightsign/keystore` module using the `require()` method. Then create an instance of the *keystore* class.

```
var keystoreClass = require("@brightsign/keystore");
var keystore = new keystoreClass();
```

## KeyStore

Use this interface to add certificates to the certificate database.

##### addCaCertificate()

```
Promise<> addCaCertificate(DOMString filename)
```

Registers the specified CA certificate with the certificate database. Client certificates can be either self-signed or signed using a 3rd-party certificate issuer (Versign, DigiCert, etc.). 

> [!WARNING]
> Chromium version 69 or later will refuse SHA-1 certificates. See [this page](https://www.chromium.org/Home/chromium-security/education/tls/sha-1/) for more information.

##### addCaPackage()

```
Promise<> addCaPackage(DOMString filename)
```

Adds the specified CA package file to the certificate database. The package name resides in the file and does not need to be the same as the filename. See the [*roKeyStore*](../../../developers/brightscript/object-reference/networking-objects/rokeystore.md) page for more information on generating CA packages.

> [!NOTE]
> Attempting to modify a CA package file that has been added to the database will invalidate it. If a package is invalidated, it will need to be removed from the database (using the r`emoveCaPackage()` method) and added again.

##### removeCaPackage()

```
Promise<> removeCaPackage(DOMString filename)
```

Removes the specified CA package from the certificate database. Use the g`etCaPackagesInstalled()` method to retrieve a list of package names in the database.

##### getCaPackagesInstalled()

```
Promise<PackageList> getCaPackagesInstalled()
```

Returns a list of names of CA packages contained in the certificate database.

##### addClientCertificate()

```
Promise<> addClientCertificate(ClientCertificateObject object)
```

Registers a .p12 client certificate with the certificate database. 

## ClientCertificateObject

This interface represents a .p12 certificate file.

*   `certificateFile` String: The file name and path of the .p12 client certificate
    
*   `passphrase` String:  A passphrase for the .p12 client certificate
    
*   `obfuscatedPassphrase` String: An obfuscated passphrase for the .p12 client certificate
    

> [!CAUTION]
> **Important**
> Only one of `obfuscatedPassphrase` and `passphrase` is required, and `obfuscatedPassphrase` takes priority if both are present. We recommend using `obfuscated_passphrase` in production environments, while `passphrase` should be used for testing purposes only. Contact [support@brightsign.biz](mailto:support@brightsign.biz) to learn more about generating a key for obfuscation and storing it on the player.

## Example

```
ksf = require('@brightsign/keystore');
k = new ksf()
k.addCaPackage("/storage/sd/example.bsca").then(() => console.log('ok'), () => console.log('failed'))
k.getCaPackagesInstalled().then((pkgs) => console.log(pkgs))
k.removeCaPackage('example').then(() => console.log('ok'), () => console.log('failed'))
```