This is the test task for PLANEKS company.

To run the application:

(Make sure you have rabbitMq server running on your machine)

1. Open cmd or any other command line tool and navigate to root directory containing 'manage.py' file.
2. Run "pip install requirements.txt"
3. Run "python manage.py runserver" command.
4. Open another command line tool and navigate to the same directory containing 'manage.py'.
5. Run "celery -A planekstest worker" command.
6. Go to localhost:8000 and login using username: "test" and password: "test".
