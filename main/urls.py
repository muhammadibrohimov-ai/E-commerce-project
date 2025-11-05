from django.urls import path
from .views import HomePageView, ListingGridPageView, ListingLargePageView, CategoryPageView, DetailProductView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/', CategoryPageView.as_view(), name='category'),
    path('category/sub/', ListingGridPageView.as_view(), name='sub_o'),
    path('category/<int:pk>/', ListingGridPageView.as_view(), name='sub'),
    path('category/large/', ListingLargePageView.as_view(), name='sub_l'),
    path('category/<int:pk>/large/', ListingLargePageView.as_view(), name='sub_large'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
]
