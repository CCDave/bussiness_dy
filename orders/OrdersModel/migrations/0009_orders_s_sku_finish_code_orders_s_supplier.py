# Generated by Django 4.1.2 on 2022-10-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersModel', '0008_orders_express_delivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='s_sku_finish_code',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='s_supplier',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]
