# Quake Liver server related Docker images

This is a collection of ready to use Quake Live server related applications.

All of them are uploaded to the official Quake Live Server Standards [Docker Hub page](https://hub.docker.com/u/quakeliveserverstandards).

## Docker-based server framework

There is an image containing a Quake Live dedicated server for game modes `stdca`, `stdctf`, `stdduel`, `stdffa`, `stdrace` and `stdtdm` using the official Quake Live Server Standards standard configurations. These exist mainly for the reason to make the Docker Compose based configuration of the servers fail safe. For example, if the user forgets to mount a `mappool.txt` into the Docker container, there is the standard version already inside the container.

All of these game type specific images base on the `ql-server` image. It only deploys the standard `server.cfg` and can be used as the base for mixed game type servers.
