# roDeviceCustomization

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This object provides miscellaneous device configuration and customization methods.  

## ifFailureReason

##### GetFailureReason() As String

Returns helpful information if one of the *ifDeviceCustomization* methods fail.

## ifDeviceCustomization

##### WriteSplashScreen(filename As String) As Boolean

Removes the default splash screen (or a previously set splash screen) and replaces it with the specified image file. The image file must use a [supported format](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/2307784705/Supported+Image+Formats). This method returns `True` on success and `False` on failure.

##### EnumerateExtensions() As Array

Returns an array of the extensions that are installed on a player.

##### FactoryReset(confirm As String) As Boolean

Applies a factory reset to the player. This method must be passed the string "confirm" to work; otherwise, it will return False and do nothing. If successful, this method will reboot without a return value. The following steps will be carried out during a factory reset:

1.  All files are wiped from the `BOOT:` drive (including custom splash screens and autorun scripts).
    
2.  All values are wiped from the registry.
    
3.  The RTC is reset (if the player has an RTC).
    
4.  The `FLASH:` drive is wiped.
    

##### ConfigureAsUsbGadget(roBool gadget)

This method allows the USB OTG (On The Go) port on the AU335 to be dynamically configured to *host* or *gadget* mode. In the *host* role, the USB port follows standard behavior (it allows USB devices to be plugged into it). In the *gadget* role, the player can behave as a USB device (for example, roUsbFilesystem). This method will return false on platforms other than the AU335. 

This script switches to *gadget* role and presents *sd:/test.img* as a filesystem to a connected USB host:

```
dc=CreateObject("roDeviceCustomization")
dc.ConfigureAsUsbGadget(1)

fs = CreateObject("roUsbFilesystem")
fs.Enable({filename: "SD:test.img"})
```

If `ConfigureAsUsbGadget(1)` isn't called on an AU335, then the USB will only run in *host* mode, regardless of what is connected. 

Note that on all BrightSign players other than AU335, the USB port doesn't need any configuration to work in USB OTG mode. The USB stack switches automatically between *host* and *gadget* depending on what is connected to the port. 

##### EncryptStorage(device As String, params As roAssociativeArray) As Boolean

Encrypts the contents of a storage device using an encryption key stored in the private section of the player registry. This prevents other devices from reading the names or contents of files on the storage device (though file metadata will still be readable). The storage device can still be mounted on other devices, which can list, delete, and copy files (even though they cannot read them).

Use the `device` parameter to specify which storage drive to encrypt (see [here](../../object-reference/hashing-and-storage-objects/rostorageinfo.md) for a list of valid drive names). Encryption parameters are passed as an associative array, which can contain the following:

*   `method As String`:(Required) The encryption method, which can be one of the following:
    
    *   `"none"`: Encryption is disabled and any encryption keys for the storage device are deleted from the registry. 
        
    *   `"passphrase"`: The storage device is encrypted using an un-obfuscated passphrase.
        
    *   `"obfuscated_passphrase"`: The storage device is encrypted using an obfuscated passphrase. Contact *support@brightsign.biz* to learn more about generating a key for obfuscation and storing it on the player. 
        
    *   `"brightsign_key"`: The storage device is encrypted using an encryption key that is common to all BrightSign players, but is not shared with outside parties. 
        
    *   `"generate_key"`: The storage device is encrypted using an encryption key that is generated on-demand using a secure random generator. The private registry of the player contains the only copy of the key; if the value in the registry is erased or becomes corrupted, there will be no way to recover data from that storage device.
        
        *   Note that the private registry does not distinguish between different physical volumes of the same drive. For example, if you encrypt two SD cards, the key for the first SD card will be overwritten when the second SD card is encrypted; in the case of a randomly generated key, the data from the first SD card will be irretrievable.
            
    *   `passphrase As String`: The passphrase for encrypting the storage device. This parameter must be included if the method is specified as `"passphrase"` or `"obfuscated_passphrase"`. 
        
    *   `format As Boolean`: Setting this parameter to `true` will cause the specified storage device to be reformatted–all existing files will be deleted (but are not guaranteed to be securely erased) before the device is encrypted; however, if the device cannot be reformatted, the operation will fail. If this parameter is set to `false`, the storage device will be mounted as if it has been previously encrypted using the supplied key.
        
        *   If the storage device hasn't been previously encrypted, it will be encrypted while leaving any preexisting files unencrypted. If the storage device has been encrypted using a different key, the operation will fail.
            
        *   If the `format` parameter is not specified, the storage device will be mounted as if it has been previously encrypted using the supplied key. If the storage device hasn't been previously encrypted, the operation will fail.