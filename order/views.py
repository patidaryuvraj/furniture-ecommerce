from django.shortcuts import render,redirect
from cart.models import Cart
from.models import Orderdetails
import stripe
# Create your views here.
stripe.api_key='sk_test_51NFsV7SHx446vnNfI6oI7XtCbAYiFHCe8ZILk7Ds4ikWohi9XKGkVaF6kZklyB5aiWWvPIKKCKNxpbOvis6rvmgL0001di4pFt'
def checkout_session(request,cart_id):
    if request.method=="POST":

        
        cart = Cart.objects.get(id = cart_id)
        session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[{
                'price_data': {
                'currency': 'inr',
                'product_data': {
                'name': cart.productname,
                },
                'unit_amount': cart.price*100,
                },
                'quantity': cart.quantity,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/pay_success',
            cancel_url='http://127.0.0.1:8000/pay_cancel',
            
        )
        
        productname = cart.productname
        quantity = cart.quantity
        price = cart.price
        image = cart.image
        totalprice = cart.totalprice
        order = Orderdetails(productname = productname,quantity = quantity,price = price,image = image,totalprice=totalprice)
        order.save()
        cart.delete()

        return redirect(session.url,code = 303)
        
    else:
        return redirect('cart')
def pay_success(request):
    totalitem = Cart.objects.all().count()
    return render(request,'paysuccess.html',{'totalitem':totalitem})
def pay_cancel(request):
    totalitem = Cart.objects.all().count()
    return render(request,'paycancel.html',{'totalitem':totalitem})
# def ordersave(request,cart_id):
#     if request.method=="POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         mobile = request.POST['mobile']
#         address = request.POST['address']
    
#         cart = Cart.objects.get(id = cart_id)
#         for c in cart:
#             productname = c.productname
#             quantity = c.quantity
#             price = c.price
#             image = c.image
#             totalprice = c.totalprice
#         order = Orderdetails(username = name,email = email,mobile = mobile,address = address,productname = productname,quantity = quantity,price = price,image = image,totalprice=totalprice)
#         order.save()
#         cart.delete()
#         totalitem = Cart.objects.all().count()
#         return render(request,'cart.html',{'totalitem':totalitem})
#         # return redirect('cart')
#     else:
#         return redirect('cart')
def orderdetail(request):
    orderdetailsitem = Orderdetails.objects.all().count()
    orderdetails = Orderdetails.objects.all()
    totalitem = Cart.objects.all().count()
    return render(request,'orderdetail.html',{'orderdetailsitem':orderdetailsitem,'orderdetails':orderdetails,'totalitem':totalitem})

def cancle(request,Order_id):
    orderdetails = Orderdetails.objects.get(id = Order_id)
    orderdetails.delete()
    return redirect('orderdetail')

def bill(request,Orderid):
    order = Orderdetails.objects.filter(id=Orderid)
    return render(request, 'bill.html', {'order':order[0]})
