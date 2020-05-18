#!/usr/bin/env bash

PORT=8000


python manage.py migrate

python manage.py loaddata users posts comments

python manage.py runserver ${PORT}
