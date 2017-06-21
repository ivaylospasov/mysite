from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from vews.py"}
    return render(request, 'correct/index.html', context=my_dict)

# def news_input_form(request):
#     form = forms.NewsInput()
#     return render(request, 'correct/news.html', {'form':form})

def news_input_form(request):
    form = forms.NewsInput()

    # Check to see if we get a POST back
    if request.method == 'POST':
        # in which case we pass in that request
        form = forms.NewsInput(request.POST)

        # Check to see form is valid
        if form.is_valid():
            # do something
            print("Form validation success. Prints in console.")
            print("Title "+form.cleaned_data['title'])
            print("Original text "+form.cleaned_data['original_text'])
    return render(request, 'correct/news.html', {'form':form})
