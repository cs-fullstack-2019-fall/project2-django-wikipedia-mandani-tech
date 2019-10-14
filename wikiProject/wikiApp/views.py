from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'wikiApp/index.html')


def home(request):
    return render(request,'wikiApp/home.html')


def newEntry(request):
    return render(request,'wikiApp/newEntry.html')


def yourWikiEntries(request):
    return render(request,'wikiApp/yourWikiEntries.html')