from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm

def hello(request):
    return render(
        request,
        'listings/hello.html'
    )

def band_list(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/band_list.html',
        {'bands': bands}
    )

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(
        request,
        'listings/band_detail.html',
        {'band': band}
    )

def about(request):
    return render(
        request,
        'listings/about.html'
    )

def listings(request):
    listings = Listing.objects.all()
    return render(
        request,
        'listings/listings.html',
        {'listings': listings}
    )

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    band = Band.objects.get(id=listing.band_id)
    return render(
        request,
        'listings/listing_detail.html',
        {'listing': listing, 'band_id': band.id}
    )

def contact(request):
    form = ContactUsForm()
    return render(
        request,
        'listings/contact.html',
        {'form': form}
    )
