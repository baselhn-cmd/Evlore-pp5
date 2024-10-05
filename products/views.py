from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm
from .forms import ReviewForm
from django.views.generic import ListView, DetailView


# Create your views here.


def all_products(request):
    """ Display all products, handle sorting, search queries,
    and category filtering. """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Check if the user is authenticated before fetching wishlist
    if request.user.is_authenticated:
        wishlist_products = Wishlist.objects.filter(
            user=request.user).values_list('product_id', flat=True)
    else:
        # For anonymous users, return an empty list for wishlist products
        wishlist_products = []

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                                "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'wishlist_products': wishlist_products,
    }

    return render(request, 'products/products.html', context)



def toggle_wishlist(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user, product=product)

        if not created:
            # If the item already exists, delete it (remove from wishlist)
            wishlist_item.delete()
            in_wishlist = False
        else:
            in_wishlist = True

        return JsonResponse({'in_wishlist': in_wishlist})
    return JsonResponse({'error': 'User not authenticated'}, status=403)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.Product = product
            review.created_by = request.user
            review.save()
            return redirect('product_detail', product_id=product_id)

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Allow staff or superusers to add a new product to the store.
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can add products"
        )
        return redirect(reverse("home"))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    # simply to query all products for now, till full CRUD is checked
    products = Product.objects.all()
    return render(
        request, 'products/add_product.html', {
            'form': form, 'products': products})


@login_required
def edit_product(request, product_id):
    """
    Allow staff or superusers to edit an existing product's details.
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can add products"
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    Allow staff or superusers to delete a product from the store.
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can add products"
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('add_product')


def submit_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)  # Default to 3 if not provided
        review_content = request.POST.get('review')

        if review_content:  # Ensure the review content is provided
            # Create a new review object
            review = Review.objects.create(
                Product=product,
                rating=rating,
                content=review_content,
                created_by=request.user
            )
            review.save()
            messages.success(request,
                             'Your review has been submitted successfully!')
        else:
            messages.error(request, 'Please provide a review.')

        return redirect('product_detail', product_id=product.id)

    return render(request, 'product_detail.html', {'product': product})
