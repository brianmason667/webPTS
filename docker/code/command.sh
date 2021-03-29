#!/bin/bash
# rm /tmp/daphne.sock &
# sleep 5s 
daphne  -u /tmp/daphne.sock webpts3.asgi:application &
sleep 5s
httpd-foreground
