#!/bin/sh

# Use like this:
# ./connect.sh 127.0.0.1 --rcon-port 28960 --rcon-password rconadmin --stats-port 27960 --stats-password statsadmin
# Further instructions: https://github.com/quakelive-server-standards/ql-console#readme

# Since this command runs in a Docker container which is its own machine
# the localhost will point to that Docker container and not to your computer
# hosting the Docker container. If you want to access a local Quake Live server which
# is running on your machine you have to use the address host.docker.internal
# instead of localhost.

docker run --rm -ti --add-host host.docker.internal:host-gateway quakeliveserverstandards/ql-console $*
