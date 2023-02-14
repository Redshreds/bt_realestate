from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), #views.listing references listing method from views.py
    path('search', views.search, name='search'),
]

#index method being called from listings/view.py