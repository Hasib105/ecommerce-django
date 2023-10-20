from django.shortcuts import render , get_object_or_404
from .models import Category, Prouct
# Create your views here.

def product_list(request, category_slug=None):
    category = None
    