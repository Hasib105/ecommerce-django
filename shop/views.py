from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

from cart.models import CartItem


def index(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)[:10]
    latest_products = Product.objects.order_by("-created")[:12]

    session_id = request.session.session_key
    cart_items = len(CartItem.objects.filter(session_id=session_id))
    
    return render(
        request,
        "shop/index.html",
        {
            "categories": categories,
            "featured_products": featured_products,
            "latest_products": latest_products,
            "cart_items": cart_items,
        },
    )


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = product.category.products.exclude(id=product.id)[:5]
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/product_details.html",
        {
            "product": product,
            "related_products": related_products,
            "cart_product_form": cart_product_form,
        },
    )


def category_details(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(
        request,
        "shop/category_details.html",
        {"category": category, "products": products},
    )


#TODO: Delete Redundant code for testing new templates
def test_template(request):
    return render(request, "shop/product_details.html")
