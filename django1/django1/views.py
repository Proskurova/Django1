from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 5+5
    return render(request, 'about.html', {'greeting': a})


def home(request):
    return render(request, 'home.html')