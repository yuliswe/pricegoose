from django import template
from django.template.loader import render_to_string
from typing import Iterable
from django.conf import settings
from ipromise import must_augment

register = template.Library()


class ProductWithPriceDropInfo():

    @must_augment
    def name(self):
        return 'Unnamed Product'

    @must_augment
    def previous_price(self):
        return 10

    @must_augment
    def current_price(self):
        return 1

    @must_augment
    def image_url(self):
        return f'{settings.STATIC_URL}/assets/placeholder.png'

    @must_augment
    def price_trend(self):
        return 'down'


@register.simple_tag
def price_drop_carousel(products: Iterable[ProductWithPriceDropInfo]):
    return render_to_string('home/tags/price_drop_carousel.html', {
        'products': products
    })
