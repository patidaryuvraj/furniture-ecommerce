# Generated by Django 4.1.4 on 2023-06-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]