from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:month>", views.month_int),
    path("<str:month>", views.month_str, name="month_str"),
]
