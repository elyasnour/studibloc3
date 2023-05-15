from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from catalog.models import Product


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name="Product1",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
            category="Category1",
            price=99.99,
        )

    def test_api_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertContains(response, self.product)
