from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('fact', views.fact, name='fact'),
    path('love', views.love, name='love'),
    path('new', views.new, name='see')
    ]