from django.db import models

class SubscribedItem(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.SET_NULL)
    start_date = models.DateField()