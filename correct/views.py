from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse
from correct.forms import NewsInput, OriginalInputForm
from correct.models import NewsText

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Според           пожарникарите надежда ,  за оцелели в изгорялата сграда вече няма .\n Има обаче опасения, че броят на жертвите ще се увеличава. 		Все още има хора в неизвестност. Властите признават, че не знаят точния брой на хората, обитавали Гренфел Тауър. Въпреки че анализите на този етап показват , че конструкцията на блока е стабилна, достъпът до него е ограничен. ",
    'number': 100}
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


def ready(request):
    data = NewsText.objects.all()
    context = {
        "data": data,
        "title": "List"
    }
    # return TemplateResponse(request, 'correct/ready.html', {'data': data})
    return TemplateResponse(request, 'correct/ready.html', context)


def detail(request, id=None):
    instance = get_object_or_404(NewsText, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'correct/detail.html', context)
