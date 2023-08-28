from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

months = {
    "january": "January: A fresh start for limitless potential.",
    "february": "February: Embrace the beauty of love and friendship.",
    "march": "March: Step into the awakening of nature's wonders.",
    "april": "April: Let the showers of inspiration bring forth growth.",
    "may": "May: Blossom with the vibrant colors of spring.",
    "june": "June: Embrace the warmth of the sun and endless possibilities.",
    "july": "July: Celebrate freedom and create lasting memories.",
    "august": "August: Embrace relaxation and savor the sweetness of life.",
    "september": "September: Embrace change and embark on new adventures.",
    "october": "October: Embrace the enchantment of autumn's arrival.",
    "november": "November: Express gratitude and embrace the spirit of giving.",
    "december": "December: Find joy in the magic of the holiday season.",
}


def home(request):
    response = ""
    for month, quote in months.items():
        url = reverse("month_str", args=[month])
        response += f"<li><a href=\"{url}\">{month}</a>: {quote}</li>"
    response = f"<ul> {response} </ul>"
    return HttpResponse(response)


def month_int(request, month):
    months_list = list(months.keys())
    if 0 < month <= len(months_list):
        month_str = months_list[month - 1]

        return HttpResponseRedirect(f"/all_together/{month_str}")

    home_url = reverse("home")
    return HttpResponseRedirect(home_url)
    # return HttpResponseNotFound(f"{month} not in range")


def month_str(request, month):
    if month in months:
        quote = months[month]
        response = f"<h1>{quote}</h1>"
        return HttpResponse(response)

    # return HttpResponseNotFound(f"{month} not found")
    home_url = reverse("home")
    return HttpResponseRedirect(home_url)