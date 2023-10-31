from django.db import models
from shop.models import Product
# Create your models here.


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(default=1)
    session_id = models.CharField(max_length=32 , default="")

    def total_cost(self):
        return self.quantity * self.product.price

