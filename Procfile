web: gunicorn planekstest.wsgi --log-file -
worker: celery -A planekstest worker --loglevel=info
beat: python manage.py celery beat --loglevel=info
