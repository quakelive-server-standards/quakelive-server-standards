# the image is based on the officially recommended steamcmd image which runs on a an up to date debian
# the 'root' flavor to be able to install further dependencies
FROM cm2network/steamcmd:root

# setting the working directory as created by the cm2network/steamcmd
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

# install the Quake Live dedicated server and minqlx
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

# set the standard ports here which should not be overwritte by the server.cfg
# the 'ports' configuration in the Docker compose file is used to redirect these port to another port on the host system (if needed)
# the hostname and the password are given through environment variables defined in the Docker compose file
CMD ./ql/run_server_x64_minqlx.sh +set net_strict 1 +set net_port 27960 +set zmq_rcon_port 28960 +set zmq_stats_port 27960 +set sv_hostname ${HOSTNAME} +set g_password ${PASSWORD}