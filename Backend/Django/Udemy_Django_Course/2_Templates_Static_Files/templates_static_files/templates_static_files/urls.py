from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("intro_template.urls")),
    path('render', include("render.urls")),
]
