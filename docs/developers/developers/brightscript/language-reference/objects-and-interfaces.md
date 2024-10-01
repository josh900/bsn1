# Objects and Interfaces

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [BrightScript Objects](#brightscript-objects)
*   [Wrapper Objects](#wrapper-objects)
*   [Interfaces](#interfaces)
*   [Statement and Interface Integration](#statement-and-interface-integration)
    *   [PRINT](#print)
    *   [WAIT](#wait)
    *   [Expression Parsing](#expression-parsing)
    *   [Array Operator](#array-operator)
    *   [Member Access Operator](#member-access-operator)

## BrightScript Objects

Though BrightScript operates independently of its object architecture and library, they are both required for programming BrightScript applications. The API of a BrightSign platform is exposed to BrightScript as a library objects: Platforms must register a new BrightScript object to expose some part of its API.

BrightScript objects are written in C (or a compatible language such as C++), and are robust against version changes: Scripts are generally backwards compatible with objects that have undergone revisions. 

BrightScript objects keep a reference count; they delete themselves when the reference count reaches zero.

## Wrapper Objects

All intrinsic BrightScript types (Boolean, Integer, Float, Double, String, and Invalid) have object equivalents. If one of these intrinsic types is passed to a function that expects an object, the appropriate wrapper object will be created, assigned the correct value, and passed to the function (this is sometimes referred to as "autoboxing"): This allows, for example, *roArray* objects to store values (e.g. integers and strings) as well as objects.

Any expression that expects one of the above types will work with the corresponding wrapper object as well: *roBoolean*, *roInt*, *roFloat*, *roDouble*, *roString*.

The following examples illustrate how wrapper objects work:

```
Print 5.tostr()+"th"
Print "5".toint()+5
 
-5.tostr()    'This will cause an error. Instead, use the following:
(-5).tostr()
 
if type(5.tostr())<> "String" then stop
if (-5).tostr()<>"-5" then stop
if (1+2).tostr()<>"3" then stop
i=-55
if i.tostr()<>"-55" then stop
if 100%.tostr()<>"100" then stop
if (-100%).tostr()<>"-100" then stop
y%=10
if y%.tostr()<>"10" then stop
      
if "5".toint()<>5 or type("5".toint())<>"Integer" then stop
if "5".tofloat()<>5.0 or type("5".tofloat())<>"Float" then stop
fs="-1.1"
if fs.tofloat()<>-1.1 or fs.toint()<>-1 then stop
      
if "01234567".left(3)<>"012" then stop
if "01234567".right(4)<>"4567" then stop
if "01234567".mid(3)<>"34567" then stop
if "01234567".mid(3,1)<>"3" then stop
if "01234567".instr("56")<>5 then stop
if "01234567".instr(6,"56")<>-1 then stop
if "01234567".instr(0,"0")<>0 then stop
```

## Interfaces

Interfaces in BrightScript operate similarly to Java or Microsoft COM: An interface is a known set of member functions that implement a set of logic. In some ways, an interface is similar to a virtual base class in C++; any script or program that is compatible with C can use an object interface without regards to the type of object it belongs to: For example, the *roSerialPort* object, which controls the standard serial interface, implements three interfaces: *ifSerialControl*, *ifStreamReceive*, and *ifStreamSend*. Since the print statement sends its output to any object that has an *ifStreamSend* interface, it works with the *roSerialPort* object, as well as any other object with the *ifStreamSend* interface.

## Statement and Interface Integration

Some BrightScript statements have integrated functionality with interfaces. This section describes how to use statements with interfaces.

### PRINT

Using the `PRINT` statement in the following format will print into an object that has an *ifStreamSend* interface, including the *roTextField* and *roSerialPort* objects:

```
port = CreateObject("roSerialPort",0,115200)
print port, "string"
```

If the expression being printed evaluates to an object with an *ifEnum* interface, the `PRINT` statement will print every item that can be enumerated.

In addition to printing the values of intrinsic types, the `PRINT` statement can also be used to print any object that exposes one of the following interfaces: *ifString*, *ifInt*, *ifFloat*.

### WAIT

The `WAIT` statement can work in conjunction with any object that has an *ifMessagePort* interface.

### Expression Parsing

Any expression that expects a certain type of variable—including Integer, Float, Double, Boolean, or String—can accept an object with an interface equivalent of that type: *ifInt*, *ifFloat*, *ifDouble*, *ifBoolean*, *ifString*.

### Array Operator

The \[ \] array operator works with any object that has an *ifArray* or *ifAssociativeArray* interface, including arrays, associative arrays, and lists.

### Member Access Operator

The member access operator (i.e. [Dot Operator](../language-reference/operators.md)) works with any object that has an *ifAssociativeArray* interface. It also works with any object when used to call a member function (i.e. method). It also has special meaning when used on an *roXMLElement* or *roXMLList* object.