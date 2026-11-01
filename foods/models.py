from django.db import models
from restaurants.models import Restaurant

class Category(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Fooditems(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="food_items"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="food_items"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="foods/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    