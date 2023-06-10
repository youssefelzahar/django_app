from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def product(request):
    return render(request,'products/product.html',{'pro':Product.objects.all()})

def products(request):
    return render(request,'products/products.html',{'pro':Product.objects.all()})