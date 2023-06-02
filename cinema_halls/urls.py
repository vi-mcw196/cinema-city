from django.urls import path
from . import views


urlpatterns = [
    path('', views.CinemaHallListAPIView.as_view(), name="cinema_hall"),
    path('<int:id>', views.CinemaHallDetailAPIView.as_view(), name="cinema_hall_detail"),
]