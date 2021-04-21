#!/bin/sh

# use like this ./download.sh 691078677
docker run --rm --volume $PWD/_items:/home/steam/items quakeliveserverstandards/workshop-download $1
