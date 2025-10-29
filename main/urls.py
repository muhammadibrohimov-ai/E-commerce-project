from django.urls import path
from .views import HomePageView, ListingGridPageView, ListingLargePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('listing-grid/', ListingGridPageView.as_view(), name='listing-grid'),
    path('listing-large/', ListingLargePageView.as_view(), name='listing-large')
]
