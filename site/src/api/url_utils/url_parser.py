from urllib.parse import urlparse

from src.api.url_utils.url_info import UrlInfo

# url = 'https://www.canadiantire.ca/en/pdp/dyson-v11-absolute-stick-vacuum-0438226p.html#srp'


class UrlParser:

    @staticmethod
    def parse_url(url):
        url_parse_ele = urlparse(url)
        netloc = url_parse_ele[1].split('.')
        company = netloc[1]
        nation = netloc[2]
        url_info = UrlInfo(url, company, nation)
        return url_info

