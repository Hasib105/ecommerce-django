from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_cart'),
    path('increment/<int:id>', views.increment_quantity, name='increment'),
    path('decrement/<int:id>', views.decrement_quantity, name='decrement'),
    path('clear/', views.clear_cart, name='clear'),
    path('', views.cart_detail, name='cart_details'),
]