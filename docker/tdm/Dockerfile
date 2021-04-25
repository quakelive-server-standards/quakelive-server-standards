# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/quakelive-base

COPY --chown=steam:steam factories/standard/duel/duel.factories /users/steam/ql/baseq3/scripts
COPY --chown=steam:steam mappools/standard/duel/mappool.txt /users/steam/ql/baseq3
COPY --chown=steam:steam minqlx-plugins/standard/duel /users/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/duel/workshop.txt /users/steam/ql/baseq3

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server - Duel"
ENV SV_TAGS "duel"
