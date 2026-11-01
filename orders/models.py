from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from foods.models import Fooditems

class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="address"
    )
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.username} - {self.city}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="orders"
        )
    restaurant = models.ForeignKey(
            Restaurant,
            on_delete=models.CASCADE,
            related_name="orders"
        )
    address = models.ForeignKey(
            Address,
            on_delete=models.PROTECT,
            related_name="order"
        )
    total_amount = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    food = models.ForeignKey(
        Fooditems,
        on_delete=models.CASCADE,
        related_name="order_items"
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    
    def __str__(self):
        return f"{self.food.name} x {self.quantity}"