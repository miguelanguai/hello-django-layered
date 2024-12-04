from django.test import TestCase, SimpleTestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product
from .views import ProductView
from django.urls import reverse, resolve

# Create your tests here.

# Modelo: Product
class ModelTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product1", price=4.25, stock=3)
        Product.objects.create(name="product2", price=3.02, stock=15)

    def test_product_name(self):
        item = Product.objects.get(name="product1")
        self.assertEqual(str(item.name), "product1")

    def test_product_price(self):
        item = Product.objects.get(name="product1")
        self.assertEqual(item.price, 4.25)

# Vistas: ProductView
class ViewTestCase(TestCase):
    def test_view_status_code(self):
        response = self.client.get(reverse('product_get'))
        self.assertEqual(response.status_code, 200)

# Formularios no testeados aquí por la inexistencia de los mismos, al estar empleando este proyecto solo para backend (los formularios van a frontend)

# URLs
class MyURLTestCase(SimpleTestCase):
    def test_url_resolves_to_view(self):
        resolver = resolve('/myApp/products/')
        self.assertEqual(resolver.func.view_class, ProductView)

# APIs (Django Rest Framework)
class MyAPITestCase(APITestCase):
    def test_get_items(self):
        response = self.client.get('/myApp/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)