from django.db import models

from authentication.models import User


# Create your models here.
class EmailNotification(models.Model):
    id_notification = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    email_body = models.CharField(max_length=100)
    send_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-send_date']

    def __str__(self):
        return self.subject
