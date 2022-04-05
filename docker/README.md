# Quake Liver server related Docker images

This is a collection of ready to use Quake Live server related applications.

All of them are uploaded to the official Quake Live Server Standards [Docker Hub page](https://hub.docker.com/u/quakeliveserverstandards).

## Docker images

### Docker-based server framework

There are images containing the Quake Live dedicated server for game types `stdca`, `stdctf`, `stdduel`, `stdffa`, `stdrace` and `stdtdm` using the official Quake Live Server Standards standard configurations. These exist mainly for the reason to make the Docker Compose based configuration of the servers fail safe. For example, if the user forgets to mount a `mappool.txt` into the Docker container, there is the standard version already inside of it.

All of these game type specific images are based on the `ql-server` image. This one only deploys the standard `server.cfg` and thus can be used as the base for mixed game type servers.

### QL Console

A command line interface to access the rcon and stats apis of a Quake Live dedicated server. It is based on the Quake Live Server Standards [QL Console](https://github.com/quakelive-server-standards/ql-console) project which is also linked as a Git sub module in the `apps` directory. The image is used through the file [`connect.sh`](https://github.com/quakelive-server-standards/server-standards/blob/master/_myservers/connect.sh) in the [Docker-based Quake Live server framework](https://github.com/quakelive-server-standards/server-standards/tree/master/_myservers) of this repository.

### Workshop download

## Participate

###