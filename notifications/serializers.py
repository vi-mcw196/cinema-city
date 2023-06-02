from rest_framework import serializers

from authentication.serializers import UserSerializer
from notifications.models import EmailNotification


class EmailNotificationsSerializer(serializers.ModelSerializer):
    id_owner = UserSerializer(read_only=True)

    class Meta:
        model = EmailNotification
        fields = ['id_notification', 'owner', 'Subject', 'email_body', 'send_date']
