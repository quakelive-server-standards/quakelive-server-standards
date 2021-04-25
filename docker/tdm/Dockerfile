# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/ql-server-base

COPY --chown=steam:steam factories/standard/tdm/tdm.factories /home/steam/ql/baseq3/scripts/tdm.factories
COPY --chown=steam:steam mappools/standard/tdm/mappool.txt /home/steam/ql/baseq3/mappool.txt
COPY --chown=steam:steam minqlx-plugins/standard/tdm /home/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/tdm/workshop.txt /home/steam/ql/baseq3/workshop.txt

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server - Team Deathmatch"
ENV SV_TAGS "tdm"
