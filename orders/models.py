from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('cancel', 'Canceled'),
        ('complete', 'Completed'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}: {self.name}"


class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
       return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity