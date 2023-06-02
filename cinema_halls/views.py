from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cinema_halls.models import CinemaHall
from cinema_halls.serializers import CinemaHallSerializer


# Create your views here.
class CinemaHallListAPIView(ListCreateAPIView):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class CinemaHallDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CinemaHallSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = CinemaHall.objects.all()
