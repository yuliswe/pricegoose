from django.db import models
from .item import Item
from .tag import Tag


class SubscribedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
