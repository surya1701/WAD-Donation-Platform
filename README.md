# Donation Platform 
This project is done by GROUP 21, as a semester project for WEB APPLICATION DEVELOPMENT course.
## How to Deploy
After [cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) the repo.
```console
foo@bar:~$ pip install -r requirements.txt
```
To deploy with sqlite3 database:
```console
foo@bar:~$ foo@bar:~$ python manage.py runserver
```
or To deploy with Postgresql
Setup your [postgresql account](https://pynative.com/python-postgresql-tutorial/#:~:text=Install%20Psycopg2%20using%20the%20pip%20command&text=This%20module%20is%20available%20on,pip%20command%20to%20install%20Psycopg2.&text=You%20can%20also%20install%20a%20specific%20version%20using%20the%20following%20command.).

Add your details to charity > settings.py :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'donationplatform',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost'
    }
}
```
```console
foo@bar:~$ python manage.py collectstatic
foo@bar:~$ python manage.py makemigrations
foo@bar:~$ python manage.py migrate
foo@bar:~$ python manage.py runserver
```
You're all set to go.

Note: sqlite3 file contains a pre-filled database, whereas, if you setup postgres, the superuser, ngos and causes must be added.

WAD | Group 21
