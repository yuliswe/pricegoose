import requests
from bs4 import BeautifulSoup
from ipromise import overrides

from .base_price_handler import BasePriceHandler


class AmazonPriceHandler(BasePriceHandler):
    @overrides(BasePriceHandler)
    def __init__(self):
        super().__init__()

    @staticmethod
    @overrides(BasePriceHandler)
    def get_price(url_info):
        pass  # TODO need to use amazon API

