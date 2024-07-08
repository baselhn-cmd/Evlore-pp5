from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product
from django.db.models import Q

# Create your views here.

def all_products(request):
    """ Display all products, handle sorting, search queries,
    and category filtering. """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)



def product_detail(request, Product_id):
    """ View to show product information when product is opened """

    product = get_opbject_or_404(product, pk=Product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)