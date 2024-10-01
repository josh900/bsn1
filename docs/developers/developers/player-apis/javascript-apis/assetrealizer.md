# assetrealizer

This *assetrealizer* object contains functions for realizing files (i.e. extracting files from an asset pool and placing them into the standard file directory).

**assetrealizer IDL**

```
interface AssetRealizer {
    constructor(AssetPool pool, String destinationPath);
    Promise<unsigned long long> estimateRealizedSize(AssetList assets);
    Promise<void> realize(AssetList assets);
    Promise<Array<ValidationResult>> validateFiles(AssetList assets, AssetValidationOptions options);
};
 
interface AssetValidationOptions {
    attribute deleteCorrupt;
};
 
interface ValidationResult {
    attribute String name;
    attribute String reason;
};
```

## Object Creation

To create an *assetrealizer* object, you will first need to create an *assetpool* instance and download files to it using an *assetpoolfetcher* instance. Then, load the `brightsign/assetrealizer` module using the `require()` method, and create an instance of the *assetrealizer* class using the *assetpool* instance and the destination directory for realization.

```
const AssetPoolClass = require("@brightsign/assetpool");
let assetPool = new AssetPoolClass("SD:/pool");
   
const AssetRealizerClass = require("@brightsign/assetrealizer");
let assetRealizer = new AssetRealizerClass(assetPool, "SD:/");
```

## AssetRealizer

Use this interface to copy assets out of the pool into real named files in the file system and perform related functions.

##### estimateRealizedSize()

```
Promise<unsigned long long> estimateRealizedSize(AssetList assets)
```

Returns the estimated amount of space (in megabytes) that would be taken up if the files specified in the [*AssetList*](../javascript-apis/assetpool.md) object are realized.

##### realize()

```
Promise<void> realize(AssetList assets)
```

Places the files into the destination directory specified in the passed AssetList object. If the pool does not contain the full set of required files, then this method will immediately fail before any files are changed (this method attempts to do as much work as possible before destructively modifying the file system). This method automatically checks the length of the file and that any hashes that match those specified. If there is a mismatch, then the affected file is deleted from the pool and realization fails. This method may cause unprotected assets to be pruned from the pool. The method indicates failure by rejecting the returned promise.

> [!NOTE]
> The pool and the destination must be on the same storage device in the same file system.

##### validateFiles()

```
Promise<Array<ValidationResult>> validateFiles(AssetList assets, AssetValidationOptions options)
```

Checks the hash of every file in the passed AssetList against the corresponding file in the destination path and returns a string list containing each mismatched file name mapped to the reason. This operation can take a long time and slow down access to the storage device. It is normally only useful if file system or storage corruption is suspected or for debugging. The `options` parameter is a string list, which can currently support a single option:

*   `"deleteCorrupt"`: Automatically deletes any files that do not match the expected hash. By default, these files are not deleted.
    

## ValidationResult

This interface is returned by the `validateFiles()` method to indicate the results of the realize operation.

*   `name` string: The name of the mismatched file (if the realize operation fails)
    
*   `reason` string: An explanation for a failed realize operation. See the [*roAssetRealizerEvent*](../../../developers/brightscript/object-reference/content-management-objects/roassetrealizerevent.md) page for a list of possible reason strings.