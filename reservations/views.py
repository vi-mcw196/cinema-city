from django.db import transaction
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            data = request.data

            seat_id = data.get('seat')
            screening_id = data.get('id_screening')
            if Reservation.objects.filter(seat__id=seat_id, id_screening__id=screening_id,
                                          reservation_status=Reservation.Status.BOOKED).exists():
                return JsonResponse({'detail': 'This seat is already booked for this screening.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        with transaction.atomic():  # ensure atomicity
            instance = self.get_object()

            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return JsonResponse(serializer.data)
