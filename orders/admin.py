from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
   model = OrderItem
   raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ['name', 'email', 'phone','status','created_at', 'updated_at']
   list_filter = ['created_at', 'updated_at']
   inlines = [OrderItemInline]