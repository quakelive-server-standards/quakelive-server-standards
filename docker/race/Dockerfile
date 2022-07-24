# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/ql-server

COPY --chown=steam:steam factories/standard/race/race.factories /home/steam/ql/baseq3/scripts/race.factories
COPY --chown=steam:steam mappools/standard/race/mappool.txt /home/steam/ql/baseq3/mappool.txt
COPY --chown=steam:steam minqlx-plugins/standard/race /home/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/race/workshop.txt /home/steam/ql/baseq3/workshop.txt

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Server Standards - Race"
ENV SV_TAGS "race std"
