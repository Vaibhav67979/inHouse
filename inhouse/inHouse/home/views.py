from django.shortcuts import render
from .models import Props
from math import ceil
# Create your views here.


def homepage(request):
    products = Props.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'home.html',params)
