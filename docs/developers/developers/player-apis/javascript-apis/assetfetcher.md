# assetfetcher

The *assetfetcher* object allows for downloading files to an asset pool (which is represented in JavaScript as an [*assetpool*](../javascript-apis/assetpool.md) instance).

**assetfetcher IDL**

```
interface AssetPoolFetcher {
    AssetPoolFetcher(AssetPool pool);
    Promise<void> start(AssetList list, AssetPoolFetcherParams assetPoolParams[optional]);
    Promise<void> cancel();
};

interface FileEvent {
    attribute String type;
    attribute String fileName;
    attribute int index;
    attribute int responseCode;
    attribute String error;
};

interface ProgressEvent {
    attribute String type;
    attribute String fileName;
    attribute int index;
    attribute int total;
    attribute long currentFileTransferred;
    [optional] attribute long currentFileTotal;
};

interface AssetPoolFetcherParams {
    attribute Authentication auth;
    attribute bool enableUnsafeAuthentication;
    attribute bool enableUnsafeProxyAuthentication;
    attribute bool enableEncodings;
    attribute bool enablePeerVerification;
    attribute bool enableHostVerification;
    attribute String certificatesFile;
    attribute HeaderList headers;
    attribute String proxy;
    attribute Array<String> proxyBypassList;
    attribute unsigned int progressInterval;
    attribute unsigned int fileRetryCount;
    attribute String relativeLinkPrefix;
    attribute String interfaceName;
    attribute MinTransferRate minimumTransferRate;
    attribute double maximumTransferRate;
    attribute bool onlyRequestCache;
};

interface Authentication {
    attribute String username;
    attribute String password;
};

interface Header {
    attribute String value;
};

interface MinTransferRate {
    attribute int bytesPerSecond;
    attribute int periodInSeconds;
};
```

## Object Creation

To create an *assetpoolfetcher* object, you will first need to create an *assetpool* instance. Then, load the `brightsign/assetpoolfetcher` module using the `require()` method, and create an instance of the *assetpoolfetcher* class using the *assetpool* instance.

```
const AssetPoolClass = require("@brightsign/assetpool");
let assetPool = new AssetPoolClass("SD:/pool");
 
const AssetPoolFetcherClass = require("@brightsign/assetpoolfetcher");
let assetPoolFetcher = new AssetPoolFetcherClass(assetPool);
```

## AssetPoolFetcher

This interface allows you start or stop the asset fetcher.

##### start()

```
Promise<void> start(AssetList list, AssetPoolFetcherParams assetPoolParams[optional])
```

Begins fetching the files specified in the passed [*assetpool.AssetList*](../javascript-apis/assetpool.md) interface. The fetching process is configured with the passed *AssetPoolFetcherParams* interface. The `start()` promise returns when the asset-fetching process is complete. Alternatively, the promise will be rejected if the *assetpoolfetcher* instance has already been started. This method may cause assets to be pruned.

##### cancel()

```
Promise<void> cancel()
```

Cancels the asset-fetching process. The promise will not be resolved until cancellation is complete.

## FileEvent

This interface contains information about a file-transfer attempt.

*   `type` string: Contains `fileevent` to indicate the type of the event.
    
*   `fileName` string: The name of the asset being downloaded.
    
*   `index` int: The zero-based index of the file in the [*assetpool.AssetList*](../javascript-apis/assetpool.md) interface.
    
*   `responseCode` int: The protocol response code associated with the event. The following codes indicate success:
    
    *   200: Successful HTTP transfer
        
    *   226: Successful FTP transfer
        
    *   0: Successful local file transfer
        

> [!NOTE]
> **Note**
> There are also numerous error codes in case of failure; see [this page](../../../developers/brightscript/object-reference/content-management-objects/roassetfetcherevent.md) for a non-exhaustive list.

*   `error` string: A textual error message which may be more descriptive than the responseCode for local errors.
    

## ProgressEvent

This interface contains information about the asset-fetching process.

*   `type` string:  Contains `progressevent` to indicate the type of the event.
    
*   `fileName` string: The name of the file currently being downloaded
    
*   `index` int: The zero-based index of the current file in the [*assetpool.AssetList*](../javascript-apis/assetpool.md) interface
    
*   `total` int: The total number of files in the *AssetList* object
    
*   `currentFileTransferred` long: The number of bytes that have been downloaded so far for the current asset.
    
*   `currentFileTotal` long optional: If the size of the asset in bytes was known prior to the download starting then it is provided in this property. If the size was not known then this property may not be present.
    

## AssetPoolFetcherParams

This interface contains configuration parameters for the asset-fetcher process.

*   `auth` Authentication: An *Authentication* interface specifying the credentials to use when downloading the asset
    
*   `enableUnsafeAuthentication`  bool: A flag enabling basic HTTP authentication. HTTP authentication uses an insecure protocol, which might allow others to easily determine the password. The *assetpoolfetcher* object will still prefer the stronger digest HTTP if it is supported by the server. If this parameter is `false` (which is the default setting), it will refuse to provide passwords via basic HTTP authentication, and any requests requiring this authentication will fail.
    
*   `enableUnsafeProxyAuthentication` bool: A flag enabling basic HTTP authentication against proxies. HTTP authentication uses an insecure protocol, which might allow others to easily determine the password. If this parameter is `false`, it will refuse to provide the proxy password via basic HTTP authentication, and any requests requiring this authentication type will fail. Unlike `enableUnsafeAuthentication`, this parameter is set to `true` by default. 
    
