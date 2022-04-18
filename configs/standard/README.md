# Standard server configuration

This is the standard `server.cfg` file. It represents the smallest common denominator for any Quake Live server configuration.

## Based on

https://github.com/quakelive-server-standards/quakelive-server-standards/blob/5168be332b7d7e2ae0027c7e7b27a34144cee265/configs/_id/server.cfg

## Standards

#### `set g_accessFile "access.txt"`

This file is mounted into the specific Docker container as denoted in the Quake Live servers Docker Compose file. It needs to have a standard location so that the usage of the Docker Compose file remains predictable.

#### `set g_floodprot_decay "1000"`

This is the id Software default.

#### `set g_floodprot_maxcount "10"`

This is the id Software default.

#### `set net_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### `set net_strict "1"`

The Quake Live server runs in a Docker container which will be restarted by the Docker system if it exits.

#### `set qlx_commandPrefix "!"`

To provide the player with a consistent experience across different servers, the minqlx commands should always use the same prefix. It should also be the standard prefix to not deviate from the minqlx standard.

#### `set qlx_database "Redis"`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### `set qlx_pluginsPath "minqlx-plugins"`

The minqlx plugins are mounted into the Docker image via the Docker Compose file. It needs to have a standard location so that the usage of the Docker Compose file remains predictable.

#### `set qlx_redisAddress "redis"`

The Redis database is part of the Docker network were it has this address. It must not be changed.

#### `set qlx_redisDatabase 0`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### `set qlx_redisPassword ""`

The Redis database is part of the Docker services and configured to work with the Quake Live server Docker containers. It needs to have this value which must not change.

#### `set qlx_redisUnixSocket 0`

The redis database is part of the Docker network. It is not a Unix socket. This value must not change.

#### `set sv_floodprotect "10"`

This is the id Software default.

#### `set sv_fps "40"`

This is the id Software default.

#### `set sv_idleExit "120"`

This is the id Software default.

#### `set sv_master "1"`

This is the id Software default.

#### `set sv_serverType "2"`

This is the id Software default.

#### `set zmq_rcon_enable "1"`

Rcon can be used to execute commands on the server remotely. Especially the `say` command might be a vital part of an external application which wants to provide new features for Quake Live. Every server should have this feature enabled to help the community evolve.

#### `set zmq_rcon_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

#### `set zmq_stats_enable "1"`

The Quake Live server sends out information regarding the matches being played, players connected and so on. These information form the foundation of external applications who want to extend the Quake Live experience with new features. QLStats is the most prominent example for this. Every server should have this feature enabled to help the community evolve.

#### `set zmq_stats_ip ""`

The Quake Live server runs in a Docker container which has exactly one IP address which is given to it by the Docker engine. This value must not change.

## History

### Version 1

#### Remove: `set com_hunkMegs "60"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_allowSpecVote "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_allowVoteMidGame "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_alltalk "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_inactivity "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_password ""`

[The Quake Live server framework](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) intends the user to set it through an environment variable. Since the environment variable is forwarded to the Quake Live dedicated server executable as a command line parameter, it must not be set in the `server.cfg` which would overwrite it.

#### Remove: `set g_voteFlags "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_warmupDelay "15"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_warmupReadyDelay "0"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set g_warmupReadyDelayAction "1"`

This cvar is either specific to a certain server instance or to a certain game type. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible, in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) or in a [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories).

#### Remove: `set net_port "27960"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set serverstartup "startRandomMap"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set sv_hostname "SERVERNAME"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set sv_maxClients "16"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set sv_privateClients "0"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set sv_privatePassword ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set zmq_rcon_password "ADMINPASSWORD"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set zmq_rcon_port "28960"`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set zmq_stats_password ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).

#### Remove: `set zmq_stats_port ""`

This cvar is either specific to a certain server instance. It should be either set as a [command line parameter](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#command-line-parameters) if possible or in the [`autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg).
