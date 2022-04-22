#!/bin/sh

# use like this ./convert.sh q3-map.pk3
docker run --rm --volume $PWD:/ quakeliveserverstandards/q3-map-converter $1
