# Standard base config

This is the base configuration which serves as a starting point for any new configuration. It contains the smallest common denominator for any Quake Live server configuration.

## Standards

##### Allow voting

`set g_allowVote "1"` - Allow Voting.

A server without voting prevents the players on the server to decide which map they want to play next for example.

##### Vote delay

`set g_voteDelay "5000"` - Delay allowing votes for X milliseconds after map load.

To prevent a player with a faster machine to dictate the next map it is useful to prevent voting for some time so that the player with the slower machine has finished loading and is able to vote.

##### Vote limit

`set g_voteLimit "10"` - Limit users to X votes per map.

A player who just does not stop to vote can be annoying. But a server which prevents players from voting enough is also annoying. A good value should not be to small and not be too big.
