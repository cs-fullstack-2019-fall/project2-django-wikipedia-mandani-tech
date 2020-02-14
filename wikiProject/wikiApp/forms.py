from django.forms import forms
from django.forms import ModelForm
from .models import SearchBarModel, NewEntryModel, RelatedEntryModel
from django.contrib.auth.models import User



class SearchBarForm(ModelForm):
    class Meta:
        model = SearchBarModel
        fields = ['Search']


class NewEntryForm(ModelForm):
    class Meta:
        model = NewEntryModel
        fields = ['Entry_Title','Entry_Text','Entry_FileUpload']
#         fields = '__all__'


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class RelatedEntryForm(ModelForm):
    class Meta:
        model = RelatedEntryModel
#         fields = '__all__'
        fields = ['Related_Title','Related_Text', 'Related_FileUpload']


