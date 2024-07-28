from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')  

    def __str__(self):
        return self.title
    
class Order(models.Model):
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.transaction_id


