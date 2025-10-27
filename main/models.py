from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Color(models.TextChoices):
        ALICEBLUE = 'aliceblue', 'AliceBlue'
        ANTIQUEWHITE = 'antiquewhite', 'AntiqueWhite'
        AQUA = 'aqua', 'Aqua'
        AQUAMARINE = 'aquamarine', 'Aquamarine'
        AZURE = 'azure', 'Azure'
        BEIGE = 'beige', 'Beige'
        BISQUE = 'bisque', 'Bisque'
        BLACK = 'black', 'Black'
        BLANCHEDALMOND = 'blanchedalmond', 'BlanchedAlmond'
        BLUE = 'blue', 'Blue'
        BLUEVIOLET = 'blueviolet', 'BlueViolet'
        BROWN = 'brown', 'Brown'
        BURLYWOOD = 'burlywood', 'BurlyWood'
        CADETBLUE = 'cadetblue', 'CadetBlue'
        CHARTREUSE = 'chartreuse', 'Chartreuse'
        CHOCOLATE = 'chocolate', 'Chocolate'
        CORAL = 'coral', 'Coral'
        CORNFLOWERBLUE = 'cornflowerblue', 'CornflowerBlue'
        CORNSILK = 'cornsilk', 'Cornsilk'
        CRIMSON = 'crimson', 'Crimson'
        CYAN = 'cyan', 'Cyan'
        DARKBLUE = 'darkblue', 'DarkBlue'
        DARKCYAN = 'darkcyan', 'DarkCyan'
        DARKGOLDENROD = 'darkgoldenrod', 'DarkGoldenRod'
        DARKGRAY = 'darkgray', 'DarkGray'
        DARKGREEN = 'darkgreen', 'DarkGreen'
        DARKKHAKI = 'darkkhaki', 'DarkKhaki'
        DARKMAGENTA = 'darkmagenta', 'DarkMagenta'
        DARKOLIVEGREEN = 'darkolivegreen', 'DarkOliveGreen'
        DARKORANGE = 'darkorange', 'DarkOrange'
        DARKORCHID = 'darkorchid', 'DarkOrchid'
        DARKRED = 'darkred', 'DarkRed'
        DARKSALMON = 'darksalmon', 'DarkSalmon'
        DARKSEAGREEN = 'darkseagreen', 'DarkSeaGreen'
        DARKSLATEBLUE = 'darkslateblue', 'DarkSlateBlue'
        DARKSLATEGRAY = 'darkslategray', 'DarkSlateGray'
        DARKTURQUOISE = 'darkturquoise', 'DarkTurquoise'
        DARKVIOLET = 'darkviolet', 'DarkViolet'
        DEEPPINK = 'deeppink', 'DeepPink'
        DEEPSKYBLUE = 'deepskyblue', 'DeepSkyBlue'
        DIMGRAY = 'dimgray', 'DimGray'
        DODGERBLUE = 'dodgerblue', 'DodgerBlue'
        FIREBRICK = 'firebrick', 'FireBrick'
        FLORALWHITE = 'floralwhite', 'FloralWhite'
        FORESTGREEN = 'forestgreen', 'ForestGreen'
        FUCHSIA = 'fuchsia', 'Fuchsia'
        GAINSBORO = 'gainsboro', 'Gainsboro'
        GHOSTWHITE = 'ghostwhite', 'GhostWhite'
        GOLD = 'gold', 'Gold'
        GOLDENROD = 'goldenrod', 'GoldenRod'
        GRAY = 'gray', 'Gray'
        GREEN = 'green', 'Green'
        

class Category(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.FileField(upload_to='images/sup_category')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'super_category'
        verbose_name = 'SuperCategory'
        verbose_name_plural = 'SuperCategroies'
        
        
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/sub_category')
    color = models.CharField(max_length=50, choices=Color.choices, default=Color.GREEN)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='sub_category')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'sub_category'
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategroies'


class DeliveryTime(models.TextChoices):
    FAST = '1-3', '1-3'
    MEDIUM = '3-5', '3-5'
    LONG = '5-15', '5-15'


class SizeChoices(models.TextChoices):
    XS = 'XS', 'Extra Small'
    S = 'S', 'Small'
    M = 'M', 'Middle'
    L = 'L', 'Large'
    XL = 'XL', 'Extra Large'


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField()
    main_image = models.FileField(upload_to='images/product')
    color = models.CharField(max_length=50, choices=Color.choices, default=Color.GOLD)
    quantity = models.PositiveIntegerField(default=1)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='product')
    guarantee = models.PositiveSmallIntegerField(default=1)
    delivery_time = models.CharField(max_length=50, choices=DeliveryTime.choices, default=DeliveryTime.FAST)
    review = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=50, choices=SizeChoices.choices, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    recomended = models.BooleanField(default=False)
    company = models.CharField(max_length=150)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='product')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class ProductImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    
    def __str__(self):
        return self.name
    
    
class Country(models.Model):
    name = models.CharField(max_length=150)
    flag = models.FileField(upload_to='images/country')
    
    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    image = models.FileField(upload_to='images/services')
    
    def __str__(self):
        return self.name
