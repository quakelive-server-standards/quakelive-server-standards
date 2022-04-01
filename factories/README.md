# Quake Live factories

A Quake Live factory is a set of cvars bound to a certain game type. It is a opportunity to set standards for and to evolve the basic game types.

## Calling a vote specifying a certain factory

In the in-game Quake Live console you can type `callvote map campgrounds ffa`.

## Creating your own factory

A `*.factories` file can contain contain the definition of one game mode.

```json
{
  "cvars": {
    "timelimit": "10"
  },
  "author": "Quake Live Server Standards",
  "description": "Some duel game mode",
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
    "author": "Quake Live Server Standards",
    "description": "Some Duel game mode",
    "basegt": "duel",
    "id": "someduel",
    "title": "Some Duel"
  },
  {
    "cvars": {
      "timelimit": "15"
    },
    "author": "Quake Live Server Standards",
    "description": "Some CA game mode",
    "basegt": "ca",
    "id": "someca",
    "title": "Some CA"
  }
]
```

All fields should be present and of the correct type.

- `id`: How you will refer to the factory inside a map pool or a callvote. Must be a string.
- `title`: The title of your game mode. Quake Live does not show this information anywhere.
- `author`: The author of your game mode. Quake Live does not show this information anywhere.
- `description`: The description of your game mode. Quake Live does not show this information anywhere.
- `basegt`: A string of the base game type it should apply the settings on. Valid values are `ffa`, `duel`, `race`, `tdm`, `ca`, `ctf`, `oneflag`, `har`, `ft`, `dom`, `ad`, `rr`
- `cvars`: An object containing key value pairs of the cvar names and values to set.

If a factory is invalid, the reason why will be printed in the console during startup, and the factory will not be available for play.

For selecting the cvars you want to adjust in your game mode, there is a factory-focused cvar collection [here](https://github.com/quakelive-server-standards/server-standards/blob/master/factories/cvars.md).

## Other

https://steamcommunity.com/app/282440/discussions/0/490125103624446696/