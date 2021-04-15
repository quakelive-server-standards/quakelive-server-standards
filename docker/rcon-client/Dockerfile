FROM debian:buster-slim

RUN set -x \
    && apt update \
    && apt install -y --no-install-recommends --no-install-suggests \
        python2 \
        wget \
        ca-certificates=20200601~deb10u2 \
    && wget https://bootstrap.pypa.io/pip/2.7/get-pip.py \
    && python2 get-pip.py \
    && rm get-pip.py \
    && python2 -m pip install zmq \
    && apt-get remove --purge -y \
		wget \
	&& apt-get clean autoclean \
	&& apt-get autoremove -y \
	&& rm -rf /var/lib/apt/lists/*

COPY zmq_rcon.py /root
COPY rcon.sh /root

WORKDIR /root

ENTRYPOINT [ "/root/rcon.sh" ]