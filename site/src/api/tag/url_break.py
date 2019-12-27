from urllib.parse import urlparses

url = 'https://www.canadiantire.ca/en/pdp/dyson-v11-absolute-stick-vacuum-0438226p.html#srp'

class Url:
    company_name = ''
    nations = ''
    url = ''

    def __init__(self, url):
        self.url = url
        parse_url

    def parse_url(self):
        url_parse_ele = urlparse(self.url)
        netloc = url_parse_ele[1].split('.')
        self.company_name = netloc[1]
        self.nations = netloc[2]


