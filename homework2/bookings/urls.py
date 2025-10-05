from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Template URLs
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/book/', views.seat_booking, name='seat_booking'),
    path('bookings/', views.booking_history, name='booking_history'),
]