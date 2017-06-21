from django import forms

class NewsInput(forms.Form):
    title = forms.CharField()
    original_text = forms.CharField(widget=forms.Textarea)
