from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from notifications.models import EmailNotification
from notifications.serializers import EmailNotificationsSerializer


# Create your views here.
class EmailNotificationListAPIView(ListCreateAPIView):
    serializer_class = EmailNotificationsSerializer
    queryset = EmailNotification.objects.all()
    permission_classes = (permissions.AllowAny,)


class EmailNotificationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmailNotificationsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = EmailNotification.objects.all()
