!#/bin/bash

clear;
export PYTHONPATH="$PYTHONPATH:$(pwd -P):$(dirname $(pwd -P))"

echo "export the sql to clear and pipe it to dbshell"
python manage.py sqlclear images | python manage.py dbshell;
echo "syncdb"
python manage.py syncdb --noinput
