from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    time = models.DateTimeField()
    level = models.CharField(max_length=50)
    message = models.TextField()
    name_logger = models.CharField(max_length=100)
    sender = models.ForeignKey(User, null=True)
