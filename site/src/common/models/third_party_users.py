from django.db import models
from .user import User

MAX_GOOGLE_SUB_LENGTH = 255


class GoogleUser(models.Model):
    # sub is the unique identifier for all Google accounts and never reused
    #  i.e. the unique google ID
    sub = models.CharField(max_length=MAX_GOOGLE_SUB_LENGTH)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
