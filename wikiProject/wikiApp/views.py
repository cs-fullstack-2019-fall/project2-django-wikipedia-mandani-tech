from django.shortcuts import render, redirect
from .forms import SearchBarForm, NewEntryForm
from .models import SearchBarModel, NewEntryModel

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


# def newEntry(request):
#     form = SearchBarForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save(commit=True)
#     context = {
#
#                 'form': form,
#             }
#     return render(request, 'wikiApp/newEntry.html', context)



#
# def newEntry(request):
#
#     entry_form = NewEntryForm()
#     if request.method == "POST":
#         print(request.POST)
#         # process the uploaded files
#         tempImageFile = request.FILES
#         if not tempImageFile:
#             tempImageFile = ''
#         else:
#             tempImageFile = tempImageFile["Entry_FileUpload"]
#         img = NewEntryModel(Entry_FileUpload=tempImageFile)
#         img.save()
#     # go get all the upload records
#     image_list = NewEntryModel.objects.all()
#     context = {
#         'entry_form': entry_form,
#         'image_list': image_list
#     }
#     return render(request, 'wikiApp/newEntry.html', context)




#
# def newEntry(request):
#     # image_list = uploaded_doc.objects.all()
#     entry_form = NewEntryForm()
#     if request.method == "POST":
#         print(request.POST)
#         entry_form = NewEntryForm(request.POST)
#         if entry_form.is_valid():
#             entry_form.save()
#             tempImageFile = request.FILES
#             if not tempImageFile:
#                 tempImageFile = ''
#             else:
#                 tempImageFile = tempImageFile["Entry_FileUpload"]
#             doc = NewEntryModel(Entry_Title=request.POST['Title'], Entry_Text=request.POST['Entry_Text'], Entry_FileUpload = tempImageFile,)
#             doc.save()
#         return render(request, "wikiApp/index.html")
#     else:
#         context = {
#             'entry_form': NewEntryForm()
#         }
#     return render(request, "wikiApp/newEntry.html", context)


def newEntry(request):
    if request.method == "POST":
        print(request.POST)
        entry_form = NewEntryForm()
        if entry_form.is_valid():
            entry_form.save()
            return redirect('index')

    return render(request, "wikiApp/newEntry.html", {'entry_form': NewEntryForm})



def yourWikiEntries(request):
    form = SearchBarForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)
        return render(request, 'wikiApp/yourWikiEntries.html', {'form': form})
