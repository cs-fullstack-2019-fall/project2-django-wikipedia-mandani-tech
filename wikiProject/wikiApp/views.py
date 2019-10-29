from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchBarForm, NewEntryForm, NewUserForm, RelatedEntryForm
from .models import NewEntryModel, RelatedEntryModel

# Create your views here.
from django.http import HttpResponse


def index(request):
    entry_list = NewEntryModel.objects.all()

    return render(request, 'wikiApp/index.html', {
                                                  'entry_list': entry_list,
                                                  'pk': request.user.pk
                                                  })


# Creating a sign up user
def new_user(request):
    if request.method == "POST":
        newUser = NewUserForm(request.POST)
        if newUser.is_valid():
            logInUser = User.objects.create_user(username=request.POST['username'],
                                                 password=request.POST['password'])
            login(request, logInUser)
            return redirect("index")
        else:
            context = {
                "errors": newUser.errors,
                "form": NewUserForm(),
            }
            return render(request, 'wikiApp/index.html', context)
    else:
        context = {
            "form": NewUserForm()
        }
        return render(request, 'wikiApp/new_user.html', context)


def login_my_user(request):
    if request.method == "POST":
        print(NewUserForm)
        loginUser = authenticate(username=request.POST['username'], password=request.POST["password"])
        if loginUser is not None:
            login(request, loginUser)
            return redirect("index")
    else:
        messages.error(request, "Wrong username or password")
        context = {
            "loginform": NewUserForm,
        }
        return render(request, 'wikiApp/login_my_user.html', context)


def log_me_out(request):
    logout(request)
    return redirect("index")


def newEntry(request, pk):
    # ________________________ CREATE NEW ENTRIES ________________________#

    if request.method == "POST":
        print(request.POST)
        form = NewEntryForm(request.POST)
        if form.is_valid():
            print(request.FILES)
            tempImageFile = request.FILES
            if not tempImageFile:
                tempImageFile = ''
            else:
                tempImageFile = tempImageFile['Entry_FileUpload']
            doc = NewEntryModel(Entry_Title=request.POST['Entry_Title'], Entry_Text=request.POST['Entry_Text'],
                                Entry_FileUpload=tempImageFile, foreignKeyUser=request.user)
            doc.save()
        return redirect("index", pk)

    context = {
        'form': NewEntryForm(),
        'pk': pk

    }
    return render(request, "wikiApp/newEntry.html", context)


def edit(request, pk):
    print(request.method)
    entry = get_object_or_404(NewEntryModel, pk=pk)
    form = NewEntryForm(request.POST or None, instance=entry)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('yourWikiEntries', pk)
    context = {'form': form,
               "allRelatedEntries": RelatedEntryModel.objects.filter(RelatedforeignKeyUser=entry),
               'pk': pk
               }
    return render(request, 'wikiApp/edit.html', context)


def delete(request, pk):

    entry = get_object_or_404(NewEntryModel, pk = pk)
    entry.delete()
    return redirect('yourWikiEntries', pk)


def yourWikiEntries(request, pk):
    if request.user.is_authenticated:

        context = {

            "allEntries": NewEntryModel.objects.filter(foreignKeyUser=request.user),
            'pk': pk

        }
        print(context)
        return render(request, 'wikiApp/yourWikiEntries.html', context)
    else:
        context = {
            "Message_Please_login": "Please Log in to see all your entries",
            "pk": pk
        }
        return render(request, 'wikiApp/yourWikiEntries.html', context)


# ________________________ CREATE RELATED ENTRIES ________________________#

def relatedEntries(request, pk):
    if request.method == "POST":
        print(request.POST)
        relatedform = RelatedEntryForm(request.POST)
        if relatedform.is_valid():
            tempImageFile = request.FILES
            if not tempImageFile:
                tempImageFile = ''
            else:
                tempImageFile = tempImageFile["Related_FileUpload"]

            doc = RelatedEntryModel(Related_Title=request.POST['Related_Title'],
                                    Related_Text=request.POST['Related_Text'], Related_FileUpload = tempImageFile,
                                    RelatedforeignKeyUser=get_object_or_404(NewEntryModel, pk=pk))
            doc.save()

        return redirect('edit', pk)

    context = {
        'relatedform': RelatedEntryForm(),
        'pk': pk
    }
    return render(request, "wikiApp/relatedEntries.html", context)



def editRelated(request, pk):
    print(request.method)
    entry = get_object_or_404(NewEntryModel, pk = pk)
    instance= RelatedEntryModel.objects.filter(RelatedforeignKeyUser=entry)
    form = RelatedEntryForm(request.POST or None, instance=instance)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editRelated', instance)
    context = {'form': form,
               'instance': instance
               }
    return render(request, 'wikiApp/edit.html', context)


def deleteRelated(request, pk):

    entry = get_object_or_404(RelatedEntryModel, pk = pk)
    entry.delete()
    return redirect('index')






def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        print(query)
    context = {
        'list': NewEntryModel.objects.filter
                (Q(Entry_Title__contains= query ) | Q(Entry_Text__contains = query)),

    }

    return render(request,'wikiApp/search_results.html',context)


def details(request,pk):
    instanceOfNewEntryModel = NewEntryModel.objects.get(pk=pk)
    relatedEntries_list = RelatedEntryModel.objects.filter(RelatedforeignKeyUser = instanceOfNewEntryModel)
    print(relatedEntries_list)
    context = {
        'Entry': instanceOfNewEntryModel,
        'allRelatedEntries':relatedEntries_list,
        'pk': request.user.pk
    }
    return render(request,'wikiApp/details.html',context)