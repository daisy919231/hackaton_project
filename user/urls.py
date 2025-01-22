from django.urls import path
from user.views import EventRegistrationView, UserListView, UserRetrieveView, FeedbackCreateView, FeedbackListView, FeedbackRetrieveView, FeedbackDelete, FeedbackUpdate
urlpatterns=[
    path('event/register/', EventRegistrationView.as_view(), name='event_register'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_retrieve/<int:id>/', UserRetrieveView.as_view(), name='user_retrieve'),
    path('feedback_list/', FeedbackListView.as_view(), name='feedback_list'),
    path('feed_back_create/<int:id>/',FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedback_retrieve/<int:id>/', FeedbackRetrieveView.as_view(), name='feedback_retrieve'),
    path('feedback_update/<int:id>/', FeedbackUpdate.as_view(), name='feedback_update'),
    path('feedback_delete/<int:id>/', FeedbackDelete.as_view(), name='feedback_delete')
]