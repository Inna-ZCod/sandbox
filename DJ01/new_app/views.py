from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'new_app/index.html', {'text_name':"BirdDjango"})


def fact(request):
    return render(request, 'new_app/fact.html')


def love(request):
    return render(request, 'new_app/love.html')


def new(request):
    return render(request, 'new_app/new.html')