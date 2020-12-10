web: gunicorn planekstest.wsgi --log-file -
worker: celery -A planekstest worker --loglevel=info --pool=solo
beat: python manage.py celery beat --loglevel=info
