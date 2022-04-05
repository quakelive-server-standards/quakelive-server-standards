# QL Console

This Docker image contains a command line client for accessing the rcon and stats apis of a Quake Live dedicated server. The client is based on [this](https://github.com/quakelive-server-standards/ql-console) open source GitHub project. This Docker image is used inside the [Quake Live Server Standards Docker-based server framework](https://github.com/quakelive-server-standards/server-standards). You can consider using it as the base for your own servers. It not only comes with easy server management and configuration, but also with community-driven Quake Live server standards.

## How to use this image

Create a one time Docker container from the image and pass the parameters for the [`connect.sh`](https://github.com/quakelive-server-standards/ql-console/blob/master/connect.sh) which the container will execute.

```
docker run --rm -ti quakeliveserverstandards/ql-console 198.51.100.0 --rcon-port 28960 --rcon-password rconadmin --stats-port 27960 --stats-password statsadmin
```

If you want to access a Quake Live server which runs on the same machine you need to use the IP address of your host machine. You cannot use `localhost` or `127.0.0.1` because those refer to the Docker container running the QL Console itself but not to your local machine which hosts that Docker container. If you find it tedious to enter the IP address of your computer you can use the Docker provided `host.docker.internal` hostname. This will work out without additional changes for Mac and Windows. For Linux you need to add the `--add-host host.docker.internal:host-gateway` option. 
```
docker run --rm -ti --add-host host.docker.internal:host-gateway quakeliveserverstandards/ql-console host.docker.internal --rcon-port 28960 --rcon-password rconadmin --stats-port 27960 --stats-password statsadmin
```

For more information on that topic, refer to this Stack Overflow [thread](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach).

You can also create a shell script `connect.sh` to execute the Docker command for running the Docker container. The `$*` part will forward any parameters given to the script to the Docker run command inside that script.

```sh
#!/bin/sh
docker run --rm -ti --add-host host.docker.internal:host-gateway quakeliveserverstandards/ql-console $*
```

Use it like this.

```
./connect.sh host.docker.internal --rcon-port 28960 --rcon-password rconadmin --stats-port 27960 --stats-password statsadmin
```

You can also use the [Quake Live Server Standards server framework](https://github.com/quakelive-server-standards/server-standards) as the base for your Quake Live servers which comes with a ready to use [`connect.sh`](https://github.com/quakelive-server-standards/server-standards/blob/master/_myservers/connect.sh).