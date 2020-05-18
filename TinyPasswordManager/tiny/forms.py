from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PasswordCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=2000)
    password = forms.CharField(max_length=32)

    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        return data