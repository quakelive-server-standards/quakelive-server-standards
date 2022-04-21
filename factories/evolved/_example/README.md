# Example factories file

This example factories file demonstrates how to create an evolved `*.factories` files.

*Note: Introduce your factories file here.*

## Based on file

https://github.com/quakelive-server-standards/quakelive-server-standards/blob/482a3e2e5fd9dd106f7221d1f12ae2df168e7610/factories/standard/duel/duel.factories

*Note: You need to base your `*.factories` file either on the [standard](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories/standard) or on one of the [evolutions](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories/evolved). Otherwise your pull request will not be accepted.*

*Note: Refer to the file by using a link which references a specific Git commit. You can get such a link by opening the file you want to refer to on the GitHub website. Then click on history at the top right side. Find the commit you want to refer to (usually the one on the top) and click the button with that file icon. Its tooltip will display the message "View at this point in the history". Now copy the link from the browser address bar.*

## Evolutions

*Note: List the cvars that you added or changed in an alphabetical order. Use the correct Markdown headline level 4 by using `####`.*

##### `pmove_CrouchSlide 1`

Adding crouch slide is a way to enable player to traverse the maps faster but not as free as with air control. This will create a faster gameplay.

*Note: State the cvar and its value in the format `<cvar> <value>`. Underneath describe why you set variable to that specific value.*

#### `timelimit 15`

Back to the old fashioned 15 minute time limit to facilitate comebacks and thus more exciting games.

*Note: State the cvar and its value in the format `<cvar> <value>`. Underneath describe why you set variable to that specific value.*

## History

*Note: Work in versions which increment with every change. Start at version 1. List what you have added, changed or removed.*

### Version 2

*Note: Put a new version above the version before.*

### Version 1

#### Add: `pmove_CrouchSlide 1`

Adding crouch slide is a way to enable player to traverse the maps faster but not as free as with air control. This will create a faster gameplay.

*Note: Just repeat the text that you already wrote from above. This repetition is for documenting the value and the reason for it because it might be changed or removed in the future.*

#### Change: `timelimit 15`

Back to the old fashioned 15 minute time limit to facilitate comebacks and thus more exciting games.

*Note: Just repeat the text that you already wrote from above. This repetition is for documenting the value and the reason for it because it might be changed or removed in the future.*

#### Remove: `fraglimit 0`

Removed because it should be set to whatever value was set on the server.

*Note: State the cvars that you removed. Underneath describe why you removed it.*