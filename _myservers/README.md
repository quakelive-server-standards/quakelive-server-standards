# My Servers

This is your working directory. Anything that is specific to your own servers can be put here. Do whatever you like with it. Adjust it exactly to the needs that you are having. Any file in here is just for your convenience and can be altered or deleted if not needed.

## Overview

All your servers are defined inside the `docker-compose.yml` file. Docker allows for easy server management. You do not need to install anything and everything runs out of the box. Combined with Git it is a perfect backup and recreation tool. If you want to move your Quake Live servers to another server computer, the only things you need to do is to install Git and Docker and to clone your own fork of the Quake Live Server Standards repository.

## Configuring your Quake Live servers

### Cvars and their locations

The Quake Live server offers four locations to put cvars into.

- As command line parameters
- `server.cfg`
- `autoexec.cfg`
- Inside a `*.factories` file

In this order, the command line parameter has the lowest priority while the factories file has the highest, which means that a cvar defined in a factories file will override any other definition of the same cvar in any other of the lower prioritized locations.

This Docker-based server framework uses the different locations for different purposes.

- Command line parameter: Server instance specific cvars like the name of the server
- `server.cfg`: Technical cvars like the location of the `mappool.txt` file
- `autoexec.cfg`: Cvars specific to to all or a group of your servers
- `*.factories`: Cvars specific to a game mode like the damage of a weapon

Your main work horses are command line parameters in the form of Docker environment variables and the `autoexec.cfg`. But of course you can also alter the standards in the `server.cfg` which you will then hopefully contribute to the Quake Live Server Standards repository if you found that they are good. Also feel free to fiddle around with the game mode specific cvars.

Apart from a lot of minqlx cvars, the `autoexec.cfg` for most invites you to set your rcon and stats password, which will then apply to all of your Quake Live servers.

If you need more than `autoexec.cfg` file because for example you are hosting Free For All and Duel servers, just create a second one and rename the original one.

### access.txt

This files holds a list of users identified by their Steam Ids, giving them either the status of an admin, a moderator or of being banned. You will find an empty `access.txt` file and the first thing you might want to do is to put your own Steam Id into it, followed by a `|admin`, which would give yourself the role of an admin on your own servers.

### mappool.txt

This file contains a list of map|factory combinations. It defines, which maps should be available for which factory, while a factory being a collection of cvars in the context of a specific game type like Duel.

Note that this map pool is not enforced by the game. This means players still can vote for any map either calling the vote through the console or by using the voting menu which still displays all available maps. The definitions made in the `mappool.txt` will only influence the maps the game offers in the voting screen which appears after a match.

If you want to enforce a map pool you can use the minqlx plugin `barelymissed/mapLimiter.py` which provides a variable `qlx_enforceMappool` which you need to set to `1`, preferably in your `autoexec.cfg`.

### workshop.txt

This file contains a list of Steam Workshop Item Ids the server will download on startup. The most items found in the Steam Workshop are maps. But there are also sounds for the different intermission minqlx plugins.

### minqlx-plugins

This is a directory containing minqlx plugins. The physical existence of these plugin files has to be paired with a listing of these files in the minqlx cvar `qlx_plugins`. Only those plugins are loaded which are defined in this list. Since this can become tedious this framework provides a mechanism that when you not define that list it will simply load any plugin it finds. If you define that list it will use the list instead.

Apart from that cvar, there are others which you can define in your `autoexec.cfg`.

## Composing your server configurations with Docker

The configuration files for a particular Quake Live server are assembled in the `docker-compose.yml` file. Here is an example for a Duel server.

```yml
version: '3.8'
services:
  duel:
    image: quakeliveserverstandards/duel
    restart: always
    ports:
      - '27960:27960/udp' # game port
      - '27960:27960/tcp' # stats port
      - '28960:28960' # rcon port
    environment:
      - NET_PORT=27960
      - SV_HOSTNAME=QL Standard Duel Server #1
    volumes:
      - './access.txt:/home/steam/ql/baseq3/access.txt'
      - './autoexec.cfg:/home/steam/ql/baseq3/autoexec.cfg'
      - '../configs/standard/server.cfg:/home/steam/ql/baseq3/server.cfg'
      - '../factories/standard/duel/duel.factories:/home/steam/ql/baseq3/scripts/duel.factories'
      - '../mappools/standard/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
      - '../minqlx-plugins/standard/duel:/home/steam/ql/minqlx-plugins'
      - '../workshop/standard/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
    depends_on: 
      - redis
  redis:
    image: redis
    restart: always
    volumes:
      - redis:/data # uses a Docker volumne by default
volumes:
  redis:
```

The section `services` defines two services `duel1` and `redis`. The first one is the Quake Live server. The second one is the Redis database as demanded by minqlx. While you leave the redis service as it is, we will have a deeper look into the Quake Live server definition.

There are three places which are interesting.

- `ports`: Definition of the exposed ports
- `environment`: Definition of server specific values
- `volumes`: Linking of different configuration files into the Quake Live server's working directory

### Ports

A Quake Live server uses three ports.

- Game port: This is the main port which a Quake Live game client will connect to
- Stats port: The port the stats API emits its events to
- Rcon port: The port the rcon API will receive commands and sends console output to

You will define those ports in the `ports` section of the `docker-compose.yml` file. 

A Docker service has two ports. An external and an internal port. Take a look at the correspoding Docker Compose file definition.

```yml
ports:
  - '27960:27960/udp' # external-port:internal-port/protocol
  - '27960:27960/tcp' # external-port:internal-port/protocol
  - '28960:28960' # external-port:internal-port
```

