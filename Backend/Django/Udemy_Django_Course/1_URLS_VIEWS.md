# URLs & views
[URLs & views slides](https://github.com/academind/django-practical-guide-course-code/blob/urls-views-zz-extra-files/slides/slides.pdf)

## Create a new Django project
```commandline
virtualenv .venv
django-admin startproject monthly_challenges .
django-admin startapp challenges
python manage.py runserver
```

## Create a view
- Update `challenges/views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is january challenge")
```
- Create `challenges/urls.py`
  - content is similar to `monthly_challenges/urls.py` 
```python
from django.urls import path
from . import views

urlpatterns = [
    path("january", views.index),
]
```
- In `monthly_challenges/urls.py`,
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # forward requests from challenges/ to the url config of the 'challenges' app defined in urls.py
    # in the main urls.py we are just parsing the url and not calling views directly
    path("challenges/", include("challenges.urls")),
]
```
- Verify the url mapping and view response works
```commandline
curl localhost:8000/challenges/january
This is january challenge
```

## Adding more views
- Update the code so that `/challenges/february` returns "This is february challenge"
- In `views.py`, add a new view function
```commandline
from django.shortcuts import render
from django.http import HttpResponse

def january(request):
    return HttpResponse("This is january challenge!")


def february(request):
    return HttpResponse("This is february challenge!")
```
- In `urls.py`, add a new path
```python
from django.urls import path
from . import views

urlpatterns = [
    path("january", views.january),
    path("february", views.february),
]
```
- Check `/challenges/february` works
```commandline
curl localhost:8000/challenges/february
This is february challenge
```

## Dynamic Path Segments & Captured Values
- `monthly_challenges/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path("march", views.march),
    # pass the path as variable
    path("<month>", views.monthly_challenge),
    path("january", views.january),
    path("february", views.february),
]
```
- `monthly_challenges/views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse


def january(request):
    return HttpResponse("This is january challenge!")


def february(request):
    return HttpResponse("This is february challenge!")


def march(request):
    return HttpResponse("This is march challenge!")


def monthly_challenge(request, month):
    return HttpResponse(f"This is the challenge of {month}")
```

- test
```commandline
curl localhost:8000/challenges/july
This is the challenge of july  

curl localhost:8000/challenges/march
This is march challenge!

# Here, the static view is still executed.
# Django examines the defined URL patterns one by one in the order they appear in the configuration file.
# It tries to match the requested URL against each pattern until it finds a match.
```

## Improving the dynamic view function with `match` and `HttpResponseNotFound`
- `views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def monthly_challenge(request, month):
    challenge = None
    match month:
        case "january":
            challenge = "cook for me"
        case "february":
            challenge = "dance for me"
        case "march":
            challenge = "work for me"
        case _:
            return HttpResponseNotFound("Month not found")

    return HttpResponse(f"{month} challenge is: {challenge}")

```

- `challenges/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path("<month>", views.monthly_challenge),]
```

- Test
```commandline
curl localhost:8000/challenges/january
january challenge is: cook for me

curl localhost:8000/challenges/july
Month not found                                                          
```

## Path converters
- We can configure paths to parse based on the type of path
- `challenges/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    # int path converters must be defined before str path converters
    # because Django matches URL patterns from top to bottom
    # and when it encounters an int path converter
    # it will try to match the URL segment with an integer value.
    # If the matching fails, it will move on to the next URL pattern.
    # However, if a str path converter is defined before an int path converter
    # Django will interpret the URL segment as a string and match it, even if it represents an integer value.

    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),
```
- `views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge(request, month):
    challenge = None
    match month:
        case "january":
            challenge = "cook for me"
        case "february":
            challenge = "dance for me"
        case "march":
            challenge = "work for me"
        case _:
            return HttpResponseNotFound("Month not found")

    return HttpResponse(f"{month} challenge is: {challenge}")


def monthly_challenge_by_number(request, month):
    challenge = None
    match month:
        case 1:
            challenge = "cook for me"
        case 2:
            challenge = "dance for me"
        case 3:
            challenge = "work for me"
        case _:
            return HttpResponseNotFound("Month int not found")

    return HttpResponse(f"{month} challenge is: {challenge}")
```
- test
```commandline
curl localhost:8000/challenges/2
2 challenge is: dance for me   
    
