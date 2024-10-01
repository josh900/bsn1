# BrightScript Encryption

BrightScript supports encrypted modules. In order to use encrypted BrightScript, make sure that the players are running OS 8.1.54 or newer.

To encrypt your BrightScript modules, first contact BrightSign and request an encryption key. BrightSign will generate a new unique key pair and provide `customer-pub.pem` and `customer.hdr`. Once those two items are in your possession, encrypt your BrightScript files using the following process:

```
$ encrypt-brightscript --customer-public-key=customer-pub.pem --encrypted-key-data=customer.hdr myscript.brs
```

This will generate `myscript.ebrs` which is the encrypted version of the script.

> [!NOTE]
> Any .brs file can be encrypted, including those loaded with LIBRARY. Additionally, if any encrypted file is loaded, the BrightScript debugger is disabled for security reasons.