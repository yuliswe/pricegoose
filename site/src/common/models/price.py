from django.db import models


class Price(models.Model):
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    time = models.TimeField()
    amount = models.DecimalField(decimal_places=2)
    currency = models.CharField(max_length=64)
