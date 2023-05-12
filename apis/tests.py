from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from catalog.models import Product


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name="sneakers",
            description="Une magnifique paire de baskets",
            category="Sport",
            price=250,
        )

    def test_api_listview(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertContains(response, self.product)
