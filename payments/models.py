from django.db import models
from orders.models import Order


class Payment(models.Model):
    order = models.OneToOneField(Order, related_name='payment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.id}"
