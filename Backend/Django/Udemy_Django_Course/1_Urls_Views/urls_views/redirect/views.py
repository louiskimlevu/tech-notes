from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

users = ["alex", "john"]

def user_int(request, user):
    str_user = users[user]
    return HttpResponse(f"Welcome {str_user}!")


def user_str(request, user):
    if user in users:
        user_id = users.index(user)
        url = reverse('user_int_url', args=[user_id])
        return HttpResponseRedirect(url)
    return HttpResponseNotFound(f"{user} not found")
