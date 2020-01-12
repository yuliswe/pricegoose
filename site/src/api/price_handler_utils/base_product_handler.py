from src.api.exception.website_layout_exception import WebsiteLayoutException


class BaseProductHandler:
    def __init__(self):
        pass

    @staticmethod
    def get_info(url_info):
        pass

    @staticmethod
    def get_element_by_class(soup, name):
        matches = soup.find_all(class_=name)
        if len(matches) == 0:
            raise WebsiteLayoutException("Element with class name '%s' is not found" % name)

        text = matches[0].text  # ex. str $8999 ($89.99)
        if text is None or len(text) == 0:
            raise WebsiteLayoutException("No text available in given HTML element: %s" % matches[0])

        return text
