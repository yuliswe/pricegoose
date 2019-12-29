from django.test import SimpleTestCase
from .bestbuy_price_handler import BestbuyPriceHandler
from ..url_utils.url_parser import UrlParser


class BestBuyPriceHandlerTest(SimpleTestCase):

    def test_get_price(self):
        test_url = 'https://www.bestbuy.ca/en-ca/product/epson-t522-colour-ink-3-pack/13836133'  # random BestBuy item
        url_info = UrlParser.parse_url(test_url)

        price = BestbuyPriceHandler.get_price(url_info)
        print(price)

