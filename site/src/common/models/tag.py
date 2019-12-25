from django.db import models

class Tag(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=255)
    discount_rqd = models.PositiveSmallIntegerField(max_digits=2, decimal_places=2, default=0)
    price_rqd = models.DecimalField(decimal_places=2, default=0)
