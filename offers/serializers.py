from rest_framework import serializers
from .models import Offer, Chat
from events.models import Event
from profiles.models import Profile
from collections import OrderedDict
from rest_framework.renderers import JSONRenderer
from datetime import datetime

class SimplifiedEventSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    venue = serializers.CharField(max_length=50)
    genre = serializers.CharField(max_length=20)
    date = serializers.DateTimeField()
    description = serializers.CharField(max_length=255)

    class Meta:
        model = Event
        fields = ('id', 'name', 'city', 'venue', 'genre', 'date', 'description')


class SimplifiedProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    age = serializers.IntegerField(source='user.age')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'bio', 'age')


class ChatSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=255)

    class Meta:
        model = Chat
        fields = ('username', 'message')


class OfferSerializer(serializers.ModelSerializer):

    # ownerId = SimplifiedProfileSerializer()
    # eventId = SimplifiedEventSerializer()
    ownerId = serializers.PrimaryKeyRelatedField(read_only=True)
    eventId = serializers.PrimaryKeyRelatedField(read_only=True)
    type = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=255)
    maxNumUsers = serializers.IntegerField()
    users = SimplifiedProfileSerializer(many=True, required=False)
    chat = ChatSerializer(many=True, required=False)

    class Meta:
        model = Offer
        fields = ('ownerId', 'eventId', 'type', 'description', 'maxNumUsers', 'users', 'chat')

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.maxNumUsers = validated_data.get('maxNumUsers', instance.maxNumUsers)
        instance.save()
        return instance