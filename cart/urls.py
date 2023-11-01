from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increment/<int:id>', views.increment_quantity, name='increment_quantity'),
    path('decrement/<int:id>', views.decrement_quantity, name='decrement_quantity'),
    path('clear/', views.clear_cart, name='clear'),
    path('', views.cart_details, name='cart_details'),
]