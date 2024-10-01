# roAssetFetcher

This object contains functions for downloading files to the pool. The JavaScript equivalent is [assetpoolfetcher](../../../../developers/player-apis/javascript-apis/assetfetcher.md).

Object Creation: The *roAssetFetcher* object must be passed an *roAssetPool* instance upon creation.

```
CreateObject("roAssetFetcher", pool As roAssetPool)
```

##### **Example**

```
Pool = CreateObject("roAssetPool", "pool")
Fetcher = CreateObject("roAssetFetcher", Pool)
```

## ifAssetFetcher

##### GetFailureReason() As String

Returns an error string if an *roAssetFetcher* method has failed (this is usually indicated by returning False). The error string may help diagnose the failure.

##### SetUserAndPassword(user As String, password As String) As Boolean

Sets the default user and password strings to be used for all download requests that are not otherwise marked using the following attributes: <auth inherit=”no”> or <auth user=”user” password =”password”>.

##### EnableUnsafeAuthentication(enable As Boolean) As Boolean

Supports basic HTTP authentication if True. HTTP authentication uses an insecure protocol, which might allow others to easily determine the password. The *roAssetFetcher* object will still prefer the stronger digest HTTP if it is supported by the server. If this method is False (which is the default setting), it will refuse to provide passwords via basic HTTP authentication, and any requests requiring this authentication will fail.

##### EnableUnsafeProxyAuthentication(enable As Boolean) As Boolean

Supports basic HTTP authentication against proxies if True (which, unlike EnableUnsafeAuthentication(), is the default setting). HTTP authentication uses an insecure protocol, which might allow others to easily determine the password. If this method is False, it will refuse to provide passwords via basic HTTP authentication, and any requests requiring this authentication type will fail.

##### EnableEncodings(enable As Boolean) As Boolean

Enables HTTP compression, which communicates to the server that the system can accept any encoding that the *roAssetFetcher* object is capable of decoding by itself (this behavior is enabled by default). Supported encodings currently include "deflate" and "gzip", which allow for transparent compression of responses. Clients of the *roAssetFetcher* instance see only the decoded data and are unaware of the encoding being used.

##### AsyncDownload(assets As roAssetCollection) As Boolean

Begins populating the asset pool using the files listed in the passed *roAssetCollection* instance. Files that are not already in the pool will be downloaded automatically. Events are raised during the download process to indicate whether individual file downloads have succeeded or failed; finally, a single event will be raised indicating whether the entire asset collection has been downloaded successfully or not. See the *roAssetFetcherEvent* and *roAssetFetcherProgressEvent* entries for more details.

##### AsyncSuggestCache(spec As roAssetCollection) As Boolean 

Begins downloading the required files from the passed *roAssetCollection* instance, then disconnects shortly afterward. If the player is set to use a suitably configured proxy (either globally or via the `SetProxy()` method), then the proxy will continue to download the files, making them readily available for `AsyncDownload()` calls in the future.

This method generates an *roAssetFetcherEvent* message with response code 202 ("Accepted") to indicate success. Other errors will be reported as usual. The final all-files-complete event code will always be -2 ("EVENT\_ALL\_FAILED") because the download does not complete.

##### AsyncCancel() As Boolean

Cancels any pending “Async” requests. Note that, prior to and during this method call, events associated with an asynchronous action may be queued. No more events will be queued once this call returns. We recommend collecting any pending events prior to calling any further “Async” methods on the same object to avoid confusion.

##### EnablePeerVerification(verification As Boolean) As Boolean

Enables checking of TLS/SSL certificates. This method is set to `true` by default. Disabling peer verification allows you to bypass an expired certificate check.

##### EnableHostVerification(verification As Boolean) As Boolean

Enables checking of the TLS/SSL certificate for the correct hostname. This method is set to `true` by default. Disabling host verification allows you to accept a certificate being sent for the wrong hostname.

> [!CAUTION]
> **Important**
> Peer verficiation and host verification are important security checks that prevent "man-in-the-middle" attacks. These features should only be disabled after careful consideration of the security implications.

##### SetCertificatesFile(filename As String) As Boolean

