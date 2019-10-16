from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newEntry/', views.newEntry, name='newEntry'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('yourWikiEntries/', views.yourWikiEntries, name='yourWikiEntries'),
    path('new_user/', views.new_user, name='new_user'),
    path('login_my_user/', views.login_my_user, name='login_my_user'),
    path('log_me_out/', views.log_me_out, name='log_me_out'),
    path('relatedEntries<int:pk>/', views.relatedEntries, name='relatedEntries'),

]