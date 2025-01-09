from django.urls import path
from App_Shop import views

app_name = 'App_Shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('product/<pk>/', views.Product_Detail.as_view(), name='product_detail')
    
]