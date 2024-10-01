# roHtmlWidgetEvent

If an *roMessagePort* is attached to an *roHtmlWidget*, it will receive *roHtmlWidgetEvent* objects when something happens to the parent *roHtmlWidget* instance. 

## ifUserData

##### SetUserData(user\_data As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifHTMLWidgetEvent

##### GetData() As roAssociativeArray

Returns the event data as an associative array with the following key/value pairs:

*   `reason` string: The cause of the event, which can be one of the following:
    
    *   `"load-started"`: The HTML widget has started loading a page.
        
    *   `"load-finished"`: The HTML widget completed loading a page.
        
    *   `"load-error"`: The HTML widget failed to load a page. Use the `uri` key to identify the failing resource and the `message` key to retrieve some explanatory text.
        
    *   `"download-request"`: The HTML widget instance has received a download request. The Chromium instance does not process download requests for MIME types it doesn't recognize (e.g. PDFs); instead, it passes this event, along with the `mime-type` and `url` parameters to the BrightScript autorun for processing.
        
    *   `"new-window-request"`: The HTML widget instance has received a request to open a URI in a new window. This request will normally come from HTML anchors with `"target=_blank"`/`"target=_top"` or the JavaScript `Window.open()` method. The requested URI is specified in the `uri` parameter.
        
*   `javascript-dialog` string: If the HTML widget instance has received a JavaScript alert, confirmation, etc., BrightScript will respond by calling the roHtmlWidget `acceptdialog(responseasString)` and `rejectdialog()` methods. See [roHtmlWidget#roHtmlWidget.acceptdialog(responseasString)](../presentation-and-widget-objects/rohtmlwidget.md). If no response is provided within one second, roHtmlWidget auto rejects the dialog attempt, and if these APIs are called when there is no dialog request on roHtmlWidget, they have no effect. This parameter was added in BOS 8.5.16.
    
*   `message` string: The message that the JavaScript dialog will display (applicable for `reason:"javascript-dialog"` only), or explanatory text related to the load failure (applicable for reason:"load-error" only). This property exists for multiple event types, but it has different meanings for different event types.
    
*   `default_text` string:  If a JavaScript prompt dialog asks the user to enter text, this default text will be displayed in the input field. This field will be empty for other dialog types (applicable for `reason:"javascript-dialog"` only). This parameter was added in BOS 8.5.16.
    
*   `type` int: The dialog type for the `“javascript-dialog”` event: either 0 for alert, 1 for confirm, 2 for prompt, 3 for an "onbeforeunload Event" (applicable for `reason:"javascript-dialog"` only). This parameter was added in BOS 8.5.16.
    
*   `security_origin` string: The security origin of the request (applicable for `reason:"javascript-dialog"` only). This parameter was added in BOS 8.5.16.
    
*   `uri` string: The URI of the failing resource or new-window request (applicable for `reason:"load-error"` or `reason:"new-window-request"`)
    
*   `mime-type` string: The MIME type of the download request (applicable for `reason:"download-request"` only)
    
*   `url` string: The URL of the download request (applicable for `reason:"download-request"` only)
    

## Example

The following event loop waits for an HTML widget event. If the event indicates that a PDF download request has been received, the script passes the relevant data to a *CreatePdfRenderer()* function that is not defined here:

```
while true
	ev = wait(0, gaa.mp)
	print "=== BS: Received event ";type(ev)
	if type(ev) = "roHtmlWidgetEvent" then
		eventData = ev.GetData()
		if type(eventData) = "roAssociativeArray" and type(eventData.reason) = "roString" then
			if eventData.reason = "load-error" then
				print "=== BS: HTML load error: "; eventData.message
			else if eventData.reason = "load-finished" then
				print "=== BS: Received load finished"
				receivedLoadFinished = true
			else if eventData.reason = "message" then
				' To use this: msgPort.PostBSMessage({text: "my message"});
			else if eventData.reason = "load-started" then
				print "=== BS: Received load started"
			else if eventData.reason = "download-request" then
				print "=== BS: Received a download request"
				if eventData.mime_type = "application/pdf" then
					CreatePdfRenderer("file:///index.html?file=" + eventData.url)
				endif
			else
				print "======= UNHANDLED HTML EVENT ========="
				print eventData.reason
			endif
		else
			print "=== BS: Unknown eventData: "; type(eventData)
		endif
	endif
endwhile
```