from django.shortcuts import render
from django.shortcuts import render , get_object_or_404
from .models import Category, Prouct

def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {
        'categories' : categories
    })
  
