from django.shortcuts import render
from django.http import HttpResponse
from correct.forms import NewsInput, OriginalInputForm

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from vews.py"}
    return render(request, 'correct/index.html', context=my_dict)


def original_input_form(request):
    form = OriginalInputForm()

    if request.method == "POST":
        form = OriginalInputForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'correct/text.html', {'form':form})
