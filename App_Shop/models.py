from itertools import product
from unicodedata import category
from django.db import models
# from star_ratings.models import Rating

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
       verbose_name_plural = "Categories"     #admin panel wont use plural form on naming it

class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.category}'
    
    class Meta:
       verbose_name_plural = "Sub-Categories"

class Product(models.Model):
    product_code = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=264)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text', null=True, blank=True)
    detail_text = models.TextField(max_length=1000, verbose_name='description',  null=True, blank=True)
    price = models.FloatField()
    old_price =  models.FloatField(default=0.00)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_code} - {self.name}'

    class Meta:
        ordering = ['-created_date',]


class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'product')
    side_image_one = models.ImageField(upload_to='Products')
    side_image_two = models.ImageField(upload_to='Products')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    network = models.TextField(max_length=255, null=True, blank=True)
    os = models.TextField(max_length=255, null=True, blank=True)
    memory = models.TextField(max_length=255, null=True, blank=True)
    camera = models.TextField(max_length=255, null=True, blank=True)
    battery = models.TextField(max_length=255, null=True, blank=True)
    display = models.TextField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.product.name)
    
    class Meta:
       verbose_name_plural = "Product Details"













