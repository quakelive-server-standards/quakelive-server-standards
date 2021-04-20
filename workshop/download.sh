#!/bin/sh

# use like this ./download.sh 691078677
docker run --rm --volume $PWD/items:/home/steam/_items quakeliveserverstandards/workshop-download $1
