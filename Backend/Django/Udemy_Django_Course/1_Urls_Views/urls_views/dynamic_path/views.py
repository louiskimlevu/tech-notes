from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
users = ["alex", "john"]


def user_int(request, user):
    return HttpResponse(f"Welcome {users[user]}")


def user_str(request, user):
    if user in users:
        return HttpResponse(f"Welcome {user}")
