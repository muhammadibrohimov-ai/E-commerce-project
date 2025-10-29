from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'main/index.html'
    
    
class ListingGridPageView(TemplateView):
    template_name = 'main/listing-grid.html'
    
    
class ListingLargePageView(TemplateView):
    template_name = 'main/listing-large.html'
