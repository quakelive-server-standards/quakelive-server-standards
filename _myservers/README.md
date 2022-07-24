# Docker-based Quake Live dedicated server framework

Docker allows for easy server management. You do not need to install anything and everything runs out of the box. Combined with Git it is a perfect backup and recreation tool. If you want to move your Quake Live dedicated servers to another computer, the only things you need to do is to install Git and Docker and to clone your own fork of the Quake Live Server Standards repository.

## Overview

All your servers are defined inside the `docker-compose.yml` file. Additionally there is a `docker-compose.source.yml` file. It is a source for Docker service definitions. You can copy and paste content from this file into your own.

This is your working directory. Anything that is specific to your own servers can be put here. Do whatever you like with it. Adjust it exactly to the needs that you are having. Any file in here is just for your convenience and can be altered or deleted if not needed.

If you want to alter any of the files that are outside of the `_myservers` directory or create new ones, we recommend to put these into your `_myservers` directory, leaving the other directories untouched. The other directories deal with the Quake Live server standards and should be left untouched. This facilitates smooth updates coming from the official Quake Live Server Standards repository into your own. For example, if there is an update to the official `configs/standard/server.cfg` but you changed it in your repository, pulling the new data from the official repository will result in merge conflicts which you would have to resolve. This is not an especially hard thing to do but it might be inconvenient.

## Installation

You only need to install Git and Docker.

### Git

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your platform. We strongly encourage you to use the command line tool which we will also base our examples on. After installation, enter the following command.

```
git clone https://github.com/quakelive-server-standards/quakelive-server-standards.git
```

Git now created a copy or a clone of the complete official Quake Live Server Standards repository onto your computer. You can access any file and you can access any prior version of any file.

### Docker

