from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm
# Create your views here.

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create_news(request):
    errors = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            errors = "Форма заполнена неверно"
    form = News_postForm()
    return render(request, 'news/add_news.html', {'form': form, 'errors': errors})