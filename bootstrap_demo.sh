#!/bin/bash

which virtualenv > /dev/null 2>&1 || \
  { echo -e "You must have python-virtualenv installed:\n    sudo apt-get install python-virtualenv"; exit 1; }

[ -d venv ] || (virtualenv venv && . venv/bin/activate && pip install -r requirements.txt)
. venv/bin/activate

[ -f db.sqlite3 ] || python manage.py migrate

python manage.py collectstatic --noinput
python manage.py compress --force

read -r -d '' USERS << EOM
from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.filter(email='admin@example.com').delete();
User.objects.create_superuser('admin', 'admin@example.com', 'Admin123');
User.objects.filter(email='demo@example.com').delete();
demo = User.objects.create(username='demo', email='demo@example.com');
demo.set_password('Demo123');
demo.save();
EOM

echo $USERS | python manage.py shell

python manage.py runserver 0.0.0.0:8000