This framework uses Docker to [compose](https://docs.docker.com/compose/) configurations and to run any amount of server instances. It will also take care of any additional software that the Quake Live server or its rcon client needs. This [link](https://docs.docker.com/engine/install/) will provide you every information you need to install it.

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

### The Docker Compose file

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
      - SV_HOSTNAME='Standard Duel Server #1'
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
      - redis:/data # uses a Docker volume by default
volumes:
redis:
```

The section `services` defines two services `duel1` and `redis`. The first one a Quake Live dedicated server. The second one is the Redis database as demanded by minqlx. In such a service definition you compose its configuration by defining ports, setting environment variables and mounting single files or whole directories into the resulting Docker container.

We will explain the `ports` and the `environment` section below.

In the `volumes` section you compose a configuration by mounting configuration files from your computer into the correct place of the Quake Live dedicated server installation inside the Docker container. The part before the colon denotes a file or directory on your computer and the one after the location inside the Docker container. Files or directories mounted like this will appear to the Quake Live server as a natural part of its file system. You can also refer to the [Docker documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes) for more information.

### Setup the ports

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

```yml
environment:
  - NET_PORT=27960
  - ZMQ_RCON_PORT=27960 # can be omitted if the same as NET_PORT
  - ZMQ_STATS_PORT=28960 # can be omitted if the same as NET_PORT + 1000
```

### Setting cvars

A cvar is a configuration variable. It sets up certain kinds of behaviours of the Quake Live dedicated server. There are four different locations to put cvars into.

- Command line parameters
- `server.cfg`
- `autoexec.cfg`
- Inside a `*.factories` file

In this order, the command line parameter has the lowest priority while the factories file has the highest, which means that a cvar defined in a factories file will override any other definition of the same cvar in any other of the lower prioritized locations.

This Docker-based server framework uses the different locations for different purposes.

- Command line parameter: Server instance specific cvars like the name of the server
- `server.cfg`: Technical cvars like the location of the `mappool.txt` file
- `autoexec.cfg`: Cvars specific to to all or a group of your servers
- `*.factories`: Cvars specific to a game mode like the damage of a weapon

Your main work horses are command line parameters and your `_myservers/autoexec.cfg`.

#### Command line parameters

In the `environment` section of the Docker Compose file you can configure Quake Live server variables which internally will be appended as command line parameters to the Quake Live server executable call. Those are the right place for server instance specific settings, like the server name. Beware that you must set `NET_PORT`, `ZMQ_RCON_PORT` and `ZMQ_STATS_PORT` to match the ports specified in the ports section of the Docker Compose file.

```yml
environment:
  - NET_PORT=27960
  - SV_HOSTNAME='Standard Duel Server #1'
  - G_PASSWORD=secret
```

The following variables are supported: 

- `COM_HUNKMEGS`: Sets the amount of memory in mega bytes reserved for the server.
- `G_PASSWORD`: Password which players have to enter if they want to access the server.
- `NET_PORT`: The game port. If you do not set it, the Docker container will set it to the default value of `27960`.
- `QLX_PLUGINS`: A list of comma separated names of minqlx plugin file names without their `.py` extension. If no value is given, the Docker container will create one containing all plugins it finds in the `minqlx-plugins` directory thus loading every plugin that is present.
- `SERVERSTARTUP`: Can be used to setup the map which the server should run after startup. Its default value is `startRandomMap`. Set a specific map by using a value like `map bloodrun stdduel`.
- `SV_HOSTNAME`: The name of your server as it appears in the in-game server browser.
- `SV_MAXCLIENTS`: Number of player slots available.
- `SV_PRIVATECLIENTS`: Number of reserved player slots, requires `SV_PRIVATEPASSWORD` to be also set.
- `SV_PRIVATEPASSWORD`: Reserved player slots password.
- `SV_TAGS`: Tags that show up on the in-game server browser. This enables users to filter servers.
- `ZMQ_RCON_PORT`: The port of the rcon api. The Docker container will set it to the same value as `NET_PORT` if none was given.
- `ZMQ_STATS_PORT`: The port of the stats api. The Docker container will set it to the same value as `NET_PORT` plus 1000 if none was given.

Note that command line parameters have the lowest priority. This means, if you set the `sv_maxClients` in the `autoexec.cfg`, you will not be able to alter it through these environment variables anymore. The definition in the `autoexec.cfg` will always override that of command line parameters. This can be a source for errors and confusion.

#### autoexec.cfg

The `autoexec.cfg` contains cvar values, each on one line. It overwrites values which were set as command line parameter and in the `server.cfg`. Its values will be overwritten by definitions made in factory files.

```
set g_allowVote "1"
set g_voteDelay "0"
set g_voteLimit "0"
set g_allowVoteMidGame "0"
```

The provided [file](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/autoexec.cfg) in your `_myservers` directory contains the the cvars of the original id Software `server.cfg` which were not standardised through Quake Live Sever Standards. Use it as a basis for your own one. You can mount it into the Docker container by specifying it in the `volumes` section of your Docker service definition.

```yml
volumes:
  - './autoexec.cfg:/home/steam/ql/baseq3/autoexec.cfg'
```

The setting that you want to do at least is to set the `zmq_rcon_password` and `zmq_stats_password` cvars. The default values for both of them is `quakeliveserverstandards`. You can also leave it like this for the stats API to enable other developers to pickup the stats events from your servers and to process them in their [Quake Live app](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/apps).

If you need more than one `autoexec.cfg` file because for example you are hosting Free For All and Duel servers, just create a second one and mount it into the Docker services as needed. In general, feel free to adjust anything in the `_myservers` directory as you need it. It is yours.

### Player permissions

A file named [`access.txt`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/access.txt) holds a list of users identified by their Steam Ids, giving them either the status of an admin, a moderator or of being banned. 

The first thing you might want to do is to put your own Steam Id into it, followed by a `|admin`, which would give yourself the role of an admin on your own servers.

Mount it into the Docker container by using the `volumes` section of a Docker service definition.

```yml
volumes:
  - './access.txt:/home/steam/ql/baseq3/access.txt'
```

### Map pools

You can define a map pool inside a `mappool.txt` file. It defines, which maps should be available for which game type. Beware that a map pool is not enforced by the game. Players can still vote for any map either calling the vote through the console or by using the voting menu which still displays all available maps. The definitions made will only influence the maps offered in the voting screen after a match.

If you want to enforce a map pool, you can use the minqlx plugin [`mino/essentials.py`](https://github.com/MinoMino/minqlx-plugins/blob/master/essentials.py) which provides a variable `qlx_enforceMappool` which you need to set to `1`, preferably in your `_myservers/autoexec.cfg`.

Before creating your own map pools, this repository offers to you carefully crafted [standard](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/mappools/standard) map pools and also [evolved](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/mappools/evolved) ones that bring the Quake Live experience forward. Choose one and mount it into you Docker container in the `volumes` section of a Docker service definition. Replace the path on the left side of the colon with one pointing to another map pool file.

```yml
volumes:
  - '../mappools/standard/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
```

In the next step, if you want to improve the Quake Live experience for the players of your servers, you might want to create your own map pools. This repository helps you in doing so by explaining to you [how to create them](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/mappools#readme).

Once you play tested the new maps and the feedback from your players are positive, you are ready to [contribute](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/mappools#evolve-quake-live) your map pool back to the official Quake Live Server Standards repository.

### Workshop items

The [Steam Workshop](https://steamcommunity.com/app/282440/workshop/) is the source for free downloadable content for the Quake Live dedicated server. The most items found in there are [maps](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop#workshop-item-lists), but also sounds for the different [intermission minqlx plugins](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop/evolved/minqlx).

The Steam Workshop item id's are put into a file called `workshop.txt` and which is mounted into the Docker container. Replace the path on the left side of the colon with any other.

```yml
volumes:
  - '../workshop/standard/duel/workshop.txt:/home/steam/ql/baseq3/workshop.txt'
```

There are predefined files which are ready to use which you can choose from before creating your own list. Take a look into the carefully drafted [standard](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop/standard) files which there is one for every game type but also take a look into the [evolved](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop/evolved) ones.

Once you are ready to search the Steam Workshop by yourself, create a `workshop.txt` file inside your `_myservers` directory, fill it with id's and mount it into the container. [Here](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop) you will find Workshop item lists, a script do download an item onto your harddrive and other useful things.

When your choice of Workshop items was a success because your players love it, [contribute](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop#evolve-quake-live) it back to the Quake Live Server Standards repository.

### Factories

A factory contains sets of cvars which are applied for certain game types. It is a good place to set up voting warmup ready percentage, warmup delay and so on, anything that is game type specific.

Factories are defined in a text file `*.factories`. Inside of is a JSON string. This JSON either contains multiple factory definitions or just one. You can create as many factories files as you like, they are put inside a `scripts` folder inside the Quake Live dedicated server installation.

Before you create your own factory, take a look at the carefully drafted [standard](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories/standard) factories for every game type and also the [evolved](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories/evolved) ones, which offer experiences apart the vanilla ones that were designed by id Software. Add factory files into the Quake Live dedicated server installation by mounting them in the `volumes` sesction in your `docker-compose.yml`. Replace the path before the colon with a path pointing to any factories file. If you want to add multiple files, you can mount as many files as you need.

```yml
volumes:
  - '../factories/standard/ffa/ffa.factories:/home/steam/ql/baseq3/scripts/ffa.factories'
      - '../factories/standard/duel/duel.factories:/home/steam/ql/baseq3/scripts/duel.factories'
```

Once you feel the need to evolve a game type, you will create your own [factory](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories). Put your `*.factories` file inside your `_myservers` directory first. Test it a while with the players of your servers and then [contribute](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/factories#evolve-quake-live) it back to the official Quake Live Server Standards repository.

### minqlx plugins

minqlx is a Quake Live dedicated server extension which enables to change the behaviour of the Quake Live dedicated server through plugins. Inside of a Quake Live dedicated server Docker container, there is a directory `/home/steam/ql/minqlx-plugins` where minqlx plugin files are put into. When the Quake Live dedicated server starts up, it will load every plugin that was mentioned in the `qlx_plugins` cvar. If a mentioned plugin was not found, an error message will be printed to the log. You can see the logs by opening a terminal, changing into the `_myservers` directory and type in `docker-compose logs -f`.

Before you create your own list of minqlx plugins this repository offers to you carfully crafted [standard lists](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins/standard) for every game type and also [evolved](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins/evolved) ones, which deviate from the standard. Choose a directory with minqlx plugin files and mount it into your Docker container. It is done in the `volumes` section of a Docker service specification inside the `docker-compose.yml` file. Replace the path an the left side of the colon with any other path to a directory containing minqlx plugin files.

```yml
volumes:
  - '../minqlx-plugins/standard/duel:/home/steam/ql/minqlx-plugins'
```

You do not need to specify the list of plugins in the `qlx_plugins` cvar, because the Docker container is configured in a way, that it will load every minqlx plugin it finds in the corresponding directory of the Quake Live dedicated server installation. It creates that list and passes it as a command line parameter.

In the next step, if you want to evolve the Quake Live experience for the players of your servers, you will want to add new minqlx plugins to your server. This repository helps you in doing so by providing an [overview](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins/_plugins#readme) over all known minqlx plugins, sorted by categories. It also contains the [Git repositories](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins/_plugins) which contain all these known minqlx plugins as Git sub modules. If you cannot see them, you need to run the Git command `git submodule init`.

Start by adding your list of minqlx plugins to the `_myservers/autoexec.cfg`. The definition will overwrite the list of all installed minqlx plugins which is created by the Docker container.

```
set qlx_plugins "balance, docs, essentials, log, permission, plugin_manager, commands, listmaps"
```

If you have tested your additional minqlx plugins and think, they are improving the Quake Live experience, you are ready to [contribute](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins#evolve-quake-live) it back to the Quake Live Server Standards repository.

## Starting and maintaining your Quake Live servers

To start your servers, open a terminal of your operating system and cd into the directory `_myservers`. Now type `docker-compose up -d` which will start every Quake Live server that is defined in the `docker-compose.yml` plus the needed Redis database for the minqlx plugins. The parameter `-d` stands for detached and means that the servers run in the background.

To stop every Quake Live server plus the Redis database use `docker-compose stop`. To stop a specific server you can use the same command followed by the Docker Compose service name as specified in the `docker-compose.yml` file like `docker-compose stop duel1`.

If you want to see the logs of your servers use `docker-compose logs -f` while the parameter `-f` means follow and results in the log output being updated every time a new entry is added.

## Backup your server configurations with Git

If you want to backup your Quake Live server configuration you can use Git to do so. Git is a versioning system which can track all the changes you have made over the time. Such a set of changes is called a commit. A commit can contain changes to the content of files, but also state new and deleted files. A Git repository basically is a chain of commits. That allows you to go back in time by restoring a certain version of your repository.

Before you can start to use Git as a backup solution, you have to work through these [first-time setup steps](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

Once you have set up everything you are ready to create your first commit. If you installed the command line tool, you can follow the upcoming instructions. Open a terminal and change into the directory containing your clone of the Quake Live Server Standards repository. At first we look at the changes that have been made. Enter the following command.

```
git status
```

This will give you an overview of the files that have changed, have been removed or are new. The next step is to pick the files that you want to be part of your commit. You can either add everything that has changed.

```
git add -A
```

Or just a specific file.

```
git add _myservers/autoexec.cfg
```

Once you composed the changes for your commit you are ready to create that commit.

```
git commit -m "Enter a descriptive commit message. It will help you later on."
```

Congratulations, you have created your first commit.

The next step is to store your own version of the Quake Live Server Standards repository to a remote location that you own. Take a look at [BitBucket](https://bitbucket.org) or [GitLab](https://about.gitlab.com). Both of them have free plans and your repository can only be seen by you. Once you have created that remote repository location, it is time to copy your repository there.

Before you can do that, you have to add this new remote location to the list of remote locations of your local Git repository. Let us find out which are already there.

```
> git remote -v
origin	https://github.com/quakelive-server-standards/quakelive-server-standards.git (fetch)
origin	https://github.com/quakelive-server-standards/quakelive-server-standards.git (push)
```

As you can see, there is already a remote location with the name `origin`. It points to the official Quake Live Server Standards repository.

Since you want your own remote location to be named `origin` and since you will still need to work with the Quake Live Server Standards repository in the future, rename it.

```
git remote rename origin upstream
```

Now it is called `upstream` which is a common name for a remote location which you are basing your own work on.

Now that the name `origin` is available, add your own remote location under that name. To do so you will need the Git URL of your remote Git repository. Here are guides for [BitBucket](https://support.atlassian.com/bitbucket-cloud/docs/clone-a-repository/) and [GitLab](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#clone-a-repository) on how to obtain it.

```
git remote add origin <your-remote-location-url>
```

Now you are ready to create your backup by pushing your new commit to your own remote location.

```
git push origin main
```

It might be the case, that instead of `main` you have to use `master`, which was the standard before.

## Receiving updates from the official Quake Live Server Standards repository

If you followed the instructions from [above](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#backup-your-server-configurations-with-git) you have two remote locations of your Git repository, `origin` and `upstream`, while `upstream` is the one pointing to the official Quake Live Server Standards GitHub repository.

You can receive an update from the `upstream` remote location by opening a terminal, changing the directory to your local clone of the official Quake Live Server Standards repository and by typing.

```
git pull upstream master
```

It will download the changes and integrate them into your own copy of the Quake Live Server Standards repository.

If you followed the advice from the beginning and you did not alter any files outside of the `_myservers` directory, then the update should pass smoothly. If you did alter files then you might run into merge conflicts which you will need to resolve manually.

## Accessing your Quake Live servers remotely with QL Console

If configured so, a Quake Live server provides two APIs, the rcon and the stats API. The first one is like the console that you also have ingame while the second one emits events regarding the games that are being played.

If you use the standard `server.cfg`, both of the APIs are enabled by default as you can read [here](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/configs/standard#readme).

There is a shell script `connect.sh` which starts a command-line client which can connect to both of these APIs at the same time. It is based on the [QL Console project](https://github.com/quakelive-server-standards/ql-console). To use it, you do not have to install anything apart from Docker. The script creates a Docker container based on this [Docker image](https://hub.docker.com/r/quakeliveserverstandards/ql-console), runs it and deletes it afterwards.

To connect to one of your servers, open a terminal and cd into the `_myservers` directory and the following command. Replace the IP, the ports and the passwords accordingly. The passwords are set in your `autoexec.cfg`.

```
./connect.sh 198.51.100.0 --rcon-port 28960 --rcon-password quakeliveserverstandards --stats-port 27960 --stats-password quakeliveserverstandards
```

If you want to connect to servers running on `localhost`, you have to use the hostname `host.docker.internal` instead. This is because `localhost` will refer to the Docker container which is running the QL Console application, but not the host machine which is running the container and your local Quake Live servers. This is working on Linux, Mac and Windows. If it does not, consider updating your Docker version. You can also refer to this Stack Overflow [thread](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach) for a deep discussion about the topic.

You can also connect to either only rcon or only stats. Refer to the [QL Console documentation](https://github.com/quakelive-server-standards/ql-console#readme) for more information.

## QLStats integration

[QLStats](https://qlstats.net) is a website which tracks played matches and most notably calculates [elo ratings](https://en.wikipedia.org/wiki/Elo_rating_system) for every player separately for every game type.

You can connect your servers to QLStats by registering them in one of the four so called [panels](https://qlstats.net/panel1/servers.html). To do so, you have to have your stats API enabled, which this server framework by [default](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs/standard#zmq-stats) does. Additionally, you need your stats API password, which is `quakeliveserverstandards` if you did not set it in your `autoexec.cfg`.

A panel can receive QL stats events from up to 340 Quake Live dedicated servers, while it is ony possible to add new server owners to a panel if there are not more than 250 servers already registered.

Most of the players like to enter the `!elos` command into the console of the Quake Live client. It will print the elo ratings of every player which is on the server. This command is provided by the minqlx plugin [`balance.py`](https://github.com/MinoMino/minqlx-plugins/blob/master/balance.py) which is a part of the [standard minqlx lists](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/minqlx-plugins/standard/common#balance) of every game type.

## Joining the Quake Live evolution

The next part, as a server administrator and Quake Live experience creator, is to join the Quake Live evolution, where we, the community, try to establish new standards to bring the game forward. Thus, if you have found a setting the players on your servers accept really well, consider to contribute it back to the original Quake Live Server Standards repository. It might be something that improves the experience for all of us and therefor it might be able to consolidate and grow our player base. It might even be worthy to be integrated into a standard.

Take a look at the root [README.md](https://github.com/quakelive-server-standards/quakelive-server-standards#readme) to get an overview over how to evolve Quake Live and take a look into the different directory's README<span>.md</span> files to get concrete instructions.

- [Contribute to configs](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs#evolve-quake-live)
- [Contribute to Docker images](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/docker#readme)
- [Contribute to factories](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/factories#readme)
- [Contribute to map pools](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/mappools#readme)
- [Contribute to minqlx plugins](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/minqlx-plugins#readme)
- [Contribute to workshop](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/workshop#readme)

## The original Quake Live dedicated server documentation

[Here](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/_myservers/server_readme.txt) you will find the original documentation created by id Software.