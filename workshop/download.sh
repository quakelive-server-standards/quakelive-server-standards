#!/bin/sh

# use like this ./download.sh 691078677
docker run --rm --volume $PWD/items:/home/steam/items quakeliveserverstandards/download-workshop $1
