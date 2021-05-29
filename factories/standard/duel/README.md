# Standard Duel factory

## Standards

##### Timlimit

`timelimit "10"` - Timelimit of 10 minutes.

This is the official id Software standard.

##### Fraglimit

`fraglimit "10"` - Fraglimit of 10 frags.

This is the official id Software standard.

##### Allow voting

`set g_allowVote "1"` - Voting allowed.

A server without voting prevents the players on the server to decide which map they want to play next for example.

##### Vote delay

`set g_voteDelay "3000"` - Delay allowing votes for 3000 milliseconds after map load.

To prevent a player with a faster machine to dictate the next map it is useful to prevent voting for some time so that the player with the slower machine has finished loading and is able to vote.

##### Vote limit

`set g_voteLimit "10"` - Limit users to 10 votes per map.

A player who just does not stop to vote can be annoying. But a server which prevents players from voting enough is also annoying. A good value should not be to small and not be too big.

##### Allow voting mid game

`g_allowVoteMidGame "0"` - Only allow votes from mid game.

Voting mid game does not make sense in duel. A duel is played until the end or the person forfeits.

##### Allow spectator voting

`g_allowSpecVote "0"`- Allow spectators to call votes.

A spectator should not be able to vote otherwise the players wanting to play a game need to wait for the spectators to also vote and hopefully vote yes.

##### Vote flags

`g_voteFlags "30200"` - Add together the below values for which callvotes should be DISABLED.

- `1` map - Of course.
- `2` map_restart - Does not make sense because mid match voting is disabled.
- `4` nextmap - Cannot by disabled because otherwise the map list in the voting menu disappears.
- `8` gametype - Do not allow to change game mode. A duel server stays a duel server.
- `16` kick - Do not allow to kick because it will be abused by friends and feels exluding, harms the community and the game.
- `32` timelimit - Do not allow to change the timelimit because it will be used by better players to minimize their game time. Better players should play worse players and also under the same conditions as everybody else.
- `64` fraglimit - Do not allow to change the timelimit because it will be used by better players to minimize their game time. Better players should play worse players and also under the same conditions as everybody else.
- `128` shuffle - Does not make no sense in duel.
- `256` teamsize - Does not make no sense in duel.
- `512` cointoss/random - Might be needed in tourneys.
- `1024` loadouts - Does not make no sense in duel.
- `2048` end-game voting - End game voting is good to change the map quickly and also to see unkown maps in the map pool.
- `4096` ammo (global) - Does not make no sense in duel.
- `8192` timers (item) - Might be an option for worse players who try to learn.
- `16382` weapon respawn - Disable voting for respawn time because this would change the standard which people would not expect.

##### Player ratio for starting

`sv_warmupReadyPercentage "1"` - Ratio of players that must be ready before the match starts.

##### Warmup ready delay

`g_warmupReadyDelay "60"` - Wait x seconds before allowing match to start to allow all players to connect.

There are no delays which annoys if the other player does not ready up and then leaves anyway. Thus a value here is a highly recommended. A lot of servers do 120 seconds which is a bit stretching. Some do 10 seconds which is a little short. 60 should be a good value.

##### Warmup ready delay action

`g_warmupReadyDelayAction "2"` - to 1 to force players to spectator after g_warmupReady Delay, 2 to force ready up.

If someone joins a server the person should be ready play. If she/he does not want to then she/he should leave.

##### Inactivity kick

`g_inactivity "600"` - Kick players who are inactive for X amount of seconds.

Some people just idle on servers which is annoying because the server browser gives the impression that someone is waiting which is not true. People should be kicked when inactive. 10 minutes is a good value here. It is enough time to go to toilet, talk to partner or something else. For the other player it might be ok to wait that long.

##### Item height

`g_itemHeight "15"` - Item height of 15 units.

This is the official id Software standard.

##### Item timers

`g_itemTimers "0"` - Item timers disabled.

This is the official id Software standard.

##### Bunny hopping

`pmove_BunnyHop "0"` - Bunny hopping disabled.

This is the official id Software standard.

##### Undocumented cvar

`pmove_CrouchStepJump "0"` - Undocumented cvar

This is the official id Software standard.

##### Undocumented cvar

`pmove_JumpTimeDeltaMin "50"` - Undocumented cvar

This is the official id Software standard.

##### Undocumented cvar

`pmove_WaterSwimScale "0.5f"` - Undocumented cvar

This is the official id Software standard.

##### Undocumented cvar

`pmove_WaterWadeScale "0.75f"` - Undocumented cvar

This is the official id Software standard.