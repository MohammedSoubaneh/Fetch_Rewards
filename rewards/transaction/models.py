from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',) 