# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    # componentName = forms.FileField
    # componentOrder = forms.FileField
    # type = forms.FileField
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']