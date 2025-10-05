from django.core.management.base import BaseCommand
from bookings.models import Movie, Seat
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample movies and seats'

    def handle(self, *args, **kwargs):
        # Create movies
        movies_data = [
            {
                'title': 'The Matrix',
                'description': 'A computer hacker learns about the true nature of reality.',
                'release_date': date(1999, 3, 31),
                'duration': 136
            },
            {
                'title': 'Inception',
                'description': 'A thief who steals corporate secrets through dream-sharing technology.',
                'release_date': date(2010, 7, 16),
                'duration': 148
            },
            {
                'title': 'Interstellar',
                'description': 'A team of explorers travel through a wormhole in space.',
                'release_date': date(2014, 11, 7),
                'duration': 169
            },
        ]
        
        for movie_data in movies_data:
            Movie.objects.get_or_create(**movie_data)
        
        # Create seats (A1-A10, B1-B10)
        for row in ['A', 'B', 'C', 'D']:
            for num in range(1, 11):
                seat_number = f"{row}{num}"
                Seat.objects.get_or_create(seat_number=seat_number)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database'))