from django import template
from django.template.loader import render_to_string
from typing import Iterable
from abc import ABC, abstractproperty
from django.conf import settings

register = template.Library()


class ProductWithPriceDropInfo(ABC):
    @abstractproperty
    def name(self):
        return 'Unnamed Product'

    @abstractproperty
    def original_price(self):
        return 10

    @abstractproperty
    def new_price(self):
        return 1

    @abstractproperty
    def image_url(self):
        return settings.STATIC_URL / 'webpack/assets/placeholder.jpg'

@register.simple_tag
def price_drop_carousel(products: Iterable[ProductWithPriceDropInfo]):
    return render_to_string('home/tags/price_drop_carousel/tmpl.html', {
        products: products
    })
