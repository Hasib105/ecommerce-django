from django.shortcuts import render
from django.shortcuts import render , get_object_or_404
from .models import Category, Prouct

def index(request):
    return render(request, 'shop/index.html')
  
def product_list(request, category_slug=None):
    category = None