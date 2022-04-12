# Quake Live apps

This is a collection of all known community created Quake Live server applications.

## Overview

### carmethene-quakelive-rcon

This projects contains two rcon client variants based on the official id Software rcon client written in Python.

### em92-quakelive-local-ratings

### id-rcon-cli

The official rcon client by id Software written in Python.

### predath0r-qlstats

### quakeliveserverstandards-id-rcon-cli

This project is based on `irc_rcon.py` of [carmethenes version](https://github.com/carmethene/quakelive-rcon) of the official id Software rcon client.

It removes all unused code and adds the command `exit` which terminates the application.

### quakeliveserverstandards-ql-console

This is a rcon and stats command line interface client written in Node. It is integrated into the official Quake Live Server Standards repository as the default command line interface for accessing the rcon and stats APIs.

### sbarisic-bspconv

## Developing a Quake Live dedicated server app

If you want to create an app for the Quake Live dedicated server, you basically have two options. Either you develop a [minqlx plugin](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins#developing-minqlx-plugins) or you work with the two API's rcon and stats offered by the Quake Live dedicated server. In this document we are getting deeper into the latter two.

### QL Stats Model

The [ql-stats-model](https://github.com/quakelive-server-standards/ql-stats-model) library aims to document the stats API and to provide a typed and slightly improved access to the data of each stats API object. It is programmed in TypeScript.

You can give it a raw stats API object and it will convert it to its typed version.

```typescript
import * from 'ql-stats-model'

MatchReportEvent.fromQl(rawQlStatsObject)
MatchStartedEvent.fromQl(rawQlStatsObject)
PlayerConnectEvent.fromQl(rawQlStatsObject)
PlayerDeathEvent.fromQl(rawQlStatsObject)
PlayerDisconnectEvent.fromQl(rawQlStatsObject)
PlayerKillEvent.fromQl(rawQlStatsObject)
PlayerMedalEvent.fromQl(rawQlStatsObject)
PlayerStatsEvent.fromQl(rawQlStatsObject)
PlayerSwitchTeamEvent.fromQl(rawQlStatsObject)
RoundOverEvent.fromQl(rawQlStatsObject)
```

It also comes with enums that catalogue the possible values of certain event object properties, like `GameType`, `HoldableType`, `MedalType`, `ModType`, `PowerUpType`, `TeamType` and `WeaponType`. All of these enums also provide human readable versions of the values which can be used to print them to a screen in an application.

### QL Api

The [ql-api](https://github.com/quakelive-server-standards/ql-api) library provides easy access to the rcon and stats API's of a Quake Live dedicated server. It is programmed in TypeScript for NodeJs.

```typescript
import { Rcon } from 'ql-api'

let rcon = new Rcon('127.0.0.1:28960', 'some_name', 'password')
rcon.connect()
```

```typescript
import { Stats } from 'ql-api'

let stats = new Stats('127.0.0.1:27960', 'password')
stats.connect()
```
