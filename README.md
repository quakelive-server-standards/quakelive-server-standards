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

In the next step you can try to deviate from the standards. For example you can offer some new maps and combine those with your own game mode in which you changed the weapon respawn time or the gravity. You can also play around with the numerous minqlx plugins or look into the apps collection.

When you found a configuration which seems to be really successful you can contribute it to the official Quake Live Server Standards repository. It might even become part of one of the standards.


### The configs directory

#### access.txt

#### Standardized and experimental Quake Live server configurations

## Create your own Quake Live server configuration

`untouched-server.cfg`

### Factories (Game modes)

### minqlx Plugins

### Workshop

## Contribute

### Discuss standards

### Contribute configs

### Contribute factories

### Contribute minqlx plugins

### Contribute workshop

## Usage

To use these files create a fork of this repository. Then clone your fork. After cloning add the original (upstream) repository to your Git configuration ([GitHub manual](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)).

```shell
git remote add upstream https://github.com/Gastmeier/quake-live-server-framework.git
```


Open the `docker-compose.yml` file and adjust two things.

At first QL ports of the demo server.

```yml
ql1:
    ports:
      - '27960:27960/udp'
      - '27960:27960/tcp'
      - '28960:28960'
ql2:
    ports:
      - '27961:27960/udp'
      - '27961:27960/tcp'
      - '28961:28960'
```

If your server is using a reverse proxy like Traefik you do not need to expose the ports to the public through Docker but the reverse proxy will do this for you. In this case, every Docker container can use the same port.

```yml
ql1:
    ports:
      - '27960/udp'
      - '27960/tcp'
      - '28960'
ql2:
    ports:
      - '27960/udp'
      - '27960/tcp'
      - '28960'
```

The second thing to adjust is the place outside the Docker container that Redis is using to store its data. This is an important step because if the data was in the container it would be lost if the container was deleted, which is a common thing.

```yml
redis
    # volumes:
    #     - /var/ql-redis:/data
```

Uncomment the two lines and replace `/var/ql-redis` with a directory on your host system outside the Docker container.

Now open the file `access.txt` and put one admin person into it.

The last step is to commit and push your configuration back to GitHub. That way you will never lose it and you can relocate to another server within minutes.

## Add a server

To configure a server you need to open the `docker-compose.yml` file. There you can add as many servers as you like. Just copy and paste such a block.

```yml
  ql1:
    image: ql
    restart: always
    ports:
      - '27960:27960/udp'
      - '27960:27960/tcp'
      - '28960:28960'
    environment:
      - HOSTNAME='QL Server #1'
      - PASSWORD=''
    volumes:
      - './access.txt:/home/steam/ql/baseq3/access.txt'
      - './default_cfg/server.cfg:/home/steam/ql/baseq3/server.cfg'
      - './default_cfg/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
      - './default_cfg/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
    depends_on: 
      - redis
```

Now adjust the information.

Start with the `ports`. The Quake Live server needs three ports:

- `27960/udp`: This is the main port for exchanging the player in game data
- `27960/tcp`: This port is for ZMQ stats for sending meta information about the played match (QLStats uses this)
- `28960/tcp`: This port is for ZMQ RCON interface which is for managing the server

In the section `environment` you can set the server name and a password if you like.

The section `volumes` is used to set the configuration.

- `access.txt` (optional): Set server moderators, administrator or ban people. There is one file for all servers.
- `server.cfg`: This file is for general server configurations.
- `mappool.txt` (optional): A list of maps and their game modes.
- `workshop.txt` (optional): Contains all workshop items your server uses.

The next section tells you which files you should be chosing and how to adjust them.

## Configure a server

Server configuration are stored in the `configs` sub directory. There is the default Quake Live server config `default_cfg` and next to it other popular configurations. You can either chose to apply them unchanged or take them as a base for your own variants.

### server.cfg

Either way, you have to adjust the `server.cfg` by setting the following important variables: `qlx_owner`, `sv_tags`, `zmq_rcon_password`. You will find a good description of what each variable does in the file itself.

Do not set one these variables as they are set as part of the wider Docker configuration: `qlx_pluginsPath`, `qlx_database`, `qlx_redisAddress`, `qlx_redisDatabase`, `qlx_redisUnixSocket`, `qlx_redisPassword`, `sv_hostname`, `g_password`, `sv_mapPoolFile`, `net_port`, `net_strict`, `zmq_rcon_port`, `g_accessFile`.

### mappool.txt

If you want to limit or extend the map pool you can create a `mappool.txt`

### Configuring through command line parameters

We discourage from configuring the server through command line parameters.

If you set `sv_maxClients` the game will tell you `sv_maxClients will be changed to 2 upon restarting.` but it does not work and if you look into the config it nothing has changed.
If you set `net_port` the game will tell you `net_port will be changed to 5000 upon restarting.` but it does not work and if you look into the config it nothing has changed.
If you set `zmq_rcon_port` the game will tell you `zmq_rcon_port is write protected.` which seems to mean that this values cannot be set through command line parameters.
If you set `zmq_stats_port` the game will tell `zmq_stats_port is write protected.` which seems to mean that this values cannot be set through command line parameters.
Also any minqlx variable cannot be set through the command line.
Also is it hard to tell if you need quotes `""` around your value or not.
Also will the `server.cfg` overwrite any value given on the command line which is not good because if you issue the command line paramater you do not know what is inside the `server.cfg`.


## Create your own server configuration

To create your own server configuration, copy and paste one of the existing directories and make your adjustments.

## Start the server using Docker

You can start the server by tying `docker-compose up -d` into your terminal. The parameter `-d` puts the process in the background. If you want to see the logs of the servers, type `docker-compose logs -f`. The parameter `-f` means follow and leads to a continuous flow of the log messages. If you want to see what is inside one of your Quake Live servers use `docker-compose exec ql1 bash`, while `ql1` is the name of a Docker container as specified in the `docker-compose.yml` file.

## Update the Docker container


## Adjust the Dockerfile

The Dockerfile is the receipt of the base image which is used for every Quake Live dedicated server Docker container. It contains the Steam Console Client and the Quake Live dedicated server with installed minqlx extension. 

If you adjusted the Dockerfile you need to build the image again. Use the script `build-docker-image.sh` to create a Docker image by the name `ql`. The `docker-compose.yml` relies on that name. If you already instantiated Docker containers from the old image, be sure to delete and build them again.

## Contributing



https://qlstats.net/panel1/servers.html
https://qlstats.net/panel2/servers.html
https://qlstats.net/panel3/servers.html
https://qlstats.net/panel4/servers.html