# the image is based on the quake live server standards base image
FROM quakeliveserverstandards/quakelive-base

# copy the standard duel server.cfg into the image
COPY --chown=steam:steam configs/duel/server.cfg /users/steam/ql/baseq3/

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server - Duel"
ENV SV_TAGS "duel"
