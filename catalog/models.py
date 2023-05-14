from django.db import models


class Discount(models.Model):
    discount_rate = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.discount_rate} %"


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_discount(self):
        discount = self.price * self.discount.discount_rate / 100
        return discount

    def get_price_with_discount(self):
        self.price = self.price + self.get_discount()
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product-images")
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)
