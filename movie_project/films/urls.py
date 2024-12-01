from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_film, name='add_film'),
    path('view/', views.view_films, name='view_films'),
]
