from django.db import models as m
from .item import Item


class Price(m.Model):

    class Currency(m.IntegerChoices):
        CAD = 1
        USD = 2

    item = m.ForeignKey(Item, on_delete=m.CASCADE)
    time = m.DateTimeField()
    amount = m.DecimalField(max_digits=10, decimal_places=2)
    currency = m.PositiveSmallIntegerField()
