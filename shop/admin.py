from django.contrib import admin
from .models import Category, Product , Brand
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price' , 'available','created', 'updated']
    list_filter = ['available','created', 'updated']
    prepopulated_fields = {'slug':('name',)}


