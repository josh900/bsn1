# compositor

The *compositor* object allows you to perform actions related to the video compositor.

**compositor IDL**

```
interface Compositor {
    void pause(int timeout_ms);
    void resume();
    int getCrc();
};
```

## Object Creation

To create a *compositor* object, first load the `brightsign/compositor` module using the `require()` method. Then create an instance of the *screenshot* class.

```
var CompositorClass = require("@brightsign/compositor");
var compositor = new CompositorClass();
```

## Compositor

##### pause()

```
void pause(int timeout_ms) 
```

Suspends graphics compositor updates for the specified number of milliseconds (or until the `resume()` method is called), up to a maximum interval of 10 seconds. While the graphics compositor is paused, no visual elements will be updated (except for [HWZ video](../../../developers/html-development/html-video.md), [scrolling tickers](../../../developers/brightscript/object-reference/presentation-and-widget-objects/rotextwidget.md), and off-screen Chromium textures). Use this method to combine intensive graphics and layout operations into a single v-sync update.

##### resume()

```
void resume()
```

Resumes the graphics compositor if it has been paused with the `pause()` method.

##### getCrc()

```
int getCrc()
```

Returns the CRC of the Y and Cb signals as a single integer. This method allows the script to compare two moments in the graphics output: If the return values differ, then the output is not identical.