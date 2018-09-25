from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
