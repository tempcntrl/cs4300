from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date=date(2024, 1, 1),
            duration=120
        )
    
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)
    
    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")

class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number="A1",
            is_booked=False
        )
    
    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertFalse(self.seat.is_booked)
    
    def test_seat_booking(self):
        self.seat.is_booked = True
        self.seat.save()
        self.assertTrue(self.seat.is_booked)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date=date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
    
    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

class APITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="Testing API",
            release_date=date(2024, 1, 1),
            duration=90
        )
    
    def test_movie_list_api(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "API Test Movie")
    
    def test_seat_list_api(self):
        Seat.objects.create(seat_number="B1", is_booked=False)
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, 200)

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(
            title="View Test Movie",
            description="Testing views",
            release_date=date(2024, 1, 1),
            duration=100
        )
        self.user = User.objects.create_user(username='viewuser', password='12345')
    
    def test_movie_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Movie")
    
    def test_booking_history_view(self):
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)