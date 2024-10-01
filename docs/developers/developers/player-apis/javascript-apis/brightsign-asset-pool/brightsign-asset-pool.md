# BrightSign Asset Pool

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Core Concepts](#core-concepts)
*   [Managing Pool Size](#managing-pool-size)
*   [Referring To Assets In The Pool](#referring-to-assets-in-the-pool)
*   [Hash Uniqueness](#hash-uniqueness)
*   [Asset Metadata](#asset-metadata)
*   [Hashing](#hashing)
*   [Usage Overview](#usage-overview)
*   [Example](#example)

The BrightSign Asset Pool provides a reliable and resilient mechanism for downloading, storing and retrieving media assets and other files required by the player for its presentations.

## Core Concepts

### The Pool

An asset pool is a directory hierarchy under a single root. The directory is often simply named "pool", but the underlying implementation does not require that. Each asset is stored in one of a number of sub-directories to improve performance on simple filesystems like FAT.

The destination for a particular asset in the pool is determined by its [hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function) (or digest) of its contents (or, in some cases, a hash of its metadata) which makes it a content-addressable store. In order to refer to an asset either before or after it has been downloaded it is necessary to know its hash. (This is similar to the way that objects are stored in a Git repository.)

The pool can be configured with a maximum size and/or to ensure that a particular amount of space remains free on the storage device that contains it. In order to stop the pool growing beyond these bounds old files are "pruned". Files that must not be pruned must be "protected" before any operations are started that may write to the pool.

An asset that is stored in the pool using a particular hash will only be stored once until it is pruned. Requests to download an asset that is already in the pool will immediately succeed since the asset is already present. This means that switching between presentations that share assets, even perhaps ones that haven't been used for a while, can avoid downloading assets unnecessarily.

### Asset Collections

An asset collection is a list of asset metadata. The metadata either directly contains the hash as a specific field or the hash can be generated directly from other fields. The metadata also provides a name for each asset which allows assets and therefore files in the pool to be looked up by name. An asset collection is necessary to provide meaning for the assets stored in the pool. Asset collections themselves exist only in memory and are not stored in the pool itself.

### Synchronization Specification

Synchronization specifications are often refered to as "sync specs". They consist of formatted XML or JSON that can be used to generate an asset collection but also have space for extra information that can be useful when downloading assets. They are not recommended unless compatibility with existing systems that use them is required.

### Asset Fetcher

An asset fetcher runs asynchronously downloading any assets mentioned in an asset collection that are not currently available in the pool. The file contents are automatically verified against the supplied hash during the download.

#### Protocols

Assets are expected to primarily be downloaded using HTTP or HTTPS. However, the fetcher also supports FTP and file URLs.

#### Authentication

Arbitrary HTTP headers can be provided when fetching all the assets in an asset collection. The fetcher supports HTTP Basic, Digest and NTLM authentication. Individual assets within a collection can be marked as opting out of providing these headers and authentication.

## Managing Pool Size

The pool is intended to live for a long time with assets being fetched into it as required. If the pool becomes too full then unused assets will be pruned to make space. This means that any assets that are still required (or will be required) must be protected before performing any operations that may prune such as fetching or realizing.

The pool size can be restricted in two ways:

*   by requiring that a certain amount of space on the storage device always be kept free. This means that space can be reserved for logs to grow into and any pool operations that can prune will ensure that at least the requested amount of space remains free. Checking the amount of free space on a storage device is a lightweight operation so this method should be preferred.
    
*   by setting a maximum size that the pool can occupy. This can be used in combination with the previous method and attempting to exceed either threshold will trigger pruning. Calculating the size of the pool requires adding up the size of each file individually, so the first operation can take longer than usual. Once the first calculation is complete the pool size is only updated based on modifications to the pool so subsequent operations have less overhead.
    

Files are considered for pruning based on how long ago they were last fetched, or would have been fetched had they not already been present in the pool. The least-recently fetched unprotected files will be pruned first. Note that unless the "working set" of assets is close to the maximum size of the pool this can often mean that any failures to protect assets have no ill effects.

## Referring To Assets In The Pool

Asset files can often be used directly from the pool. The pool filename corresponding to an asset can be looked up by name in an asset collection.

Sometimes it is necessary for the asset files to appear with their names within the filesystem. Asset files can be copied to a destination directory. This is known as "realization" and should only be used when necessary since it can be very slow. Alternatively, an asset collection can be made to appear as a virtual filesystem.

## Hash Uniqueness

The hash for a particular asset file must be unique. This happens automatically for normal hash algorithms such as SHA-256 since hash collisions should not be possible. If two files with different contents generate the same hash, this is known as a "hash collision". Some older hash algorithms such as MD5 and SHA-1 are known to have hash collisions, but these only occur when files have been deliberately constructed to create such collisions – they do not occur by accident.

Sometimes the actual hash of the asset is not available prior to the download. In this case parts of the asset metadata, such as the URL and a change hint are hashed together instead. If the asset changes then some part of the metadata must also change so that the asset fetcher knows to download the asset again.

It is not possible to use HTTP headers like ETag or Last-Modified as part of the hash since these aren't known prior to the download and can change independently.

## Asset Metadata

| Tag | Description |
| --- | --- |
| name | Relative filename (may contain slashes but if so the file may not be realized.) Asset names must be unique within an asset collection, but it is expected that different asset collections will contain assets with the same name. The asset name is not stored in the pool, and the same asset file in the pool may be referenced by multiple names, even within the same asset collection. |
| size | File length in bytes |
| hash | Hash algorithm and hash of file contents. |
| link | Source URL |
| change\_hint | An arbitrary value used by the client to ensure that files that have the same hash are not considered to be identical unless this value and the URL also matches. |
| auth | Specify extra authentication information (see below). |
| probe | Media probe data (useful for Cheetah and Panther). |
| pattern | Wildcard pattern to match against |

## Hashing

### Simple Hash Algorithms

md5, sha1, sha224, sha256, sha384, sha512

### BESHA1 Algorithm

This algorithm is only useful for referring to remote content that is too large to download during authoring. Its use is not recommended.

### No Hash

If no hash is specified then the hash is generated internally by hashing together the "link" and "change\_hint" fields.

## Usage Overview

The BrightSign asset pool can be used from BrightScript or from Javascript but it is not possible to share a single pool across both. However, the BrightScript `roHtmlWidget.MapFileFromAssetPool` method can be used to make a particular asset collection appear as files under a particular URI prefix.

### BrightScript

TBD

### Javascript

1.  Create @brightsign/assetpool object to represent the asset pool passing the path to the pool directory.
    
2.  Create the asset collection data structure. This is a Javascript array of objects containing the metadata for the assets you wish to use.
    
3.  Protect the assets by calling the assetpool.protectAssets method to stop them being deleted in order to make space.
    
4.  Create a @brightsign/assetfetcher object passing the pool.
    
5.  Call the assetfetcher.start method passing the asset collection. Any assets that are not present in the pool will start to be downloaded.
    
6.  Progress can be monitored by adding handlers for the progressevent and fileevent events.
    
7.  If the fetch attempt completes successfully then the promise returned by assetfetcher.start will be resolved. If at least one of the assets could not be fully downloaded then the promise will be rejected.
    
8.  When the promise returned by assetfetcher.start resolves, the fetch attempt is complete. 
    
9.  Create your set of assets as a Javascript array of objects containing the metadata.
    
10.  Create a @brightsign/assetfiles object passing the pool and asset collection.This object can be used to retrieve the full path to the files in the pool that correspond to the asset name specified. See [assetpoolfiles](https://docs.brightsign.biz/display/DOC/assetpoolfiles) for more information.
    
11.  Create a @brightsign/assetrealizer object passing the pool and call the realize method if you wish to copy assets from the pool to a directory using the asset names. Note that this is slow and is only recommended for files that must exist in the filesystem such as BrightSignOS upgrade files (bsfw).
    
12.  Create a @brightsign/assetcollectionview object passing the pool and the asset collection to create a virtual storage device containing the assets using the names and directory structure in the asset collection. See [assetpoolfiles](https://docs.brightsign.biz/display/DOC/assetpoolfiles) for more information.
    

## Example

[BrightSign Asset Pool Example](https://docs.brightsign.biz/display/DOC/BrightSign+Asset+Pool+Example) shows how the Asset Pool can be used from JavaScript. It works from both NodeJS and Chromium, and can be run from the BrightSign shell as follows:

```
node bs-assetpool-example.js
```