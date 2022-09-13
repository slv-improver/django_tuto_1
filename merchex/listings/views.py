from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Les annonces</p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
        </ul>
        <p>Mes plats préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Liste d\'annonces</h1><p>Nothing here</p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous !</h1><p>Formulaire</p>')
