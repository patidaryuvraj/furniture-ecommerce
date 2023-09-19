from django.db import models

STATUS_CHOICE = (
    ('Order has been placed','Order has been placed'),
    ('Order has been shiped', 'Order has been shiped'),
    ('Your order has been recieved in the hub nearest to you', 'Your order has been recieved in the hub nearest to you'),
    ('Out for delivery', 'Out for delivery'),
    ('Dilivered', 'Dilivered'),
)

# Create your models here.
class Orderdetails(models.Model):
    Order_id = models.AutoField
    productname = models.CharField(max_length=500)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="order", default="")
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,default='Order has been placed',choices=STATUS_CHOICE)
    totalprice = models.IntegerField(default=0)

    class Meta:
        db_table = "orderdetails"