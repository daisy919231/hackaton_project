from event.models import Location, Event
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'

