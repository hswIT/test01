from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices, bedroom_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

# def index(request):
#   return HttpResponse("<h1>Hello<h1>")


def index(request):
    # show 3 listing only
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    # add choices into the object
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context)