*   `enableEncodings` bool:  A flag enabling HTTP compression, which communicates to the server that the system can accept any encoding that the *assetpoolfetcher* instance is capable of decoding by itself (this behavior is enabled by default). Supported encodings currently include "deflate" and "gzip", which allow for transparent compression of responses. Clients of the *assetpoolfetcher* instance see only the decoded data and are unaware of the encoding being used.
    
*   `enablePeerVerification` bool: A flag that enables checking of TLS/SSL certificates. This parameter is set to `true` by default. Disabling peer verficiation allows you to bypass an expired certificate check.
    
*   `enableHostVerification` bool: A flag that enables checking of the TLS/SSL certificate for the correct hostname. This parameter is set to `true` by default. Disabling host verification allows you to accept a certificate being sent for the wrong hostname.
    

> [!CAUTION]
> **Important**
> Peer verification and host verification are important security checks that prevent "man-in-the-middle" attacks. These features should only be disabled after careful consideration of the security implications.

*   `certificatesFile` string: The filename of an alternative set of CA certificates for the connection. This method is useful if the connection certificates are signed by a CA that is not on the the default trusted list (for example, if your organization uses a private CA hierarchy that is not signed by a well known root CA). This file replaces the default list, so the passed certificate file must contain all acceptable CA certificates required for the connection.
    
*   `headers` HeaderList: A list of headers that will be passed to HTTP requests made by the *assetpoolfetcher* instance.
    
*   `proxy` string: The name or address of the proxy server that will be used by the *assetpoolfetcher* instance. The proxy string should be formatted as "[http://user:password@hostname:port](http://user:password@hostnameport/)". It can contain up to four "\*" characters; each "\*" character can be used to replace one octet from the player's current IP address. For example, if the IP address is currently 192.168.1.2, and the proxy is set to "proxy-\*-\*", then the player will attempt to use a proxy named "proxy-192-168". If present, this setting overrides the player global proxy setting.
    
*   `proxyBypassList` Array<String>: A list of hosts to exempt from the proxy setting. The list should consist of one or more hostnames (IP addresses cannot be used). The *assetpoolfetcher* instance will attempt to reach the specified hosts directly rather than using the proxy that has been specified with the `proxy` parameter. For example, the hostname "[example.com](http://example.com/)" would exempt "[example.com](http://example.com/)", "[example.com](http://example.com/):80", and "[www.example.com](http://www.example.com/)" from the proxy setting. If present, this setting overrides the global proxy bypass setting.
    
*   `progressInterval` unsigned int: The interval (in seconds) between progress events when an individual file is being downloaded. Setting the interval to `null` disables all progress events. Setting the interval to 0 specifies that events should be generated as often as possible, though this will slow down the transfer process. If the interval is set to 0 or any positive integer, events will always be generated at the start and end of the file download irrespective of elapsed time. The default interval is 300 seconds.
    
*   `fileRetryCount` unsigned int: The maximum number of times each file download will be retried before moving on to the next file download. The default retry count is five.
    
*   `relativeLinkPrefix` string: A prefix that will be prepended to links that lack a protocol in the *AssetList* object. Normally, this method is used to make `file:///` URIs drive agnostic, but it can also be used to reduce the size of the sync spec if all files are stored in the same place. Links that have a protocol are not affected by this method.
    
*   `interfaceName` string: A string specifying which network interface the *assetpoolfetcher* instance should try to use for network access, for example "eth0" for Ethernet or "wlan0" for WiFi. The default behavior (indicated by a null value) is to send requests using the most appropriate network interface, which may depend on the routing metric configured via the *networkconfiguration* object. If multiple interfaces are on the same layer 2 network, this method may not work as expected due to the Linux weak-host model.
    
*   `minimumTransferRate` MinTransferRate: A *MinTransferRate* interface specifying the average minimum transfer rate for file downloads. If a file transfer falls below this rate, it will be terminated.
    
*   `maximumTransferRate` long: The maximum transfer rate for file downloads. The source data rate isn't under the direct control of the BrightSign player, but download rates should average below the specified value over time. 
    
*   `onlyRequestCache` bool: A flag indicating that the player should disconnect shortly after beginning the asset download. If the player is set to use a suitably configured proxy (either globally or via the *AssetPoolFetcherParams* interface), then the proxy will continue to download the files, making them readily available for asset-fetching calls in the future. If this parameter is `true`, the `fileevent` will return response code 202 ("Accepted") to indicate success. Other errors will be reported as usual. The `progressevent` for the final all-files-complete event will always be -2 ("EVENT\_ALL\_FAILED") because the download does not complete.
    

## Authentication

This interface contains authentication information for downloading files.

*   `username` string: The user name for authentication
    
*   `password` string: The password for authentication
    

## Header

This interface contains a list of headers to pass to a file download URL. Each entry in the list contains the following parameters:

*   `value` string: The header value
    

## MinTransferRate

The values in this interface are used to calculate the minimum transfer rate.

*   `bytesPerSecond` int: The transfer rate below which, when it is averaged over the `periodInSeconds`, the file transfer will be terminated
    
*   `periodInSeconds` int: The time frame over which the `bytesPerSecond` measurement is averaged
    

> [!NOTE]
> **Note**
> If the transfer is over the Internet, you may not want to set the `periodInSseconds` to a small number in case network problems cause temporary drops in performance. For large file transfers and a small `bytesPerSecond` limit, averaging fifteen minutes or more may be appropriate.