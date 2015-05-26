#!/bin/bash
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@test.com', 'admin')" | python ./manage.py shell
python manage.py loaddata forum.json
python manage.py runserver