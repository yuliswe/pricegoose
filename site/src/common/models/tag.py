from django.db import models
from .user import User


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=255)
    discount_rqd = models.PositiveSmallIntegerField(default=0)
    price_rqd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
