from django.shortcuts import render
from django.views import View 
from django.views.generic import TemplateView, ListView
from .models import (
    Product,Category, SubCategory,
    Country, Service, ProductImage
)

# Create your views here.


class HomePageView(ListView):
    template_name = 'main/index.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        data['countries'] = Country.objects.all()
        # data['offers'] = Product.objects.filter(discount_gt=20)[:5]
        data['clothes'] = Product.objects.filter(sub_category__category__name='clothes')[:8]
        data['electronics'] = Product.objects.filter(sub_category__category__name='electronics')[:8]
        data['electronic'] = Category.objects.get(name__icontains='electronics')
        data['clothe'] = Category.objects.get(name__icontains='clothes')
        data['recomended'] = Product.objects.filter(recomended=True)[:12]
        data['services'] = Service.objects.filter()[:4]

        return data
    
    
class ListingGridPageView(TemplateView):
    template_name = 'main/listing-grid.html'
    
    
class ListingLargePageView(TemplateView):
    template_name = 'main/listing-large.html'
