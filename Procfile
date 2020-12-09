web: gunicorn planekstest.wsgi --log-file -
worker: celery worker -A planekstest  --loglevel=info
beat: python manage.py celery beat --loglevel=info
