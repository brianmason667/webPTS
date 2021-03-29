#!/bin/bash
python manage.py runserver 0.0.0.0:8000 &
daphne -u /tmp/daphne.sock webpts3.asgi:application
