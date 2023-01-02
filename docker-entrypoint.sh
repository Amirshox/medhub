#!/bin/sh
set -e

# shellcheck disable=SC2039
if [[ $RUN == "testing" ]];
then
    echo "Run testing mode"
    python manage.py test
elif [[ $RUN == "dev" ]];
then
    echo "Run dev mode"
    python manage.py migrate
    python manage.py loaddata fixtures.json
    python manage.py runserver 0.0.0.0:8000
#elif [[ $RUN == "celery" ]];
#then
#    echo "Run celery"
#    celery -A config worker -B -l info
elif [[ $RUN == "prod" ]];
then
    echo "Run prod mode"
    python manage.py collectstatic --noinput
    python manage.py migrate
    gunicorn config.wsgi:application --bind 0.0.0.0:8050 --workers 3
else
    echo "run mode not found"
fi
