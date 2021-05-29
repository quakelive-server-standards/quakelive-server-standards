# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/ql-server

COPY --chown=steam:steam factories/standard/ca/ca.factories /home/steam/ql/baseq3/scripts/ca.factories
COPY --chown=steam:steam mappools/standard/ca/mappool.txt /home/steam/ql/baseq3/mappool.txt
COPY --chown=steam:steam minqlx-plugins/standard/ca /home/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/ca/workshop.txt /home/steam/ql/baseq3/workshop.txt

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server - Clan Arena"
ENV SV_TAGS "ca"
