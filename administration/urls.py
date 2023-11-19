from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('product_list/', views.product_list, name='product-list' ),
    path('order_list/', views.order_list, name='order-list' ),
    path('category_list/', views.category_list, name='category-list' ),
    path('create_product/', views.product_create, name='create-product' ),
    path('create_category/', views.category_create, name='create-category' ),
    path('update_product/<int:pk>/', views.product_update, name='update-product' ),
    path('update_category/<int:pk>/', views.category_update, name='update-category' ),
    path('delete_product/<int:pk>/', views.product_delete, name='delete-product' ),
    path('delete_category/<int:pk>/', views.category_delete, name='delete-category' ),
]
