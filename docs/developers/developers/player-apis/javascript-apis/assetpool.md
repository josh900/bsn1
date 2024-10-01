# assetpool

The *assetpool* object represents a directory on a storage device used to store downloaded assets. See the [Asset Pool](https://docs.brightsign.biz/display/DOC/BrightSign+Asset+Pool) overview for more general information and examples.

**assetpool IDL**

```
interface AssetPool {
    AssetPool(String poolPath);
    Promise<void> protectAssets(String assetCollectionName, AssetList assets);
    Promise<void> unprotectAssets(String assetCollectionName);
    Promise<void> reserveStorage(long reservedStorageInBytes);
    Promise<void> setMaximumPoolSize(long? maximumPoolSizeInBytes);
    Promise<long> getPoolSize();
    Promise<AssetValidationResult> validate(AssetList assets, AssetValidationOptions options);
    Promise<AssetQueryResult> queryFiles(AssetList assets);
    Promise<bool> areAssetsReady(AssetList assets);
};

interface AssetInfo {
    attribute String name;
    attribute String link;
    [optional] attribute long size;
    [optional] attribute AssetHash hash;
    [optional] attribute String changeHint;
    [optional] attribute AssetFetchAuthentication? auth;
    [optional] attribute AssetFetchHeaders? headers;
};

interface AssetHash {
    attribute String method;
    attribute String hex;
};

interface AssetFetchAuthentication {
    [optional] attribute String user;
    [optional] attribute String password;
};

interface AssetFetchHeaders {
};

interface AssetValidationOptions {
    attribute deleteCorrupt;
};

interface AssetQueryResult {
    attribute String name;
    attribute bool present;
};

interface AssetValidationResult {
    attribute String name;
    attribute String reason;
};
```

## Object Creation

To create an *assetpool* object, first load the `brightsign/assetpool` module using the `require()` method. Then create an instance of the *assetpool* class with a string value specifying the pool path. You must create only one *assetpool* instance per pool path. This means that it is not possible to safely share a single pool path between BrightScript and JavaScript code.

```
const AssetPoolClass = require("@brightsign/assetpool");
let assetPool = new AssetPoolClass("SD:/pool");
```

## AssetPool

Use this interface to perform operations on the asset pool.

##### protectAssets()

```
Promise<void> protectAssets(String assetCollectionName, AssetList assets)
```

Requests that a set of files in the asset pool be protected from deletion when the system software needs to prune files from the pool to make space. The passed `assetCollectionName` is used to reference the set of files if their protection needs to be removed later using the `unprotectAssets()` method. Protection only affects this a`ssetpool` instance and the other objects that use it. You must protect all the assets you care about before performing any operation that might prune files from the pool in order to be sure that the assets you still need are not pruned. This setting is not persistent beyond the lifetime of the `assetpool` instance.

##### unprotectAssets()

```
Promise<void> unprotectAssets(String assetCollectionName)
```

Removes protection from a set of files that have been protected by passing the corresponding `assetCollectionName` to the the `protectAssets()` method.

##### reserveStorage()

```
Promise<void> reserveStorage(long reservedStorageInBytes)
```

Operations on this assetpool instance, and any other assetpoolfetcher and assetrealizer instances using it, will attempt to keep the specified amount of space free on the storage device containing the pool. As other files are written to the storage device, the maximum size occupied by the pool will be reduced to compensate. This setting is not stored persistently in the pool, so the method must be called each time an assetpool object is created.

##### setMaximumPoolSize()

```
Promise<void> setMaximumPoolSize(long? maximumPoolSizeInBytes)
```

Specifies the maximum size of the asset pool. This method is more resource-intensive than `reserveStorage()`, but it is useful when creating multiple pools on a storage device to ensure they don't grow unevenly. This setting is not stored persistently in the pool, so the method must be called each time an assetpool object is created.

##### getPoolSize()

```
Promise<long> getPoolSize()
```

Returns the current size of the asset pool in bytes. It is necessary to walk the pool directory structure looking at every asset file to do this, which may slow down other access to the storage device. It is recommended that this method is not called regularly in production code.

##### validate()

```
Promise<AssetValidationResult> validate(AssetList assets, AssetValidationOptions options)
```

Recalculates the hashes of every file in the pool and compares them with the expected values in the passed AssetList. This means every asset file needs to be read in its entirety which may take a long time and may slow down other access to the storage device. This method can be used to detect storage and file system corruption. This method returns an *AssetValidationResult* interface containing validation results for each file. The second parameter is an *AssetValidationsOptions* interface specifying validation options. The only option currently supported indicates whether any assets with mismatched hashes are automatically deleted. The default behaviour is to leave such asset files in place.

##### queryFiles()

```
Promise<AssetQueryResult> queryFiles(AssetList assets)
```

Determines whether the specified files are present in the asset pool. This method returns an *AssetQueryResult* interface containing query results. This method is normally only useful for debugging during development.

##### areAssetsReady()

```
Promise<bool> areAssetsReady(AssetList assets)
```

Returns `true` if every asset in the AssetList is present in the asset pool.

## AssetInfo 

This interface represents a single asset file that may be in the pool may not yet be in the pool. Each asset has a subset of the following properties:

*   `name` string: The name that can be used to look up the asset. For a file to be realized, it must have a valid filename without any slashes. Asset names must be unique within an asset collection, but different asset collections may use the same asset name to refer to the same asset in the pool or a different asset in the pool. Asset names are not stored in the pool, the only way to refer to an asset by name is using an asset collection.
    
*   `link` string: The URI that can be used by assetpoolfetcher to download the file. http, https, ftp and file URIs are supported.
    
*   `size` long optional : The file length (in bytes) if known.
    
*   `hash` AssetHash optional: A *Hash* interface specifying the hash algorithm and hash value of the file. If no hash is provided then one is created automatically from the link and changeHint.
    
*   `changeHint` string optional: An arbitrary value that can be used by the client to specify that a file has changed even when the hash value and download URL remain the same. This is mostly useful when the hash is not known but the provider of the asset collection can tell when the content has changed. For example, MediaRSS feeds often provide a GUID for the content.
    
*   `auth` AssetFetchAuthentication? optional: An *AssetFetchAuthentication* interface specifying the credentials to use when downloading the asset. By default, credentials are inherited from the [*assetpoolfetcher*](../javascript-apis/assetfetcher.md) instance used to download the asset.
    
*   `headers` AssetFetchHeaders? optional: By default, the HTTP headers specified via the `headers` property passed to the s`tart` method will be used for each asset. The use of these headers can be disabled for a particular asset by setting this property to `null`. This is useful if a particular subset of assets are retrieved from somewhere else that does not require authentication. It is not currently possible to provided specific headers for a single asset.
    

## AssetHash

This interface contains hash information about the file.

*   `method` string: The hash algorithm. Accepted values include "SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5" and "BESHA1". "BESHA1" is a custom hash algorithm that is only useful for referring to large assets that are stored remotely and its use is not recommended.
    
*   `hex` string: The hash value in hexadecimal format
    

## AssetFetchAuthentication

This interface contains authentication information for downloading files.

*   `user`string optional: The user name for authentication
    
*   `password` string optional: The password for authentication
    

## AssetValidationOptions

This interface contains validation options for the `validate()` method.

*   `deleteCorrupt`: A flag specifying whether corrupt files should be deleted during validation
    

## AssetQueryResult

This interface is returned by the `queryFiles()` method. Each entry in the list contains the following parameters:

*   `name` string: The name of the queried file
    
*   `present` bool: A flag indicating whether the queried file exists in the asset pool
    

## AssetValidationResult

This interface is returned by the `validate()` method. Each entry in the list contains the following parameters:

*   `name` string: The name of the checked file
    
*   `reason` string: An explanation for a failed validation