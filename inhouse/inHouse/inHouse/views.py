from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def properties(request):
    return render(request, 'properties.html')


def contact(request):
    if request.method=="POST":
        print(request)
    return render(request, 'contact.html')

