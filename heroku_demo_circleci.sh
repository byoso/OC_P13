#! /bin/bash


heroku login
heroku container:login
heroku create oc-lettings-vf

./heroku_environment.sh
