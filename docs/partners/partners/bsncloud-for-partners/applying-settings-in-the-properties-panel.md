# Applying Settings in the Properties Panel

![](https://brightsign.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Table of Contents

*   [Prerequisites](#prerequisites)
*   [Implementing the Settings Handler / Disabling Property Lock](#implementing-the-settings-handler-disabling-property-lock)
*   [API Specification](#api-specification)
    *   [POST /api/v1/system/supervisor/capabilities](#post-apiv1systemsupervisorcapabilities)
        *   [Request Body](#request-body)
        *   [Response Body](#response-body)
*   [Example Script](#example-script)
*   [Caveats](#caveats)

BrightSign’s OS version 8.2.72 and BrightAuthor:connected version 1.6.29 contain a new feature that lets users see and modify settings using the BSN.cloud Properties Panel or through the BSN.cloud API. To avoid backwards compatibility issues, the supervisor won't honor these settings unless it is first enabled in a custom presentation or custom application/plugin.

This feature is natively supported and enabled in BrightAuthor:connected presentations using version 1.6.29 or later, but you must enable it if you are running custom scripts. The steps required to enable this feature are described below.

## Prerequisites

*   You must be using BSN.cloud
    
*   Minimum BrightAuthor:connected version: 1.6.29
    
*   Minimum OS version: OS 8.2.72
    

## Implementing the Settings Handler / Disabling Property Lock

A player under the control of BSN.cloud will, by default, disallow updates pushed from the cloud to the player if it is using a partner application. To allow the player to accept property updates from BSN.cloud, implement the Settings Handler which allows you to disable [Property Lock](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/404623943/Presentation+Settings#Property-Lock). Partners can do this using the Example Script on this page.

To enable the Settings Handler:

1.  Include the code snippet from the Example Script section in your custom presentation or custom application/plugin.
    
2.  In BrightAuthor:connected, navigate to the player’s network (under the [Network](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/384958995/Network) tab on the top right). In this section, the player settings are available in the Properties panel.
    

Once the device-side API is turned on, the player settings will be accessible in the Properties panel of BrightAuthor:connected (under the [Network](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/384958995/Network) tab).

## API Specification

This API specification is used by custom presentations or plugins, either invoked by BrightScript or JavaScript, to enable the “Settings Panel” (Settings Handler).

The base URL or player’s IPv4 IP address (the default port server is hosted on 80) is [http://localhost](http://localhost)

> [!NOTE]
> This is an internal endpoint and will only respond to a Node or JavaScript application running on the player (it is not part of the local DWS).

### POST /api/v1/system/supervisor/capabilities

#### Request Body

```
{
	"script": {
	“type”: “Custom”
	“version”: “10.0.60” // Can be any version in a x.x.x format. Used to communicate script version to BSN.cloud,
	displayed in “Settings Panel” }
}
```

#### Response Body

*   Success: {"success":true}
    
*   Error: {"status”: <error status code>, “message”: <error message>}
    

## Example Script

Partners who want to upgrade to use this feature must include the following code snippet in their BrightSign presentation or plugin. 

Note that this example is a simple autorun which can be run as is. However the `EnableSettingsHandler`() subroutine should either be copied and called in an appropriate location relative to the other logic in the script, or the code within `EnableSettingsHandler()` can be copied and pasted into a valid location in script to be run within the existing logic. This assumes the developer has basic knowledge of BrightScript.

```
Sub main()
  EnableSettingsHandler()
end sub
 
Sub EnableSettingsHandler()
  localBaseUrl = "http://localhost"
  supervisorApiV1Route = "/api/v1"
   
  supervisorCapabilitiesUrlXfer = CreateObject("roUrlTransfer")
  supervisorCapabilitiesUrlXfer$ = localBaseUrl + supervisorApiV1Route + "/system/supervisor/capabilities"
  supervisorCapabilitiesUrlXfer.SetUrl(supervisorCapabilitiesUrlXfer$)
  supervisorCapabilitiesUrlXfer.SetTimeout(15000)
  supervisorCapabilitiesUrlXfer.SetProxyBypass(["127.0.0.1", "localhost"])
  supervisorCapabilitiesUrlXfer.addHeader("Content-type", "application/json")
   
  msgPort = CreateObject("roMessagePort")
  supervisorCapabilitiesUrlXfer.SetPort(msgPort)
  initiatorIdentity = supervisorCapabilitiesUrlXfer.GetIdentity()
   
  script = CreateObject("roAssociativeArray")
  scriptType$ = "Custom"
  version$ = "10.0.60" ' current autorun script version
     
  script.AddReplace("type", scriptType$)
  script.AddReplace("version", version$)
   
  body = {}
  body.AddReplace("script", script)
     
  stringifiedJson = FormatJson(body)
     
  ok = supervisorCapabilitiesUrlXfer.AsyncPostFromString(stringifiedJson)
   
  if not ok then
    print "=== Failed to send POST Request"
  else
    print "=== Settings Handler request sent"
  end if
   
  while true
    msg = Wait(0, msgPort)
    if (type(msg) = "roUrlEvent")
      receivedIdentity = msg.GetSourceIdentity()
      if (initiatorIdentity = receivedIdentity) then
        print "=== " + supervisorCapabilitiesUrlXfer$ + ", Response Code: " + strI(msg.GetResponseCode())
      end if
    end if
  end while
end sub

```

## Caveats

*   The settings handler can override custom settings applied by the setup script.
    
*   Edits to the property sheet settings in the interface will not be applied on the device side unless the code snippet above is added to the runtime application or it is added as a plugin to the custom presentation.