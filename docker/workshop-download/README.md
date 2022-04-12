# Steam workshop item downloader

This docker image uses the Steam Console Client to download a workshop item. It is used by the [Quake Live Server Standards Docker-based server framework](https://github.com/quakelive-server-standards/quakelive-server-standards) to offer its users a convenient way to work with the Steam Workshop.

## Usage

You can create a one time Docker container which downloads the steam item given through a command line parameter. Also, mount a directory into the location `/home/steam/items` inside the Docker container. This is the place where the downloaded Steam Workshop items will be moved to.

```
docker run --rm --volume $PWD:/home/steam/items quakeliveserverstandards/workshop-download 691078677
```

You can also put that call inside a shell script `download.sh`. It will mount the current directory into the container so that downloaded Steam Workshop items will appear outside in you current directory. The `$*` part will forward any parameters given to the script to the Docker run command inside that script.

```sh
#!/bin/sh
docker run --rm --volume $PWD/_items:/home/steam/items quakeliveserverstandards/workshop-download $1
```

Use it like this.

```
./download.sh 691078677
```

A third option is to use the [Quake Live Server Standards server framework](https://github.com/quakelive-server-standards/quakelive-server-standards) which comes with Steam Workshop item lists, the above mentioned shell script and a way to easily manage arbitrary many Quake Live dedicated servers.