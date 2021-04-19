# Standard base config

This is the base configuration which serves as a starting point for any new configuration. It contains the smallest common denominator for any Quake Live server configuration.

## Standards

### server.cfg

##### Hostname

`set sv_hostname "Quake Live Standard Server"` - Hostname for server.

If somebody uses this configuration it should have a name which references its type. This cvar is commented out so that it can be set in the `docker-compose.yml` of this framework. You find the default in the Docker file `docker/base/Dockerfile`.

##### Tags

`set sv_tags "ca, ctf, duel, ffa, race, tdm"` - Server tags - Tags show up on the in-game server browser. This helps users filter servers.

If somebody uses this configuration it should have a name which references its type. This cvar is commented out so that it can be set in the `docker-compose.yml` of this framework. You find the default in the Docker file `docker/base/Dockerfile`.

##### Allow voting

`set g_allowVote "1"` - Allow Voting.

A server without voting prevents the players on the server to decide which map they want to play next for example.

##### Vote delay

`set g_voteDelay "5000"` - Delay allowing votes for X milliseconds after map load.

To prevent a player with a faster machine to dictate the next map it is useful to prevent voting for some time so that the player with the slower machine has finished loading and is able to vote.

##### Vote limit

`set g_voteLimit "10"` - Limit users to X votes per map.

A player who just does not stop to vote can be annoying. But a server which prevents players from voting enough is also annoying. A good value should not be to small and not be too big.

##### ZMQ rcon (remote connection)

`set zmq_rcon_enable "1"` - Enable rcon.

Website like QLStats are vital for the Quake Live scene. Every server therefor should have receiving commands enabled to help the community evolve. For easy access the password is a standard one.

##### ZeroMQ Stats

`set zmq_stats_enable "1"` - Enable ZeroMQ stats

Website like QLStats are vital for the Quake Live scene. Every server therefor should have sending stats enabled to help the community evolve.

### minqlx plugins

##### Docs

`docs.py` - A plugin that generates a command list of all the plugins currently loaded, in the form of a Markdown file.

It is in general useful for any server configuration.

##### Log

`log.py` - A plugin that logs chat and commands. All logs go to fs_homepath/chatlogs.

It is in general useful for any server configuration.

##### Motd

`motd.py` - Adds commands to set a message of the day.

It is in general useful for any server configuration.

##### Permission

`permission.py` - Adds commands to set player permissions.

It is in general useful for any server configuration.

##### Plugin manager

`plugin_manager.py` - Adds commands to load, reload and unload plugins at run-time.

It is in general useful for any server configuration.

#### Workshop

`workshop.py` - A plugin that allows the use of custom workshop items that the server might not reference by default, and thus not have the client download them automatically.

It is in general useful for any server configuration.

### mappool.txt

No changes were made to the original Quake Live version.

### workshop.txt

No changes were made to the original Quake Live version which is empty.

## Technical details regarding this framework

### Variables that must not be changed

The following variables must not be changed beacause the framework expects them to be like they are set.

##### Network IP

`set net_ip ""` - Blank will bind to all interfaces.

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

##### Server Port

`set net_port "27960"` -  Server port (UDP).

The Quake Live server runs inside a Docker container. The Docker container exposes its own port but only to other Docker container inside that Docker network. To be able to access a Docker container inside that Docker network you have to define an additional external port. The Docker engine then will map that external port to a Docker containers internal port. Thus the Docker containers which running the Quake Live servers can all expose the same port and thus the Quake Live servers all can run on the same standard port 27960.

##### ZMQ rcon IP address

`set zmq_rcon_ip ""` - Which IP to bind to. Blank will bind to all interfaces.

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

##### ZMQ rcon port

`set zmq_rcon_port "28960"` - Rcon port.

Same reason like `net_port`.

##### ZMQ stats IP address

`set zmq_stats_ip ""` - Which IP to bind to. Blank will bind to all interfaces.

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

##### ZMQ stats port

`set zmq_stats_port "27960"` - ZeroMQ stats port (TCP).

Same reason like `net_port`.

##### Access file

`set g_accessFile "access.txt"` - Used to determine which 64-bit Steam IDs have admin access, or are banned.

This file is mounted into the specific Docker container as denoted in the Quake Live servers Docker Compose file. It needs to have a standard location and name so that it is consistent all over the board.

##### minqlx plugin directory

`set qlx_pluginsPath "minqlx-plugins"` - The path (either relative or absolute) to the directory with the plugins.

The minqlx plugins are mounted into the Docker image via the Docker Compose file. It needs to have a standard location to that it is consistent all over the board.

##### minqlx Redis database name

`set qlx_database "Redis"` - The default database to use. You should not change this unless you know what you're doing.

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

##### minqlx Redis address

`set qlx_redisAddress "redis"` - The address to the Redis database. Can be a path if qlx_redisUnixSocket is "1".

The Redis database is part of the Docker network were it has this address. It must not be changed.

##### minqlx Redis database number

`set qlx_redisDatabase 0` - The Redis database number.

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

##### minqlx Redis socket

`qlx_redisUnixSocket 0` - A boolean that determines whether or not qlx_redisAddress is a path to a UNIX socket.

The redis database is part of the Docker network. It is not a Unix socket. This value must not change.

##### minqlx Redis password

`set qlx_redisPassword` - The password to the Redis server, if any.

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

### Variables that were commented out

The cvars set in the `server.cfg` overwrite the ones given through the command line. This framework uses command line parameters to adjust a configuration for a specific server instance given through environment variables that are denoted on the Quake Live servers Docker Compose file in the root of this repository. 

`sv_hostname`, `g_password`, `sv_tags`, `sv_maxClients`, `sv_privateClients`, `sv_privatePassword`, `g_allowVoteMidGame`, `g_allowSpecVote`, `g_voteFlags`, `set sv_warmupReadyPercentage`, `g_warmupDelay`, `g_warmupReadyDelay`, `g_warmupReadyDelayAction`, `g_inactivity`, `g_alltalk`