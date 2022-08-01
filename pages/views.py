from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices, bedroom_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

# def index(request):
#   return HttpResponse("<h1>Hello<h1>")


def index(request):

    # add choices into the object
    context = {
        # 'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")
