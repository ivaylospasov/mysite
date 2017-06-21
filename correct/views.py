from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from vews.py"}
    return render(request, 'correct/index.html', context=my_dict)

def news_input_form(request):
    form = forms.NewsInput()
    return render(request, 'correct/news.html', {'form':form})
