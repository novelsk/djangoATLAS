from django.db import models
from django.contrib.auth.models import User


class Ai1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    current = models.FloatField()
    sts = models.IntegerField()
