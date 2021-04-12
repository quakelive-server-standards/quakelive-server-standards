# Docker based Quake Live Server Framework

A Docker-based Quake Live decicated server framework with preinstalled Minqlx and full configurability. You can take these files as a base for your own Quake Live servers. This respository will be constantly updated with popular server configurations variables, recommendable workshop maps, factories and minqlx plugins. It aims to colect and provide sensible standards.

## Overview

The following minqlx plugins are installed:

https://github.com/MinoMino/minqlx-plugins

## Installation / Usage

To use these files create a fork of this repository. Then clone your fork.

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

- `access.txt`: Set server moderators, administrator or ban people. There is one file for all servers.
- `server.cfg`: This file is for general server configurations.
- `workshop.txt`: Contains all workshop items your server uses.

The next section tells you which files you should be chosing and how to adjust them.

## Configure a server

Server configuration are stored in the `configs` sub directory. There is the default Quake Live server config `default_cfg` and next to it other popular configurations. You can either chose to apply them unchanged or take them as a base for your own variants.

### server.cfg

Either way, you have to adjust the `server.cfg` by setting the following important variables: `qlx_owner`, `sv_tags`, `zmq_rcon_password`. You will find a good description of what each variable does in the file itself.

Do not set one these variables as they are set as part of the wider Docker configuration: `qlx_pluginsPath`, `qlx_database`, `qlx_redisAddress`, `qlx_redisDatabase`, `qlx_redisUnixSocket`, `qlx_redisPassword`, `sv_hostname`, `g_password`, `net_port`, `net_strict`, `zmq_rcon_port`, `g_accessFile`.

### mappool.txt



## Create your own server configuration

To create your own server configuration, copy and paste one of the existing directories and make your adjustments.

## Adjust the Dockerfile

The Dockerfile is the receipt of the base image which is used for every Quake Live dedicated server Docker container. It contains the Steam Console Client and the Quake Live dedicated server with installed minqlx extension. 

If you adjusted the Dockerfile you need to build the image again. Use the script `build-docker-image.sh` to create a Docker image by the name `ql`. The `docker-compose.yml` relies on that name. If you already instantiated Docker containers from the old image, be sure to delete and build them again.

## Contributing

