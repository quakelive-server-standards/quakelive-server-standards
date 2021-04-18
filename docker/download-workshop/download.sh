#!/bin/sh

# use like this ./download.sh 691078677

set -x
/home/steam/steamcmd/steamcmd.sh +login anonymous +workshop_download_item 282440 $1 validate +quit