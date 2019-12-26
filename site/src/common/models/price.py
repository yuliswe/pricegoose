from django.db import models
from enum import IntEnum
from .item import Item


class Currency(IntEnum):
    cad = 1
    usd = 1


class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.PositiveSmallIntegerField()
