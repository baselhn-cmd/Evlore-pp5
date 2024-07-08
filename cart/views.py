from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):

    """ View cart to render users added items """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity is not None:
        quantity = int(quantity)
    else:
        quantity = 1

    if item_id in cart:
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)