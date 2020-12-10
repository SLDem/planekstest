web: gunicorn planekstest.wsgi --log-file -
worker: celery -A planekstest worker
beat: python manage.py celery beat --loglevel=info