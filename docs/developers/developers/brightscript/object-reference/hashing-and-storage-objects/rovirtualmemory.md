# roVirtualMemory

The *roVirtualMemory* object allows you to create a virtual memory repository for the Chromium HTML engine. This allows Chromium to automatically swap unused elements out of physical memory.

This object is only available on platforms that can support SSD/mSATA drives: XTx44, XTx43, XDx34, XDx33, and 4Kx42.

Object Creation: This object is instantiated without parameters.

```
CreateObject("roVirtualMemory")
```

## ifVirtualMemory

##### AddSwapFile(parameters As roAssociativeArray) As Boolean

Adds a virtual memory repository to local storage. This method accepts an associative array with the following parameters:

*   `filename` string: The URI of the swap file to be created. It is possible to specify a file location other than the SSD/mSATA drive, but it is not recommended.
    
*   `megabytes` int: The size of the swap file to be created.
    

If the specified file does not already exist, it will be created. If it already exists, the size will be modified. Either way, this operation can take some time, but it should only need to be called once.

##### RemoveSwapFile(filename As String) As Boolean

Removes a swap file with the specified filename.

## ifFailureReason

##### GetFailureReason() As String

Returns additional useful information when a method on the *ifVirtualMemory* interface returns `False`.