from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser
from event.models import Event

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MyUser(EmailAbstractUser):
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    event = models.ManyToManyField(Event, through='NotAttendedUser', blank=True)


    objects = EmailUserManager()

class NotAttendedUser(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    date_unavailable = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.event.name} - {self.date_unavailable}"

    @classmethod
    def get_missed_events_count(cls, user):
        # Count the number of events a user has missed
        return cls.objects.filter(user=user).count()

    @classmethod
    def is_blacklisted(cls, user):
        # Check if a user is blacklisted based on the number of missed events
        missed_events = cls.get_missed_events_count(user)
        return missed_events >= 3  # Blacklist the user if they missed 3 or more events

class Feedback(BaseModel):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    is_liked=models.BooleanField(null=True, blank=True)
    feedback_and_suggestions=models.TextField(null=True, blank=True)

class EventRegistration(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    registered_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} registered for {self.event.title}'