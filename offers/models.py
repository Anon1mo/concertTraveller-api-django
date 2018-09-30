from django.db import models
from events.models import Event
from profiles.models import Profile


class Offer(models.Model):
    ownerId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='offers')
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    maxNumUsers = models.IntegerField(default=0)
    users = models.ManyToManyField(Profile, related_name='offers')

    def __str__(self):
        return self.ownerId.user.username


class Chat(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='chat')
