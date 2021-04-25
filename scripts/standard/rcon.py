#!/usr/bin/env python

import sys
import time
import struct
import argparse
import uuid
import threading
import Queue

import logging
logging.basicConfig( format='%(message)s', level=logging.DEBUG )

import zmq

import unittest

def _readSocketEvent( msg ):
    # NOTE: little endian - hopefully that's not platform specific?
    event_id = struct.unpack( '<H', msg[:2] )[0]
    # NOTE: is it possible I would get a bitfield?
    event_names = {
        zmq.EVENT_ACCEPTED : 'EVENT_ACCEPTED',
        zmq.EVENT_ACCEPT_FAILED : 'EVENT_ACCEPT_FAILED',
        zmq.EVENT_BIND_FAILED : 'EVENT_BIND_FAILED',
        zmq.EVENT_CLOSED : 'EVENT_CLOSED',
        zmq.EVENT_CLOSE_FAILED : 'EVENT_CLOSE_FAILED',
        zmq.EVENT_CONNECTED : 'EVENT_CONNECTED',
        zmq.EVENT_CONNECT_DELAYED : 'EVENT_CONNECT_DELAYED',
        zmq.EVENT_CONNECT_RETRIED : 'EVENT_CONNECT_RETRIED',
        zmq.EVENT_DISCONNECTED : 'EVENT_DISCONNECTED',
        zmq.EVENT_LISTENING : 'EVENT_LISTENING',
        zmq.EVENT_MONITOR_STOPPED : 'EVENT_MONITOR_STOPPED',
    }
    event_name = event_names[ event_id ] if event_names.has_key( event_id ) else '%d' % event_id
    event_value = struct.unpack( '<I', msg[2:] )[0]
    return ( event_id, event_name, event_value )

def _checkMonitor( monitor ):
    try:
        event_monitor = monitor.recv( zmq.NOBLOCK )
    except zmq.Again:
        #logging.debug( 'again' )
        return

    ( event_id, event_name, event_value ) = _readSocketEvent( event_monitor )
    event_monitor_endpoint = monitor.recv( zmq.NOBLOCK )
    logging.info( 'monitor: %s %d endpoint %s' % ( event_name, event_value, event_monitor_endpoint ) )
    return ( event_id, event_value )

# start a thread, read a queue that will read input lines
def setupInputQueue():
    def waitStdin( q ):
        while ( True ):
            l = sys.stdin.readline()
            q.put( l )
    q = Queue.Queue()
    t = threading.Thread( target = waitStdin, args = ( q, ) )
    t.daemon = True
    t.start()
    return q

HOST = 'tcp://127.0.0.1:27961'
POLL_TIMEOUT = 100

def WriteMessageFormatted( message ):
    # Skip empty messages
    if len( message ) == 0:
        return

    # Strip unnecessary chars
    message = message.replace( "\n", "" )
    message = message.replace( "\\n", "", )
    message = message.replace( chr(25), "" )

    # Use mIRC color codes
    message = message.replace( "^0", chr(3) + "0,01" )  # black
    message = message.replace( "^1", chr(3) + "4,01" )  # red
    message = message.replace( "^2", chr(3) + "9,01" )  # green
    message = message.replace( "^3", chr(3) + "8,01" )  # yellow
    message = message.replace( "^4", chr(3) + "12,01" ) # blue
    message = message.replace( "^5", chr(3) + "11,01" ) # cyan
    message = message.replace( "^6", chr(3) + "13,01" ) # magenta
    message = message.replace( "^7", chr(3) + "0,01" )  # white

    # Strip broadcast statement
    if message[:10] == "broadcast:":
        message = message[11:]

    # Strip print statement
    if message[:7] == "print \"":
        message = message[7:-1]

    # Write
    logging.info( message )

if ( __name__ == '__main__' ):
    logging.info( 'zmq python bindings %s, libzmq version %s' % ( repr( zmq.__version__ ), zmq.zmq_version() ) )
    parser = argparse.ArgumentParser( description = 'Verbose QuakeLive server statistics' )
    parser.add_argument( '--host', default = HOST, help = 'ZMQ URI to connect to. Defaults to %s' % HOST )
    parser.add_argument( '--password', required = False )
    parser.add_argument( '--identity', default = uuid.uuid1().hex, help = 'Specify the socket identity. Random UUID used by default' )
    args = parser.parse_args()
    # TODO: put a curses or a tk interface on top of this
    q = setupInputQueue()
    try:
        ctx = zmq.Context()
        socket = ctx.socket( zmq.DEALER )
        monitor = socket.get_monitor_socket( zmq.EVENT_ALL )
        if ( args.password is not None ):
            logging.info( 'setting password for access' )
            socket.plain_username = 'rcon'
            socket.plain_password = args.password
            socket.zap_domain = 'rcon'
        socket.setsockopt( zmq.IDENTITY, args.identity )
        socket.connect( args.host )
        print( 'Connecting to %s' % args.host )
        while ( True ):
            event = socket.poll( POLL_TIMEOUT )
            event_monitor = _checkMonitor( monitor )
            if ( event_monitor is not None and event_monitor[0] == zmq.EVENT_CONNECTED ):
                # application layer protocol - notify the server of our presence
                logging.info( 'Registering with the server.' )
                socket.send( 'register' )

            while ( not q.empty() ):
                l = q.get()

                if (l == 'exit\n'):
                    logging.info( 'exiting...' )
                    exit()

                logging.info( 'sending command: %s' % repr( l ) )
                socket.send( l )

            if ( event == 0 ):
                continue

            while ( True ):
                try:
                    msg = socket.recv( zmq.NOBLOCK )
                except zmq.error.Again:
                    break
                except Exception as e:
                    logging.info( e )
                    break
                else:
                    WriteMessageFormatted( msg )
    except Exception as e:
        logging.info( e )
