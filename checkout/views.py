from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'strip_public_key': 'pk_live_51JgOwKE1oxsgBFnhlb4QYmJNRNH3LMiQB8BVTQ63Em83LdylZsIrCBrE4gSP2wOSQCEvbBHnBrruS3VBTz3i4sr800yfz55a99',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
