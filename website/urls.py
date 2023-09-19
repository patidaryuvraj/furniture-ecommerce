from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('home', views.home,name='home'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('contactus', views.contactus,name='contactus'),
    path('signuppage',views.signuppage, name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('logout',views.logout,name='logout'),
    path('contantpage', views.contactpage,name="contactpage")
    # path('addtocart', views.addtocart,name='addtocart'),
]