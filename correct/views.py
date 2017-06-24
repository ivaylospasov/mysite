from django.shortcuts import render
from django.http import HttpResponse
from correct.forms import NewsInput, OriginalInputForm

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Според           пожарникарите надежда ,  за оцелели в изгорялата сграда вече няма . Има обаче опасения, че броят на жертвите ще се увеличава. 		Все още има хора в неизвестност. Властите признават, че не знаят точния брой на хората, обитавали Гренфел Тауър. Въпреки че анализите на този етап показват , че конструкцията на блока е стабилна, достъпът до него е ограничен. ",
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
