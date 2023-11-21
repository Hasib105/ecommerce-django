from django.shortcuts import render, redirect
from shop.models import Product, Category , Brand
from orders.models import Order, OrderItem
from .forms import ProductForm, CategoryForm , BrandForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def dashboard(request):
    product = Product.objects.count()
    order_items = OrderItem.objects.filter(order__status="complete")
    total_cost = sum(item.get_cost() for item in order_items)
    orders = Order.objects.count()
    # earn = sum(item.get_cost() for order in orders for item in order.items.all())
    return render(
        request,
        "admin/dashboard.html",
        {"product": product, "orders": orders, "total_cost": total_cost},
    )


@login_required(login_url='/login/')
def order_list(request):
    orders = Order.objects.order_by("-id")
    total = Order.objects.count()
    complete = Order.objects.filter(status="complete").count()
    pending = Order.objects.filter(status="pending").count()
    cancel = Order.objects.filter(status="cancel").count()
    return render(
        request,
        "admin/order/list.html",
        {
            "orders": orders,
            "complete": complete,
            "pending": pending,
            "cancel": cancel,
            "total": total,
        },
    )


@login_required(login_url='/login/')
def product_list(requset):
    products = Product.objects.order_by("-id")

    return render(requset, "product/product_list.html", {"products": products})


@login_required(login_url='/login/')
def category_list(requset):
    categories = Category.objects.order_by("-id")

    return render(requset, "category/category_list.html", {"categories": categories})

@login_required(login_url='/login/')
def brand_list(requset):
    brands = Brand.objects.order_by("-id")

    return render(requset, "brand/brand_list.html", {"brands": brands})

@login_required(login_url='/login/')
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm()
    return render(request, "product/create.html", {"form": form})


@login_required(login_url='/login/')
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("category-list")
    else:
        form = CategoryForm()
    return render(request, "category/create.html", {"form": form})

@login_required(login_url='/login/')
def brand_create(request):
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("brand-list")
    else:
        form = BrandForm()
    return render(request, "brand/create.html", {"form": form})


@login_required(login_url='/login/')
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm(instance=product)
    return render(request, "product/update.html", {"form": form})


@login_required(login_url='/login/')
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect("product-list")


@login_required(login_url='/login/')
def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category-list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category/update.html", {"form": form})


@login_required(login_url='/login/')
def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect("category-list")




@login_required(login_url='/login/')
def brand_update(request, pk):
    brand = Brand.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect("brand-list")
    else:
        form = CategoryForm(instance=brand)
    return render(request, "brand/update.html", {"form": form})


@login_required(login_url='/login/')
def brand_delete(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand.delete()
    return redirect("brand-list")