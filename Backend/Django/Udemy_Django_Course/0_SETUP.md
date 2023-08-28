[Udemy Django Course](https://www.udemy.com/course/python-django-the-practical-guide/)

# Setup section
[Setup slides](https://github.com/academind/django-practical-guide-course-code/blob/setup-zz-extra-files/slides/slides.pdf)

## Install django
```commandline
source .venv/bin/activate
pip install django
```

## Create a project
```commandline
django-admin startproject mypage
```

## Review project directory
- `urls.py` -> routes (URL config) mapping urls to views
- `manage.py` -> cli
- `settings.py` -> global settings
- `db.sqlite3` -> local database

## Start development server
```commandline
python manage.py runserver
```

## Create an app
```commandline
python manage.py startapp challenges
```

## Review app directory
- `migration/` -> empty python package
- `admin.py` -> for administration
- `apps.py` -> app configuration
- `models.py` -> data model definition
- `test.py` -> unit tests
- `views.py` -> function/class triggered when a request hits a url

