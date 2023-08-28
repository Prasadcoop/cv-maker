from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    Ptype = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    
