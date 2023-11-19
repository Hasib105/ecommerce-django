from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("product_details/<pk>/", views.product_details, name="product_details"),
    path("category_details/<pk>/", views.category_details, name="category_details"),
    # TODO: Delete Redundant code for testing new templates
    path("test", views.test_template),
]
