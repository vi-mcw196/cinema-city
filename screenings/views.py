from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cinema_halls.models import Screening
from screenings.serializers import ScreeningSerializer


# Create your views here.
class ScreeningListAPIView(ListCreateAPIView):
    serializer_class = ScreeningSerializer
    queryset = Screening.objects.all()
    permission_classes = (permissions.AllowAny,)


class ScreeningDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ScreeningSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Screening.objects.all()
