#! /bin/bash

# before running this script, be sure you have a functionnal
# docker container ready
# $ docker container ps -a

heroku login
heroku container:login
heroku create oc-lettings-vf
heroku git:remote -a oc-lettings-vf
heroku container:push web
heroku container:release web
