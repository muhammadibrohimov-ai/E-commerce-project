from django.shortcuts import render
from django.views import View 
from django.views.generic import TemplateView, ListView, DetailView
from .models import (
    Product,Category, SubCategory,
    Country, Service, ProductImage, SizeChoices, DeliveryTime, Country
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
        data['recomended'] = Product.objects.filter(recomended=True,)
        data['services'] = Service.objects.filter()[:4]
        data['discount'] = Product.objects.filter(discount__gte=20)

        return data


class CategoryPageView(ListView):
    model = Category
    template_name = 'main/category.html'
    context_object_name = 'categories'


class ListingGridPageView(ListView):
    template_name = 'main/listing-grid.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        sub_id = self.kwargs.get('pk')
        return Product.objects.filter(sub_category__id=sub_id)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sub_id'] = self.kwargs.get('pk')
        return data

    
    
class ListingLargePageView(ListView):
    template_name = 'main/listing-large.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        sub_id = self.kwargs.get('pk')
        return Product.objects.filter(sub_category__id=sub_id)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sub_id'] = self.kwargs.get('pk')
        data['subs'] = SubCategory.objects.all()

        return data

class DetailProductView(DetailView):
    model = Product
    template_name = 'main/detail-product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['images'] = ProductImage.objects.filter(product__id = self.kwargs['pk'])
        return data
