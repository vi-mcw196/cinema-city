from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmailNotificationListAPIView.as_view(), name="email_notification"),
    path('<int:id>', views.EmailNotificationDetailAPIView.as_view(), name="email_notification_detail"),
]