from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="restaurant/", blank=True, null=True)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    