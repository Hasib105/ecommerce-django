from decimal import Decimal
import stripe
from ecommerce import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from orders.models import Order
from cart.models import CartItem



stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)

    session_id = request.session.session_key
    cart_items = CartItem.objects.filter(session_id=session_id)

    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('completed'))
        cancel_url = request.build_absolute_uri(reverse('canceled'))

        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': [],
        }

        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })

        total_price = 0
        
        session = stripe.checkout.Session.create(**session_data)

        cart_items.delete()
        
        return redirect(session.url, code=303)

    else:
        return render(request, 'process.html', locals())


def payment_completed(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    
    # Update order status to 'completed'
    order.status = 'complete'
    order.save()

    return render(request, 'completed.html')


def payment_canceled(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    
    # Update order status to 'cancel'
    order.status = 'cancel'
    order.save()

    return render(request, 'canceled.html')