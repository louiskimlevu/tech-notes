from django.shortcuts import render
from django.http import HttpResponse


def user(request, user):
    response = f"<h1>{user}</h1>"
    return HttpResponse(response)
