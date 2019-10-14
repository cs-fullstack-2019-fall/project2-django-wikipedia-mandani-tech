from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('newEntry/', views.newEntry, name='newEntry'),
    path('yourWikiEntries/', views.yourWikiEntries, name='yourWikiEntries'),



]