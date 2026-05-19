release: python manage.py migrate

web: gunicorn core.wsgi:application

worker: python manage.py consume