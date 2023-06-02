from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MoviesSerializer


# Create your views here.
class MoviesListAPIView(ListCreateAPIView):
    serializer_class = MoviesSerializer
    queryset = Movie.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.all()
