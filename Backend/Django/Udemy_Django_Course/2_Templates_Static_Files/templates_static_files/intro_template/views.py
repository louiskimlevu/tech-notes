from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    try:
        response = render_to_string("intro_template/my_template.html")
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("Not Found")

