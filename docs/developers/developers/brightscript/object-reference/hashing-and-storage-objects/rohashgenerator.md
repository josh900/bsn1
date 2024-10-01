# roHashGenerator

This object allows you to generate a variety of message digests. The JavaScript equivalent is the Node.js Crypto API.

Object Creation: The hashing algorithm is specified when creating the *roHashGenerator* object.

```
CreateObject("roHashGenerator", algorithm As String)
```

The algorithm parameter accepts the following strings:

*   "SHA256"
    
*   "SHA384"
    
*   "SHA512"
    
*   "SHA1"
    
*   "MD5"
    
*   "CRC32"
    

> [!NOTE]
> CRC32 is only available on firmware versions 4.4.x or later.

## ifHashGenerator

##### Hash(obj As Object) As Object

Hashes the payload, which can be supplied in the form of a string (or any object implementing *ifString*) or an *roByteArray*. The hash is returned as an *roByteArray*.

##### SetHmacKey(key As Dynamic) As Boolean

Supplies a cryptographic key for the hashing function. This method accepts a plain-text key.

##### SetObfuscatedHmacKey(key As String) As Boolean

Supplies a cryptographic key for the hashing function. This method accepts a key that is obfuscated using a shared secret.

##### GetFailureReason() As String