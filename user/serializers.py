from rest_framework import serializers
from user.models import MyUser, NotAttendedUser, Feedback, EventRegistration

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'

class NotAttendedSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotAttendedUser
        fields='__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventRegistration
        fields='__all__'

    def validate(self,data):
        user=data.get('user')
        event=data.get('event')
    
        if EventRegistration.objects.filter(user=user,event=event).exists():
            raise serializers.ValidationError('You are already registered for this event.')
        
        return data
