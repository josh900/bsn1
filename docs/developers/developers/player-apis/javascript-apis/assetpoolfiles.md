# assetpoolfiles

This *assetpoolfiles* object provides direct access to the files for assets in the pool.

**assetrealizer IDL**

```
interface AssetPoolFiles {                                                                                                                                                                                   
    AssetPoolFiles(AssetPool pool, AssetList assets);                                                                                                                                                        
    Promise<String> getPath(String assetName);                                                                                                                                                               
    Promise<AssetInfo> getInfo(String assetName);                                                                                                                                                            
    Promise<void> moveFileIntoPool(String sourceFileName, String destinationAssetName);                                                                                                                          
}                                                                                                                                                                                                            
```

## Object Creation

To create an *assetpoolfiles* object, you will first need to create an *assetpool* instance and download files to it using an *assetpoolfetcher* instance. Then, load the `brightsign/assetrealizer` module using the `require()` method, and create an instance of the *assetrealizer* class using the *assetpool* instance and the destination directory for realization.

```
const AssetPoolClass = require("@brightsign/assetpool");
let assetPool = new AssetPoolClass("SD:/pool");
  
const AssetPoolFilesClass = require("@brightsign/assetpoolfiles");
let assetPoolFiles = new AssetPoolFilesClass(assetPool, assetCollection);
```

## AssetPoolFiles

Use this interface to gain access to information about the files for assets in the pool.

##### getPath()

```
Promise<String> getPath(String assetName)
```

Returns the full path to the file in the pool that corresponds to the named asset. This can be used to read, play or execute the corresponding asset as required. You must not modify the file since this will change its hash.

##### getInfo()

```
Promise<AssetInfo> getInfo(String assetName)
```

Returns the [AssetInfo](https://docs.brightsign.biz/display/DOC/BrightSign+Asset+Pool) for the named asset if it is present in the pool. If the asset is not present then the returned promise is rejected.

##### moveFileIntoPool()

```
Promise<void> moveFileIntoPool(String sourceFileName, String destinationAssetName)
```

Move an existing file on the same storage device as the pool into the pool as the asset with the corresponding name. This is a quick operation because the hash is not checked. Note that this method does not cause any pruning of assets already in the pool to take place (although it may cause a subsequent operation that can prune the pool to do so.) This method is only rarely useful.