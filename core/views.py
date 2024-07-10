from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.


def homepage(request):
    product_lst = Product.objects.all()
    context = {"products": product_lst}
    return render(request, 'index.html', context)


