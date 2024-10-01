# roSystemTime

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This object provides the ability to read and write the time stored in the real-time clock (RTC). It can also be used to read and write the time-zone setting. The JavaScript equivalent is [systemtime](https://docs.brightsign.biz/display/DOC/systemtime).

> [!NOTE]
> Dates up to January 1, 2038 are supported.

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifMessagePort

##### SetPort(port As roMessagePort)

Posts messages of the type *roNetworkTimeEvent* to the attached message port.

## ifSystemTime

##### GetLocalDateTime() As roDateTime

Returns the current time from the RTC (modulated using the current time zone) as an *roDateTime* instance.

##### GetUtcDateTime() As roDateTime

Returns the current time from the RTC (modulated using the UTC/GMT time zone) as an *roDateTime* instance.

##### GetZoneDateTime(timezone\_name As String) As Object

Returns the current time from the RTC (modulated using the specified time zone) as an *roDateTime* instance. Supported time zones are listed below.

##### SetLocalDateTime(local\_DateTime As roDateTime) As Boolean

Specifies a new time for the RTC using the current time zone.

##### SetUtcDateTime(utc\_DateTime As roDateTime) As Boolean

Specifies a new time for the RTC using the UTC/GMT time zone.

##### GetTimeZone() As String

Returns the current time-zone setting of the player. A `POSIX:` value is appended to the beginning of the string if the time zone has been set using the POSIX format.

##### SetTimeZone(zone\_name As String) As Boolean

Specifies a new time-zone setting for the player (supported time zones are listed below). Alternatively, a POSIX formatted time zone can be applied by appending a `POSIX:` value to the beginning of the string.

The following code specifies a POSIX-formatted time zone:

```
t = CreateObject("roSystemTime")
t.SetTimeZone("POSIX:GMT-0BST-1,M3.5.0/1:00,M10.5.0/2:00")
```

##### IsValid() As Boolean

Returns True if the system time is set to a valid value. The time can be set from the RTC or with NTP.

##### GetLastNetworkTimeResult() As roAssociativeArray

Returns an associative array containing information about the last attempt to set the time via the network:

*   `success_timestamp`: A value indicating when the clock was last set successfully via the network. This value is zero if the clock has never been set successfully via the network.
    
*   `attempt_timestamp`: A value indicating when the last attempt was made to set the clock via the network. This value is zero if no attempt has been made yet.
    
*   `failure_reason`: If the last attempt to set the clock via the network failed, this string will contain an error message. If the last attempt was successful, this string will be empty.
    

In this associative array, "timestamp" refers to the number of seconds since the player booted. This value can be compared against the total uptime of the player, which is retrieved by calling `UpTime(0)`.

## Supported Time Zones 

The following are supported system time zones (this list does not apply to POSIX-formatted time zones):

*   EST: US Eastern Time
    
*   CST: US Central Time
    
*   MST: US Mountain Time
    
*   PST: US Pacific Time
    
*   AKST: Alaska Time
    
*   HST: Hawaii-Aleutian Time with no Daylight Savings (Hawaii)
    
*   HST1: Hawaii-Aleutian Time with Daylight Saving
    
*   MST1: US MT without Daylight Saving Time (Arizona)
    
*   EST1: US ET without Daylight Saving Time (East Indiana)
    
*   AST: Atlantic Time
    
*   CST2: Mexico (Mexico City)
    
*   MST2: Mexico (Chihuahua)
    
*   PST2: Mexico (Tijuana)
    
*   BRT: Brazil Time (Sao Paulo)
    
*   NST: Newfoundland Time
    
*   AZOT: Azores Time
    
*   GMTBST: London/Dublin Time
    
*   WET: Western European Time
    
*   CET: Central European Time
    
*   EET: Eastern European Time
    
*   MSK: Moscow Time
    
*   SAMT: Delta Time Zone (Samara)
    
*   YEKT: Echo Time Zone (Yekaterinburg)
    
*   IST: Indian Standard Time
    
*   NPT: Nepal Time
    
*   OMST: Foxtrot Time Zone (Omsk)
    
*   JST: Japanese Standard Time
    
*   CXT: Christmas Island Time (Australia)
    
*   AWST: Australian Western Time
    
*   AWST1: Australian Western Time without Daylight Saving Time
    
*   ACST: Australian Central Standard Time (CST) with Daylight Saving Time
    
*   ACST1: Darwin, Australia/Darwin, and Australian Central Standard Time (CST) without Daylight Saving Time
    
*   AEST: Australian Eastern Time with Daylight Saving Time
    
*   AEST1: Australian Eastern Time without Daylight Saving Time (Brisbane)
    
*   NFT: Norfolk (Island) Time (Australia)
    
*   NZST: New Zealand Time (Auckland)
    
*   CHAST: , Fiji Time, , Fiji, Pacific/Fiji, Yankee Time Zone (Fiji)
    
*   SST: X-ray Time Zone (Pago Pago)
    
*   GMT: Greenwich Mean Time
    
*   GMT-1: 1 hour behind Greenwich Mean Time
    
*   GMT-2: 2 hours behind Greenwich Mean Time
    
*   GMT-3: 3 hours behind Greenwich Mean Time
    
*   GMT-3:30: 3.5 hours behind Greenwich Mean Time
    
*   GMT-4: 4 hours behind Greenwich Mean Time
    
*   GMT-4:30: 4.5 hours behind Greenwich Mean Time
    
*   GMT-5: 5 hours behind Greenwich Mean Time
    
*   GMT-6: 6 hours behind Greenwich Mean Time
    
*   GMT-7: 7 hours behind Greenwich Mean Time
    
*   GMT-8: 8 hours behind Greenwich Mean Time
    
*   GMT-9: 9 hours behind Greenwich Mean Time
    
*   GMT-9:30: 9.5 hours behind Greenwich Mean Time
    
*   GMT-10: 10 hours behind Greenwich Mean Time
    
*   GMT-11: 11 hours behind Greenwich Mean Time
    
*   GMT-12: 12 hours behind Greenwich Mean Time
    
*   GMT-13: 13 hours behind Greenwich Mean Time
    
*   GMT-14: 14 hours behind Greenwich Mean Time
    
*   GMT+1: 1 hour ahead of Greenwich Mean Time
    
*   GMT+2: 2 hours ahead of Greenwich Mean Time
    
*   GMT+3: 3 hours ahead of Greenwich Mean Time
    
*   GMT+3:30: 3.5 hours ahead of Greenwich Mean Time
    
*   GMT+4: 4 hours ahead of Greenwich Mean Time
    
*   GMT+4:30: 4.5 hours ahead of Greenwich Mean Time
    
*   GMT+5: 5 hours ahead of Greenwich Mean Time
    
*   GMT+5:30: 5.5 hours ahead of Greenwich Mean Time
    
*   GMT+6: 6 hours ahead of Greenwich Mean Time
    
*   GMT+6:30: 6.5 hours ahead of Greenwich Mean Time
    
*   GMT+7: 7 hours ahead of Greenwich Mean Time
    
*   GMT+7:30: 7.5 hours ahead of Greenwich Mean Time
    
*   GMT+8: 8 hours ahead of Greenwich Mean Time
    
*   GMT+8:30: 8.5 hours ahead of Greenwich Mean Time
    
*   GMT+9: 9 hours ahead of Greenwich Mean Time
    
*   GMT+9:30: 9.5 hours ahead of Greenwich Mean Time
    
*   GMT+10: 10 hours ahead of Greenwich Mean Time
    
*   GMT+10:30: 10.5 hours ahead of Greenwich Mean Time
    
*   GMT+11: 11 hours ahead of Greenwich Mean Time
    
*   GMT+11:30: 11.5 hours ahead of Greenwich Mean Time
    
*   GMT+12: 12 hours ahead of Greenwich Mean Time
    
*   GMT+12:30: 12.5 hours ahead of Greenwich Mean Time
    
*   GMT+13: 13 hours ahead of Greenwich Mean Time
    
*   GMT+14: 14 hours ahead of Greenwich Mean Time