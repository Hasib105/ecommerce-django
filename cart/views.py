from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from django.contrib.sessions.models import Session
from .models import CartItem
from django.contrib import messages

# Create your views here.

def add_to_cart(request, id):
    session_id = request.session.session_key

    # Check if the session_id exists, and create a new one if it doesn't
    if not session_id:
        request.session.create()

    session_id = request.session.session_key
    cart_item, created = CartItem.objects.get_or_create(
        product_id=id, session_id=session_id
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_details')


def cart_detail(request):
    session_id = request.session.session_key
    cart_items = CartItem.objects.filter(session_id=session_id)
    
    total_price = 0
    
    for item in cart_items:
        total_price += item.quantity * item.product.price

    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def increment_quantity(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_details')


def decrement_quantity(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity -= 1
    cart_item.save()

    if cart_item.quantity <= 0:
        cart_item.delete()
    return redirect('cart_details')


def remove_from_cart(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart_details')


def clear_cart(request):
    cart_items = CartItem.objects.all()
    cart_items.delete()
    messages.success(request, 'Cart cleared.')
    return redirect('cart_details')