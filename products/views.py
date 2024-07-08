from django.shortcuts import render, get_object_or_404
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



def product_detail(request, Product_id):
    """ View to show product information when product is opened """

    product = get_opbject_or_404(product, pk=Product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)