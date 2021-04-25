#!/bin/sh

# use like this ./rcon.sh 127.0.0.1:27960 rcon_password

# since this command runs in a Docker container which is its own machine
# the localhost will point to that Docker container and not to your computer
# hosting the Docker container. If you want to access a local Quake Live server which
# is running on your machine you have to use the address host.docker.internal
# instead of localhost.

docker run --rm -i --add-host host.docker.internal:host-gateway quakeliveserverstandards/rcon $1 $2
