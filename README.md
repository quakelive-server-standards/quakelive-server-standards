# Quake Live server standards and Docker-based server framework

This repository is two in one. It is a community-driven collection of Quake Live server configurations which aims to evolve Quake Live in all its different aspects and at the same it is a Docker-based Quake Live server framework with which you can host as many Quake Live servers as you like.

## Features

- Docker-based server management
- Community-driven configuration standards
- New configurations to evolve Quake Live
- Factories
- Map pools
- Docker images
- Gathered and documented minqlx plugins
- Gathered and documented 3rd party Quake Live applications
- Command-line Quake Live rcon and stats console
- Cvar collections
- Workshop item lists
- Download of Steam Workshop items
- Convert Quake 3 maps to Quake Live maps

## Overview

### Community-driven Quake Live server standards

There are directories regarding the different aspects of the community-driven Quake Live server configurations.

- `configs`: Contains variants of the `server.cfg` which is the place for technical cvars
- `factories`: Contains factories which are a way to bind cvars to a certain gametype
- `mappools`: Contains map pool definitions
- `minqlx-plugins`: Contains all known minqlx plugins and carefully drafted sets of them for different contexts
- `workshop`: Contains overviews of workshop items and sets of them for different purposes

All of these directories contain an `_id` directory in which the original id Software configuration resides. In the case of the minqlx plugins this directory is called `_mino` because the plugin extension was not created by id Software but by a guy named mino.

Furthermore there are two directories `standard` and `evolved`. The former one containing the carefully drafted and voted upon Quake Live server standards and the latter one containing evolved configurations which later on might be integrated into the standard.

In some cases there are also additional directories which are explained in the corresponding README.md files of these.

### Docker-driven server framework

There is a directory `_myservers` which contains a `docker-compose.yml` which is the heart of the Dockerization. You will also find a `connect.sh` which allows you to connect to your Quake Live servers via the command line.

### Apps

There is a directory `apps` which is a collection of all known Quake Live dedicated server related apps. These apps are more from a viewpoint of an admin as opposed to the viewpoint of a player. You will not find apps like custom Quake Live server browsers for example.

### Docker

The directory `docker` contains all of the Docker images used for the Docker-based Quake Live server framework but also for all other apps collected in the `apps` directory.

## Quickstart hosting servers

Here we give you instructions on how to start hosting servers real quick. You will have your Quake Live servers up and running in about 5 minutes, all of them using community developed standards providing the best experience for the players.

### Installing

Install Git and clone this repository using `git clone https://github.com/quakelive-server-standards/server-standards.git`. Install Docker https://docs.docker.com/engine/install/.

### Configuring

Open the `docker-compose.yml` file in the `_myservers` directory. It contains all servers. When freshly cloned, it defines one server for every standard game mode. Delete those that you do not want and duplicate those that you want more than one time. For example, if you want to have four duel servers, delete all the other definitions apart from the duel one and duplicate that duel server definition three times.

Here you can see the definition for the duel server.

```yml
duel1:
    image: quakeliveserverstandards/duel
    restart: always
    ports:
      - '27962:27962/udp' # game port
      - '27962:27962/tcp' # stats port
      - '28962:28962/tcp' # rcon port
    environment:
      - NET_PORT=27962
      - SV_HOSTNAME=QL Standard Duel Server #1
      - SV_TAGS=duel
      - SV_MAXCLIENTS=
      - SV_PRIVATECLIENTS=
      - SV_PRIVATEPASSWORD=
      - G_PASSWORD=
      - G_ALLTALK=
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

The next step is to adjust the ports so that every server uses its own unique set. Every Quake Live server uses three of them. The game port which runs with UDP and starts at `27960`, the stats port which most of the time is the same port as the game port but runs with TCP and the rcon port which is the game port plus 1000. To be quick we use exactly that scheme.

Adjust the ports in the `ports` section of the Docker Compose file and set the game port in the environment variable `NET_PORT`. Using the above mention scheme, the other ports configured through the environment variables `ZMQ_RCON_PORT` and `ZMQ_STATS_PORT` will be set automatically.

Additionally, setup a name for your servers by setting the environment variable `SV_HOSTNAME`.

### Running

To run your freshly defined server, open a terminal, cd into the `_myservers` directory and execute `docker-compose up -d`. Congratulations, you are now successfully hosting your own Quake Live servers.

### What is next?

The next step is to start and understand how to configure a Quake Live server in all of its different aspects. Take a look into this [README.md](https://github.com/quakelive-server-standards/server-standards/tree/master/_myservers#readme) file to learn about everything.

## Participating

Community-driven Quake Live server standards come to life through the participation of the community.

### Contribute configs

### Contribute factories

### Contribute minqlx plugins

### Contribute workshop

### Contribute Docker files

### Contribute apps