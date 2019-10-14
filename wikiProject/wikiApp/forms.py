from django.forms import ModelForm
from .models import SearchBarModel , NewEntryModel


class SearchBarForm(ModelForm):
    class Meta:
        model = SearchBarModel
        fields = ['Search']


class NewEntryForm(ModelForm):
    class Meta:
        model = NewEntryModel
        fields = ['Entry_Title','Entry_Text','Entry_FileUpload']
