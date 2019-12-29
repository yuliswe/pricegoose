import requests
from bs4 import BeautifulSoup
from ipromise import overrides

from .base_price_handler import BasePriceHandler


# test for website layout no change & money format no change
from ..exception.website_layout_exception import WebsiteLayoutException


class BestbuyPriceHandler(BasePriceHandler):
    @overrides(BasePriceHandler)
    def __init__(self):
        super().__init__()

    @staticmethod
    @overrides(BasePriceHandler)
    def get_price(url_info):
        req = requests.get(url_info.url)
        soup = BeautifulSoup(req.content, "html.parser")
        matches = soup.find_all(class_='price_FHDfG')
        if len(matches) == 0:
            raise WebsiteLayoutException("Element with class name 'price_FHDfG' is not found")

        price_str = matches[0].text  # ex. str $8999 ($89.99)
        if price_str is None or len(price_str) == 0:
            raise WebsiteLayoutException("No price available in given HTML element: %s" % matches[0])

        if price_str[0] != '$':
            raise WebsiteLayoutException("Price is not start with '$': %s." % price_str)

        price_str = price_str[1:]  # ex. str 8999
        if price_str.isdigit() is False:
            raise WebsiteLayoutException("Price format error %s" % price_str)

        price = int(price_str)  # ex. int 8999
        return price
