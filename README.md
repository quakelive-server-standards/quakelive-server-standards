# Docker-based Quake Live Server Framework

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

## Installation

You will need to install Git, clone the Quake Live Server Standards repository and install Docker.

### Git

At first you need to create your own Git repository. You can do that either by creating a fork on GitHub or by directly cloning this repository. If you do not have experience in working with Git use a GitHub fork.

#### Using a GitHub fork

To be able to fork you need to have to log in to your GitHub account. If you do not have one you need to register first. The free plan lets you create as many publically visible repositories as you like.

To create a fork you click on the "Fork" button on the top right corner. This will create new GitHub repository in one of your namespaces.

Now clone your new repository. Cloning a repository can either be done with the official [command line tool](https://git-scm.com/downloads) or one of the many [graphical user interfaces](https://git-scm.com/downloads/guis). In this guide we will refer to the command line tool.

On the command line type `git clone https://github.com/<your-github-name>/<your-repository-name>.git`. You can copy and paste the clone link from the GitHub website. If you do not know how to do this use these [instructions](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

Your repository now resides on two locations. On your harddrive and on GitHub. The GitHub location is known to your local version as the `origin`. It is the main location your repository resides in and you can create arbitrary many clones from it. If you change something in your local version you will push these changes to the origin. If something changed in the origin you will merge theses changes into your local version. That way, arbitrary many people can work together.

To be able to stay up to date regarding the latest server trends, you need to add the official Quake Live Server Standards Git repository as an additional location next to `origin`. On the command line type `git remote add upstream https://github.com/quakelive-server-standards/quakelive-server-framework.git`. Every time there is something new you now can pull these changes by typing `git pull upstream origin`.

The last step is to clone all of the Git sub modules which are other Git repositories that were integrated into that one. One the command line type `git submodule init`.

#### Not using a GitHub fork

If you do not have a GitHub account or if you do not want your repository to be publicly available you can also directly clone this repository with `git clone https://github.com/quakelive-server-standards/quakelive-server-framework.git`.

After cloning, the official Quake Live Server Standards repository will be listed as the `origin` location. You will want to replace that with a repository location of your own. Since you also want keep the official location you start by renaming it from `origin` to `upstream` by typing `git remote rename origin upstream` into the command line.

Now you can add your own Git repository location as the `origin` by typing `git remote add origin <url-to-your-git-repository>`.

The last step is to clone the sub modules with `git submodule init`.

### Docker

This framework uses Docker to compose configurations and to run any amount of server instances. It will also take care of any additional software that the Quake Live server or its rcon client needs. This link https://docs.docker.com/engine/install/ will provide you every information on how to install it.

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

## Starting and managing your Quake Live servers

To start your servers, start a terminal of your operating system and cd into the root directory of this framework. Now type `docker-compose up -d` which will start every Quake Live server that is defined in the `docker-compose.yml` plus the needed Redis database for the minqlx plugins. The parameter `-d` stands for detached and means that the servers run in the background.

To stop every Quake Live server plus the Redis database use `docker-compose stop`. To stop a specific server you can use the same command followed by the Docker Compose service name as specified in the `docker-compose.yml` file like this `docker-compose stop duel1`.

If you want to see the logs of your servers use `docker-compose logs -f` while the parameter `-f` means follow and results in the log output being updated every time a new entry is added.

## Maintaining your Quake Live servers via rcon

To maintain a server you use `./rcon.sh 127.0.0.1:27960 rconpassword` to start an rcon terminal into one of your running servers. Replace the ip address `127.0.0.1` with the one pointing to your Quake Live servers, chose the corresponding port and set the password that you have configured.

## Configuring your Quake Live servers

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
      - './configs/standard/duel/server.cfg:/home/steam/ql/baseq3/server.cfg'
      - './configs/standard/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
      - './configs/standard/duel/minqlx-plugins:/home/steam/ql/minqlx-plugins'
      - './configs/standard/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
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
  - './configs/standard/duel/server.cfg:/home/steam/ql/baseq3/server.cfg'
  - './configs/standard/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
  - './configs/standard/duel/minqlx-plugins:/home/steam/ql/minqlx-plugins'
  - './configs/standard/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
```

Here you see a mapping from a file or directory on your computer to a location inside the Quake Live server directory which is inside the Docker service. They will appear to the starting Quake Live dedicated server as a natural part of its file system.

Also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes).

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