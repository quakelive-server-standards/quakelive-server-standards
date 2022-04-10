# Quake Live map pools

A Quake Live map pool is a list of maps bound to a specific game type. Be aware that Quake Live only regards the map pool in the map voting overlay after a match. The players can still see and vote every installed map.

## Creating a map pool

Creating a map pool means to create a text file with the name of `mappool.txt`. This name is set by the standardised [`server.cfg`](https://github.com/quakelive-server-standards/server-standards/tree/master/configs/standard) but could by any name otherwise.

The content of such a file consists of lines of `mapname|gametypename` pairs. That means that every mentioned map is in the context of a specific gametype.

```
aerowalk|duel
battleforged|duel
bloodrun|duel
almostlost|ca
asylum|ca
blackcathedral|ca
```

Valid gametypes are `ffa`, `duel`, `race`, `tdm`, `ca`, `ctf`, `oneflag`, `har`, `ft`, `dom`, `ad` and `rr`.

Additional gametypes can be added through [factories](https://github.com/quakelive-server-standards/server-standards/tree/master/factories#readme). Quake Live Server Standards uses this possibility to define standardised versions of the most popular gametypes [`stdffa`](https://github.com/quakelive-server-standards/server-standards/tree/master/factories/standard/ffa), [`stdduel`](https://github.com/quakelive-server-standards/server-standards/tree/master/factories/standard/duel), [`stdrace`](https://github.com/quakelive-server-standards/server-standards/tree/master/factories/standard/race), [`stdtdm`](https://github.com/quakelive-server-standards/server-standards/tree/master/factories/standard/tdm), [`stdca`](https://github.com/quakelive-server-standards/server-standards/tree/master/factories/standard/ca) and [`stdctf`](https://github.com/quakelive-server-standards/server-standards/tree/master/factories/standard/ctf).

Since those factory files are at the heart of the Quake Live Server Standards idea, they were copied into every gametype related Quake Live dedicated server Docker image. Use those gametypes instead of the original ones when creating map pools.

```
aerowalk|stdduel
battleforged|stdduel
bloodrun|stdduel
almostlost|stdca
asylum|stdca
blackcathedral|stdca
```

## Incorporating new maps

To incorporate a new map you also need to work with [Steam Workshop items](https://github.com/quakelive-server-standards/server-standards/tree/master/workshop) which can contain Quake Live maps. Add such an item to your Quake Live dedicated server installation and mention in in the `mappool.txt`.

## Participating