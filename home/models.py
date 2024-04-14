from django.db import models
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sold_quantity = models.IntegerField(default=0)
    remaining_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    origin = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def discounted_price(self):
        discount_amount = Decimal(self.price) * Decimal(self.discount) / Decimal(100)
        discounted_price = Decimal(self.price) - discount_amount
        return discounted_price
    
    def __str__(self):
        return self.name
