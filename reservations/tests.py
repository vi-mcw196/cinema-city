from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.db import DatabaseError
from authentication.models import User
from cinema_halls.models import CinemaHall
from movies.models import Movie
from notifications.models import EmailNotification
from screenings.models import Screening
from reservations.models import Reservation, ReservedSeat


class ReservationModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='TestUser', password='testpassword', email='test@email.com')
        self.movie = Movie.objects.create()
        self.cinema_hall = CinemaHall.objects.create(rows=8, columns=8)
        self.screening = Screening.objects.create(
            id_movie=self.movie,
            id_owner=self.user,
            id_cinema_hall=self.cinema_hall,
            screening_time='2023-06-03 14:00:00'
        )
        self.seat = ReservedSeat.objects.create(seat_type=ReservedSeat.Type.STANDARD, seat_code='A1')
        self.email_notification = EmailNotification.objects.create(
            id_owner=self.user,
            subject='Test',
            email_body='Test Content',
        )

    def test_optimistic_locking(self):
        # create a reservation
        reservation1 = Reservation.objects.create(owner=self.user, id_notification=self.email_notification,
                                                  id_screening=self.screening, seat=self.seat, date='2023-06-03')

        # fetch the same reservation from the database
        reservation2 = Reservation.objects.get(id_reservation=reservation1.id_reservation)

        # update the first instance of the reservation
        another_seat = ReservedSeat.objects.create(seat_type=ReservedSeat.Type.VIP, seat_code='B1')  # Create a new seat
        reservation1.seat = another_seat
        reservation1.save()

        # Now, attempt to save the second instance of the reservation.
        # Because we've already updated the first instance, the versions won't match,
        # and this should raise a DatabaseError.
        with self.assertRaises(DatabaseError):
            reservation2.save()
