from rest_framework import serializers
from .models import Listing, Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price', 'bookings']
