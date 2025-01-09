from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect
from urllib import request
# Create your views here.
from App_Shop.models import Product, ProductDetails
# Import Views
from django.views.generic import ListView, DetailView
#mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# user log
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from App_Shop.models import Product
# from App_UserLog.models import UserLog

def home(request):
    return render(request, 'App_Shop/home.html')     
   
def about(request):
    return render(request, 'App_Shop/about.html')     
   
def contact(request):
    return render(request, 'App_Shop/contact.html')        

class Shop(ListView):
    model = Product
    template_name = 'App_Shop/shop.html'
    # by default context value is : object_list


class Product_Detail(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'App_Shop/product_details.html'  
        # by default context value is : object
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_detail = ProductDetails.objects.get(product=self.object)
        context['product_detail'] = product_detail
        return context    



# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     product_detail = get_object_or_404(ProductDetail, product=product)
#     context = {'product': product, 'product_detail': product_detail}
#     return render(request, 'App_Shop/product_details.html', context)


# @login_required
# def cart_add(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     # add the product to the user's cart here
    
#     # log the user's action
#     UserLog.objects.create(user=request.user, action='added to cart', product=product)
    
#     return redirect('cart_detail')