from django.test import SimpleTestCase
from django.urls import resolve

from apps.products.views import ProductViewSet


class ProductUrlsTests(SimpleTestCase):
    def test_products_route_is_registered(self):
        match = resolve("/products/products/")
        self.assertEqual(match.func.cls, ProductViewSet)
