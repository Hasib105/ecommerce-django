from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

@require_POST 
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = CartAddProductForm(require_POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['quantity'])
    
    return redirect('cart:cart_details')


@require_POST
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, cart/cart_detail.html,{
        'cart':cart
    })