# Global BrightScript-JavaScript Functions

The following functions are implemented at the global level.

`IsBSLocalFilePresent()`

Determines whether the specified file exists on local storage. This function interfaces with the BrightScript pool and determines if the file exists there; it also searches for files with standard names.

`CloseAllBSClasses()`

This function effectively calls `Close()` on all custom objects that have been created and have yet to be garbage collected. Call this function when initializing a new web page to ensure all previous links to hardware interfaces on the player have been removed.