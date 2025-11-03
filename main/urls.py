from django.urls import path
from .views import HomePageView, ListingGridPageView, ListingLargePageView, CategoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/', CategoryPageView.as_view(), name='category'),
    path('category/<int:pk>/', ListingGridPageView.as_view(), name='sub'),
]
