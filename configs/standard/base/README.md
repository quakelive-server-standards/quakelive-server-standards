# Base

This is the base configuration which serves as a starting point for any new configuration. It contains the smallest common denominator for any Quake Live server configuration.

## Standards

### server.cfg

##### Hostname

`set sv_hostname "Quake Live Standard Server"` - Hostname for server.

If somebody uses this configuration it should have a name which references its type. This cvar is commented out so that it can be set in the `docker-compose.yml` of this framework. You find the default in the Docker file `docker/base/Dockerfile`.

##### Tags

`set sv_tags "ca, ctf, duel, ffa, race, tdm"` - Server tags - Tags show up on the in-game server browser. This helps users filter servers.

If somebody uses this configuration it should have a name which references its type. This cvar is commented out so that it can be set in the `docker-compose.yml` of this framework. You find the default in the Docker file `docker/base/Dockerfile`.

##### ZeroMQ Stats

`set zmq_stats_enable "1"` - Enable ZeroMQ stats
`set zmq_stats_port "27960"` - ZeroMQ stats port (TCP).
`set zmq_stats_password "quakeliveserverstandards"` - ZeroMQ stats password.

Website like QLStats are vital for the Quake Live scene. Every server therefor should have sending stats enabled to help to evolve the community.

##### Allow voting

`set g_allowVote "1"` - Allow Voting.

A server without voting prevents the players on the server to decide which map they want to play next for example.

##### Vote delay

`set g_voteDelay "5000"` - Delay allowing votes for X milliseconds after map load.

To prevent a player with a faster machine to dictate the next map it is useful to prevent voting for some time so that the player with the slower machine has finished loading and is able to vote.

##### Vote limit

`set g_voteLimit "10"` - Limit users to X votes per map.

A player who just does not stop to vote can be annoying. But a server which prevents players from voting enough is also annoying. A good value should not be to small and not be too big.

### minqlx plugins

`docs.py` - A plugin that generates a command list of all the plugins currently loaded, in the form of a Markdown file.

It is in general useful for any server configuration.

`motd.py` - Adds commands to set a message of the day.

It is in general useful for any server configuration.

`permission.py` - Adds commands to set player permissions.

It is in general useful for any server configuration.

`plugin_manager.py` - Adds commands to load, reload and unload plugins at run-time.

It is in general useful for any server configuration.

`workshop.py` - A plugin that allows the use of custom workshop items that the server might not reference by default, and thus not have the client download them automatically.

It is in general useful for any server configuration.

### mappool.txt

No changes were made to the original Quake Live version.

### workshop.txt

No changes were made to the original Quake Live version which is empty.

## Technical details regarding this framework

### Variables that must not be changed

The following variables must not be changed beacause the framework expects them to be like they are set.

`set net_port "27960"` -  Server port (UDP).

The Quake Live server runs inside a Docker container. The Docker container exposes its own port but only to other Docker container inside that Docker network. To be able to access a Docker container inside that Docker network you have to define an additional external port. The Docker engine then will map that external port to a Docker containers internal port. Thus the Docker containers which running the Quake Live servers can all expose the same port and thus the Quake Live servers all can run on the same standard port 27960.

`set net_strict "1"` -  Quit out immediately if we can't bind the IP and port.

The Docker engine will restart a Docker container if it went offline. So if there was anything wrong with the Quake Live server it should crash.

`set zmq_rcon_port "28960"` - Rcon port.

Same reason like `net_port`.

`set zmq_stats_port "27960"` - ZeroMQ stats port (TCP).

Same reason like `net_port`.

`set g_accessFile "access.txt"` - Used to determine which 64-bit Steam IDs have admin access, or are banned.

This file is mounted into the specific Docker container as denoted in the Quake Live servers Docker Compose file. It needs to have a standard location and name so that it is consistent all over the board.

### Variables that were commented out

The cvars set in the `server.cfg` overwrite the ones given through the command line. This framework uses command line parameters to adjust a configuration for a specific server instance given through environment variables that are denoted on the Quake Live servers Docker Compose file in the root of this repository. 

`sv_hostname`, `g_password`, `sv_tags`, `sv_maxClients`, `sv_privateClients`, `sv_privatePassword`, `g_allowVoteMidGame`, `g_allowSpecVote`, `g_voteFlags`, `set sv_warmupReadyPercentage`, `g_warmupDelay`, `g_warmupReadyDelay`, `g_warmupReadyDelayAction`, `g_inactivity`, `g_alltalk`