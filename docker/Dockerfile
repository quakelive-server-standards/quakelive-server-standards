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

COPY --chown=steam:steam ./server.cfg /home/steam/ql/baseq3

ENV QLX_PLUGINS "plugin_manager, essentials, motd, permission, docs, log, workshop"
ENV SV_HOSTNAME "Quake Live Standard Server"
ENV SV_TAGS "ca, ctf, duel, ffa, race, tdm"
ENV SV_MAPPOOLFILE "mappool.txt"
ENV SERVERSTARTUP "startRandomMap"
ENV NET_PORT 27960
ENV ZMQ_RCON_PASSWORD "ADMINPASSWORD"
ENV ZMQ_STATS_ENABLE 1
ENV ZMQ_STATS_PASSWORD "quakeliveserverstandards"
ENV G_ACCESSFILE "access.txt"
ENV SV_FPS 40
ENV SV_IDLE_EXIT 10
ENV COM_HUNKMEGS 60

# set the standard ports here which should not be overwritte by the server.cfg
# the 'ports' configuration in the Docker compose file is used to redirect these port to another port on the host system (if needed)
# the hostname and the password are given through environment variables defined in the Docker compose file
CMD set -x \
    # if ZMQ_STATS_PORT is not set then set it to NET_PORT
    && export ZMQ_STATS_PORT=${ZMQ_STATS_PORT:-$NET_PORT} \
    # if ZMQ_RCON_PORT is not set then set it to NET_PORT + 1000
    && export ZMQ_RCON_PORT=${ZMQ_RCON_PORT:-$(($NET_PORT + 1000))} \
    # start the minqlx extended quake live server
    && ./ql/run_server_x64_minqlx.sh \
    # +set qlx_plugins "plugin_manager, essentials, motd, permission, docs, log, workshop" +set sv_hostname "QL Server" +set sv_tags "ca, ctf, duel, ffa, race, tdm" +set sv_mapPoolFile "mappool.txt" +set net_port 27960 +set zmq_rcon_port 28960 +set zmq_rcon_password "ADMINPASSWORD" +set zmq_stats_enable 1 +set zmq_stats_port 27960 +set zmq_stats_password "quakeliveserverstandards" +set g_accessFile "access.txt" +set sv_fps 40 +set com_hunkMegs 60
    # only attach the parameter if the environment variable is set
    ${QLX_OWNER:+"+set qlx_owner ${QLX_OWNER}"} \
    ${QLX_PLUGINS:+"+set qlx_plugins ${QLX_PLUGINS}"} \
    ${QLX_PLUGINSPATH:+"+set qlx_pluginsPath ${QLX_PLUGINSPATH}"} \
    ${QLX_DATABASE:+"+set qlx_database ${QLX_DATABASE}"} \
    ${QLX_COMMANDPREFIX:+"+set qlx_commandPrefix ${QLX_COMMANDPREFIX}"} \
    ${QLX_REDISADDRESS:+"+set qlx_redisAddress ${QLX_REDISADDRESS}"} \
    ${QLX_REDISDATABASE:+"+set qlx_redisDatabase ${QLX_REDISDATABASE}"} \
    ${QLX_REDISUNIXSOCKET:+"+set qlx_redisUnixSocket ${QLX_REDISUNIXSOCKET}"} \
    ${QLX_REDISPASSWORD:+"+set qlx_redisPassword ${QLX_REDISPASSWORD}"} \
    ${QLX_LOGS:+"+set qlx_logs ${QLX_LOGS}"} \
    ${QLX_LOGSSIZE:+"+set qlx_logsSize ${QLX_LOGSSIZE}"} \
    ${QLX_VOTEPASS:+"+set qlx_votepass ${QLX_VOTEPASS}"} \
    ${QLX_VOTEPASSTHRESHOLD:+"+set qlx_votepassThreshold ${QLX_VOTEPASSTHRESHOLD}"} \
    ${QLX_TEAMSIZEMINIMUM:+"+set qlx_teamsizeMinimum ${QLX_TEAMSIZEMINIMUM}"} \
    ${QLX_TEAMSIZEMAXIMUM:+"+set qlx_teamsizeMaximum ${QLX_TEAMSIZEMAXIMUM}"} \
    ${QLX_MOTDSOUND:+"+set qlx_motdSound ${QLX_MOTDSOUND}"} \
    ${QLX_MOTDHEADER:+"+set qlx_motdHeader ${QLX_MOTDHEADER}"} \
    ${QLX_MOTDHEADER:+"+set qlx_motdHeader ${QLX_MOTDHEADER}"} \
    ${QLX_CHATLOGS:+"+set qlx_chatlogs ${QLX_CHATLOGS}"} \
    ${QLX_CHATLOGSSIZE:+"+set qlx_chatlogsSize ${QLX_CHATLOGSSIZE}"} \
    ${SV_HOSTNAME:+"+set sv_hostname ${SV_HOSTNAME}"} \
    ${G_PASSWORD:+"+set g_password ${G_PASSWORD}"} \
    ${SV_TAGS:+"+set sv_tags ${SV_TAGS}"} \
    ${SV_MAPPOOLFILE:+"+set sv_mapPoolFile ${SV_MAPPOOLFILE}"} \
    ${SERVERSTARTUP:+"+set serverstartup ${SERVERSTARTUP}"} \
    ${SV_MAXCLIENTS:+"+set sv_maxClients ${SV_MAXCLIENTS}"} \
    ${SV_PRIVATECLIENTS:+"+set sv_privateClients ${SV_PRIVATECLIENTS}"} \
    ${SV_PRIVATEPASSWORD:+"+set sv_privatePassword ${SV_PRIVATEPASSWORD}"} \
    ${SV_ALLOWVOTE:+"+set g_allowVote ${SV_ALLOWVOTE}"} \
    ${SV_VOTEDELAY:+"+set g_voteDelay ${SV_VOTEDELAY}"} \
    ${SV_VOTELIMIT:+"+set g_voteLimit ${SV_VOTELIMIT}"} \
    ${SV_ALLOWVOTEMIDGAME:+"+set g_allowVoteMidGame ${SV_ALLOWVOTEMIDGAME}"} \
    ${SV_ALLOWSPECVOTE:+"+set g_allowSpecVote ${SV_ALLOWSPECVOTE}"} \
    ${SV_VOTEFLAGS:+"+set g_voteFlags ${SV_VOTEFLAGS}"} \
    ${SV_WARMUPREADYPERCENTAGE:+"+set sv_warmupReadyPercentage ${SV_WARMUPREADYPERCENTAGE}"} \
    ${SV_WARMUPDELAY:+"+set g_warmupDelay ${SV_WARMUPDELAY}"} \
    ${SV_WARMUPREADYDELAY:+"+set g_warmupReadyDelay ${SV_WARMUPREADYDELAY}"} \
    ${SV_WARMUPREADYDELAYACTION:+"+set g_warmupReadyDelayAction ${SV_WARMUPREADYDELAYACTION}"} \
    ${G_INACTIVITY:+"+set g_inactivity ${G_INACTIVITY}"} \
    ${G_ALLTALK:+"+set g_alltalk ${G_ALLTALK}"} \
    ${NET_IP:+"+set net_ip ${NET_IP}"} \
    ${NET_PORT:+"+set net_port ${NET_PORT}"} \
    ${NET_STRICT:+"+set net_strict ${NET_STRICT}"} \
    ${SV_SERVERTYPE:+"+set sv_serverType ${SV_SERVERTYPE}"} \
    ${ZMQ_RCON_ENABLE:+"+set zmq_rcon_enable ${ZMQ_RCON_ENABLE}"} \
    ${ZMQ_RCON_IP:+"+set zmq_rcon_ip ${ZMQ_RCON_IP}"} \
    ${ZMQ_RCON_PORT:+"+set zmq_rcon_port ${ZMQ_RCON_PORT}"} \
    ${ZMQ_RCON_PASSWORD:+"+set zmq_rcon_password ${ZMQ_RCON_PASSWORD}"} \
    ${ZMQ_STATS_ENABLE:+"+set zmq_stats_enable ${ZMQ_STATS_ENABLE}"} \
    ${ZMQ_STATS_IP:+"+set zmq_stats_ip ${ZMQ_STATS_IP}"} \
    ${ZMQ_STATS_PORT:+"+set zmq_stats_port ${ZMQ_STATS_PORT}"} \
    ${ZMQ_STATS_PASSWORD:+"+set zmq_stats_password ${ZMQ_STATS_PASSWORD}"} \
    ${G_FLOODPROT_MAXCOUNT:+"+set g_floodprot_maxcount ${G_FLOODPROT_MAXCOUNT}"} \
    ${SV_FLOODPROTECT:+"+set sv_floodprotect ${SV_FLOODPROTECT}"} \
    ${G_FLOODPROT_DECAY:+"+set g_floodprot_decay ${G_FLOODPROT_DECAY}"} \
    ${G_ACCESSFILE:+"+set g_accessFile ${G_ACCESSFILE}"} \
    ${SV_MASTER:+"+set sv_master ${SV_MASTER}"} \
    ${SV_FPS:+"+set sv_fps ${SV_FPS}"} \
    ${SV_IDLEEXIT:+"+set sv_idleExit ${SV_IDLEEXIT}"} \
    ${COM_HUNKMEGS:+"+set com_hunkMegs ${COM_HUNKMEGS}"}