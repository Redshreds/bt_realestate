from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing #Goal is to fetch listings using model then insert into a template, allowing us to loop through and output the listings in the database

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator =  Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context) #Use Dictioanaries to pass in values through template. Example of MvC framework

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listings': listings
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)

#^^^ request address called from white text un urls.py

