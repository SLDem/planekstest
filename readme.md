This is the test task for PLANEKS company.

To run the application:

1. Open cmd or any other command line tool and navigate to root directory containing 'manage.py' file.
2. Run "python manage.py runserver" command.
3. Open another command line tool and navigate to the same directory containing 'manage.py'.
4. Run "celery -A planekstest worker"
5. Go to localhost:8000 and login using username: "test" and password: "test"
