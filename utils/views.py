from django.http import JsonResponse
from rest_framework import status


def handle404(request, exception):
    message = 'The endpoint is not found'

    response = JsonResponse(data={'message': message, 'status_code': status.HTTP_404_NOT_FOUND})
    response.status_code = status.HTTP_404_NOT_FOUND
    return response


def handle500(request):
    message = 'An error occurred, it is on us. Please try again later.'

    response = JsonResponse(data={'message': message, 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR})
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return response
