from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser


class Alert(models.Model):
    noti_type = models.CharField(max_length=30)
    time = models.DateTimeField()
    location = models.CharField(max_length=30)
    description = models.TextField()

# Create your models here.


class Alert(models.Model):
    Alert_type = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    time = models.DateTimeField()
    location = models.CharField(max_length=30)
    description = models.TextField()


class Participant(models.Model):
    user_id = models.CharField(max_length=60,blank=True)
    username = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    language = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    question_5 = models.CharField(max_length=30, blank=True)
    question_6 = models.CharField(max_length=30, blank=True)
    question_7 = models.CharField(max_length=30, blank=True)
    question_8 = models.CharField(max_length=30, blank=True)
    question_9 = models.CharField(max_length=30, blank=True)
    qr_code = models.TextField()
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id

    def save(self):
        self.id = self.username + self.phone
        super(Participant, self).save()


class Event(models.Model):
    entry = models.ManyToManyField(Participant)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=30)
    description = models.TextField()

    question_5 = models.CharField(max_length=50, blank=True)
    question_6 = models.CharField(max_length=50, blank=True)
    question_7 = models.CharField(max_length=50, blank=True)
    question_8 = models.CharField(max_length=50, blank=True)
    question_9 = models.CharField(max_length=50, blank=True)