Configures an alternative set of CA certificates for the connection. This method is useful if the connection certificates are signed by a CA that is not on the the default trusted list (for example, if your organization uses a private CA hierarchy that is not signed by a well known root CA). This method replaces the default list, so the passed certificate file must contain all acceptable CA certificates required for the connection.

##### AddHeader(name As String, value As String) As Boolean

Specifies a header that will be passed to HTTP requests made by the *roAssetFetcher* instance. A particular download will not include the header if it has the <headers inherit=”no”> attribute in the sync spec.

##### SetHeaders(headers As roAssociativeArray) As Boolean

Specifies all headers that will be passed to HTTP requests made by the *roAssetFetcher* instance. This method removes any previously set headers. A particular download will not include the headers if it has the <headers inherit=”no”> attribute in the sync spec.

##### SetProxy(proxy As String) As Boolean

Sets the name or address of the proxy server that will be used by the *roAssetFetcher* instance. The proxy string should be formatted as "[http://user:password@hostname](http://user:password@hostname):port". It can contain up to four "\*" characters; each "\*" character can be used to replace one octet from the current IP address. For example, if the IP address is currently 192.168.1.2, and the proxy is set to "proxy-\*-\*", then the player will attempt to use a proxy named "proxy-192.168".

##### SetProxyBypass(hostnames As Array) As Boolean

Exempts the specified hosts from the proxy setting. The passed array should consist of one or more hostnames. The *roAssetFetcher* instance will attempt to reach the specified hosts directly rather than using the proxy that has been specified with the `SetProxy()` method. For example, the hostname "[http://example.com](http://example.com) " would exempt "[http://example.com](http://example.com) ", "[http://example.com:80](http://example.com:80) ", and "[http://www.example.com](http://www.example.com) " from the proxy setting.

##### SetFileProgressIntervalSeconds(interval As Integer) As Boolean

Specifies the interval (in seconds) between progress events when an individual file is being downloaded. Setting the interval to -1 disables all progress events. Setting the interval to 0 specifies that events should be generated as often as possible, though this will slow down the transfer process. If the interval is set to 0 or any positive integer, events will always be generated at the start and end of the file download irrespective of elapsed time. The default interval is 300 seconds.

##### SetFileRetryCount(count As Integer) As Boolean

Specifies the maximum number of times each file download will be retried before moving on to the next file download. The default retry count is five.

##### SetRelativeLinkPrefix(prefix As String) As Boolean

Specifies a prefix that will be appended to the front of relative links in the sync spec. Normally, this method is used to make file:/// URIs drive agnostic, but it can also be used to reduce the size of the sync spec if all files are stored in the same place. Non-relative links are not affected by this method.

##### BindToInterface(interface As Integer) As Boolean

Ensures that the HTTP request goes out over the specified network interface (0 for Ethernet or 1 for WiFi). The default behavior (which can be specified by passing -1) is to send requests using the most appropriate network interface, which may depend on the routing metric configured via the *roNetworkConfiguration* object. If both interfaces are on the same layer 2 network, this method may not work as expected due to the Linux weak-host model.

##### SetMaximumReceiveBytesPerSecond(bytes\_per\_second as Double) As Boolean

Limits the rate at which downloads are performed by the *roAssetFetcher* instance. The source data rate isn't under the direct control of the BrightSign player, but download rates should average below the specified value over time. 

This method returns `true` on success and `false` on failure. In event of failure, the `GetFailureReason()` method may provide more information.

##### SetMinimumTransferRate(bytes\_per\_second As Integer, period\_in\_seconds As Integer) As Boolean

Sets the minimum transfer rate for each file download. A transfer will be terminated if the rate drops below *bytes\_per\_second* when averaged over *period\_in\_seconds*. Note that if the transfer is over the Internet, you may not want to set `period_in_seconds` to a small number in case network problems cause temporary drops in performance. For large file transfers and a small `bytes_per_second` limit, averaging fifteen minutes or more may be appropriate.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of type *roAssetFetcherEvent* and *roAssetFetcherProgressEvent* to the attached message port.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()` . It will return Invalid if no data has been set.