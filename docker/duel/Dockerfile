# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/ql-server

COPY --chown=steam:steam factories/standard/duel/duel.factories /home/steam/ql/baseq3/scripts/duel.factories
COPY --chown=steam:steam mappools/standard/duel/mappool.txt /home/steam/ql/baseq3/mappool.txt
COPY --chown=steam:steam minqlx-plugins/standard/duel /home/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/duel/workshop.txt /home/steam/ql/baseq3/workshop.txt

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server - Duel"
ENV SV_TAGS "duel"
