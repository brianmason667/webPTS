Web production tracking system 

Blank database

Track quantity of produced products 
Track quantity of defect Product
Track Machine downtime
View production stats, totals
Visualize the data for monthly production charts

requres:
    docker
    docker-compose


setup:

    clone

    docker-compose up --build

    if that fails try ./cleanbuild.sh

    docker ps

    note the container id of httpd

    docker exec -it (container id) /bin/bash

    ./manage.py migrate

    ./manage.py makesuperuser

    you should then be able to login to the /admin page

    phpmyadmin is aval at port 8080

    server: mysql

    username: root

    password: example1

    these can be configured in docker-compose.yml