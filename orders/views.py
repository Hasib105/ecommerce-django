from django.shortcuts import render,redirect
from django.urls import reverse
from cart.models import CartItem
from .models import Order, OrderItem
from .forms import OrderForm


def create_order(request):
    session_id = request.session.session_key
    cart_items = CartItem.objects.filter(session_id=session_id)
    total_price = 0

    for item in cart_items:
        total_price += item.quantity * item.product.price

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            

            # Save the order
            order.save()

            # Associate the cart items with the order
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )

        # cart_items.delete()

        request.session['order_id']=order.id

        # Additional logic to handle the order creation
        #return render(request, 'order_success.html', {'order': order})
        return redirect('payment_process')
