from django.urls import path
from . import views


urlpatterns = [
    path('', views.ScreeningListAPIView.as_view(), name="screening"),
    path('<int:id>', views.ScreeningDetailAPIView.as_view(), name="screening_detail"),
]