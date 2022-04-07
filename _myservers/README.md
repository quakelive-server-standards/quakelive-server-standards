# My Servers

This is your working directory. Anything that is specific to your own servers can be put here. Do whatever you like with it. Adjust it exactly to the needs that you are having. Any file in here is just for your convenience and can be altered or deleted if not needed.

## Overview

All your servers are defined inside the `docker-compose.yml` file. Docker allows for easy server management. You do not need to install anything and everything runs out of the box. Combined with Git it is a perfect backup and recreation tool. If you want to move your Quake Live servers to another server computer, the only things you need to do is to install Git and Docker and to clone your own fork of the Quake Live Server Standards repository.

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

This framework uses Docker to compose configurations and to run any amount of server instances. It will also take care of any additional software that the Quake Live server or its rcon client needs. This [link](https://docs.docker.com/engine/install/) will provide you every information you need to install it.

## Configuring your Quake Live servers

There are six different means by which you will configure your server.

- Cvars: Config variables which represent most aspects of the game. There are cvars of a technical nature and cvars that alter the experience towards the player.
- Factories: Factories represent a set of cvars bound to a certain game type like Duel.
- Player permissions: In a file called `access.txt` you can assign roles like admin, moderator or simply ban a player.
- Map pools: You can define map pools but which by default only influence the after match voting screen.
- Workshop items: You can specify a list of free downloadable content for your server, mostly additional maps.
- minqlx plugins: There is a Quake Live server extension called minqlx which allows to alter the server's behaviour through plugins.

Before you start and try to figure out which configurations are the best, this server frameworks comes with carefully drafted standards which you can use. Every directory outside `_myservers` engage with one of the above mentioned topics. You will find a standard `server.cfg` which at defines all the technical necessities in the context of the Docker-based framework but also community determined standards. You will find lists of workshop items that are useful and ready-to-use map pools. Just take a look by yourself.

All of those directories contain a `standard` and an `evolved` directory. The first one contains community determined standards and the latter one community contributed variants, which can offer a special or a carefully evolved experience to the players.

When you compose your server configuration you can draw on those resources as a starting point. The next step then is to create your own variants. And then to contributing them back into the official Quake Live Server Standards repository to make them available for all of us.

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

Your main work horses are command line parameters in the form of Docker environment variables and the `autoexec.cfg`. But of course you can also alter the standards in the `server.cfg` which you will then hopefully contribute to the Quake Live Server Standards repository if you found that they are good. Also feel free to fiddle around with the game type specific cvars.

Apart from a lot of minqlx cvars, the `autoexec.cfg` mostly invites you to set your rcon and stats password.

If you need more than one `autoexec.cfg` file because for example you are hosting Free For All and Duel servers, just create a second one. Later on we will show you how to mount it into your Docker containers.

Feel free to adjust anything as you need it. It is your own working directory.

### factories



### access.txt

This files holds a list of users identified by their Steam Ids, giving them either the status of an admin, a moderator or of being banned. You will find an empty `access.txt` file and the first thing you might want to do is to put your own Steam Id into it, followed by a `|admin`, which would give yourself the role of an admin on your own servers.

### mappool.txt

This file contains a list of `map|factory` combinations. It defines, which maps should be available for which factory, while a factory being a collection of cvars in the context of a specific game type like Duel.

Note that this map pool is not enforced by the game. This means players can still vote for any map either calling the vote through the console or by using the voting menu which still displays all available maps. The definitions made in the `mappool.txt` will only influence the maps the game offers in the voting screen after a match.

If you want to enforce a map pool you can use the minqlx plugin `barelymissed/mapLimiter.py` which provides a variable `qlx_enforceMappool` which you need to set to `1`, preferably in your `autoexec.cfg`.

### workshop.txt

This file contains a list of Steam Workshop Item Ids the server will download on startup. The most items found in the Steam Workshop are maps. But there are also sounds for the different intermission minqlx plugins.

### minqlx-plugins

minqlx is an extension for the Quake Live server programmed by Mino which can be found on [GitHub](https://github.com/MinoMino/minqlx). He himself describes it the following way.

<cite>minqlx is a modification to the Quake Live Dedicated Server that extends Quake Live's dedicated server with extra functionality and allows scripting of server behavior through an embedded Python interpreter.</cite>

minqlx itself is extended by plugins which come in the form of Python files. This repository links all known plugin file sources as Git sub modules inside the `minqlx-plugins/_plugins` repository. If you ran the Git command `git submodule init` you will be able to browse through all the files of those repositories.

There is also a [structured overview](https://github.com/quakelive-server-standards/server-standards/blob/master/minqlx-plugins/_plugins#readme) over all known minqlx plugins sorted by topics.

There is a directory for minqlx plugins in the directoy of the Quake Live server installation. With the help of Docker you can put minqlx plugins in the form of Python files inside of it. The physical existence of these files in that directory paired with a list of the names of these plugins in the minqlx cvar `qlx_plugins` will load them when the Quake Live server starts. The cvar gives you the possibility to only select a sub set out of the physical present plugin files.

It can become tedious if you just want the plugins inside that directory to be loaded. For that reason, this framework by default provides a mechanism that when you do not state any plugin name it will simply load any plugin it finds in the `plugins` directory. But still, if you state plugin names it will only load those stated.

Apart from that cvar, there are many others and many others plugin specific which you can define in your `autoexec.cfg`.

## Composing your server configurations with Docker

The configuration files for a particular Quake Live server are assembled in the `docker-compose.yml` file. Here is an example for Duel.

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

- Game port: This is the main port which a Quake Live game client will connect to using UDP.
- Rcon port: The port the rcon API will receive commands and sends console output to using TCP. It is usually the same port as the game port.
- Stats port: The port the stats API emits its events to. It is usually the game port plus 1000.

You will define those ports in the `ports` section of the `docker-compose.yml` file.

A Docker service has two ports. An external and an internal port. Take a look at the correspoding Docker Compose file definition.

```yml
ports:
  - '27960:27960/udp' # external-port:internal-port/protocol
  - '27960:27960/tcp' # external-port:internal-port/protocol
  - '28960:28960' # external-port:internal-port
```

To be able to undestand this you need to know that every service defined in a Docker Compose file runs in a Docker network. The internal port is one that is only visible inside that network. Thus if you would try and access it from outside you could not. Thus you also need to define an external port. The Docker engine will then map that external port to the internal one of the corresponding Docker service. The definition is `external-port:internal-port/protocol`. You can also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#ports) if you want to know more.

In our case, the internal and external ports are the same. Thus, just write the port number two times, separated by a colon. 

The next step is to set up the Quake Live dedicated server instance to actually use these ports. Use the environment variables `NET_PORT`, `ZMQ_RCON_PORT` and `ZMQ_STATS_PORT` as described in the next section to do so. If you use the value of the game port for the rcon port and the value of the game port plus 1000 for the stats port, then you only have to specify the `NET_PORT` environment variable since the Docker container will set the other two accordingly.

### Environment

In the `environment` section of the Docker Compose file you can configure Quake Live server variables which internally will be appended as command line parameters to the Quake Live server executable call. Those are the right place for server instance specific settings, like the server name. Beware that you must set `NET_PORT`, `ZMQ_RCON_PORT` and `ZMQ_STATS_PORT` to match the ports specified in the ports section of the Docker Compose file.

```yml
environment:
  - NET_PORT=27960
  - SV_HOSTNAME=QL Standard Duel Server #1
  - G_PASSWORD=secret
```

The following variables are supported: 

- `COM_HUNKMEGS`: Sets the amount of memory in mega bytes reserved for the server.
- `G_PASSWORD`: Password which players have to enter if they want to access the server.
- `NET_PORT`: The game port. If you do not set it, the Docker container will set it to the default value of `27960`.
- `QLX_PLUGINS`: A list of comma separated names of minqlx plugins. If no value is given, the Docker container will create one containing all plugins it found in the `minqlx-plugins` directory thus just loading every plugin that is present.
- `SV_HOSTNAME`: The name of your server as it appears in the in-game server browser.
- `SV_MAXCLIENTS`: Number of player slots available.
- `SV_PRIVATECLIENTS`: Number of reserved player slots, requires `SV_PRIVATEPASSWORD` to be also set.
- `SV_PRIVATEPASSWORD`: Reserved player slots password.
- `SV_TAGS`: Tags that show up on the in-game server browser. This enables users to filter servers.
- `ZMQ_RCON_PORT`: The port of the rcon api. The Docker container will set it to the same value as `NET_PORT` if none was given.
- `ZMQ_STATS_PORT`: The port of the stats api. The Docker container will set it to the same value as `NET_PORT` plus 1000 if none was given.

Note that command line parameters have the lowest priority. This means, if you set the `sv_maxClients` in the `autoexec.cfg`, you will not be able to alter it through these environment variables anymore. The definition in the `autoexec.cfg` will always override that of command line parameters. This can be a source for errors and confusion.

### Volumes

In the `volumes` section you compose a Quake Live server configuration by mounting the configuration files from your computer directly into the correct place of the Quake Live server installation inside the Docker container. Here is a complete list of those mappings.

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

If you want to alter any of the files that are outside of the `_myservers` directory or if you want to create your own files, we recommend to put these into your `_myservers` directory, leaving the other directories untouched. This facilitates smooth updates coming from the official Quake Live Server Standards repository. For example, if you changed the `configs/standard/server.cfg` directly while receiving such an update, it might result in merge conflicts which you would have to resolve. This is not an especially hard thing to do but it might be inconvenient.

## Starting and managing your Quake Live servers

To start your servers, open a terminal of your operating system and cd into the directory `_myservers`. Now type `docker-compose up -d` which will start every Quake Live server that is defined in the `docker-compose.yml` plus the needed Redis database for the minqlx plugins. The parameter `-d` stands for detached and means that the servers run in the background.

To stop every Quake Live server plus the Redis database use `docker-compose stop`. To stop a specific server you can use the same command followed by the Docker Compose service name as specified in the `docker-compose.yml` file like `docker-compose stop duel1`.

If you want to see the logs of your servers use `docker-compose logs -f` while the parameter `-f` means follow and results in the log output being updated every time a new entry is added.

## Accessing your Quake Live servers with QL Console

If configured so, a Quake Live server provides two APIs, the rcon and the stats API. The first one is like the console that you also have ingame while the second one emits events regarding the games that are being played.

If you use the standard `server.cfg`, both of the APIs are enabled by default as you can read [here](https://github.com/quakelive-server-standards/server-standards/blob/master/configs/standard#readme).

There is a shell script `connect.sh` which starts a command-line client which can connect to both of these APIs at the same time. It is based on the [QL Console project](https://github.com/quakelive-server-standards/ql-console). To use it, you do not have to install anything apart from Docker. The script creates a Docker container based on this [Docker image](https://hub.docker.com/r/quakeliveserverstandards/ql-console), runs it and deletes it afterwards.

To connect to one of your servers, open a terminal and cd into the `_myservers` directory, then type `./connect.sh 198.51.100.0 --rcon-port 28960 --rcon-password quakeliveserverstandards --stats-port 27960 --stats-password quakeliveserverstandards`. Replace the IP, the ports and the passwords accordingly. The passwords are set in your `autoexec.cfg`.

If you want to connect to servers running on `localhost`, you have to use the hostname `host.docker.internal` instead. This is because `localhost` will refer to the Docker container which is running the QL Console application, but not the host machine which is running the container and your local Quake Live servers. This is working on Linux, Mac and Windows. If it does not, consider updating your Docker version. You can also refer to this Stack Overflow [thread](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) for a deep discussion about the topic.

You can also connect to either only rcon or only stats. Refer to the [QL Console documentation](https://github.com/quakelive-server-standards/ql-console#readme) for more information.

## QLStats

https://qlstats.net/panel1/servers.html
https://qlstats.net/panel2/servers.html
https://qlstats.net/panel3/servers.html
https://qlstats.net/panel4/servers.html

## Backup your server configurations with Git

## Receiving updates from the official Quake Live Server Standards repository

## Joining the Quake Live evolution

The next part, as a server administrator and Quake Live experience creator, is to join the Quake Live evolution, where we, the community, try to establish new standards to bring the game forward. Thus, if you have found a setting the players on your servers accept really well, consider to contribute it back to the original Quake Live Server Standards repository. It might be something that improves the experience for all of us and therefor it might be able to consolidate and grow our player base. It might even be worthy to be integrated into a standard.

Take a look at the root [README.md](https://github.com/quakelive-server-standards/server-standards#readme) to get an overview over how to participate and take a look into the different directory's README<span>.md</span> files to get concrete instructions.

- [Contribute to configs](https://github.com/quakelive-server-standards/server-standards/tree/master/configs#participating)
- [Contribute to Docker images](https://github.com/quakelive-server-standards/server-standards/blob/master/docker#readme)
- [Contribute to factories](https://github.com/quakelive-server-standards/server-standards/blob/master/factories#readme)
- [Contribute to map pools](https://github.com/quakelive-server-standards/server-standards/blob/master/mappools#readme)
- [Contribute to minqlx plugins](https://github.com/quakelive-server-standards/server-standards/blob/master/minqlx-plugins#readme)
- [Contribute to workshop](https://github.com/quakelive-server-standards/server-standards/blob/master/workshop#readme)