# from bs4 import BeautifulSoup
# import requests


# class PriceFetcher:

#     def __init__(self, url):
#         self.url = url
#         pass

#     def parse(self, class_name):
#         req = requests.get(self.url)
#         soup = BeautifulSoup(req.content, "html.parser")
#         result = soup.find_all(class_=class_name)
