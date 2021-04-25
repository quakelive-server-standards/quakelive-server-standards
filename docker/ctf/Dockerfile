# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/ql-server-base

COPY --chown=steam:steam factories/standard/ctf/ctf.factories /home/steam/ql/baseq3/scripts/ctf.factories
COPY --chown=steam:steam mappools/standard/ctf/mappool.txt /home/steam/ql/baseq3/mappool.txt
COPY --chown=steam:steam minqlx-plugins/standard/ctf /home/steam/ql/minqlx-plugins
COPY --chown=steam:steam workshop/standard/ctf/workshop.txt /home/steam/ql/baseq3/workshop.txt

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server - Capture the Flag"
ENV SV_TAGS "ctf"
