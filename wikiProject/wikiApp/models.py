from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.


class SearchBarModel(models.Model):
    Search = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Search}'

