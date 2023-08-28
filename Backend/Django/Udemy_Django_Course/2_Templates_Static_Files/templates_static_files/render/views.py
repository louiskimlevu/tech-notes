from django.shortcuts import render


def index(request):
    # render always takes request as argument
    return render(request, "render/index.html")
