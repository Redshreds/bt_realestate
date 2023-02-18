from django.shortcuts import render

from .models import Listing #Goal is to fetch listings using model then insert into a template, allowing us to loop through and output the listings in the database

def index(request):
    listings = Listing.objects.all()

    context{
        'listings': listings
    }

    return render(request, 'listings/listings.html') #Use Dictioanaries to pass in values through template. Example of MvC framework

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

#^^^ request address called from white text un urls.py

