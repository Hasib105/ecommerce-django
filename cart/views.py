from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cart.add(product=product)
        return JsonResponse({"message": "Item added to the cart", "cartItemsCount": len(cart)})
    else:
        return JsonResponse({"message": "Failed to add item to the cart"}, status=400)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)
    return redirect("cart:cart_details")


def cart_details(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_for"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "override": True}
        )
    return render(request, "cart/cart_details.html", {"cart": cart})
