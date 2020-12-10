web: gunicorn planekstest.wsgi --log-file -
worker: celery worker -A planekstest  --loglevel=info --pool=solo
beat: python manage.py celery beat --loglevel=info
