from rest_framework import serializers
from .models import Event
from offers.serializers import OfferSerializer


class EventSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    venue = serializers.CharField(max_length=50)
    genre = serializers.CharField(max_length=20)
    date = serializers.DateTimeField()
    description = serializers.CharField(max_length=255)
    offers = OfferSerializer(many=True, required=False)

    class Meta:
        model = Event
        fields = ('name', 'city', 'venue', 'genre', 'date', 'description', 'offers')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.venue = validated_data.get('venue', instance.venue)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
