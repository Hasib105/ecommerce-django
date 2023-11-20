from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("product_details/<pk>/", views.product_details, name="product_details"),
    path("category_details/<slug>/", views.category_details, name="category_details"),
    path('search/', views.search_items, name='search_item'),
]
