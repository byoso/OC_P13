#! /bin/bash

# this demonstrate how to recreate the site if completely deleted from
# heroku

heroku login
heroku container:login
heroku create oc-lettings-vf

./heroku_environment.sh
git commit --allow-empty -am 'empty commit'
git push
