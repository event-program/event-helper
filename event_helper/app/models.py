from django.db import models


class Event(models.Model):
    pass

class Alert(models.Model):
    noti_type = models.CharField(max_length=30)
    time = models.DateTimeField()
    location = models.CharField(max_length=30)
    description = models.TextField()

# Create your models here.
