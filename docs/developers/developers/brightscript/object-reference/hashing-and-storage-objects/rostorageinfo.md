# roStorageInfo

This object is used to report usage information for storage devices.

Object Creation: The *roStorageInfo* object is created with a parameter that specifies the path of the storage device. The path does not need to extend to the root of the storage device. The JavaScript equivalent is [filesysteminfo](https://docs.brightsign.biz/display/DOC/filesysteminfo) and [storageinfo](https://docs.brightsign.biz/display/DOC/storageinfo) (see [BrightScript-JavaScript Migration Guide](../../../../developers/player-apis/brightscript-javascript-migration-guide.md) for the method equivalents).

```
CreateObject("roStorageInfo", path As String) 
```

### Drive Specifications 

Use the following string values to specify different storage drives:

*   `"USB1:"` – The drive for USB storage devices connected to the player
    
*   `"SD:"` – The primary SD or microSD drive on the player.
    
*   `"SD2:"` – The internal microSD drive on the player (4Kx42, XDx32 models only)
    
*   `"SSD:"` – The internal SSD on the player (XTx44, XTx43, XDx34, and XDx33 models only)
    

## ifStorageInfo

##### GetFailureReason() As String

Yields additional useful information if a function return indicates an error.

##### GetBytesPerBlock() As Integer

Returns the size of a native block on the filesystem used by the specified storage device.

##### GetSizeInMegabytes() As Integer

Returns the total size (in mebibytes) of the storage device.

> [!CAUTION]
> **Important**
> On some filesystems that have a portion of space reserved for the super user, the following expression may not be true:  GetUsedInMegabytes() + GetFreeInMegabytes() == GetSizeInMegabytes()

##### GetUsedInMegabytes() As Integer

Returns the amount (in mebibytes) of space currently used on the storage device. This amount includes the size of the pool because this class does not integrate pools into its calculations.

##### GetFreeInMegabytes() As Integer

Returns the available space (in mebibytes) on the storage device.

##### GetFileSystemType() As String

Returns a string describing the type of filesystem used on the specified storage or whether it is encrypted (“+ecryptfs”). The following are potential values:

*   "exfat"
    
*   "ext3"
    
*   "ext4"
    
*   "fat12"
    
*   "fat16"
    
*   "fat32"
    
*   "hfs"
    
*   "hfsplus"
    
*   "ntfs"
    
*   “+ecryptfs” (as of BOS version 9.0.145.1)
    

##### GetStorageCardInfo() As roAssociativeArray

Returns an associative array containing details of the storage device hardware. For SD cards, the returned data may include the following:

|     |     |     |
| --- | --- | --- |
| `sd_mfr_id` | Integer | Card manufacturer ID as assigned by the SD Card Association |
| `sd_oem_id` | String | Two-character card OEM identifier as assigned by the SD Card Association |
| `sd_product_name` | String | Product name, assigned by the card manufacturer (5 bytes for SD, 6 bytes for MMC) |
| `sd_spec_vers` | Integer | Version of SD spec to which the card conforms |
| `sd_product_rev` | String | Product revision assigned by the card manufacturer |
| `sd_speed_class` | String | Speed class (if any) declared by the card |
| `sd_au_size` | Integer | Size of the SD AU in bytes. |

Example:

```
si=CreateObject("roStorageInfo", "SD:/")
Print si.GetFreeInMegabytes(); "MiB free"
```