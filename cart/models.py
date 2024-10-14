from django.db import models
from core.models import Product
from django.contrib.auth.models import User


class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return f"{self.product.title} - {self.quantity} items"

    def get_total_price(self):
        return self.product.price * self.quantity


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment


