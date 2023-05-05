from django.shortcuts import render
from django.http import HttpResponse
# from rdflib import Graph, URIRef, Literal, Namespace
from api.loadOntology import *


# Create your views here.
def home(request):
    allData = getAllInfluencer()
    return render(request, 'filtering/filtering.html', {'data': allData})


def individual(request, name_id):
    print('individual')
    print(name_id)
    return render(request, 'filtering/individual.html')
