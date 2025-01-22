
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from event.serializers import EventSerializer, LocationSerializer
from event.models import Event, Location
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.
class EventListView(ListAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class EventCreateView(ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[IsAdminUser]

class EventRetrieveView(RetrieveAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    lookup_field='id'

class EventUpdate(RetrieveUpdateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[IsAdminUser]
    lookup_field='id'

class EventDelete(RetrieveDestroyAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[IsAdminUser]
    lookup_field='id'



class LocationView(ListAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer

class LocationRetrieve(RetrieveAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    lookup_field='id'

