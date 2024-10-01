# cookiestore

The *cookiestore* object retrieves a list of cookies from the containing browser (which implies that this class is only available for code running inside a browser instance, not from roNodeJs).

**cookiestore IDL**

```
interface Cookie {
    attribute String domain;
    attribute String path;
    attribute String name;
    attribute String value;
};
 
interface cookiestore {
    Array<Cookie> getCookies();
}
```

## Object Creation

```
let CookieStoreClass = require("@brightsign/cookiestore");
let cookieStore = new CookieStoreClass();
```

## Cookie

##### getCookies()

```
    Array<Cookie> getCookies()
```

Gets cookies from the containing browser.

*   `domain` string:  Specifies the hosts that are allowed to receive the cookie, including subdomains.
    
*   `path` string: To send the Cookie header, this URL path must exist in the URL request. 
    
*   `name` string: The name of the cookie
    
*   `value` string: The value of the cookie
    

## Example

To list the cookies saved on a browser instance on a console:

```
let CookieStoreClass = require("@brightsign/cookiestore");
let cookieStore = new CookieStoreClass();

let cookies = cookieStore.getCookies();

cookies.forEach((cookie) => {console.log("Cookie domain: " + cookie.domain + " Cookie path:" + cookie.path + " Cookie name:" + cookie.name + " Cookie value:" + cookie.value)});
```