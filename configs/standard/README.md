# Standard server configuration

The community voted upon standard `server.cfg` which replaces the one from id Software. It represents the smallest common denominator for any Quake Live server configuration.

## Based on

https://github.com/quakelive-server-standards/quakelive-server-standards/blob/5168be332b7d7e2ae0027c7e7b27a34144cee265/configs/_id/server.cfg

## Standards

#### `g_accessFile "access.txt"`

This file is mounted into the specific Docker container as denoted in the Quake Live servers Docker Compose file. It needs to have a standard location so that the usage of the Docker Compose file remains predictable.

#### `g_floodprot_decay "1000"`

Adopted from id Software.

#### `g_floodprot_maxcount "10"`

Adopted from id Software.

#### `net_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### `net_strict "1"`

The Quake Live server runs in a Docker container which will be restarted by the Docker system if it exits.

#### `qlx_commandPrefix "!"`

To provide the player with a consistent experience across different servers, the minqlx commands should always use the same prefix. It should also be the standard prefix to not deviate from the minqlx standard.

#### `qlx_database "Redis"`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### `qlx_pluginsPath "minqlx-plugins"`

The minqlx plugins are mounted into the Docker image via the Docker Compose file. It needs to have a standard location so that the usage of the Docker Compose file remains predictable.

#### `qlx_redisAddress "redis"`

The Redis database is part of the Docker network were it has this address. It must not be changed.

#### `qlx_redisDatabase 0`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### `qlx_redisPassword ""`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### `qlx_redisUnixSocket 0`

The redis database is part of the Docker network. It is not a Unix socket. This value must not change.

#### `sv_floodprotect "10"`

Adopted from id Software.

#### `sv_fps "40"`

Adopted from id Software.

#### `sv_idleExit "120"`

Adopted from id Software.

#### `sv_master "1"`

Adopted from id Software.

#### `sv_serverType "2"`

Adopted from id Software.

#### `zmq_rcon_enable "1"`

Adopted from id Software.

#### `zmq_rcon_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### `zmq_stats_enable "1"`

The Quake Live server sends out information regarding the matches being played, players connected and so on. These information form the foundation of external applications who want to extend the Quake Live experience with new features. QLStats is the most prominent example for this. Every server should have this feature enabled to help the community evolve.

#### `zmq_stats_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

## History

### Version 1

#### Add: `g_accessFile "access.txt"`

This file is mounted into the specific Docker container as denoted in the Quake Live servers Docker Compose file. It needs to have a standard location so that the usage of the Docker Compose file remains predictable.

#### Add: `g_floodprot_decay "1000"`

Adopted from id Software.

#### Add: `g_floodprot_maxcount "10"`

Adopted from id Software.

#### Add: `net_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### Add: `net_strict "1"`

The Quake Live server runs in a Docker container which will be restarted by the Docker system if it exits.

#### Add: `qlx_commandPrefix "!"`

To provide the player with a consistent experience across different servers, the minqlx commands should always use the same prefix. It should also be the standard prefix to not deviate from the minqlx standard.

#### Add: `qlx_database "Redis"`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### Add: `qlx_pluginsPath "minqlx-plugins"`

The minqlx plugins are mounted into the Docker image via the Docker Compose file. It needs to have a standard location so that the usage of the Docker Compose file remains predictable.

#### Add: `qlx_redisAddress "redis"`

The Redis database is part of the Docker network were it has this address. It must not be changed.

#### Add: `qlx_redisDatabase 0`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### Add: `qlx_redisPassword ""`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### Add: `qlx_redisUnixSocket 0`

The redis database is part of the Docker network. It is not a Unix socket. This value must not change.

#### Add: `sv_floodprotect "10"`

Adopted from id Software.

#### Add: `sv_fps "40"`

Adopted from id Software.

#### Add: `sv_idleExit "120"`

Adopted from id Software.

#### Add: `sv_master "1"`

Adopted from id Software.

#### Add: `sv_serverType "2"`

Adopted from id Software.

#### Add: `zmq_rcon_enable "1"`

Adopted from id Software.

#### Add: `zmq_rcon_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### Add: `zmq_stats_enable "1"`

The Quake Live server sends out information regarding the matches being played, players connected and so on. These information form the foundation of external applications who want to extend the Quake Live experience with new features. QLStats is the most prominent example for this. Every server should have this feature enabled to help the community evolve.

#### Add: `zmq_stats_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### Remove: `com_hunkMegs "60"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_allowSpecVote "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_allowVoteMidGame "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_alltalk "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_inactivity "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_password ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `g_voteFlags "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_warmupDelay "15"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_warmupReadyDelay "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `g_warmupReadyDelayAction "1"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `net_port "27960"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `serverstartup "startRandomMap"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `sv_hostname "SERVERNAME"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `sv_maxClients "16"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `sv_privateClients "0"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `sv_privatePassword ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `zmq_rcon_password "ADMINPASSWORD"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `zmq_rcon_port "28960"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `zmq_stats_password ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `zmq_stats_port ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).
