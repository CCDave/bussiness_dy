# Generated by Django 4.1.2 on 2022-10-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersModel', '0003_orders_order_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_link',
            field=models.CharField(default='null', max_length=128, null=True),
        ),
    ]