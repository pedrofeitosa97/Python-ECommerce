from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    ...