from django.test import TestCase

from .amazon_price_handler import AmazonPriceHandler


class AmazonPriceHandlerTest(TestCase):
    def __init__(self):
        super().__init__()
        self.price_handler = AmazonPriceHandler()

    def test_get_price(self):
        pass

