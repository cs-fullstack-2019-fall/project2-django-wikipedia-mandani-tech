from django.shortcuts import render, redirect
from .forms import SearchBarForm
from .models import SearchBarModel

# Create your views here.
from django.http import HttpResponse


def index(request):
    form = SearchBarForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)
        return redirect('index')
    return render(request, 'wikiApp/index.html', {'form': form})


def home(request):
    return render(request, 'wikiApp/home.html')


def newEntry(request):
    return render(request, 'wikiApp/newEntry.html')


def yourWikiEntries(request):
    return render(request, 'wikiApp/yourWikiEntries.html')
