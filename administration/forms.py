from django import forms
from shop.models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_image', 'price', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500', 'placeholder': 'Enter product name'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'w-full'}),
            'price': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500', 'placeholder': 'Enter price'}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500', 'placeholder': 'Enter description'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'category_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500', 'placeholder': 'Enter category name'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'w-full'}),
        }