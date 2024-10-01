# BSSyncManager

For more information about available methods, refer to the [*roSyncManager*](https://docs.brightsign.biz/display/DOC/roSyncManager) entry. To enable Genlock in JavaScript, pass the *BSSyncManager*/*roSyncManager* domain to the [*videooutput.setSyncDomain()*](../../player-apis/javascript-apis/videooutput.md) method

## Object Creation

BSSyncManager(in DOMString interface, in DOMString domain, in DOMString multicast\_address, in DOMString multicast\_port)

Setting the interface to `""` (empty) will use all interfaces, and omitting the `interface` parameter is equivalent to specifying an empty interface name. 

## Methods

`void SetAsLeader(in boolean leader_mode) raises(DOMException)`

`void Synchronize(in DOMString id, in unsigned long ms_delay) raises(DOMException)`

`void Close()`

Shuts down the instance, preventing it from further consuming resources. If this method is not called, garbage collection determines when the instance will be destroyed.

`BindToInterface(in DOMString interface)`

Binds the SyncManager to a specific network interface (for example, "eth0", "wifi0"). Setting the interface to `""` (empty) will use all interfaces.

`boolean SetEncryptionEnable(in boolean enable)`  
  
`boolean SetEncryptionEnable(in boolean enable, in DOMString key)`  
  
`boolean SetEncryptionEnable(in boolean enable, in ArrayBuffer key)`

Enables or disables encryption of *BSSyncManager* messages over the network. This method returns `true` on success and `false` on failure.

The key may be specified as a string or binary array. Alternatively, a `key` value may not be supplied, in which case a pseudo-randomly generated key is used. Setting `enable` to `false` and supplying a `key` at the same time will cause this method to fail. 

Encryption is available (and enabled by default) in OS8 and later. Note the following behavior in mixed-version environments:

*   Follower units that have encryption enabled can ingest unencrypted synchronization messages from a leader unit. Once a follower unit receives encrypted packets, it will no longer accept unencrypted packets from a leader unit, unless encryption is explicitly disabled using this method.
    
*   Follower units that have encryption disabled (or do not support encryption) cannot ingest encrypted messages from a leader unit. Therefore, if a synchronization group includes mixed versions of OS, the leader unit should always have an older version of OS than the follower units.
    

`boolean SetEncryptionEnableWithObfuscatedKey(in DOMString obfuscated_key) As Boolean`

Enables encryption of *BSSyncManager* messages using an obfuscated key. Contact [support@brightsign.biz](mailto:support@brightsign.biz) to learn more about generating a key for obfuscation and storing it on the player.

## HTML Video Functions

setSyncParams(in DOMString domain, in DOMString id, in DOMString iso\_timestamp)

HTML video tags include the `setSyncParams()` function. Calling this function synchronizes the video with the specified sync group.

## Events

The following event is available on the *BSSyncManager* object. It can receive events of the type *BSSyncManagerEvent*.

`onsyncevent` 

### BSSyncManagerEvent – Attributes

The following attributes are relevant to the onsyncevent event:

`readonly attribute DOMString domain`

`readonly attribute DOMString id`

`readonly attribute DOMString iso_timestamp`

## Examples

The following JavaScript example contains two videos being synchronized locally with *BSSyncManager*. If a follower player is configured to be in the same PTP domain as the leader player and uses the follower HTML script, then it will display the videos in sync with the leader player. This can be implemented on multiple follower players.

### Leader Script

```
<video id="one" hwz="on">
    <source id="one_src" src="pirates.mov">
</video>

<script>
    // Create the sync manager with provided multicast settings
    var sync = new BSSyncManager("domain1", "224.0.126.10", 1539);

    sync.onsyncevent = function (e) {
        document.getElementById("one").setSyncParams(e.domain, e.id, e.iso_timestamp);
        document.getElementById("one").load();
        document.getElementById("one").play();
        console.log(e.domain);
        console.log(e.id);
        console.log(e.iso_timestamp);
    };

    function startTimer() {
        setTimeout(function () {
            restartLeader()
        }, 30000);
    }
    function restartLeader() {
        // Synchronize the videos to start playing in 1000ms
        sync.SetAsLeader(1);
        sync.Synchronize("sync_event1", 1000);
        startTimer();
    }
    restartLeader();

</script>
```

### Follower Script

```
<video id="one" hwz="on">
    <source id="one_src" src="pirates.mov">
</video>

<script>
    // Create the sync manager with provided multicast settings
    var sync = new BSSyncManager("domain1", "224.0.126.10", 1539);

    sync.onsyncevent = function (e) {
        document.getElementById("one").setSyncParams(e.domain, e.id, e.iso_timestamp);
        document.getElementById("one").load();
        document.getElementById("one").play();
        console.log(e.domain);
        console.log(e.id);
        console.log(e.iso_timestamp);
    };
 
</script>

</body>
</html>
```