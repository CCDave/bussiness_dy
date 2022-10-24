# Generated by Django 4.1.2 on 2022-10-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersModel', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ad_chanel',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='after_sale_remarks',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='app_chanel',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='arbitration_status',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='area',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='cancel_reason',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='channel_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='detailed_address',
            field=models.CharField(default=None, max_length=2046, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='dy_month_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='dy_pay_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='estimated_collection_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='express_delivery_days',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='investment_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='live_3part_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='msg_from_user',
            field=models.CharField(default=None, max_length=2046, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_remarks',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_submit_month',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_type',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='other_commission',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='other_commission_desc',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='p_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='p_specs',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='parent_id',
            field=models.BigIntegerField(db_index=True, default=None),
        ),
        migrations.AlterField(
            model_name='orders',
            name='partner_id',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='partner_name',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='partner_pay_discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='partner_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='pay_way',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payable',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='platform_pay_discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='platform_service_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='platform_subsidy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='post_sale_id',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='post_sale_reason',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='post_sale_reason_tag',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='post_sale_status',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='post_sale_type',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='province',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='refund_days',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='remark',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='responsible',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='return_express_number',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='safe_buy',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='service_charge',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='settle_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shop_pay_discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shop_remarks',
            field=models.CharField(default=None, max_length=2046, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='street',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_expend',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_income',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_from',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_name',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_phone',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_post_sale_desc',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_total_pay',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]
