# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/ql-server

COPY --chown=steam:steam factories/standard/ffa/ffa.factories /users/steam/ql/baseq3/scripts
COPY --chown=steam:steam mappools/standard/ffa/mappool.txt /users/steam/ql/baseq3
COPY --chown=steam:steam minqlx-plugins/standard/ffa /users/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/ffa/workshop.txt /users/steam/ql/baseq3

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Server Standards - FFA"
ENV SV_TAGS "ffa std"
