from django import forms
from django.core import validators

class NewsInput(forms.Form):
    title = forms.CharField()
    original_text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
