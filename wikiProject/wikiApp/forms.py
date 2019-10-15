from django.forms import ModelForm
from .models import SearchBarModel , NewEntryModel
from django.contrib.auth.models import User


class SearchBarForm(ModelForm):
    class Meta:
        model = SearchBarModel
        fields = ['Search']


class NewEntryForm(ModelForm):
    class Meta:
        model = NewEntryModel
        fields = ['Entry_Title','Entry_Text','Entry_FileUpload']


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
