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
COPY --chown=steam:steam configs/base/server.cfg /users/steam/ql/baseq3/

# set standard values which will be overriden by environment variables with higher precedence
ENV SV_HOSTNAME "Quake Live Standard Server"
ENV SV_TAGS "ca, ctf, duel, ffa, race, tdm"

# execute the server and allow certain cvars to be set by environment variables
CMD set -x \
    # start the minqlx extended quake live server
    && ./ql/run_server_x64_minqlx.sh \
    # only attach the parameter if the environment variable is set
    ${SV_HOSTNAME:+"+set sv_hostname ${SV_HOSTNAME}"} \
    ${G_PASSWORD:+"+set g_password ${G_PASSWORD}"} \
    ${SV_TAGS:+"+set sv_tags ${SV_TAGS}"} \
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
    ${G_ALLTALK:+"+set g_alltalk ${G_ALLTALK}"}