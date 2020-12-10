web: gunicorn planekstest.wsgi --log-file -
worker: celery worker -A planekstest
beat: celery beat -A planekstest --loglevel=info
