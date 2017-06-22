from django import forms
from django.core import validators
from correct.models import NewsText

class NewsInput(forms.Form):
    title = forms.CharField()
    original_text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])


class OriginalInputForm(forms.ModelForm):
    class Meta():
        model = NewsText
        fields = ['title', 'original_text']
