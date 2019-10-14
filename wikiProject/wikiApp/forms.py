from django.forms import ModelForm
from .models import SearchBarModel




class SearchBarForm(ModelForm):
    class Meta:
        model = SearchBarModel
        fields = ['Search']