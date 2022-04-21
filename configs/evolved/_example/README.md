# Example config

This example config demonstrates how to create an evolved `server.cfg` file.

*Note: Introduce your config file here.*

## Based on file

https://github.com/quakelive-server-standards/quakelive-server-standards/blob/a5389437bfd2be4f02bbc2c1d89145b2e9bf8f9d/configs/standard/server.cfg

*Note: You need to base your `server.cfg` either on the [standard](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs/standard) or on one of the [evolutions](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs/evolved). Otherwise your pull request will not be accepted.*

*Note: Refer to the file by using a link which references a specific Git commit. You can get such a link by opening the file you want to refer to on the GitHub website. Then click on history at the top right side. Find the commit you want to refer to (usually the one on the top) and click the button with that file icon. Its tooltip will display the message "View at this point in the history". Now copy the link from the browser address bar.*

## Evolutions

*Note: List the cvars that you added or changed in an alphabetical order. Use the correct Markdown headline level 4 by using `####`.*

#### `set com_hunkMegs "120"`

To support servers with 16 players this value is set to 120 mega bytes.

*Note: State the cvar and its value in the format `set <cvar> <value>`. Underneath describe why you set the variable to that specific value.*

#### `set sv_fps "60"`

This value has been tested and improves hitscan weapon hit detection.

*Note: State the cvar and its value in the format `set <cvar> <value>`. Underneath describe why you set the variable to that specific value.*

## History

*Note: Work in versions which increment with every change. Start at version 1. State what you have added and what you have removed.*

### Version 2

*Note: Put a new version above the version before.*

### Version 1

#### Add: `set com_hunkMegs "120"`

To support servers with 16 players this value is set to 120 mega bytes.

*Note: Just repeat the text that you already wrote from above. This repetition is for documenting the value and the reason for it because it might be changed or removed in the future.*

#### Change: `set sv_fps "60"`

This value has been tested and improves hitscan weapon hit detection.

*Note: Just repeat the text that you already wrote from above. This repetition is for documenting the value and the reason for it because it might be changed or removed in the future.*

#### Remove: `set g_floodprot_maxcount "10"`

This value can now be set in the Docker Compose file using [this](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/89ca0a79371017677a12dda7f28bc4db50c677c7/docker/ql-server) Docker image.

*Note: State the cvars that you removed. Underneath describe why you removed it.*