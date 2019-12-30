import requests
from bs4 import BeautifulSoup
from ipromise import overrides

from .base_product_handler import BaseProductHandler

# test for website layout no change & money format no change
from .product import Product
from ..exception.website_layout_exception import WebsiteLayoutException


class BestbuyProductHandler(BaseProductHandler):
    price_keyword = 'price_FHDfG'
    name_keyword = 'productName_19xJx'

    @overrides(BaseProductHandler)
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_price(soup):
        price_str = BaseProductHandler.get_element_by_class(soup, BestbuyProductHandler.price_keyword)
        if price_str[0] != '$':
            raise WebsiteLayoutException("Price is not start with '$': %s." % price_str)

        price_str = price_str[1:]  # ex. str 8999
        if price_str.isdigit() is False:
            raise WebsiteLayoutException("Price format error %s" % price_str)

        price = int(price_str)  # ex. int 8999
        return price

    @staticmethod
    def get_name(soup):
        name_str = BaseProductHandler.get_element_by_class(soup, BestbuyProductHandler.name_keyword)
        return name_str

    @staticmethod
    @overrides(BaseProductHandler)
    def get_info(url_info):
        req = requests.get(url_info.url)
        soup = BeautifulSoup(req.content, "html.parser")
        price = BestbuyProductHandler.get_price(soup)
        name = BestbuyProductHandler.get_name(soup)
        # image = BestbuyProductHandler.get_image(soup)

        return Product(name, price, None)
