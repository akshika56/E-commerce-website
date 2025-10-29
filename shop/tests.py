from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Toy Car",
            description="A small toy car for kids.",
            price=9.99,
            stock=100,
            image="path/to/image.jpg"
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Toy Car")
        self.assertEqual(self.product.price, 9.99)
        self.assertEqual(self.product.stock, 100)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Toy Car")