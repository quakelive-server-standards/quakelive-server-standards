# Q3 Map Converter

This Docker image is not implemented yet. If you have an idea on how to do it, take look at this [GitHub issue](https://github.com/quakelive-server-standards/quakelive-server-standards/issues/18).

## How to use this image

Create a one time Docker container from the image and pass it a Quake 3 `*.pk3` file.

```
docker run --rm --volume $PWD:/home quakeliveserverstandards/q3-map-converter quake3-map.pk3
```

You can also create a shell script `convert.sh` to execute the Docker command for running the Docker container. The `$*` part will forward any parameters given to the script to the Docker run command inside that script.

```sh
#!/bin/sh
docker run --rm --volume $PWD:/home quakeliveserverstandards/q3-map-converter $*
```

Use it like this.

```
./convert.sh quake3-map.pk3
```

You can also use the [Quake Live Server Standards server framework](https://github.com/quakelive-server-standards/quakelive-server-standards) as the base for your Quake Live servers which comes with a ready to use [`convert.sh`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/workshop/convert.sh).