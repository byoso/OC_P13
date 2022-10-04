#! /bin/bash

heroku login
heroku container:login
heroku create oc-lettings-vf
heroku git:remote -a oc-lettings-vf
heroku container: push web
heroku container: release web
