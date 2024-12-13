from django.test import TestCase
import datetime
from product.models import Product

class BaseTestCore(TestCase):

    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()
    
    def create_product(self):

        product = Product(
            name = "product test",
            quantity = 12,
            price = 10.99,
        )
        product.save()
        return product
