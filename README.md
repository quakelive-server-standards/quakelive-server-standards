# Docker-based Quake Live Server Framework

A Docker-based Quake Live server framework with preinstalled minqlx and full configurability. You can use these files as a base for your own Quake Live servers. This respository will be constantly updated with popular server configurations variables, recommendable workshop maps, factories and minqlx plugins. It aims to collect and provide sensible standards.

accessible

## Overview

In the root directory there are two files which are your basic work horses.

- `docker-compose.yml`: Defines your Quake Live servers and sets their configurations.
- `rcon.sh`: Starts an rcon terminal into one of your Quake Live servers.

The directory `configs` contains standard and evolved server configurations you can apply to your servers. A standard configuration is one which configuration values were debated and agreeded upon by the community. There is one for every basic game mode `ca`, `ctf`, `duel`, `ffa`, `race` and `tdm`. An evolved configuration bases on a standard one but introduces new settings. If one of them seems to be more fun to you then try it out.

A configuration does not only consist of a `server.cfg` and a `mappool.txt`, but also items that can be found in the following directories.

- `minqlx-plugins`: A collection of plugins for the server extends minqlx contributed by the community.
- `factories`: A collection of game modes which is evolved and experimented with by the community.
- `workshop`: The workshop is the official place of Steam were maps and other additional files are offered for download. In this directory you will find elaborated sets of workshop items for different purposes.

## Installation

This framework uses Docker to compose configurations and to run any amount of server instances. It will also take care of any additional software that the Quake Live server or its rcon client needs. This link https://docs.docker.com/engine/install/ will provide you every information on how to install it.

--- GIT ---

## Starting and managing your Quake Live servers

To start your servers, start a terminal of your operating system and cd into the root directory of this framework. Now type `docker-compose up -d` which will start every Quake Live server that is defined in the `docker-compose.yml` plus the needed Redis database for the minqlx plugins. The parameter `-d` stands for detached and means that the servers run in the background.

To stop every Quake Live server plus the Redis database use `docker-compose stop`. To stop a specific server you can use the same command followed by the Docker Compose service name as specified in the `docker-compose.yml` file like this `docker-compose stop duel1`.

If you want to see the logs of your servers use `docker-compose logs -f` while the parameter `-f` means follow and results in the log output being updated every time a new entry is added.

## Maintaining your Quake Live servers via rcon

To maintain a server you use `./rcon.sh 127.0.0.1:27960 rconpassword` to start an rcon terminal into one of your running servers. Replace the ip address `127.0.0.1` with the one pointing to your Quake Live servers, chose the corresponding port and set the password that you have configured.

## Configuring your Quake Live severs

There are two places you need to take into consideration when configuring your Quake Live servers.

- `docker-compose.yml`: Here you define all of your server instance and compose their configuration.
- `configs`: A directory containing standardized and your own customized server configurations.

### The Docker Compose file

If you take a look at the `docker-compose.yml` there you will find something like this.

```yml
version: '3.8'
services:
  duel1:
    image: quakeliveserverstandards/quakelive-base
    restart: always
    ports:
      - '27962:27960/udp' # game port
      - '27962:27960/tcp' # stats port
      - '28962:28960' # rcon port
    environment:
      - SV_HOSTNAME=QL Standard Duel Server #1
      - G_PASSWORD=secret
    volumes:
      - './configs/access.txt:/home/steam/ql/baseq3/access.txt'
      - './configs/duel/server.cfg:/home/steam/ql/baseq3/server.cfg'
      - './configs/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
      - './configs/duel/minqlx-plugins:/home/steam/ql/minqlx-plugins'
      - './configs/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
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

This is a yaml file in which information is given in a certain indentation to determine the structure of the contained information. The section `services` defines two services `duel1` and `redis`. The first one is a Quake Live server. The second one is the Redis database used by minqlx plugins. While you leave the Redis service definition untouched, you can fiddle around with the Quake Live server one.

There are three parts in a Quake Live service definition that you want to adjust to meet your needs.

#### Ports

The first one is `ports` where you can determine the ports your server exposes to the public. A Docker service has two ports. An external and an internal port. Take a look at the correspoding Docker Compose file definition.

```yml
ports:
# external_port:internal_port/protocol
  - '27962:27960/udp' # game port
  - '27962:27960/tcp' # stats port
  - '28962:28960' # rcon port
```

To be able to undestand this you need to know that every service defined in a Docker Compose file runs in a Docker network. The internal port is one that is only visible inside that network. Thus if you would try and access it from outside you could not. Thus you also need to define an external port. The Docker engine will then map that external port to the internal one of the corresponding Docker service.

Using that mechanics, every Quake Live server instance runs at the same ports `27960/tcp` for the game, `27960/tcp` for the stats API and `28960` for rcon (remote console) and that never has to change. The only thing that you need to do is to map these internal ports to different external ports. `27962:27960/udp` maps the external port `27962` to the internal `27960` regarding the UPD protocol, for example. These external ports have to differ from each other and must be unique. The internal ones can all be the same.

Also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#ports).

#### Environment

In the `environment` section of the Docker Compose file you can configure Quake Live server variables like the hostname or the password.

```yml
environment:
  - SV_HOSTNAME=QL Standard Duel Server #1
  - G_PASSWORD=secret
```

The notion here is that you define variables that are specific to that specific server instance here and variables that are sprcific to a class of servers, like duel servers, in the files found in the `configs` directory. For example a server name is specific to a particular server instance while setting the time limit to 10 is specific for duel servers in general. You need to differentiate between the two and chose the correct locations for the variables.

The following variables are supported: `SV_HOSTNAME`, `G_PASSWORD`, `SV_TAGS`, `SV_MAXCLIENTS`, `SV_PRIVATECLIENTS`, `SV_PRIVATEPASSWORD`, `SV_ALLOWVOTE`, `SV_VOTEDELAY`, `SV_VOTELIMIT`, `SV_ALLOWVOTEMIDGAME`, `SV_ALLOWSPECVOTE`, `SV_VOTEFLAGS`, `SV_WARMUPREADYPERCENTAGE`, `SV_WARMUPDELAY`, `SV_WARMUPREADYDELAY`, `SV_WARMUPREADYDELAYACTION`, `G_INACTIVITY`, `G_ALLTALK`

Another thing you need to take into consideration is that variables declared in `server.cfg` will overwrite the ones given in the `environments` section. For example, you will not be able to set `SV_TAGS` when using our standard server configurations because they already set it the `server.cfg`.

### Volumes

In the `volumes` section you can compose a Quake Live server configuration by either using the provided standardized configrations or by using your own.

```yml
volumes:
# file_on_your_computer:file_inside_the_docker_service
  - './configs/access.txt:/home/steam/ql/baseq3/access.txt'
  - './configs/duel/server.cfg:/home/steam/ql/baseq3/server.cfg'
  - './configs/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
  - './configs/duel/minqlx-plugins:/home/steam/ql/minqlx-plugins'
  - './configs/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
```

Here you see a mapping from a file or directory on your computer to a location inside the Quake Live server directory which is inside the Docker service. They will appear to the starting Quake Live dedicated server as a natural part of its file system.

Also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes).

### The configs directory

#### access.txt

#### Standardized and experimental Quake Live server configurations

## Create your own Quake Live server configuration

`untouched-server.cfg`

### Factories (Game modes)

### Minqlx Plugins

### Workshop

## Contribute

### Discuss standards

### Contribute configs, factories, minqlx plugins and workshop sets

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