curl localhost:8000/challenges/march
march challenge is: work for me
```
## Complete the logic for all months
- `views.py` 
```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Start a new exercise routine and stick to it for the entire month.",
    "february": "Read a new book every week and share your thoughts with others.",
    "march": "Learn a new programming language or framework.",
    "april": "Explore a new hobby and dedicate time to practice it.",
    "may": "Take on a 30-day coding challenge to enhance your skills.",
    "june": "Spend time outdoors every day and appreciate nature.",
    "july": "Learn to cook a new dish each week and surprise your loved ones.",
    "august": "Practice mindfulness and meditation daily for a calmer mind.",
    "september": "Set personal goals for self-improvement and track your progress.",
    "october": "Engage in a social cause and volunteer your time.",
    "november": "Write a novel or start a blog to express your creativity.",
    "december": "Spread joy and kindness by doing a random act of kindness every day.",
}


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(f"{month} challenge is: {challenge}")
    except:
        return HttpResponseNotFound(f"Month {month} not found")


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())  
        if month > len(months):
          raise Exception(f"Month {month} not in range")
        challenge = monthly_challenges[str_month]
        
        return HttpResponse(f"{str_month} challenge is: {challenge}")
    except Exception as e:
        return HttpResponseNotFound(e)
```


## Redirect
- Instead of returning a response in `monthly_change_by_number`, we can use a 302 Redirect
- `views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Start a new exercise routine and stick to it for the entire month.",
    "february": "Read a new book every week and share your thoughts with others.",
    "march": "Learn a new programming language or framework.",
    "april": "Explore a new hobby and dedicate time to practice it.",
    "may": "Take on a 30-day coding challenge to enhance your skills.",
    "june": "Spend time outdoors every day and appreciate nature.",
    "july": "Learn to cook a new dish each week and surprise your loved ones.",
    "august": "Practice mindfulness and meditation daily for a calmer mind.",
    "september": "Set personal goals for self-improvement and track your progress.",
    "october": "Engage in a social cause and volunteer your time.",
    "november": "Write a novel or start a blog to express your creativity.",
    "december": "Spread joy and kindness by doing a random act of kindness every day.",
}


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(f"{month} challenge is: {challenge}")
    except:
        return HttpResponseNotFound(f"Month {month} not found")


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        if month > len(months) or month == 0:
            raise Exception(f"Month {month} not in range")
        str_month = months[month - 1]

        return HttpResponseRedirect(f"/challenges/{str_month}")
    except Exception as e:
        return HttpResponseNotFound(e)
```
- test
```commandline
curl -L  localhost:8000/challenges/1 
january challenge is: Start a new exercise routine and stick to it for the entire month.

curl -L  localhost:8000/challenges/0
Month 0 not in range
```

## Reverse Function & Named URLs
- How to avoid hardcoding the full path of the Redirect url?
- `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [

    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge-str"),

]
```
- `views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start a new exercise routine and stick to it for the entire month.",
    "february": "Read a new book every week and share your thoughts with others.",
    "march": "Learn a new programming language or framework.",
    "april": "Explore a new hobby and dedicate time to practice it.",
    "may": "Take on a 30-day coding challenge to enhance your skills.",
    "june": "Spend time outdoors every day and appreciate nature.",
    "july": "Learn to cook a new dish each week and surprise your loved ones.",
    "august": "Practice mindfulness and meditation daily for a calmer mind.",
    "september": "Set personal goals for self-improvement and track your progress.",
    "october": "Engage in a social cause and volunteer your time.",
    "november": "Write a novel or start a blog to express your creativity.",
    "december": "Spread joy and kindness by doing a random act of kindness every day.",
}


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(f"{month} challenge is: {challenge}")
    except:
        return HttpResponseNotFound(f"Month {month} not found")


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        if month > len(months) or month == 0:
            raise Exception(f"Month {month} not in range")
        str_month = months[month - 1]
        url = reverse("month-challenge-str", args=[str_month])
        # url = /challenges/str_month
        return HttpResponseRedirect(url)
    
    except Exception as e:
        return HttpResponseNotFound(e)
```

## Return html
- `views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse


def user(request, user):
    response = f"<h1>{user}</h1>"
    return HttpResponse(response)
```
- test
- ```commandline
curl localhost:8000/return_html/helo
<h1>helo</h1>
```