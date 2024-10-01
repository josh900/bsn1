# Using API Access and Refresh Tokens

> [!WARNING]
> BSN.cloud is changing its authorization server to be able support SSO and other security features requested by customers, and our access and refresh token lifetimes will be changing because of this.
> **Access tokens will have a 5 minute lifetime**
> **Refresh tokens will have a 30 minute lifetime**
> **Session lifetime will be 12 hours**
> You must ensure that all of your applications and/or scripts are correctly handling and refreshing these tokens or you may find that they stop working correctly.
> All customers will be notified in advance of this change so that they have time to check and prepare their applications and scripts.

# Refresh token-based authentication workflow

To access the BSN.cloud APIs you are required to submit your credentials in order to obtain your access and refresh tokens. Access tokens are temporary credentials that grant access to a protected resource, while refresh tokens are used to obtain new access tokens when the current ones expire.

When your application or script accesses the token endpoint and authorizes successfully, it is granted an access token and a refresh token. The access token is then passed with each API request to allow the resource to be accessed.

> [!INFO]
> BSN.cloud Token Endpoint: [https://api.bsn.cloud/2022/06/REST/Token/](https://api.bsn.cloud/2022/06/REST/Token/)

After a period of time (the access token lifetime), making the API call will fail with an error because the access token has expired. At this point, your code should use the refresh token to exchange for a new access token. This is done by passing the refresh token to the token endpoint, which verifies the refresh token and issues new access and refresh tokens in the response. You should then use this new access token in your subsequent API call.

This process continues until either:

*   the refresh token is expired
    
*   the refresh token is revoked
    
*   the current session is expired
    

At this point you will need to re-authenticate with your credentials.

The following flow diagram shows this flow:

![Screenshot 2024-08-02 at 8.55.33 AM.png](./attachments/Screenshot%202024-08-02%20at%208.55.33%20AM.png)

1.  The client application authenticates with the BSN.cloud token endpoint by providing the credentials
    
2.  If the credentials are valid, an access token and a refresh token are returned in the result
    
3.  The client application makes an API call and must pass the access token
    
4.  The API component validates the access token and allows access to the resource
    
5.  Steps 3 and 4 can continue until the access token expires and the API signals this by returning an error response (this will be a `401` or `403` status code)
    
6.  When the access token expires, the client application requests a new access token by providing the refresh token
    
7.  The BSN.cloud token endpoint then issues a new access token and a *new refresh* token
    
8.  Steps 3 through 7 repeat until the refresh token expires, or is revoked, or the current session ends
    
9.  The client needs to re-authenticate with the authentication server once again and the flow repeats from step 1.
    

> [!INFO]
> [BSN.cloud API Authentication Documentation](../cloud-apis/bsncloud-main-apis/main-rest-http-api-version-202206.md)
> Person Authentication: [Main REST HTTP API version 2022/06 | Authenticating as a Person](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1313046529/Main+REST+HTTP+API+version+2022+06#Authenticating-as-a-Person)
> Person Token Refresh: [Main REST HTTP API version 2022/06 | Person OAuth2 Token Renewal](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1313046529/Main+REST+HTTP+API+version+2022+06#Person-OAuth2-Token-Renewal)
> User Authentication: [Main REST HTTP API version 2022/06 | Authenticating as a User](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1313046529/Main+REST+HTTP+API+version+2022+06#Authenticating-as-a-User)
> User Token Refresh: [Main REST HTTP API version 2022/06 | User OAuth2 Token Renewal](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1313046529/Main+REST+HTTP+API+version+2022+06#User-OAuth2-Token-Renewal)

# Refresh Tokens

**So, why do we need both access tokens and refresh tokens?** Why don’t we just set a long expiration date, like a month or a year for the access tokens? If we do that and someone manages to get hold of our access token they can use it for a long period, even if we change our password

The idea of refresh tokens is that we can make the access token short-lived so that, **even if it is compromised, the attacker gets access only for a short period**. With refresh token-based flow, the authentication server issues a one-time use refresh token along with the access token. Your application should store the refresh token safely

Every time your application sends a request to the server it sends the access token in the Authorization header and the server can identify the application using it. When the access token expires, the server will send a token expired response. When your application receives the token expired response, it must send the refresh token to obtain a new access token and refresh token

If something goes wrong, **the refresh token can be revoked** which means that when the your application tries to use it to get a new access token, that request will be rejected and you will have to enter the credentials once again and authenticate.

**Why can’t we just use Steps 1, 2 and 3 constantly instead of having to deal with refresh tokens?** Issuing many active access tokens is not an efficient process and it leads to an increase in storage and decrease in performance for our backend servers. Up until now we have permitted this approach but going forward we will be adding limitations to the number of unexpired access tokens that an application can have at any one time.