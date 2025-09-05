from django.urls import path
from .views import DestinationListCreateView

urlpatterns = [
    path("destinations/", DestinationListCreateView.as_view(), name="destination-list"),
]
