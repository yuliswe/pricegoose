from django.db import models as m
from .user import User
from .item import Item


class Tag(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    name = m.CharField(max_length=255)
    discount_threshold = m.PositiveSmallIntegerField(default=0)
    price_threshold = m.DecimalField(max_digits=10, decimal_places=2, default=0)
    items = m.ManyToManyField(Item, through='TagItem')


class TagItem(m.Model):
    tag = m.ForeignKey(Tag, on_delete=m.CASCADE)
    item = m.ForeignKey(Item, on_delete=m.CASCADE)
    start_date = m.DateTimeField(auto_now=True)
