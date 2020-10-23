from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product
# Create your views here.
def index(request):
    # products = Product.objects.all()
    # # print(products)
    
    # params = {'no_of_Slides': nSlides,'range': range(1, nSlides),  'product':products}
    allProds = []
    catprods = Product.objects.values('category', 'id', 'desc')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4) )
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')



def contact(request):
    return HttpResponse("We are at Contact")


def tracker(request):
    return HttpResponse("We are at Tracker")


def search(request):
    return HttpResponse("We are at Search")


def productView(request):
    return HttpResponse("We are at ProductView")


def checkout(request):
    return HttpResponse("We are at Checkout")


