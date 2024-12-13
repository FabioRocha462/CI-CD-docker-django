from Docker.tests import test_base
from django.urls import reverse_lazy, reverse
class Test_Model_Product(test_base.BaseTestCore):
    def test_create_product(self):
        product = self.create_product()
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'product test')
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.quantity, 12)
    def test_url_product_detail(self):
        product = self.create_product()
        url = reverse_lazy('product:product_detail' , kwargs={'pk':product.pk})
        self.assertEqual(url, f'/product/{product.pk}/')
    def test_url_product_list(self):
        product = self.create_product()
        url = reverse_lazy('product:list_products')
        self.assertEqual(url, f'/product/list/')