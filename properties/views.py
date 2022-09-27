from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def properties(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'properties.html', params)


def bng(request):
    bngProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if cat == "Bangalore":
            bng = Product.objects.filter(category=cat)
            bngProds.append([bng, range(1, nSlides), nSlides])
    params = {'bngProds': bngProds}
    return render(request, 'bng.html', params)


def che(request):
    cheProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if cat == "Chennai":
            che = Product.objects.filter(category=cat)
            cheProds.append([che, range(1, nSlides), nSlides])
    params = {'cheProds': cheProds}
    return render(request, 'che.html', params)


def hyd(request):
    hydProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if cat == "Hyderabad":
            hyd = Product.objects.filter(category=cat)
            hydProds.append([hyd, range(1, nSlides), nSlides])
    params = {'hydProds': hydProds}
    return render(request, 'hyd.html', params)


def homepage(request):
    allProds = []
    catprods = Product.objects.values('popu', 'id')
    popu = {item['popu'] for item in catprods}
    for pop in popu:
        prod = Product.objects.filter(popu=pop)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if pop == True:
            popularity = Product.objects.filter(popu=pop)
            allProds.append([popularity, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'homepage.html', params)
