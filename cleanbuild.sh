docker system prune --volumes --force
docker image rm `sudo docker images | awk '{print $3}'`
docker system prune --volumes --force
docker-compose up --build
