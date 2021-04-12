#!/bin/bash

items=""

for item in $(cat ql/baseq3/workshop.txt | grep -v "^#"); do
  items="$items +workshop_download_item 282440  $item"
done

set -x
./steamcmd.sh +login anonymous $items +quit && mkdir ql/steamapps && mv Steam/steamapps/workshop ql/steamapps/workshop