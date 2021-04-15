#!/bin/sh

# use like this ./rcon 127.0.0.1:27960 rcon_password
python2 zmq_rcon.py --host=tcp://$1 --password=$2