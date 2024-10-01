# roXMLElement

This object is used to contain an XML tree. The JavaScript equivalent is `DOMParser()`.

The *roXMLElement* object is created with no parameters: 

```
CreateObject("roXMLElement")
```

The following examples illustrate how XML elements are parsed in BrightScript:

```
<tag1>This is example text</tag1>
```

*   Name = tag1
    
*   Attributes = Invalid
    
*   Body = *roString* containing "This is example text"
    

```
<tag2 caveman="barney"/>
```

*   Name = tag2
    
*   Attributes = *roAssociativeArray* with one entry, `{caveman, barney}`
    
*   Body = Invalid
    

If the tag contains other tags, the body will be of type *roXMLList*.

To generate XML content, create an *roXMLElement* and call the `SetBody()` and `SetName()` methods to build it–then call the `GenXML()` method to generate it.

##### **Example**

```
root.SetName("myroot")
root.AddAttribute("key1","value1")
root.AddAttribute("key2","value2")
ne=root.AddBodyElement()
ne.SetName("sub")
ne.SetBody("this is the sub1 text")
ne=root.AddBodyElement()
ne.SetName("subelement2")
ne.SetBody("more sub text")
ne.AddAttribute("k","v")
ne=root.AddElement("subelement3")
ne.SetBody("more sub text 3")
root.AddElementWithBody("sub","another sub (#4)")
PrintXML(root, 0)
print root.GenXML(false)
```

## ifXMLElement

##### GetBody() As Object  
 

##### GetAttributes() As Object  
 

##### GetName() As String  
 

##### GetText() As String  
 

##### GetChildElements() As Object  
 

##### GetNamedElements(a As String) As Object  
 

##### GetNamedElementsCi(a As String) As Object  
 

##### SetBody(a As Object)

Generates an *roXMLList* for the body if needed. The method then adds the passed item (which should be an *roXMLElement* tag).

##### AddBodyElement() As Object  
 

##### AddElement(a As String) As Object  
 

##### AddElementWithBody(a As String, b As Object) As Object  
 

##### AddAttribute(a As String, b As String)  
 

##### SetName(a As String)  
 

##### Parse(a As String) As Boolean

Parses the XML content passed to it. In the event of failure, this method returns False. However, it also populates *roXMLElement* with whatever text could be successfully parsed. To avoid passing along erroneous strings, it is always best to have the script check the return value of `Parse()` before using them.

##### GenXML(a As Boolean) As String

Generates XML content. This method takes a single Boolean parameter, indicating whether or not the XML should have an `<?xml …>` tag at the top.

##### Clear() As Void  
 

##### GenXMLHdr(a As String) As String  
 

##### IsName(a As String) As Boolean  
 

##### HasAttribute(a As String) As Boolean  
 

##### ParseFile(a As String) As Boolean

## Example

This subroutine example prints out the contents of an *roXMLElement* tree:

```
PrintXML(root, 0)

Sub PrintXML(element As Object, depth As Integer)
    print tab(depth*3);"Name: ";element.GetName()
    if not element.GetAttributes().IsEmpty() then
        print tab(depth*3);"Attributes: ";
        for each a in element.GetAttributes()
            print a;"=";left(element.GetAttributes()[a], 20);
            if element.GetAttributes().IsNext() then print ", ";
        end for
        print
    end if
    if element.GetText()<>invalid then
        print tab(depth*3);"Contains Text: ";left(element.GetText(), 40)
    end if
    if element.GetChildElements()<>invalid
        print tab(depth*3);"Contains roXMLList:"
        for each e in element.GetChildElements()
            PrintXML(e, depth+1)
        end for
    end if
    print
end sub
```