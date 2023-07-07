from django.test import TestCase
from django.urls import reverse

from .models import Product, Discount


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
        self.assertTemplateUsed(response, "catalog/product_list.html")

    def test_create_pdf_with_html(self):
        pass


class DiscountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.discount = Discount.objects.create(
            discount_rate=-30,
        )

    def test_model_content(self):
        self.assertEqual(self.discount.discount_rate, -30)
