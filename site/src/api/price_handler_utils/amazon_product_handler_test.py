from django.test import TestCase

from .amazon_product_handler import AmazonProductHandler


class AmazonProductHandlerTest(TestCase):
    def __init__(self):
        super().__init__()
        self.price_handler = AmazonProductHandler()

    def test_get_price(self):
        pass
