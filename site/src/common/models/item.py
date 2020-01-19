from django.db import models


class Item(models.Model):
    url = models.CharField(max_length=2000)
    name = models.CharField(max_length=100)
