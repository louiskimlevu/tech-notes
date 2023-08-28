# Templates

[URLs & views slides](https://github.com/academind/django-practical-guide-course-code/blob/urls-views-zz-extra-files/slides/slides.pdf)

## Start a base Project

- In the previous section, we generated the html inside the view function, it would be better if we can render it from a
  html template

```commandline
django-admin startproject templates_static_files
cd templates_static_files
django-admin startapp intro_template
python manage.py runserver
```

- `templates_static_files/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("intro_template.urls")),
]
```

- Create `intro_template/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```

- Update `templates/views.py`
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("ok")
```

## Create a template

- Create dir `<app_name>/templates/<app_name>`
```commandline
mkdir -p intro_template/templates/intro_template 
```

- Create a html template `<app_name>/templates/<app_name>/my_template.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My HTML Document</title>
</head>
<body>

<h1>Hello</h1>
</body>
</html>
```

- `render_to_string` in `views.py`
```python
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    try:
        response = render_to_string("intro_template/my_template.html")
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("Not Found")
```

- Add the rest of the base path in `settings.py`
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # base paths where django should look for templates
            BASE_DIR / "intro_template" / "templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- test

```commandline
curl localhost:8000
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My HTML Document</title>
</head>
<body>
<h1>Hello</h1>
</body>
</html>
```

## Find templates automatically with `DIRS`
- Just now we added the template base path for each app in `settings.py`
```python
        'DIRS': [
            # base paths where django should look for templates
            BASE_DIR / "intro_template" / "templates"
        ],
```
- The problem is that we need to update the `settings.py` everytime we add a new app
- We can leverage the `'APP_DIRS': True` settings to automatically find templates inside the app
- Remove the template dir in `settings.py/TEMPLATES`
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # base paths where djanko should look for templates
            # BASE_DIR / "intro_template" / "templates"
        ],
        'APP_DIRS': True,
    }
]
## Find templates automatically with `INSTALLED_APPS` 
```
- Install the app in `settings.py/INSTALLED.APPS`
```python
INSTALLED_APPS = [
    'intro_template',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
- test
```commandline
curl localhost:8000
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My HTML Document</title>
</head>
<body>
<h1>Hello</h1>
</body>
</html>
```

## Render function
- create render app
```commandline
django-admin startapp render
```
- In project dir, `urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("intro_template.urls")),
    path('render', include("render.urls")),
]
```
- `settings.py` install app
```python
INSTALLED_APPS = [
    'intro_template',
    'render',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
- In render app, `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```
- In render app, `views.py`
```python
from django.shortcuts import render


def index(request):
    # render always takes request as argument
    return render(request, "render/index.html")
```
- test
```commandline
curl localhost:8000/render          
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My HTML Document</title>
</head>
<body>
<h1>Hello</h1>
</body>
</html>
```