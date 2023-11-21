from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Brand, Category, Product
from cart.forms import CartAddProductForm


def search_items(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    featured_products = Product.objects.filter(featured=True)[:10]

    return render(
        request,
        "shop/search_results.html",
        {
            "products": products,
            "featured_products": featured_products,
            "query": query,
        },
    )


def index(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    featured_products = Product.objects.filter(featured=True)[:10]
    latest_products = Product.objects.order_by("-created")[:12]

    return render(
        request,
        "shop/index.html",
        {
            "categories": categories,
            "brands": brands,
            "featured_products": featured_products,
            "latest_products": latest_products,
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


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(
        request,
        "shop/category_details.html",
        {"category": category, "products": products},
    )


def categories(request):
    categories = Category.objects.all()

    return render(
        request,
        "shop/categories.html",
        {
            "categories": categories,
        },
    )


def brands(request):
    brands = Brand.objects.all()

    return render(
        request,
        "shop/brands.html",
        {
            "brands": brands,
        },
    )


def brand_details(request, id):
    brand = get_object_or_404(Brand, id=id)
    products = brand.products.all()
    return render(
        request,
        "shop/brand_details.html",
        {"brand": brand, "products": products},
    )
