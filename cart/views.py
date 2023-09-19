from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart
# from django.http import JsonResponse
# Create your views here.
def add_to_cart(request, product_id):
    productid = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        productname = p.product_name
        price = p.price 
        image = p.image
        
        
    totalprice = price
    try:
        cart = Cart.objects.get(productname=productname)
        return redirect('cart')
    except:
        cart=Cart(productname=productname, price=price,image=image,productid=productid,totalprice=totalprice)
        cart.save()
        return redirect('userhome')


def cart(request):
    totalitem = Cart.objects.all().count()
    cart = Cart.objects.all()
    return render(request,'cart.html',{'cart':cart,'totalitem':totalitem})

def plus_cart(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.quantity+=1
    c.totalprice = c.quantity*c.price
    c.save()
    return redirect('cart')
def minus_cart(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.quantity-=1    
    if c.quantity>=1:
        c.totalprice = c.totalprice-c.price
        c.save()
    else:
        c.quantity=0
    return redirect('cart')
def remove(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.delete()
    return redirect('cart')