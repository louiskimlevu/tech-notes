from django.urls import path
from . import views

urlpatterns = [
    path("<int:user>", views.user_int),
    path("<str:user>", views.user_str),
]