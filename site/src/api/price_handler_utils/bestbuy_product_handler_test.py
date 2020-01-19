from django.test import SimpleTestCase
from .bestbuy_product_handler import BestbuyProductHandler
from ..url_utils.url_parser import UrlParser


class BestBuyProductHandlerTest(SimpleTestCase):

    def test_get_product(self):
        test_url = 'https://www.bestbuy.ca/en-ca/product/epson-t522-colour-ink-3-pack/13836133'  # random BestBuy item
        url_info = UrlParser.parse_url(test_url)

        product = BestbuyProductHandler.get_info(url_info)
        print(product.price)
        print(product.name)
