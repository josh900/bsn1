# roBoolean

This is the object equivalent of the Boolean intrinsic type. It is useful in the following situations:

*   **When an object is needed instead of an intrinsic value**: For example, if a Boolean is added to *roList*, it will be automatically wrapped in an *roBoolean* object by the language interpreter. When a function that expects a BrightScript component as a parameter is passed a Boolean, BrightScript automatically creates the equivalent BrightScript component.
    
*   **When an object exposes the** ***ifBoolean*** **interface**: That object can then be used in any expression that expects an intrinsic value.
    

## ifBoolean 

##### GetBoolean() As Boolean

##### SetBoolean(a As Boolean

#####