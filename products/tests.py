from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class ProductAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        url = reverse('product-list', kwargs={'version': 'v1'})
        data = {
            "name": "Laptop",
            "description": "Gaming laptop",
            "price": 50000.00,
            "stock": 10
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201)
