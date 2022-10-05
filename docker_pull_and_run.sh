#! /bin/bash


# pull from https://hub.docker.com/repository/docker/byoso/oc-lettings
# docker pull byoso/oc-lettings:3a2b9a2b2c4f9cf1266bf31f2518e66888be40b2
# docker run -p 8000:8000 byoso/oc-lettings:3a2b9a2b2c4f9cf1266bf31f2518e66888be40b2

# pull the image created by heroku
docker pull registry.heroku.com/oc-lettings-vf/web
docker run -p 8000:8000 registry.heroku.com/oc-lettings-vf/web
