from django.test import TestCase
from django.urls import reverse


from .models import Product


class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name="Bicyclette",
            description="Un super vélô de competition",
            category="Sport",
            price=1250.99,
        )

    def test_product_content(self):
        self.assertEqual(self.product.name, "Bicyclette")
        self.assertEqual(self.product.description, "Un super vélô de competition")
        self.assertEqual(self.product.category, "Sport")
        self.assertEqual(self.product.price, 1250.99)

    def test_product_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Un super vélô de competition")
        self.assertTemplateUsed(response, "product_list.html")
