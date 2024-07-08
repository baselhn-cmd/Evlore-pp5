from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ View cart to render users added items """
    return render(request, 'cart/cart.html')
