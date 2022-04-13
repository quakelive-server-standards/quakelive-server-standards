# Quake Live factories

A Quake Live factory is a set of cvars bound to a certain game type. It is a opportunity to set standards for and to evolve the basic game types. Inside of Quake Live you can reference a game type when calling a vote for a map like this `callvote map campgrounds ffa`.

## Creating your own factory

A `*.factories` file can contain contain the definition of one game mode.

```json
{
  "cvars": {
    "timelimit": "10"
  },
  "author": "Some author",
  "description": "Some duel game type",
  "basegt": "duel",
  "id": "someduel",
  "title": "Some Duel"
}
```

Or a list of definitions.

```json
[
  {
    "cvars": {
      "timelimit": "10"
    },
    "author": "Some author",
    "description": "Some Duel game type",
    "basegt": "duel",
    "id": "someduel",
    "title": "Some Duel"
  },
  {
    "cvars": {
      "timelimit": "15"
    },
    "author": "Quake Live Server Standards",
    "description": "Some CA game type",
    "basegt": "ca",
    "id": "someca",
    "title": "Some CA"
  }
]
```

All of the following fields should be present and of the correct type.

- `id`: How you will refer to the factory inside a map pool or a callvote. Must be a string.
- `title`: The title of your game type. Quake Live does not show this information anywhere.
- `author`: The author of the game type. Quake Live does not show this information anywhere.
- `description`: The description of your game type. Quake Live does not show this information anywhere.
- `basegt`: A string of the base game type it should apply the settings on. Valid values are `ffa`, `duel`, `race`, `tdm`, `ca`, `ctf`, `oneflag`, `har`, `ft`, `dom`, `ad`, `rr`
- `cvars`: An object containing key value pairs of the cvar names and values to set.

If a factory is invalid, the reason for it will be printed in the console during startup, and the factory will not be available for play.

For selecting the cvars you want to adjust in your game type, there is a factory-focused cvar collection [here](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/factories/cvars.md).

## Participate

## Other

https://steamcommunity.com/app/282440/discussions/0/490125103624446696/