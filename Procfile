web: gunicorn planekstest.wsgi --log-file -
worker: python manage.py celery worker -B -l info
beat: python manage.py celery beat --loglevel=info
