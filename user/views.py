from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from user.serializers import MyUserSerializer, FeedbackSerializer
from user.models import MyUser, NotAttendedUser, Feedback, EventRegistration
from event.models import Event
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from user.permissions import IsOwnerOrReadOnly
# Create your views here.


class UserListView(ListAPIView):
    queryset=MyUser.objects.all()
    serializer_class=MyUserSerializer

class UserRetrieveView(RetrieveAPIView):
    queryset=MyUser.objects.all()
    serializer_class=MyUserSerializer
    lookup_field='id'

class UserUpdate(RetrieveUpdateAPIView):
    queryset=MyUser.objects.all()
    serializer_class=MyUserSerializer
    permission_classes=[IsAdminUser]
    lookup_field='id'



class FeedbackListView(ListAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer

class FeedbackCreateView(ListCreateAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated]

class FeedbackRetrieveView(RetrieveAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    lookup_field='id'

class FeedbackUpdate(RetrieveUpdateAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=IsOwnerOrReadOnly
    lookup_field='id'

class FeedbackDelete(RetrieveDestroyAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=IsOwnerOrReadOnly
    lookup_field='id'

class EventRegistrationView(APIView):
    permisssion_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user=request.user
        event_id=request.data.get('event_id')

        if not event_id:
            return Response({'detail':'Event ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        event=get_object_or_404(Event, id=event_id)

        if NotAttendedUser.is_blacklisted(user):
            return Response({'detail':'You have missed three events and cannot register for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate if the user has already registered for this event
        if EventRegistration.objects.filter(user=user, event=event).exists():
            return Response({"detail": "You are already registered for this event."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        registration=EventRegistration.objects.create(user=user, event=event)
        return Response({'detail':'Registration succesful!'}, status=status.HTTP_201_CREATED)