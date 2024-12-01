from django.shortcuts import render, redirect
from .models import Film

def home(request):
    return render(request, 'films/home.html')

def add_film(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        review = request.POST['review']
        Film.objects.create(title=title, description=description, review=review)
        return redirect('view_films')
    return render(request, 'films/add_film.html')

def view_films(request):
    films = Film.objects.all()
    return render(request, 'films/view_films.html', {'films': films})
