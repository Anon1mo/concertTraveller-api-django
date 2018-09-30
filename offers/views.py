from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from .models import Offer
from events.models import Event
from profiles.models import Profile
from .serializers import OfferSerializer
from events.serializers import EventSerializer


class OfferList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OfferSerializer

    def get_queryset(self):
        offers = Offer.objects.all()
        userid = self.request.query_params.get('userId', None)
        eventid = self.request.query_params.get('eventId', None)
        ownerid = self.request.query_params.get('ownerId', None)
        if userid is not None:
            offers = offers.filter(users__id=userid)
        elif eventid is not None:
            offers = offers.filter(eventId=eventid)
        elif ownerid is not None:
            offers = offers.filter(ownerId=ownerid)
        return offers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        ownerId = self.request.data['ownerId']
        owner_instance = Profile.objects.get(pk=ownerId)
        eventId = self.request.data['eventId']
        event_instance = Event.objects.get(pk=eventId)
        serializer.save(ownerId=owner_instance, eventId=event_instance)


class OfferDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Offer.objects.get(pk=pk)
        except Offer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        offer = self.get_object(pk)
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        offer = self.get_object(pk)
        serializer = OfferSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        offer = self.get_object(pk)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OfferJoin(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Offer.objects.get(pk=pk)
        except Offer.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        offer = self.get_object(pk)
        user = Profile.objects.get(pk=request.user.id)
        offer.users.add(user)
        offer.save()
        return Response('You have successfully joined the offer')


class OfferLeave(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Offer.objects.get(pk=pk)
        except Offer.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        offer = self.get_object(pk)
        user = Profile.objects.get(pk=request.user.id)
        offer.users.remove(user)
        offer.save()
        return Response('You have successfully left the offer')
