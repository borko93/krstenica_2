from django import forms
from .models import krsteni_list

class krsteni_listForm(forms.ModelForm):
    class Meta:
        model = krsteni_list
        fields = '__all__'

