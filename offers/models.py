from django.db import models
from events.models import Event
from users.models import User


class Offer(models.Model):
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='offers')
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    maxNumUsers = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='offers')


class Chat(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
