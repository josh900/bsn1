# Power BI Announcement

Microsoft [has announced](https://powerbi.microsoft.com/en-us/blog/power-bi-june-2024-feature-summary/) that Chromium 94 will be the minimum browser supported on Power BI. Because of this change, BrightSign will upgrade our current Chromium 87 browser version (for Series 4 and 5 players), to accommodate Power BI users.

## Series 5

The current BOS 9.0.145.1 release contains a Beta version of Chromium 110. This version, which exceeds the Power BI requirement for Series 5, can be set by using the `chromium110` registry key.

The next BOS 9.0 release, which should be available before the end of August, will upgrade the beta Chromium 110 version to version 120. This functionality, set through the registry, will be considered a beta, but will eventually move into a BOS 9.1 release which will contain Chromium 120 as the default. These versions offer significant performance improvements, enhanced security, and access to the latest web technologies.

See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673541/Diagnostic+Web+Server#Registry) for more information about changing registry key settings in BrightAuthor:connected.

### Registry Key Example Settings

You must reboot after updating the registry to apply the changes.

#### DWS  

Don't forget to add authentication to the Curl command below:

```
curl --location --request PUT 'http://<player_ip>/api/v1/registry/html/widget_type' \
--header 'Content-Type: application/json' \
--digest -u '{username}:{password}' \
--data-raw '{"value": "chromium110"}'
```

#### BrightScript Console

See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/1988100153/BrightSign+Shell) for more information.

```
registry write html widget_type chromium110
```

#### BrightScript

See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370673018/roRegistrySection) for more information.

```
RegHtml = CreateObject("roRegistrySection", "html")
RegHtml.Write("widget_type", "chromium110")
RegHtml.Flush()
```

#### JavaScript

See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370678545/registry) for more information.

```
var registryClass = require("@brightsign/registry");
var registry = new registryClass();
registry.write("html", { widget_type: "chromium110" }).then(() => {
  console.log("Write Successful");
}).catch((error) => {
  console.error("Write Failed", error);
});
```

#### TypeScript

See [this page](https://brightsign.atlassian.net/wiki/spaces/DOC/pages/370678545/registry) for more information.

```
import RegistryClass from "@brightsign/registry";
const registry = new RegistryClass();
registry.write("html", { widget_type: "chromium110" }).then(() => {
  console.log("Write Successful");
}).catch((error: Error) => {
  console.error("Write Failed", error);
});
```

#### Player CLI

See [@brightsign/bsc](https://www.npmjs.com/package/@brightsign/bsc) (CLI Tool) for more information.

```
bsc local registry --player PLAYER_NAME --set --value chromium110 --section html --key widget_type
```

## Series 4

BrightSign plans to release BOS 9.1 with a Chromium 120 beta before the end of August to help customers using Power BI. We are investigating if this version can unify the Series 4 and 5 BOS versions.

## Series 3

BrightSign is investigating the Series 3 product line hardware capabilities in order to provide a higher Chromium version.

> [!WARNING]
> Beta OS versions may contain functional differences with the production OS.