To be able to undestand this you need to know that every service defined in a Docker Compose file runs in a Docker network. The internal port is one that is only visible inside that network. Thus if you would try and access it from outside you could not. Thus you also need to define an external port. The Docker engine will then map that external port to the internal one of the corresponding Docker service. The definition is `external-port:internal-port/protocol`.

In our case, the internal and external ports are the same. Thus, just write the port number two times, separated by a colon.

You can also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#ports) if you want to know more.

### Environment

In the `environment` section of the Docker Compose file you can configure Quake Live server variables which internally will be appended as command line parameters to the Quake Live server executable call. Those are the right place for server instance specific settings, like the server name.

```yml
environment:
  - SV_HOSTNAME=QL Standard Duel Server #1
  - G_PASSWORD=secret
```

The following variables are supported: `SV_HOSTNAME`, `G_PASSWORD`, `SV_TAGS`, `SV_MAXCLIENTS`, `SV_PRIVATECLIENTS`, `SV_PRIVATEPASSWORD`, `SV_ALLOWVOTE`, `SV_VOTEDELAY`, `SV_VOTELIMIT`, `SV_ALLOWVOTEMIDGAME`, `SV_ALLOWSPECVOTE`, `SV_VOTEFLAGS`, `SV_WARMUPREADYPERCENTAGE`, `SV_WARMUPDELAY`, `SV_WARMUPREADYDELAY`, `SV_WARMUPREADYDELAYACTION`, `G_INACTIVITY`, `G_ALLTALK`

Note that command line parameters have the lowest priority. This means, if you set the `sv_maxClients` in the `server.cfg`, you will not be able to alter it through these environment variables anymore. The definition in the `server.cfg` will always override that of command line parameters. This can be a source for errors and confusion.

### Volumes

In the `volumes` section you compose a Quake Live server configuration by mounting the configuration files from your computer directly into the correct place of the Quake Live server installation inside the Docker container. Here is a complete list of that mappings.

```yml
volumes:
      - './access.txt:/home/steam/ql/baseq3/access.txt'
      - './autoexec.cfg:/home/steam/ql/baseq3/autoexec.cfg'
      - '../configs/standard/server.cfg:/home/steam/ql/baseq3/server.cfg'
      - '../factories/standard/duel/duel.factories:/home/steam/ql/baseq3/scripts/duel.factories'
      - '../mappools/standard/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
      - '../minqlx-plugins/standard/duel:/home/steam/ql/minqlx-plugins'
      - '../workshop/standard/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
```

The part before the colon denotes a file or directory on your computer and the one after the location inside the Docker container. Files or directories mounted like this will appear to the Quake Live server as a natural part of its file system. You can also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes) for more information.

To customize your server, you can replace any file from the left side. You can start by using one of the evolved versions coming with this repository. People created new `server.cfg` variations, new factories, new map pools, new sets of minqlx plugins or lists of workshop items.

If you want to alter any of the files that are outside of the `_myservers` directory or if you want to create your own files, we recommend to put these into the `_myservers` directory, leaving the other directories untouched. This facilitates smooth updates coming from the official Quake Live Server Standards repository. For example, if you changed the `configs/standard/server.cfg` directly while receiving such an update, it might result in merge conflicts which you would have to resolve. This is not an especially hard thing to do but it might be inconvenient.

## Backup your server configurations with Git

## Receiving updates from the official Quake Live Server Standards repository

## Starting and managing your Quake Live servers

To start your servers, start a terminal of your operating system and cd into this directory `_myservers`. Now type `docker-compose up -d` which will start every Quake Live server that is defined in the `docker-compose.yml` plus the needed Redis database for the minqlx plugins. The parameter `-d` stands for detached and means that the servers run in the background.

To stop every Quake Live server plus the Redis database use `docker-compose stop`. To stop a specific server you can use the same command followed by the Docker Compose service name as specified in the `docker-compose.yml` file like this `docker-compose stop duel1`.

If you want to see the logs of your servers use `docker-compose logs -f` while the parameter `-f` means follow and results in the log output being updated every time a new entry is added.

## Accessing your Quake Live servers with QL Console

If configured so, a Quake Live server provides two APIs, the rcon and the stats API. The first one is like the console that you also have ingame while the second one emits events regarding the game that are being played.

There is a shell script `connect.sh` which starts a command-line client which can connect to both of these APIs at the same time. It is based on the [QL Console project](https://github.com/quakelive-server-standards/ql-console). To use it, you do not have to install anything apart from Docker. The script creates a Docker container based on [this](https://hub.docker.com/r/quakeliveserverstandards/ql-console) Docker image.

To connect to one of your servers, open a terminal and cd into the `_myservers` directory, then type `./connect.sh 127.0.0.1 --rcon-port 28960 --rcon-password quakeliveserverstandards --stats-port 27960 --stats-password quakeliveserverstandards`. Replace the IP, the ports and the passwords accordingly. You can also connect to either only rcon or only stats. Refer to the [QL Console documentation](https://github.com/quakelive-server-standards/ql-console#readme) for more information.

## Joining the Quake Live evolution

The next part, as a server administrator and Quake Live experience creator, is to join the Quake Live evolution, where we, the community, try to establish new standards to bring the game forward. Thus, if you have found a setting the players on your servers accept really well, consider to contribute it back to the original Quake Live Server Standards repository. It might be something that improves the experience for us all and therefor might be able to consolidate and grow our community. It might even be worthy to be integrated into the standard.
