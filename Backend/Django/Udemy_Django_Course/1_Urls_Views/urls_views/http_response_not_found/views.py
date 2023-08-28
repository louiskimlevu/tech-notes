from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
users = ["alex", "john"]


def user_int(request, user):
    if user > len(users):
        return HttpResponseNotFound(f"User {user} not found")
    str_user = users[user]
    return HttpResponse(f"Welcome {str_user}")


def user_str(request, user):
    if user in users:
        return HttpResponse(f"Welcome {user}")
    return HttpResponseNotFound(f"User {user} not found")
