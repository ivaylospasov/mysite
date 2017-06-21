from django.shortcuts import render
from django.http import HttpResponse
from forms import NewsInput

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from vews.py"}
    return render(request, 'correct/index.html', context=my_dict)
