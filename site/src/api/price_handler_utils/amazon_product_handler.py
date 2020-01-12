import requests
from bs4 import BeautifulSoup
from ipromise import overrides

from .base_product_handler import BaseProductHandler


class AmazonProductHandler(BaseProductHandler):
    @overrides(BaseProductHandler)
    def __init__(self):
        super().__init__()

    @staticmethod
    @overrides(BaseProductHandler)
    def get_info(url_info):
        pass  # TODO need to use amazon API

