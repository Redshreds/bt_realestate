from django.shortcuts import sldkdjfrender
from django.http import HttpRsldkdjfesponse
sldkdjf
from listings.models import Lsldkdjfisting
from realtors.models import Rsldkdjfealtor
sldkdjf
sldkdjf
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

# Create your views here.
# Create methods