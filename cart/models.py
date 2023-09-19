from django.db import models
from product.models import Product
# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField   
    productid = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    productname = models.CharField(max_length=500)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="cart", default="")
    totalprice = models.IntegerField(default=0)

    class Meta:
        db_table = "cart"