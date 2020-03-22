from django.test import SimpleTestCase
from .bestbuy_usa_product_handler import BestbuyUSAProductHandler


class BestBuyUSAProductHandlerTest(SimpleTestCase):

    def test_get_product(self):
        # random BestBuy item
        test_url = 'https://www.bestbuy.com/site/apple-11-inch-ipad-pro-latest-model-with-wi-fi-128gb-space-gray/3755015.p?skuId=3755015'

        product = BestbuyUSAProductHandler.get_info(test_url)
        print(product)
