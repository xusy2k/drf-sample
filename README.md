# DRF Sample

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Install the project

After cloning the project you can install the project in a virtualenv with the following commands:

```bash
$ sudo apt install python3.12-dev python3.12-venv
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements/local.txt
```

## Settings

Copy the [.env-template](.env-template) file as `.env` and update the values as needed. Specially these:

```bash
DJANGO_DATABASE_URL=sqlite:///db.sqlite3
DJANGO_DEBUG=True

# In case you want to log the application, set the following variables
# DJANGO_LOGGER_FILE=logs/logging.log
# DJANGO_LOGGER_LEVEL=INFO

# In case you want to log the database queries in a different file, set the following variables
# DJANGO_LOGGER_DB_FILE=logs/db.log
# DJANGO_LOGGER_DB_LEVEL=DEBUG
```

## Migrate the database and create a superuser

After installing the project, you can migrate the database and create a superuser with the following commands:

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Start the server

You can start the server with the following command:

```bash
$ python manage.py runserver localhost:8000
```

In case of start the server with de production settings, you can do it as:

```bash
$ pip install -r requirements/production.txt
$ DJANGO_SETTINGS_MODULE="config.settings.production" python manage.py check --deploy # Check dependencies
$ DJANGO_SETTINGS_MODULE="config.settings.production" python manage.py runserver localhost:8000
```

## API

The API current version, `settings.VERSION_API`, is **v1**, so the base URL is `/api/v1/`. If you want to access the
API documentation, you can use the following URL: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/),
but you must be logged in to access it. So, you can create users in several ways:

* Create a **superuser account**, use this command:
```bash
$ python manage.py createsuperuser
```
* Using the API endpoint [/api/v1/signup/](http://localhost:8000/api/v1/signup/) with the following payload:
```json
{
  "first_name": "",
  "last_name": "",
  "phone_number": "",
  "email": "",
  "hobbies": "",
  "password": ""
}
```
* Also, there is a django command, [create_fake_users](main/users/management/commands/create_fake_users.py), able to generate fake users:
```bash
$ python manage.py create_fake_users --number 10
```
* Or generating the full curl command (for paste it on linux command line):
```bash
python manage.py create_fake_users --curl
```

## Development



### Type checks

Running type checks with mypy:

    $ mypy main

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest


## Documentation

Create the documentation with sphinx:

```bash
$ cd docs
$ make livehtml
```
