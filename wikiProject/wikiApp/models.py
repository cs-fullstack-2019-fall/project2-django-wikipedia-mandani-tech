from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class SearchBarModel(models.Model):
    Search = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Search}'


class NewEntryModel(models.Model):
    Entry_Title = models.CharField(max_length=100)
    Entry_Text = models.TextField(max_length=10000)
    Entry_Date = models.DateTimeField(default=timezone.now())
    Entry_FileUpload = models.ImageField(upload_to='media/', null=True, blank=True)
    foreignKeyUser = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.Entry_Title}, {self.Entry_Text}'


class RelatedEntryModel(models.Model):
    Related_Title = models.CharField(max_length=100)
    Related_Text = models.TextField(max_length=10000)
    Related_Date = models.DateTimeField(default=timezone.now())
    Related_FileUpload = models.ImageField(upload_to='media/', null=True, blank=True)
    RelatedforeignKeyUser = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.Related_Title}, {self.Related_Text}'