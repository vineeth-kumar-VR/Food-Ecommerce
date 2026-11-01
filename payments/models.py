from django.db import models
from orders.models import Order

class Payment(models.Model):
    PAYMENT_STATUS = [
        ('pending','Pending'),
        ('success','Success'),
        ('failed','Failed')
    ]
    PAYMENT_CHOICE = [
        ('upi','UPI'),
        ('card','CARD'),
        ('cash','Cash on Delivery')
    ]
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICE
    )
    transaction_id = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.order.id}"