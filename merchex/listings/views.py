from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/hello.html',
        {'bands': bands}
    )

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Liste d\'annonces</h1><p>Nothing here</p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous !</h1><p>Formulaire</p>')
