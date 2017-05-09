from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView

from BEMSapi.serializers import ResourceReservationSerializer, ProfileResourceReservationSerializer, \
    GroupResourceReservationSerializer
from resources.models import ProfileResourceReservation, GroupResourceReservation


class ProfileResourceReservationCreateView(CreateAPIView):
    serializer_class = ProfileResourceReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupResourceReservationCreateView(CreateAPIView):
    serializer_class = GroupResourceReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileResourceReservationUpdateView(UpdateAPIView):
    serializer_class = ProfileResourceReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProfileResourceReservation.objects.all()


class GroupResourceReservationUpdateView(UpdateAPIView):
    serializer_class = GroupResourceReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = GroupResourceReservation.objects.all()