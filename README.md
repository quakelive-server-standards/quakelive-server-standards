# Quake Live server standards and Docker-based server framework

This repository is two in one. It is a community-driven collection of Quake Live server configurations which aims to evolve Quake Live in all its different aspects and at the same it is a Docker-based Quake Live server framework with which you can host as many Quake Live servers as you like.

## Features

- [Docker-based server management](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers)
- Community-driven configuration standards
- Evolved configurations to bring Quake Live forward
- [Factories](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories)
- [Map pools](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/mappools)
- [Docker images](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/docker)
- [Gathered and documented minqlx plugins](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins/_plugins)
- [Gathered and documented 3rd party Quake Live applications](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/apps)
- [Command-line Quake Live rcon and stats console](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#accessing-your-quake-live-servers-remotely-with-ql-console)
- [Cvar collections](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/factories/cvars.md)
- [Download of Steam Workshop items](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop#download-a-workshop-item)
- [Convert Quake 3 maps to Quake Live maps](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop#convert-a-quake-3-map-to-a-quake-live-map)

## Overview

### Community-driven Quake Live server standards

There are directories regarding the different aspects of the community-driven Quake Live server configurations.

- [`configs`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs): Contains variants of the `server.cfg` which is the place for technical cvars
- [`factories`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories): Contains factories which are a way to bind cvars to a certain gametype
- [`mappools`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/mappools): Contains map pool definitions
- [`minqlx-plugins`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins): Contains all known minqlx plugins and carefully drafted sets of them for different contexts
- [`workshop`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop): Contains overviews of workshop items and sets of them for different purposes

All of these directories contain an `_id` directory in which the original id Software configuration resides. In the case of the minqlx plugins this directory is called `_mino` because the plugin extension was not created by id Software but by a guy named mino.

Furthermore there are two directories `standard` and `evolved`. The former one containing the carefully drafted and voted upon Quake Live server standards and the latter one containing evolved configurations which later on might be integrated into the standard.

In some cases there are also additional directories which are explained in the corresponding README.md files of these.

### Docker-driven server framework

There is a directory [`_myservers`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers) which contains a [`docker-compose.yml`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/docker-compose.yml) which is the heart of the [Dockerization](https://www.docker.com). You will also find a [`connect.sh`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/connect.sh) which allows you to connect to your Quake Live servers via the command line.

### Apps

There is a directory [`apps`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/apps) which is a collection of all known Quake Live dedicated server related apps. These apps are more from a viewpoint of an admin as opposed to the viewpoint of a player. You will not find apps like custom Quake Live server browsers for example.

### Docker

The directory [`docker`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/docker) contains all of the Docker images used for the Docker-based Quake Live server framework but also for all other apps collected in the [`apps`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/apps) directory.

## Quickstart hosting servers

Here we give you instructions on how to start hosting servers real quick. You will have your Quake Live servers up and running in about 5 minutes, all of them using community developed standards providing the best experience for the players.

### Installing

Install Git and clone this repository using `git clone https://github.com/quakelive-server-standards/quakelive-server-standards.git`. Install Docker https://docs.docker.com/engine/install/.

### Configuring

Open the [`docker-compose.source.yml`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/docker-compose.source.yml) file in the [`_myservers`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers) directory. It contains reference server definitions for every game type. Copy those that you want into the [`docker-compose.yml`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/docker-compose.yml) file. If you want more than one server for a game type, copy the reference definition multiple times.

Here you can see the definition for a duel server.

```yml
duel1:
    image: quakeliveserverstandards/duel
    restart: always
    ports:
      - '27960:27960/udp' # game port
      - '27960:27960/tcp' # stats port
      - '28960:28960/tcp' # rcon port
    environment:
      - NET_PORT=27960
      - SV_HOSTNAME=QL Standard Duel Server #1
      - SV_TAGS=duel
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
```

Change the Docker service names like `duel1` so that every name is unique.

Change the ports so that every server uses its own unique set. Every Quake Live dedicated server uses three of them. The game port which runs with UDP and starts at `27960`, the stats port which most of the time is the same port as the game port but runs with TCP and the rcon port which is the game port plus 1000. To be quick we use exactly that scheme.

Adjust the ports in the `ports` section of the Docker Compose file and set the game port in the environment variable `NET_PORT`. Using the above mention scheme, the other two ports configured through the environment variables `ZMQ_RCON_PORT` and `ZMQ_STATS_PORT` will be set automatically.

Additionally, set unique names for your servers by setting the environment variable `SV_HOSTNAME`.

### Running

To run your freshly defined server, open a terminal, cd into the `_myservers` directory and execute `docker-compose up -d`. Congratulations, you are now successfully hosting your own Quake Live servers.

### What is next?

The next step is to start and understand how to configure a Quake Live server in all of its different aspects. Take a look into this [README.md](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#readme) file to learn about everything.

## Evolve Quake Live

Community-driven Quake Live server standards come to life through the participation of the community.

### Contribute evolved Quake Live dedicated server configurations

### Discuss what to transfer into the Quake Live server standards

### Fix files
