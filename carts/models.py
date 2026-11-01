from django.db import models
from django.contrib.auth.models import User
from foods.models import Fooditems

class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}`s, Cart"
    
class Cartitems(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    food = models.ForeignKey(
        Fooditems,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.food.name} - {self.quantity}"