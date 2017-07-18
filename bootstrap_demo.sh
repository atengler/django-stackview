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
from stackview.identity.models import Tenant, TenantMembership;
User = get_user_model();
User.objects.all().delete();
Tenant.objects.all().delete();
TenantMembership.objects.all().delete();
User.objects.create_superuser('admin', 'admin@example.com', 'Admin123');
demo1 = User.objects.create(username='demo1', email='demo1@example.com');
demo1.set_password('Demo123');
demo1.save();
demo2 = User.objects.create(username='demo2', email='demo2@example.com');
demo2.set_password('Demo123');
demo2.save();
tenant1 = Tenant.objects.create(name="Demo Tenant 1");
TenantMembership.objects.create(user=demo1, tenant=tenant1);
TenantMembership.objects.create(user=demo2, tenant=tenant1);
demo3 = User.objects.create(username='demo3', email='demo3@example.com');
demo3.set_password('Demo123');
demo3.save();
demo4 = User.objects.create(username='demo4', email='demo4@example.com');
demo4.set_password('Demo123');
demo4.save();
tenant2 = Tenant.objects.create(name="Demo Tenant 2");
TenantMembership.objects.create(user=demo3, tenant=tenant2);
TenantMembership.objects.create(user=demo4, tenant=tenant2);
EOM

echo $USERS | python manage.py shell

python manage.py runserver 0.0.0.0:8000

