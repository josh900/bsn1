# devicecustomization

This object provides a method to encrypt storage and is released in BOS version 9.0.146.

**devicecustomization IDL**

```
interface DeviceCustomization {
    Promise<void> encryptStorage(String device, StorageEncryptionOptions params);
};

interface StorageEncryptionOptions {
attribute String method;
attribute String passphrase;
attribute Boolean format;
};
```

## Object Creation

```
let DeviceCustomizationClass = require("@brightsign/devicecustomization");
let devicecustomization = new DeviceCustomizationClass();
```

## DeviceCustomization

##### encryptStorage()

```
Promise<void> encryptStorage(String device, StorageEncryptionOptions params)
```

Encrypts the contents of a storage device using an encryption key stored in the private section of the player registry. This prevents other devices from reading the names or contents of files on the storage device (though file metadata will still be readable). The storage device can still be mounted on other devices, which can list, delete, and copy files (even though they cannot read them).

The device parameter specifies which storage drive to encrypt (for example, `/storage/sd`, `/storage/usb1` or `/storage/ssd`), and the process is configured with the passed *StorageEncryptionOptions* parameters.

## StorageEncryptionOptions

##### Attributes

*   `method` string: The encryption method, which can be one of the following:
    
    *   `"none"`: Encryption is disabled and any encryption keys for the storage device are deleted from the registry. 
        
    *   `"passphrase"`: The storage device is encrypted using an un-obfuscated passphrase.
        
    *   `"obfuscated_passphrase"`: The storage device is encrypted using an obfuscated passphrase. Contact [support@brightsign.biz](mailto:support@brightsign.biz) to learn more about generating a key for obfuscation and storing it on the player. 
        
    *   `"brightsign_key"`: The storage device is encrypted using an encryption key that is common to all BrightSign players, but is not shared with outside parties. 
        
    *   `"generate_key"`: The storage device is encrypted using an encryption key that is generated on-demand using a secure random generator. The private registry of the player contains the only copy of the key; if the value in the registry is erased or becomes corrupted, there will be no way to recover data from that storage device. The private registry does not distinguish between different physical volumes of the same drive. For example, if you encrypt two SD cards, the key for the first SD card will be overwritten when the second SD card is encrypted; in the case of a randomly generated key, the data from the first SD card will be irretrievable.
        
*   `passphrase` string: The passphrase for encrypting the storage device. This parameter must be included if the method is specified as `"passphrase"` or `"obfuscated_passphrase"`. 
    
*   `format` boolean: Setting this parameter to `true` will cause the specified storage device to be reformatted–all existing files will be deleted (but are not guaranteed to be securely erased) before the device is encrypted; however, if the device cannot be reformatted, the operation will fail. If this parameter is set to `false`, the storage device will be mounted as if it has been previously encrypted using the supplied key.
    
    *   If the storage device hasn't been previously encrypted, it will be encrypted while leaving any preexisting files unencrypted. If the storage device has been encrypted using a different key, the operation will fail.
        
    *   If the `format` parameter is not specified, the storage device will be mounted as if it has been previously encrypted using the supplied key. If the storage device hasn't been previously encrypted, the operation will fail.