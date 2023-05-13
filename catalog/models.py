from django.db import models


class Product(models.Model):
    class Zone(models.IntegerChoices):
        A = 10
        B = 20
        C = 30
        D = 40
        E = 50
        F = 60
        G = 70

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_rate = models.IntegerField(choices=Zone.choices, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_discount(self):
        discount = self.price * self.discount_rate / 100
        return discount

    def get_price_with_discount(self):
        self.price = self.price - self.get_discount()
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product-images")
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)
