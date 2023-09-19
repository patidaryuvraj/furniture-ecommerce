from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    mobile = models.CharField(max_length=15)
    comment = models.CharField(max_length=1000)

    class Meta:
        db_table = "contact"