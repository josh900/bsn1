# roBtClient

Each instance of this object represents a single BLE client. This object is not instantiated by the script; instead, when a BLE client connects to the player, the [*roBtClientManager*](../inputoutput-objects/robtclientmanager.md)  object sends an event to its attached message port and creates a *roBtClient* instance. The JavaScript equivalent is [BSBtManager](../../../../developers/player-apis/brightscript-javascript-objects/bsbtmanager.md).

The primary purpose of the *roBtClient* object is to transfer data between the player and the client via user variables (i.e. characteristics). When a client updates user-variables or sends a command, an  [*roBtClientEvent*](../inputoutput-objects/robtclientevent.md) is sent to the attached message port. The state can be retrieved using either the *roBtClient.GetUserVars()* method or the *roBtClientEvent.GetParam()* method: Updates from the *roBtClientEvent* object are queued until the script processes them, while the *roBtClient* object returns the most current state.

## ifBtClient

##### GetClientId() As String

Retrieves the UUID of the client associated with the object instance.

##### SetUserVars(data As String) As Boolean

Specifies new data for the client to retrieve.

##### GetUserVars() As String

Retrieves the latest data from the *roBtClient* state.

##### Disconnect() As Boolean

Forces the player to disconnect from the client.

## ifMessagePort

##### SetPort(a As Object)

Posts messages of type *roBtClientEvent* to the attached message port. An event is raised whenever the end of the queue is reached.

## ifUserData

##### SetUserData(a As Object)

Sets the user data that will be returned when events are raised.

##### GetUserData() As Object

Returns the user data that has previously been set via `SetUserData()`. It will return Invalid if no data has been set.

## ifIdentity

##### GetIdentity() As Integer

Returns a unique number that can be used to identify *roBtClientEvent* objects that originate from this object.

> [!NOTE]
> The *ifIdentity* interface has been deprecated. We recommend using the *ifUserData* interface instead.

## ifFailureReason

##### GetFailureReason() As String

Returns additional useful information if a method on the *ifBtClient* interface returns False.