from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
