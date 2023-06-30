from django.contrib import admin
from .models import Product, Computer, Order, OrderItem 


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "category",
        "price",
        "product_id",
    ]

class ComputerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "RAM",
        "hard_drive",
        "CPU",
        "display",
        "OS",
        "soundcard",
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Computer, ComputerAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_num",
        "total",
    ]
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
   #     "order",
        "computer",
        "price",
    ]
admin.site.register(OrderItem, OrderItemAdmin)