# Standard base config

This is the base configuration which serves as a starting point for any new configuration. It contains the smallest common denominator for any Quake Live server configuration.

## Standards

##### minqlx command prefix

`set qlx_commandPrefix "!"` - The prefix used before command names in order to execute them.

To provide the player with a consistent experience across different servers, the minqlx commands should always use the same prefix. It should also be the standard prefix to not deviate from the minqlx standard.

##### ZMQ rcon (remote connection)

`set zmq_rcon_enable "1"` - Enable rcon.

Rcon can be used to execute commands on the server remotely. Especially the `say` command might be a vital part of an external application which wants to provide new features for Quake Live. Every server should have this feature enabled to help the community evolve.

##### ZMQ Stats

`set zmq_stats_enable "1"` - Enable ZeroMQ stats

The Quake Live server sends out information regarding the matches being played, players connected and so on. These information form the foundation of external applications who want to extend the Quake Live experience with new features. QLStats is the most prominent example for this. Every server should have this feature enabled to help the community evolve.

## Technical details regarding this framework

### Variables that must not be changed

The following variables must not be changed beacause the framework expects them to be like they are set.

##### Network IP

`set net_ip ""` - Blank will bind to all interfaces.

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

##### Server Port

`set net_port ""` -  Server port (UDP).

To be able to configure the UDP port of the server through an environment variable in the Docker Compose file, this value must not be set in order to be able to set it via the command line.

##### ZMQ rcon IP address

`set zmq_rcon_ip ""` - Which IP to bind to. Blank will bind to all interfaces.

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

##### ZMQ rcon port

`set zmq_rcon_port ""` - Rcon port.

To be able to configure the rcon port of the server through an environment variable in the Docker Compose file, this value must not be set in order to be able to set it via the command line.

##### ZMQ stats IP address

`set zmq_stats_ip ""` - Which IP to bind to. Blank will bind to all interfaces.

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

##### ZMQ stats port

`set zmq_stats_port ""` - ZeroMQ stats port (TCP).

To be able to configure the stats port of the server through an environment variable in the Docker Compose file, this value must not be set in order to be able to set it via the command line.

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

This framework uses command line parameters to configure server instance specific settings. Since cvars given in the command line can be overriden by definitions made in the `server.cfg`, they must not be set there. The following cvars are commented out.

`sv_hostname`, `g_password`, `sv_tags`, `sv_maxClients`, `sv_privateClients`, `sv_privatePassword`, `g_allowVoteMidGame`, `g_allowSpecVote`, `g_voteFlags`, `set sv_warmupReadyPercentage`, `g_warmupDelay`, `g_warmupReadyDelay`, `g_warmupReadyDelayAction`, `g_inactivity`, `g_alltalk`