# Quake Liver server related Docker images

This is a collection of ready to use Quake Live server related applications.

All of them are uploaded to the official Quake Live Server Standards [Docker Hub account](https://hub.docker.com/u/quakeliveserverstandards).

## Docker images

### Docker-based server framework

There are images containing the Quake Live dedicated server for game types [Clan Arena](https://hub.docker.com/repository/docker/quakeliveserverstandards/ca), [Capture the Flag](https://hub.docker.com/repository/docker/quakeliveserverstandards/ctf), [Duel](https://hub.docker.com/repository/docker/quakeliveserverstandards/duel), [Free For All](https://hub.docker.com/repository/docker/quakeliveserverstandards/ffa), [Race](https://hub.docker.com/repository/docker/quakeliveserverstandards/race) and [Team Deathmatch](https://hub.docker.com/repository/docker/quakeliveserverstandards/tdm) using the official Quake Live Server Standards standard configurations. These images mainly exists for the reason to make the Docker Compose based configuration of the servers fail safe. For example, if the user forgets to mount a `mappool.txt` into the Docker container, there is still the standardised version inside of it.

All of these game type specific images are based on the [ql-server](https://hub.docker.com/repository/docker/quakeliveserverstandards/ql-server) image. This one only deploys the standard `server.cfg` and thus can be used as the base for mixed game type servers.

### QL Console

A [Docker image](https://hub.docker.com/repository/docker/quakeliveserverstandards/ql-console) containing a command line interface to access the rcon and stats apis of a Quake Live dedicated server. It is based on the Quake Live Server Standards [QL Console](https://github.com/quakelive-server-standards/ql-console) project which is also linked as a Git sub module in the `apps` directory. The image is used by the file [`connect.sh`](https://github.com/quakelive-server-standards/server-standards/blob/master/_myservers/connect.sh) in the [Docker-based Quake Live server framework](https://github.com/quakelive-server-standards/server-standards/tree/master/_myservers) of this repository.

### Workshop download

A [Docker image](https://hub.docker.com/repository/docker/quakeliveserverstandards/workshop-download) which offers to possibility to download Steam Workshop items. It is used in [`download.sh`](https://github.com/quakelive-server-standards/server-standards/blob/master/workshop/download.sh) of the workshop directory to offer a convenient way to download Steam Workshop items for inspection before deploying the to a Quake Live dedicated server.

## Participating

###