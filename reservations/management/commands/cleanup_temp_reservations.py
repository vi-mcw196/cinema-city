from django.core.management.base import BaseCommand
from django.utils import timezone
from reservations.models import TempReservation


class Command(BaseCommand):
    help = 'Removes expired temporary reservations'

    def handle(self, *args, **options):
        now = timezone.now()
        expired_reservations = TempReservation.objects.filter(created_at__lte=now)
        count = expired_reservations.count()
        expired_reservations.delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} expired temporary reservations'))
