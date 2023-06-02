from rest_framework import serializers

from authentication.serializers import UserSerializer
from notifications.models import EmailNotification


class EmailNotificationsSerializer(serializers.ModelSerializer):
    id_owner = UserSerializer()

    class Meta:
        model = EmailNotification
        read_only_fields = ['id_notification']
        fields = ['id_notification', 'id_owner', 'Subject', 'email_body', 'send_date']
