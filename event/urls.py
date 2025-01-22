from django.urls import path
from event.views import EventListView, EventCreateView, EventRetrieveView, EventUpdate, EventDelete, LocationView, LocationRetrieve

urlpatterns=[
    path('event_list/', EventListView.as_view(), name='event_list'),
    path('event_create/', EventCreateView.as_view(), name='event_create'),
    path('event_retrieve/<int:id>/', EventRetrieveView.as_view(), name='event_retrieve'),
    path('event_update/<int:id>/', EventUpdate.as_view(), name='event_update'),
    path('event_delete/<int:id>/', EventDelete.as_view(), name='event_delete'),
    path('location_view/', LocationView.as_view(), name='location_name'),
    path('location_retrieve/<int:id>/', LocationRetrieve.as_view(), name='location_retrive'),
    
]