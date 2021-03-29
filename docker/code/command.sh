#!/bin/bash
daphne -u /tmp/daphne.sock webpts3.asgi:application &
httpd-foreground
