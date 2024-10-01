# XML Support

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

*   [Dot Operator](#dot-operator)
*   [Attribute Operator](#attribute-operator)
*   [Examples](#examples)
    *   [Flikr code clip](#flikr-code-clip)

BrightScript provides XML support with two BrightScript objects and a set of dedicated language features:

*   **roXMLElement**: This object provides support for parsing, generating, and containing XML.
    
*   **roXMLList**: This object is used to contain a list of *roXMLElement* instances.
    

## Dot Operator

The "." [Dot Operator](../language-reference/operators.md) has the following features when used with XML objects:

*   When used with an *roXMLElement* instance, the "." Dot Operator returns an *roXMLList* instance of the child tags that match the dot operand. If no tags match the operand, an empty list is returned.
    
*   When applied to an *roXMLList* instance, the "." Dot Operator aggregates the results of performing the above operation on each *roXMLElement* in the list.
    
*   When applied to XML, which is technically case sensitive, the "." Dot Operator is still case insensitive. If you wish to perform a case-sensitive XML operation, use the member functions of the *roXMLElement*/*roXMLList* objects.
    

## Attribute Operator

The “@” Attribute Operator can be used with an *roXMLElement* instance to return a named attribute. Though XML is case sensitive, the Attribute Operator is always case insensitive. If the Attribute Operator is used with an *roXMLList* instance, it will only return a value if that list contains exactly one element.

## Examples

```
<?xml version="1.0" encoding="utf-8" ?>
<rsp stat="ok">
    <photos page="1" pages="5" perpage="100" total="500">
        <photo id="3131875696" owner="21963906@N06" secret="f248c84625" server="3125"
        farm="4" title="VNY 16R" ispublic="1" isfriend="0" isfamily="0" />
        <photo id="3131137552" owner="8979045@N07" secret="b22cfde7c4" server="3078"
        farm="4" title="hoot" ispublic="1" isfriend="0" isfamily="0" />
        <photo id="3131040291" owner="27651538@N06" secret="ae25ff3942" server="3286"
        farm="4" title="172 • 365 :: Someone once told me..." ispublic="1" isfriend="0"
        />
    </photos>
</rsp>
```

Given the XML in the above *example.xml* file, then the following code will return an *roXMLList* instance with three entries:

```
rsp=CreateObject("roXMLElement")
rsp.Parse(ReadAsciiFile("example.xml"))
 
? rsp.photos.photo
```

The following will return an *roXMLElement* reference to the first photo (id="**3131875696**"):

```
? rsp.photos.photo[0]
```

The following will return an *roXMLList* reference containing the <photos> tag:

```
? rsp.photos
```

The following will return the string “100”:

```
rsp.photos@perpage
```

You can use the *roXMLElement.GetText()* method to return an element’s text: For example, if the variable `<booklist>` contains the element `<book lang=eng>The Dawn of Man</book>`, then the following code will print the string “The Dawn of Man”.

```
Print booklist.book.gettext()
```

Alternatively, using the Attribute Operator will print the string “eng”.

```
print booklist.book@lang
```

### Flikr code clip

```
REM
REM Interestingness
REM pass an (optional) page of value 1 - 5 to get 100 photos
REM starting at 0/100/200/300/400
REM
REM returns a list of "Interestingness" photos with 100 entries
REM


Function GetInterestingnessPhotoList(http as Object, page=1 As Integer) As Object


	print "page=";page


    http.SetUrl("http://api.flickr.com/services/rest/?method=flickr.interestingness.getList&api_key=YOURKEYGOESHERE&page="+mid(stri(page),2))


    xml=http.GetToString()


    rsp=CreateObject("roXMLElement")
    if not rsp.Parse(xml) then stop

       return helperPhotoListFromXML(http, rsp.photos.photo) 'rsp.GetBody().Peek().GetBody())

      
End Function


Function helperPhotoListFromXML(http As Object, xmllist As Object, owner=invalid As dynamic) As Object


    photolist=CreateObject("roList")
    for each photo in xmllist
       photolist.Push(newPhotoFromXML(http, photo, owner))
    end for
    return photolist


End Function


REM
REM newPhotoFromXML
REM
REM    Takes an roXMLElement Object that is an <photo> ... </photo>
REM    Returns an brs object of type Photo
REM       photo.GetTitle()
REM       photo.GetID()
REM       photo.GetURL()
REM       photo.GetOwner()
REM


Function newPhotoFromXML(http As Object, xml As Object, owner As dynamic) As Object
    photo = CreateObject("roAssociativeArray")
    photo.http=http
    photo.xml=xml
    photo.owner=owner
    photo.GetTitle=function():return m.xml@title:end function
    photo.GetID=function():return m.xml@id:end function
    photo.GetOwner=pGetOwner
    photo.GetURL=pGetURL
    return photo
End Function


Function pGetOwner() As String
	if m.owner<>invalid return m.owner
	return m.xml@owner
End Function


Function pGetURL() As String
	a=m.xml.GetAttributes()
	url="http://farm"+a.farm+".static.flickr.com/"+a.server+"/"+a.id+"_"+a.secret+".jpg"
	return url
End Function
```