from django.shortcuts import render
from django.views.generic import ListView, FormView


def home(request):
    return render(request, 'main/home.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})


def contact(request):
    return render(request, 'main/contact.html', {'title': 'Связаться с нами'})

