from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'author', 'pub_date']
        widgets = {
            'title' : TextInput(attrs={'class':'form-control', 'placeholder': 'Введите заголовок новости'}),
            'short_description' : TextInput(attrs={'class':'form-control', 'placeholder': 'Введите краткое описание'}),
            'text' : Textarea(attrs={'class':'form-control', 'placeholder': 'Введите содержание новости'}),
            'author' : TextInput(attrs={'class':'form-control', 'placeholder': 'Введите имя автора'}),
            'pub_date' : DateTimeInput(attrs={'class':'form-control', 'placeholder': 'Дата публикации'})
        }