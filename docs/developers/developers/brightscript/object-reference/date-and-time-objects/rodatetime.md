# roDateTime

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Version 9 and Older Versions

*   [Version 9 (OS 9)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual_ver9.pdf?version=1&modificationDate=1681926520148&cacheVersion=1&api=v2)
    
*   [Version 8 (OS 8)](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScriptReferenceManual%20(ver%208).pdf?version=1&modificationDate=1681851693731&cacheVersion=1&api=v2)
    
*   [Version 7.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.1).pdf?version=1&modificationDate=1681851450896&cacheVersion=1&api=v2)
    
*   [Version 7.0](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%207.0).pdf?version=1&modificationDate=1681851517656&cacheVersion=1&api=v2)
    
*   [Version 6.2](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightScript%20Reference%20Manual%20(ver%206.2).pdf?version=1&modificationDate=1681851180597&cacheVersion=1&api=v2)
    
*   [Version 6.1](https://brightsign.atlassian.net/wiki/download/attachments/370674351/BrightSignReferenceManual_V6.1.pdf?version=1&modificationDate=1681851246728&cacheVersion=1&api=v2)
    
*   [Previous Versions](https://support.brightsign.biz/hc/en-us/articles/218067797-Legacy-Documentation-and-User-Guides) 
    

This object is used to represent an instant in time. At the time of its creation, a new object represents zero seconds. The JavaScript equivalent is "Date".

## ifDateTime

##### GetDayOfWeek() As Integer  
 

##### GetDay() As Integer  
 

##### GetMonth() As Integer  
 

##### GetYear() As Integer  
 

##### GetHour() As Integer  
 

##### GetMinute() As Integer  
 

##### GetSecond() As Integer  
 

##### GetMillisecond() As Integer  
 

##### SetDay(day As Integer) As Void  
 

##### SetMonth(month As Integer) As Void  
 

##### SetYear(year As Integer) As Void  
 

##### SetHour(hour As Integer) As Void  
 

##### SetMinute(minute As Integer) As Void  
 

##### SetSecond(second As Integer) As Void  
 

##### SetMillisecond(millisecond As Integer) As Void  
 

##### AddSeconds(seconds As Integer) As Void  
 

##### SubtractSeconds(seconds As Integer) As Void  
 

##### AddMilliseconds(milliseconds As Integer) As Void  
 

##### SubtractMilliseconds(milliseconds As Integer) As Void  
 

##### Normalize() As Boolean

Checks that all the fields supplied are correct. This function fails if the values are out of bounds.

##### ToIsoString() As String

Returns the current *roDateTime* value as an ISO-8601 basic formatted string. Hyphens for date and colons for time are omitted, and a comma is used to separate seconds from milliseconds: For example, the ISO-8601 standard "2014-05-29T12:30:00.100" would be formatted as "20140529T123000,100".

This method returns an empty string if the year is less than 1970 or greater than 2100. Since a new, un-configured *roDateTime* object lies outside the acceptable range, it will also return an empty string.

##### FromIsoString(date-time As String) As Boolean

Sets the value of the *roDateTime* object using an ISO-8601 basic formatted string. Hyphens for date and colons for time are omitted, and either a period or comma can be used to separate seconds from milliseconds: The ISO-8601 standard "2014-05-29T12:30:00.100" could, for example, be formatted as either "20140529T123000,100" or "20140529T123000.100". This method will return `false` (indicating that it has not affected changes to the *roDateTime* object) if the string is formatted incorrectly or if the date passed is outside the range of January 1, 1970 and December 31, 2100.

##### ToSecondsSinceEpoch() As Integer

Returns the number of seconds that have elapsed since midnight on January 1, 1970, as represented by the *roDateTime* instance (not the system time).

##### FromSecondsSinceEpoch(seconds As Integer) As Boolean

Populates the *roDateTime* instance with the specified number of seconds since midnight on January 1, 1970.

##### GetString() As String

## ifString

##### GetString() As String

Returns the current date using a sortable date format: "YYYY/MM/DD hh:mm:ss.sss".