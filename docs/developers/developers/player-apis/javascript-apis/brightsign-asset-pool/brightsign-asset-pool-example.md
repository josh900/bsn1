# BrightSign Asset Pool Example

This script shows how the BrightSign Asset Pool can be used from JavaScript. It works from both NodeJS and Chromium. It is not intended as a full application and it doesn’t do anything with the assets that are downloaded.  

```
// MIT License
//
// Copyright (c) 2020 BrightSign
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

// Customise these settings for your environment
const storagePath = "/storage/sd/";
const poolPath = storagePath + "examplePool";
const serverPrefix = "https://github.com/brightsign/javascript-assetpoolfetcher/blob/video-training/";

const fs = require('fs');
const AssetPool = require("@brightsign/assetpool");
const AssetPoolFiles = require("@brightsign/assetpoolfiles");
const AssetFetcher = require("@brightsign/assetfetcher");
const AssetRealizer = require("@brightsign/assetrealizer");

// Create the asset collection array to be used by the rest of the
// program. The asset collection will usually come either directly or
// indirectly from a server somewhere rather than being generated in
// code like this.
function makeAssetCollection()
{
    // Assets must have a name and a link. Everything else is
    // optional. You can add your own properties if required. For
    // example, the "osUpdate" property here is only used by this
    // script.
    let videoAsset1 = {
	name: "brightlink.mp4",
	hash: { method: "SHA256",
		hex: "82e5e800ff4b2608ae996b6c9fce78c0d84b82cba0da270251846324f48fb076" },
	link: serverPrefix + "brightlink%201min.mp4?raw=true",
	size: 17219989,
    };

    let videoAsset2 = {
	name: "CMScontrol.mp4",
	hash: { method: "SHA512",
		hex: "d476296b114fda612917b1568a9f7ffe6f54f3f927b2d1ecc932816e912619eeef980e1adc16d8b1d7914d3f172cd6a2ef17172ea3251ddcdbb3d151faa6818f" },
	link: serverPrefix + "CMS%2BControl%201%20min.mp4?raw=true",
	size: 5633877,
    };

    // We don't want to risk actually changing the OS version on the
    // BrightSign running this example cript, so this is not a real
    // BrightSignOS file. It will be realized into the root of the
    // storage device, but the OS will fail to find the expected
    // header and rename it to placeholder.bsfw_invalid.
    let osUpdateAsset = {
	name: "placeholder.bsfw",
	hash: { method: "SHA1", hex: "20e89c9ba0491590e3c34bc704171c0c02e643c3" },
	link: serverPrefix + "placeholder.bsfw?raw=true",
	size: 43,
	osUpdate: true,
    };

    let assetCollection = [
	videoAsset1,
	videoAsset2,
	osUpdateAsset,
    ];

    return assetCollection;
}

// Convert a progress event to a useful string for reporting
function progressString(event)
{
    if (event.currentFileTotal === undefined) {
	// If the size of the asset was not specified in the asset collection, then the total size may not be reported
	// during the fetch.
	return event.currentFileTransferred.toString() + " of unknown";
    } else {
	return event.currentFileTransferred.toString() + " of " + event.currentFileTotal.toString() + " "
	    + (100*event.currentFileTransferred / event.currentFileTotal).toFixed(0) + "%";
    }
}

// Download any assets that aren't already in the pool into the pool
// whilst reporting progress.
async function fetchAssets(assetPool, assetCollection)
{
    console.log("Fetch: " + JSON.stringify(assetCollection.map(asset => asset.name)));

    let assetFetcher = new AssetFetcher(assetPool);

    assetFetcher.addEventListener("fileevent", (event) => {
	// This is called each time the fetcher has finished trying to
	// download an asset, whether successful or not. It is not
	// called for any assets that are already in the pool.
	console.log("ASSET [" + (event.index + 1).toString() + "] "
		    + event.fileName + " complete: " + event.responseCode.toString() + " " + event.error);
    });

    assetFetcher.addEventListener("progressevent", (event) => {
	// This is called at approximately the progress interval
	// specified in the options to indicate how far through the
	// download
	console.log("ASSET [" + (event.index + 1).toString() + "/" + event.total.toString() + "] " + event.fileName
		    + " progress: " + progressString(event));
    });

    const fetchOptions = {
	// receive asset progress events about every five seconds.
	progressInterval: 5,
	// try to download each asset three times before giving up.
	fileRetryCount: 3,
	// Give up if we fail to download at least 1024 bytes in each
	// ten second period.
	minimumTransferRate: { bytesPerSecond: 1024, periodInSeconds: 10 },
    };

    try {
	await assetFetcher.start(assetCollection, fetchOptions);
    }
    catch (err) {
	console.log("FETCH FAILED: " + err.message);
	throw(err);
    }
}

// In order to make use of an asset from the pool you need to look up
// its pool filename so you can refer to it there.
async function useAssets(assetPool, assetCollection)
{
    let files = new AssetPoolFiles(assetPool, assetCollection);

    for (const fileName of [ 'brightlink.mp4', 'CMScontrol.mp4' ]) {
	const path = await files.getPath(fileName);
	console.log("Asset " + fileName + " is at " + path);
    }
}

// Some files need to appear in the filesystem outside the pool. For
// example, BrightSignOS update files must be written to the root of
// a storage device for them to be found. Realizing will copy files,
// so can be slow on large files.
async function realizeAssets(assetPool, assetCollection)
{
    let realizer = new AssetRealizer(assetPool, storagePath);

    // We only want to realize the files that we have to
    const assetsToRealize = assetCollection.filter(asset => asset.osUpdate);
    console.log("Realize: " + JSON.stringify(assetsToRealize.map(asset => asset.name)));
    await realizer.realize(assetsToRealize);
}

function ensureDirectoryExists(path) {
    try {
	fs.mkdirSync(path);
    } catch (err)
    {
	if (err.code != 'EEXIST')
	    throw(err);
    }
}

function exceptionToString(err)
{
    if (err instanceof Error)
        return err.name + ":" + err.message;
    else if (typeof(err) === "string")
        return err;
    else
        return JSON.stringify(err);
}

async function runExample()
{
    console.log("Start");
    ensureDirectoryExists(poolPath);

    // Only one AssetPool instance should be created for a given pool
    // path. Having multiple instances risks them disagreeing over
    // which assets are protected during pruning.
    let assetPool = new AssetPool(poolPath);

    // Don't let the pool grow any larger than 500MiB
    await assetPool.setMaximumPoolSize(500 * 1024 * 1024);

    // Don't let free space on the storage device fall below 100MiB
    await assetPool.reserveStorage(100 * 1024 * 1024);

    const assetCollection = makeAssetCollection();

    // We need to stop the fetcher from pruning any of the assets we
    // currently care about in order to make space for fetching new
    // assets or realizing existing ones. Assets are protected until
    // the AssetPool instance is destroyed or unprotectAssets is
    // called for the same name.
    await assetPool.protectAssets("collection1", assetCollection);

    await fetchAssets(assetPool, assetCollection);

    // In this case any failure to fetch the assets will cause
    // fetchAssets to have thrown an exception, so we won't get this
    // far. However, in a larger script it may be more convenient to
    // call areAssetsReady to determine whether the asset collection
    // is ready for use.
    if (await assetPool.areAssetsReady(assetCollection)) {
	await useAssets(assetPool, assetCollection);
	await realizeAssets(assetPool, assetCollection);
    } else {
	console.log("Assets were not downloaded successfully");
    }
}

runExample()
    .then(() => {
	console.log("Complete");
	process.exit(0);
    })
    .catch((err) => {
	console.log("Failed " + exceptionToString(err));
	process.exit(1);
    });
```