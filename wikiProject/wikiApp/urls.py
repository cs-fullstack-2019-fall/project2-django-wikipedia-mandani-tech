from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newEntry/', views.newEntry, name='newEntry'),
    path('display/', views.display, name='display'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.newEntry, name='delete'),
    path('yourWikiEntries/', views.yourWikiEntries, name='yourWikiEntries'),




]