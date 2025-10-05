from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# API ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        seat = self.get_object()
        if seat.is_booked:
            return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
        seat.is_booked = True
        seat.save()
        return Response({'status': 'seat booked'})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        queryset = Booking.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    def perform_create(self, serializer):
        seat = serializer.validated_data['seat']
        if seat.is_booked:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("This seat is already booked")
        seat.is_booked = True
        seat.save()
        serializer.save()

# Template Views
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

from django.http import HttpResponseRedirect

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Natural sort: A1, A2, ..., A9, A10 instead of A1, A10, A2, ...
    from django.db.models import CharField, Value
    from django.db.models.functions import Length, Substr
    
    seats = Seat.objects.annotate(
        row=Substr('seat_number', 1, 1),
        num=Substr('seat_number', 2)
    ).order_by('row', Length('num'), 'num')
    
    # Check which seats are already booked for THIS movie
    booked_seat_ids = Booking.objects.filter(movie=movie).values_list('seat_id', flat=True)
    
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        user_id = request.POST.get('user', 1)
        
        try:
            seat = Seat.objects.get(id=seat_id)
            
            # Check if this seat is already booked for THIS movie
            if Booking.objects.filter(movie=movie, seat=seat).exists():
                messages.error(request, 'This seat is already booked for this movie!')
            else:
                user = User.objects.get(id=user_id)
                
                Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user=user
                )
                messages.success(request, f'Successfully booked seat {seat.seat_number}!')
                return HttpResponseRedirect('/bookings/')
        except Exception as e:
            messages.error(request, f'Error booking seat: {str(e)}')
    
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats,
        'booked_seat_ids': booked_seat_ids,
    })

def booking_history(request):
    bookings = Booking.objects.all().select_related('movie', 'seat', 'user')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})