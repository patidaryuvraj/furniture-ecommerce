from django.shortcuts import render
from .models import Product
from cart.models import Cart
# Create your views here.
def userhome(request):
    totalitem = Cart.objects.all().count()
    prod = Product.objects.all()
    return render(request,'userhome.html',{'prod':prod,'totalitem':totalitem})
def prodview(request,product_id):
    totalitem = Cart.objects.all().count()
    prods = Product.objects.get(id=product_id)

    return render(request,'productview.html',{'prods':prods,'totalitem':totalitem})
