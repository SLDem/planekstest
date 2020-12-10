web: gunicorn planekstest.wsgi --log-file -
worker: celery -A planekstest worker
beat: celery -A planekstest beat --loglevel=info
