
from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, InlineModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Product,Category, SubCategory,
    Country, Service, ProductImage
)

# Register your models here.



class ProductImageModelAdmin(TabularInline):
    model = ProductImage
    extra = 3


class SubCategoryModelAdmin(TabularInline):
    model = SubCategory
    extra = 3


@admin.register(Product)
class ProductModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['title', 'price', 'quantity', 'size', 'sub_category', 'recomended']
    search_fields = ['title', 'desc', 'country', 'company', 'size']
    list_filter = ['sub_category', 'recomended', 'size', 'company']
    list_display_links = ['title', 'price', 'quantity', 'size', 'sub_category', 'recomended']
    ordering = ['-created_at']
    inlines = [ProductImageModelAdmin,]


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name', 'title', 'color']
    search_fields = ['name', 'title', 'desc']
    list_filter = ['color']
    inlines = [SubCategoryModelAdmin,]


@admin.register(Service)
class ServiceModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Country)
class CountryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']


    




