# Duel focused settings

This factory extends the standard and tries to add additional values which should be added to the standard at some point in the future.

If you want to use this factory, use this instead of the standard one. Its game type is also called `stdduel` so that it is easy to adopt.

## Based on

https://github.com/quakelive-server-standards/quakelive-server-standards/blob/5168be332b7d7e2ae0027c7e7b27a34144cee265/factories/_id/factories.txt

## Standards

#### `g_allowSpecVote "0"`

A spectator should not be able to vote otherwise the players wanting to play a game need to wait for the spectators to also vote and hopefully vote yes.

#### `g_allowVote "1"`

A server without voting prevents the players on the server to decide which map they want to play next for example.

#### `g_allowVoteMidGame "0"`

Voting mid game does not make sense in Duel. A Duel is played until the end or the person forfeits.

#### `g_inactivity "600"`

Some people just idle on servers which is annoying because the server browser gives the impression that someone is waiting which is not true. People should be kicked when inactive. 10 minutes is a good value here. It is enough time to go to toilet, talk to partner or something else. For the other player it might be ok to wait that long.

#### `g_voteDelay "3000"`

To prevent a player with a faster machine to dictate the next map it is useful to prevent voting for some time so that the player with the slower machine has finished loading and is able to vote.

#### `g_voteFlags "30200"`

- `1` map - Of course.
- `2` map_restart - Does not make sense because mid match voting is disabled.
- `4` nextmap - Cannot by disabled because otherwise the map list in the voting menu disappears.
- `8` gametype - Do not allow to change game mode. A Duel server stays a Duel server.
- `16` kick - Do not allow to kick because it will be abused by friends and feels exluding, harms the community and the game.
- `32` timelimit - Do not allow to change the timelimit because it will be used by better players to minimize their game time. Better players should play worse players and also under the same conditions as everybody else.
- `64` fraglimit - Do not allow to change the timelimit because it will be used by better players to minimize their game time. Better players should play worse players and also under the same conditions as everybody else.
- `128` shuffle - Does not make sense in Duel.
- `256` teamsize - Does not make sense in Duel.
- `512` cointoss/random - Might be needed in tourneys.
- `1024` loadouts - Does not make sense in Duel.
- `2048` end-game voting - End game voting is good to change the map quickly and also to see unkown maps in the map pool.
- `4096` ammo (global) - Does not make sense in Duel.
- `8192` timers (item) - Might be an option for worse players who try to learn.
- `16382` weapon respawn - Disable voting for respawn time because this would change the standard which people would not expect.

#### `g_voteLimit "10"`

A player who just does not stop to vote can be annoying. But a server which prevents players from voting enough is also annoying. A good value should not be to small and not be too big.

#### `g_warmupReadyDelay "60"`

There are no delays which annoys if the other player does not ready up and then leaves anyway. Thus a value here is a highly recommended. A lot of servers do 120 seconds which is a bit stretching. Some do 10 seconds which is a little short. 60 should be a good value.

#### `g_warmupReadyDelayAction "2"`

If someone joins a server the person should be ready play. If she/he does not want to then she/he should leave.

#### `sv_warmupReadyPercentage "1"`

`sv_warmupReadyPercentage "1"` - Ratio of players that must be ready before the match starts.

## History

### Version 1

#### Add: `g_allowSpecVote "0"`

A spectator should not be able to vote otherwise the players wanting to play a game need to wait for the spectators to also vote and hopefully vote yes.

#### Add: `g_allowVote "1"`

A server without voting prevents the players on the server to decide which map they want to play next for example.

#### Add: `g_allowVoteMidGame "0"`

Voting mid game does not make sense in Duel. A Duel is played until the end or the person forfeits.

#### Add: `g_inactivity "600"`

Some people just idle on servers which is annoying because the server browser gives the impression that someone is waiting which is not true. People should be kicked when inactive. 10 minutes is a good value here. It is enough time to go to toilet, talk to partner or something else. For the other player it might be ok to wait that long.

#### Add: `g_voteDelay "3000"`

To prevent a player with a faster machine to dictate the next map it is useful to prevent voting for some time so that the player with the slower machine has finished loading and is able to vote.

#### Add: `g_voteFlags "30200"`

- `1` map - Of course.
- `2` map_restart - Does not make sense because mid match voting is disabled.
- `4` nextmap - Cannot by disabled because otherwise the map list in the voting menu disappears.
- `8` gametype - Do not allow to change game mode. A Duel server stays a Duel server.
- `16` kick - Do not allow to kick because it will be abused by friends and feels exluding, harms the community and the game.
- `32` timelimit - Do not allow to change the timelimit because it will be used by better players to minimize their game time. Better players should play worse players and also under the same conditions as everybody else.
- `64` fraglimit - Do not allow to change the timelimit because it will be used by better players to minimize their game time. Better players should play worse players and also under the same conditions as everybody else.
- `128` shuffle - Does not make sense in Duel.
- `256` teamsize - Does not make sense in Duel.
- `512` cointoss/random - Might be needed in tourneys.
- `1024` loadouts - Does not make sense in Duel.
- `2048` end-game voting - End game voting is good to change the map quickly and also to see unkown maps in the map pool.
- `4096` ammo (global) - Does not make sense in Duel.
- `8192` timers (item) - Might be an option for worse players who try to learn.
- `16382` weapon respawn - Disable voting for respawn time because this would change the standard which people would not expect.

#### Add: `g_voteLimit "10"`

A player who just does not stop to vote can be annoying. But a server which prevents players from voting enough is also annoying. A good value should not be to small and not be too big.

#### Add: `g_warmupReadyDelay "60"`

There are no delays which annoys if the other player does not ready up and then leaves anyway. Thus a value here is a highly recommended. A lot of servers do 120 seconds which is a bit stretching. Some do 10 seconds which is a little short. 60 should be a good value.

#### Add: `g_warmupReadyDelayAction "2"`

If someone joins a server the person should be ready play. If she/he does not want to then she/he should leave.
