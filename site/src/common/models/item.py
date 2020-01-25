from django.db import models as m


class Item(m.Model):
    url = m.CharField(max_length=2000)
