# roPassKey

This object provides a means for generating keys (hashes) from a password and salt. The JavaScript equivalent is the Node.js Crypto API.

Object Creation: The object is passed an associative array that specifies the generation methods and cipher.

```
CreateObject("roPassKey", parameters As roAssociativeArray)
```

The associative array should contain the following parameters:

*   `method`: The key derivation method. Currently, only "pbkdf2" can be specified.
    
*   `keyfn`: The pseudorandom function (PRF). Currently, only "hmac-sha256" can be specified.
    
*   `keylen`: The key length
    
*   `iterations`: The number of iterations
    

## ifPassKey

##### GenerateKey(password As Object, salt As Object) As roByteArray

Generates a key using the supplied password and salt. The parameters may be passed as either strings or *roByteArray* instances. The generated *roByteArray* instance may contain all possible byte values, including NUL.

##### GenerateSalt(length As Integer) As roByteArray

Generates a salt of the specified length. This salt can be used when calling the `GenerateKey()` method. The generated *roByteArray* instance may contain all possible byte values, including NUL.

##### **Example**

```
' Create input test data
salt = CreateObject("roByteArray")
pass = CreateObject("roByteArray")
pass.FromAsciiString("password")
salt.FromAsciiString("salt")
' Create the key generator
pk = CreateObject("roPassKey",  { method: "pbkdf2", keyfn: "hmac-sha256", keylen: 32, iterations: 4096 } )
' key with be a roByteArray
key = pk.GenerateKey(pass, salt)
```