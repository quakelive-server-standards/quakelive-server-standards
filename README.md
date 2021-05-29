# Quake Live server standards and Docker-based server framework

This repository is two in one. It is a community-drive collection of Quake Live server configurations which aims to evolve Quake Live in all its different aspects and at the same it is a Docker-based Quake Live server framework with which you can host as many Quake Live servers as you like.

## Features

- Docker-based server management
- Community-driven configuration standards
- New configurations to evolve Quake Live
- Factories
- Map pools
- Docker images
- Gathered and documented Minqlx plugins
- Gathered and documented 3rd party Quake Live applications
- Command-line Quake Live rcon and stats console
- Complete and up to date CVAR guide
- Workshop item lists
- Download of Steam Workshop items
- Convert Quake 3 maps to Quake Live maps

## Overview

In the root directory there are two files which are your basic work horses.

- `docker-compose.yml`: Defines your Quake Live servers and sets their configurations.
- `rcon.sh`: Starts an rcon terminal into one of your Quake Live servers.

The directory `configs` contains standard and evolved server configurations you can apply to your servers. A standard configuration is one which configuration values were debated and agreeded upon by the community. There is one for every basic game mode `ca`, `ctf`, `duel`, `ffa`, `race` and `tdm`. An evolved configuration bases on a standard one but introduces new settings. If one of them seems to be more fun to you then try it out.

A configuration does not only consist of a `server.cfg` and a `mappool.txt`, but also items that can be found in the following directories.

- `minqlx-plugins`: A collection of plugins for the server extends minqlx contributed by the community.
- `factories`: A collection of game modes which is evolved and experimented with by the community.
- `workshop`: The workshop is the official place of Steam were maps and other additional files are offered for download. In this directory you will find elaborated sets of workshop items for different purposes.

## Quickstart

Here we give you instructions on how to start real quick. You will have your Quake Live servers up and running in about 5 minutes, all of them using community developed standards providing the best experience for the players.

### Installing

Install Git and clone this repository `git clone https://github.com/quakelive-server-standards/server-standards.git`. Install Docker https://docs.docker.com/engine/install/.

### Configuring

Open the `docker-compose.yml` file in the `_myservers` directory. It contains all servers. When freshly cloned, it defines one server for every standard game mode. Delete those that you do not want and duplicate those that you want to have more than one time. For example, if you want to have four duel servers, delete all the other definitions apart from the duel one and duplicate that duel server definition three times.

Here you can see the definition of the duel server.

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

The next step is to adjust the ports. Quake Live servers use three ports. The game port which uses UDP and starts at `27960`, the stats port which most of the time is the same port as the game port but uses TCP and the rcon port which is the game port plus 1000. To be quick we use exactly that scheme.

Adjust the ports in the `ports` section of the Docker Compose file and set the game port in the environment variable `NET_PORT`.

Additionally, setup a name for your server by setting the environment variable `SV_HOSTNAME`.

### Running

To run your freshly defined server, open a terminal, cd into the `_myservers` directory and execute `docker-compose up -d`. Congratulations, you are now successfully hosting your own Quake Live servers.

### What is next?

The next step is to start and understand how to configure a Quake Live server in all of its different aspects. Take a look into the `_myservers` [README.md](https://github.com/quakelive-server-standards/server-standards/tree/master/_myservers#readme) file to get learn every aspect.

## Participating

### Discuss standards

### Contribute configs

### Contribute factories

### Contribute minqlx plugins

### Contribute workshop

### Configuring through command line parameters

We discourage from configuring the server through command line parameters.

If you set `sv_maxClients` the game will tell you `sv_maxClients will be changed to 2 upon restarting.` but it does not work and if you look into the config it nothing has changed.
If you set `net_port` the game will tell you `net_port will be changed to 5000 upon restarting.` but it does not work and if you look into the config it nothing has changed.
If you set `zmq_rcon_port` the game will tell you `zmq_rcon_port is write protected.` which seems to mean that this values cannot be set through command line parameters.
If you set `zmq_stats_port` the game will tell `zmq_stats_port is write protected.` which seems to mean that this values cannot be set through command line parameters.
Also any minqlx variable cannot be set through the command line.
Also is it hard to tell if you need quotes `""` around your value or not.
Also will the `server.cfg` overwrite any value given on the command line which is not good because if you issue the command line paramater you do not know what is inside the `server.cfg`.
