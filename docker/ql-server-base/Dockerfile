# the image is based on the officially recommended steamcmd image which runs on debian
# the 'root' flavor is used to be able to install further dependencies
FROM cm2network/steamcmd:root

# setting the working directory as created by the cm2network/steamcmd base image
WORKDIR /home/steam

# install further dependencies for minqlx
# https://github.com/MinoMino/minqlx#installation
RUN set -x \
    && apt-get update \
    && apt-get -y install python3 python3-dev wget git build-essential \
    && wget https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm get-pip.py

# change the user
USER steam

# install the Quake Live dedicated server, minqlx and the minqlx plugin requirements
# https://github.com/MinoMino/minqlx-plugins#minqlx-plugins
RUN set -x \
    && ./steamcmd/steamcmd.sh +login anonymous +app_update 349090 +quit \
    && ln -s "Steam/steamapps/common/Quake Live Dedicated Server/" ql \
    && git clone https://github.com/MinoMino/minqlx.git \
    && cd minqlx \
    && make \
    && cd ~ \
    && cp minqlx/bin/* ql \
    && cd ql \
    && git clone https://github.com/MinoMino/minqlx-plugins.git \
    && python3 -m pip install -r minqlx-plugins/requirements.txt

# copy the standard server.cfg into the image
COPY --chown=steam:steam configs/standard/server.cfg /users/steam/ql/baseq3/

# execute the server and allow certain cvars to be set by environment variables
CMD set -x \
    && export NET_PORT=${NET_PORT:-27690} \
    # if ZMQ_STATS_PORT is not set then set it to NET_PORT
    && export ZMQ_STATS_PORT=${ZMQ_STATS_PORT:-$NET_PORT} \
    # if ZMQ_RCON_PORT is not set then set it to NET_PORT + 1000
    && export ZMQ_RCON_PORT=${ZMQ_RCON_PORT:-$(($NET_PORT + 1000))} \
    # if SERVERSTARTUP is not set we need to set it because otherwise the server will
    # not function properly
    && export SERVERSTARTUP=${SERVERSTARTUP:-startRandomMap} \
    # start the minqlx extended quake live server
    && ./ql/run_server_x64_minqlx.sh \
    # only attach the parameter if the environment variable is set
    ${NET_PORT:++set net_port ${NET_PORT}} \
    ${ZMQ_RCON_PORT:++set zmq_rcon_port ${ZMQ_RCON_PORT}} \
    ${ZMQ_STATS_PORT:++set zmq_stats_port ${ZMQ_STATS_PORT}} \
    ${SV_HOSTNAME:++set sv_hostname ${SV_HOSTNAME}} \
    ${SV_TAGS:++set sv_tags ${SV_TAGS}} \
    ${SERVERSTARTUP:++set serverstartup ${SERVERSTARTUP}} \
    ${G_PASSWORD:++set g_password ${G_PASSWORD}} \
    ${SV_MAXCLIENTS:++set sv_maxClients ${SV_MAXCLIENTS}} \
    ${SV_PRIVATECLIENTS:++set sv_privateClients ${SV_PRIVATECLIENTS}} \
    ${SV_PRIVATEPASSWORD:++set sv_privatePassword ${SV_PRIVATEPASSWORD}} \
    ${G_ALLTALK:++set g_alltalk ${G_ALLTALK}} \
    ${COM_HUNKMEGS:++set com_hunkMegs ${COM_HUNKMEGS}}