from django.shortcuts import render

# Create your views here.

def index(request, page='', subpage='', other_args=''):
    return render(request, "index.html", {"title": 'Главная'})

def bakery(request, other_args=''):
    return render(request, 'bakery.html', {"title": 'Выпечка'})