# Known Issues

BrightSign’s HTML5 rendering engine is a constant work-in-progress. The following are known issues that we are working to resolve in future versions of player firmware.

## Rotated 4K Output

Displaying an HTML page and rotated video while using a 4K output mode will cause the video to glitch. This is the case even if the video is not part of the HTML page (i.e. it's displayed and rotated using BrightScript).

## Localized JavaScript Time

The JavaScript `toLocaleTimeString()` call does not retrieve localized time formats (i.e. 24-hour vs. 12-hour clock): Instead, the hour/minute clock defaults to 24-hour time on the BrightSign player. The below code provides a workaround in JavaScript if you would like to display time using a 12-hour clock:

```
function format12Hour(date)
{
    var zero = '0';

    hh = date.getHours();
    mm = date.getMinutes();
    ss = date.getSeconds()

    if((hh % 12) == 0)
        hh = 12;

    else
        hh %= 12;

    // Pad zero values to 00
    hh = (zero+hh).slice(-2);
    mm = (zero+mm).slice(-2);
    ss = (zero+ss).slice(-2);

    return hh + ':' + mm + ':' + ss + ' ' + ((date.getHours() < 12) ? 'AM' : 'PM');
}
```

If you would prefer not to display seconds information, you can replace the above “return” line with the following:

```
return hh + ':' + mm + ' ' + ((date.getHours() < 12) ? 'AM' : 'PM');
```

Implement the function in the HTML script as follows:

```
var dateString = (startJSDate.getMonth() + 1) + "/" +
startJSDate.getDate();
    if (!startDateTime.isDateOnly()) {
      dateString += " -- " + format12Hour(startJSDate);
    }
```