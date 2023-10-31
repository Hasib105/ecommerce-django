from django import forms 

from .models import Order
from cart.models import CartItem

class OrderForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Enter your name'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Enter your email'
            }
        )
    )
    phone = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Enter your phone number'
            }
        )
    )
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email']

        