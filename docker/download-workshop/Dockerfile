FROM cm2network/steamcmd:root

WORKDIR /home/steam
USER steam

# copy the download steam item script into the image
COPY --chown=steam:steam ./download.sh /home/steam

# execute the server and allow certain cvars to be set by environment variables
ENTRYPOINT [ "/home/steam/download.sh" ]