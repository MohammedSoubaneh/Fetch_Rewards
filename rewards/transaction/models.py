from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payer = models.CharField(max_length=50)
    points = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',) 