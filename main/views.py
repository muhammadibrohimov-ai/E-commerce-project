from django.shortcuts import render
from django.views import View 
from django.views.generic import TemplateView, ListView
from .models import Category, Product, Country

# Create your views here.


class HomePageView(View):
    template_name = 'main/index.html'
    
    
class ListingGridPageView(TemplateView):
    template_name = 'main/listing-grid.html'
    
    
class ListingLargePageView(TemplateView):
    template_name = 'main/listing-large.html'
