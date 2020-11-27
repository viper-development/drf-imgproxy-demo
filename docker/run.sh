#!/bin/sh

set -e -x

python manage.py migrate
python manage.py createbucket

exec su \
     --preserve-environment \
     --command "uvicorn --host 0.0.0.0 $@ drf_imgproxy_demo.asgi:application" \
     "$APP_USER"
