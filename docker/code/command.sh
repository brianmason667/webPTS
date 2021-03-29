#!/bin/bash
# this was really annoying, turns out daphne
# dose not clean up its unix sockets so
# remove these at startup 
rm /tmp/daphne.sock &
rm /tmp/daphne.sock.lock &
sleep 2s 
daphne  -u /tmp/daphne.sock webpts3.asgi:application &
sleep 5s
httpd-foreground
