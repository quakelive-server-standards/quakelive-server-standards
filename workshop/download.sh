#!/bin/sh

# use like this ./download.sh 691078677
docker run --rm --volume items:/home/steam/Steam/steamapps/workshop/content/282440 quakeliveserverstandards/download-workshop $1
