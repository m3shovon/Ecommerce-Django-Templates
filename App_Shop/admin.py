from django.contrib import admin
from App_Shop.models import Category, SubCategory, Product, ProductDetails
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductDetails)
