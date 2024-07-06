from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ Display all products, handle sorting, search queries,
    and category filtering. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)