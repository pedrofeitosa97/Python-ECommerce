from django.db import models
from accounts.models import Account

# Create your models here.

class Cart(models.Model):
    product_id = models.IntegerField(max_length=20)
    cart_user_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="cart")
    ...