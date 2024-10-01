# roBlockCipher

This object provides a means for symmetric block encryption. It currently supports AES and CBC ciphers, at block sizes of 128, 192, or 256 bits. The JavaScript equivalent is the Node.js Crypto API.

Object Creation: The *roBlockCipher* object is created with an associative array representing a set of parameters.

```
CreateObject("roBlockCipher", parameters As roAssociativeArray)
```

The associative array should contain the following parameters:

*   mode: `"aes-128-cbc"`, `"aes-192-cbc"`, or `"aes-256-cbc"`
    
*   padding: `"zero"` or `"pkcs7"`. The object defaults to zero padding if this parameter is omitted.
    

Padding is required for inputs that are not an exact multiple of the cipher block size. Specifying `"zero"` will add padding only when needed, while specifying `"pkcs7"` always adds padding, even if the data is already a multiple of the block size (in this case, an entire block will be added). PKCS#7 padding is automatically removed upon decryption, and zero padding will be retained since there are no means to unambiguously distinguish pad values from data.

## ifBlockCipher

##### SetIV(iv As Object) As Void

Sets the Initialization Vector (IV) for CBC (Cipher-Block-Chaining) modes. If the supplied IV is shorter than required, then it will be zero padded (passing an empty string will set the vector to all zeroes). The IV will typically contain arbitrary characters and be in the form of an *roByteArray*, though it can also be a string.

##### Encrypt(key As Object, plaintext As Object) As roByteArray

Uses the specified key to encrypt the plaintext parameter, which can be passed as either a string or an *roByteArray*.

##### Decrypt(key As Object, cipher\_text As Object) As roByteArray

Uses the specified key to decrypt cipher text, which should be passed as an *roByteArray*. Because the cipher text is encrypted, it can contain any character.

##### **Example**

```
' This is Case#4 from RFC3602
key = CreateObject("roByteArray")
iv = CreateObject("roByteArray")
plain = CreateObject("roByteArray")
key.FromHexString("56e47a38c5598974bc46903dba290349")
iv.FromHexString("8ce82eefbea0da3c44699ed7db51b7d9")   plain.FromHexString("a0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedf")
c = CreateObject("roBlockCipher", { mode: "aes-128-cbc" })
c.SetIV(iv)
crypt = c.Encrypt(key, plain)
result = crypt.ToHexString()
expected = UCase("c30e32ffedc0774e6aff6af0869f71aa0f3af07a9a31a9c684db207eb0ef8e4e35907aa632c3ffdf868bb7b29d3d46ad83ce9f9a102ee99d49a53e87f4c3da55")


' Decrypt example to recover the encrypted data
c.SetIV(iv)
roundtrip = c.Decrypt(key, crypt)


' Second example selecting PKCS#7 padding
c = CreateObject("roBlockCipher", { mode: "aes-128-cbc", padding: "pkcs7" })
```