# Generated by Django 4.1.2 on 2022-10-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersModel', '0002_orders_sku_code_alter_orders_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_link',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]