FROM ubuntu:20.10

RUN set -x \
    && apt update \
    && apt install -y --no-install-recommends --no-install-suggests \
        nodejs \
        git \
        ca-certificates \
    && git clone https://github.com/quakelive-server-standards/ql-console.git \
    && apt-get remove --purge -y \
        git \
        ca-certificates \
	&& apt-get clean autoclean \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /ql-console

ENTRYPOINT [ "/ql-console/connect.sh" ]
