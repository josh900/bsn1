# filesysteminfo

The *filesysteminfo* object provides information about the file system of a storage device connected to the player. To retrieve information about the storage device itself, use the *storageinfo* object.

**filesysteminfo IDL**

```
[
    constructor(String path, String type);
] interface FilesystemInfo {
    Promise<bool> isReadOnly();
    Promise<String> getFilesystemType();
    Promise<FilesystemStats> getStatistics();
};

interface FilesystemStats {
    attribute Number blockSize;
    attribute Number sizeBytes;
    attribute Number bytesFree;
    attribute Number filesUsed;
    attribute Number filesFree;
    attribute bool isReadOnly;
};
```

## Object Creation

To create a *filesysteminfo* object, first load the `brightsign/filesysteminfo` module using the `require()` method. Then create an instance of the *filesysteminfo* class with a string value specifying the storage path.

```
var FileSystemInfoClass = require("@brightsign/filesysteminfo");
var fileSystemInfo = new FileSystemInfoClass("/storage/sd");
```

Use the following string values to specify different storage drives:

*   `"/storage/usb1"` – The drive for USB storage devices connected to the player
    
*   `"/storage/sd"` – The primary SD or microSD drive on the player.
    
*   `"/storage/sd2"` – The internal microSD drive on the player (4Kx42, XDx32 models only)
    
*   `"/storage/ssd"` – The internal SSD on the player (XTx44, XTx43, XDx34, and XDx33 models only)
    

## FilesystemInfo

Use this interface to retrieve information about the file system.

##### isReadOnly()

```
Promise<bool> isReadOnly()
```

Returns a Boolean value indicating whether the filesystem is read-only. 

##### getFilesystemType()

```
Promise <DOMString> getFilesystemType()
```

Returns the filesystem type or whether it is encrypted (“+ecryptfs”). The following are potential values:

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
    

##### getStatistics()

```
Promise<FilesystemStats> getStatistics()
```

Returns a `FilesystemStats` interface containing information about the filesystem. This method can take a significant amount of time to return its promise.

## FilesystemStats

This interface contains information about the filesystem:

*   `blockSize` Number: The size of a native block
    
*   `sizeBytes` Number: The amount of total space
    
*   `bytesFree` Number: The amount of free space
    
*   `filesUsed` Number: The number of used inodes
    
*   `filesFree` Number: The number of free inodes
    
*   `isReadOnly` bool: A flag indicating whether the filesystem is read-only.
    

## Example

```
var FileSystemInfoClass = require("@brightsign/filesysteminfo");
var fileSystemInfo = new FileSystemInfoClass("/storage/sd");

fileSystemInfo.getFilesystemType().then(
        function(data) {
            console.log(JSON.stringify(data));
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        });

fileSystemInfo.getStatistics().then(
        function(data) {
            console.log(JSON.stringify(data));
        })
    .catch(
        function(data) {
            console.log(JSON.stringify(data));
        });
```