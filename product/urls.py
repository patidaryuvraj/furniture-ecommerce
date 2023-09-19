from django.urls import path
from .import views
urlpatterns = [
    path('userhome',views.userhome, name='userhome' ),
    path('prodview/<int:product_id>',views.prodview, name='prodview'),
    
    

]