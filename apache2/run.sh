#!/bin/bash

# this will run the image you build

docker run -d -p 80:80/tcp --name my-running-app my-php-app
