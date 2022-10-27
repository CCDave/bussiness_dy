# Generated by Django 4.1.2 on 2022-10-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersModel', '0009_orders_s_sku_finish_code_orders_s_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='channel_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='dy_month_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='dy_pay_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='estimated_collection_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='investment_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='live_3part_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='other_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='p_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='partner_pay_discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='partner_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payable',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='platform_pay_discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='platform_service_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='platform_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='service_charge',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='settle_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shop_pay_discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_expend',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_income',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_total_pay',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True),
        ),
    ]