import requests
import json
from ipromise import overrides
from .base_product_handler import BaseProductHandler
from urllib.parse import parse_qs, urlparse

# test for website layout no change & money format no change
from .product import Product


class BestbuyUSAProductHandler():
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_info(url):
        parsed = urlparse(url)
        sku = parse_qs(parsed.query)['skuId'][0]
        query_url = "https://api.bestbuy.com/v1/products/%s.json" % sku
        # TODO make apikey a environment variable
        payload = {'apiKey': 'xxxxxx'}
        resp = requests.get(query_url, payload)
        # ensure r is 200
        info = json.loads(resp.text)

        name = info["name"]
        salePrice = info["salePrice"]
        regularPrice = info["regularPrice"]
        image = info["image"]

        return Product(name, price, image)
