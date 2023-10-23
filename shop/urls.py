from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path("product_details/<pk>/", views.product_details, name="product_details"),
]
