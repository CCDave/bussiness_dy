from django.db import models
import pandas as pd

# Create your models here.
# 订单表

# '主订单编号','子订单编号','商品名称','商品规格','商品单价','订单应付金额','支付方式','手续费'
#     ,'收件人','收件人手机号','省','市','区','街道','详细地址','买家留言'
#     ,'订单提交时间','商家备注','订单完成时间','支付完成时间','APP渠道','流量来源','订单状态','承诺发货时间'
#     ,'订单类型','达人ID','达人昵称','售后状态','取消原因','预约发货时间','是否安心购','广告渠道'
#      ,'平台实际承担优惠金额','商家实际承担优惠金额','达人实际承担优惠金额','预计送达时间','订单提交月份','订单提交日期','预估收款金额','发货日期'
#      ,'几天发货','售后单号','售后类型','售后申请时间','售后原因','售后原因标签','退货物流单号','退货发货时间'
#      ,'同意售后申请时间','商家退款时间','用户到账时间','售后关闭时间','仲裁状态','纠纷责任方','售后完结时间','订单备注'
#      ,'用户售后说明','售后备注','售后申请日期','几天退款','结算时间','结算金额','收入合计','平台服务费'
#      ,'平台补贴','达人补贴','抖音支付补贴','抖音月付营销补贴','用户实付','佣金','渠道分成','招商服务费'
#      ,'直播间站外推广','其他分成','其他分成说明','支出合计','备注'


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    # '子订单编号'
    order_id = models.CharField(unique=True, max_length=128, default=None)
    # models.BigIntegerField(db_index=True, unique=True, default=None)
    # '主订单编号'
    parent_id = models.CharField(
        db_index=True, max_length=128, default=None)
    #models.BigIntegerField(db_index=True, default=None)

    # '商品ID'
    p_id = models.CharField(db_index=True, max_length=128, default=None)
    #models.BigIntegerField(null=True, db_index=True, default=None)

    # '商品数量'
    p_count = models.IntegerField(null=True, default=None)

    # '商品名称'
    name = models.CharField(null=True, max_length=512, default=None)
    # '商品规格'
    p_specs = models.CharField(null=True, max_length=128, default=None)

    # 'SKU拼接码'
    sku_code = models.CharField(null=True, max_length=128, default=None)

    # '商品单价'
    p_price = models.DecimalField(
        null=True, max_digits=5, decimal_places=2, default=None)
    # '订单应付金额'
    payable = models.DecimalField(
        null=True, max_digits=5, decimal_places=2, default=None)
    # '支付方式'
    pay_way = models.CharField(null=True, max_length=128, default=None)
    # '手续费'
    service_charge = models.DecimalField(null=True,
                                         max_digits=5, decimal_places=2, default=None)
    # '收件人'
    user_name = models.CharField(null=True, max_length=512, default=None)
    # '收件人手机号'
    user_phone = models.CharField(null=True, max_length=512, default=None)
    # '省'
    province = models.CharField(null=True, max_length=128, default=None)
    # '市'
    city = models.CharField(null=True, max_length=128, default=None)
    # '区'
    area = models.CharField(null=True, max_length=128, default=None)
    # '街道'
    street = models.CharField(null=True, max_length=512, default=None)
    # '详细地址'
    detailed_address = models.CharField(
        null=True, max_length=2046, default=None)
    # '买家留言'
    msg_from_user = models.CharField(null=True, max_length=2046, default=None)
    # '订单提交时间'
    order_submit_time = models.DateTimeField(null=True, default=None)
    # '商家备注'
    shop_remarks = models.CharField(null=True, max_length=2046, default=None)
    # '订单完成时间'
    order_finish_time = models.DateTimeField(null=True, default=None)
    # '支付完成时间'
    order_pay_time = models.DateTimeField(null=True, default=None)
    # 'APP渠道'
    app_chanel = models.CharField(null=True, max_length=128, default=None)
    # '流量来源'
    user_from = models.CharField(null=True, max_length=128, default=None)
    # '订单状态'
    order_status = models.CharField(null=True, max_length=128, default=None)
    # '承诺发货时间'
    promised_delivery_time = models.DateTimeField(null=True, default=None)
    # '订单类型'
    order_type = models.CharField(null=True, max_length=128, default=None)
    # '达人ID'
    partner_id = models.CharField(null=True, max_length=128, default=None)
    # '达人昵称'
    partner_name = models.CharField(null=True, max_length=128, default=None)
    # '售后状态'
    post_sale_status = models.CharField(
        null=True, max_length=128, default=None)
    # '取消原因'
    cancel_reason = models.CharField(null=True, max_length=128, default=None)
    # '预约发货时间'
    scheduled_delivery_time = models.DateTimeField(null=True, default=None)
    # '是否安心购'
    safe_buy = models.CharField(null=True, max_length=128, default=None)
    # '广告渠道'
    ad_chanel = models.CharField(null=True, max_length=128, default=None)
    # '平台实际承担优惠金额'
    platform_pay_discount_amount = models.DecimalField(null=True,
                                                       max_digits=5, decimal_places=2, default=None)
    # '商家实际承担优惠金额'
    shop_pay_discount_amount = models.DecimalField(null=True,
                                                   max_digits=5, decimal_places=2, default=None)
    # '达人实际承担优惠金额'
    partner_pay_discount_amount = models.DecimalField(null=True,
                                                      max_digits=5, decimal_places=2, default=None)
    # '预计送达时间'
    estimated_delivery_time = models.DateTimeField(null=True, default=None)
    # '订单提交月份'
    order_submit_month = models.IntegerField(null=True, default=None)
    # '订单提交日期'
    order_submit_date = models.DateTimeField(null=True, default=None)
    # '预估收款金额'
    estimated_collection_amount = models.DecimalField(null=True,
                                                      max_digits=5, decimal_places=2, default=None)
    # '发货日期'
    express_delivery_date = models.DateTimeField(null=True, default=None)
    # '几天发货'
    express_delivery_days = models.IntegerField(null=True, default=None)
    # '售后单号'
    post_sale_id = models.BigIntegerField(null=True, default=None)
    # '售后类型'
    post_sale_type = models.CharField(null=True, max_length=128, default=None)
    # '售后申请时间'
    post_sale_apply_time = models.DateTimeField(null=True, default=None)
    # '售后原因'
    post_sale_reason = models.CharField(
        null=True, max_length=128, default=None)
    # '售后原因标签'
    post_sale_reason_tag = models.CharField(
        null=True, max_length=128, default=None)
    # '退货物流单号'
    return_express_number = models.CharField(
        null=True, max_length=128, default=None)
    # '退货发货时间'
    return_delivery_time = models.DateTimeField(null=True,  default=None)
    # '同意售后申请时间'
    post_sale_apply_agree_time = models.DateTimeField(null=True, default=None)
    # '商家退款时间'
    shop_refund_time = models.DateTimeField(null=True, default=None)
    # '用户到账时间'
    user_arrival_time = models.DateTimeField(null=True, default=None)
    # '售后关闭时间'
    post_sale_close_time = models.DateTimeField(null=True, default=None)
    # '仲裁状态'
    arbitration_status = models.CharField(
        null=True, max_length=128, default=None)
    # '纠纷责任方'
    responsible = models.CharField(null=True, max_length=128, default=None)
    # '售后完结时间'
    post_sale_finish_time = models.DateTimeField(null=True, default=None)
    # '订单备注'
    order_remarks = models.CharField(null=True, max_length=1024, default=None)
    # '用户售后说明'
    user_post_sale_desc = models.CharField(
        null=True, max_length=1024, default=None)
    # '售后备注'
    after_sale_remarks = models.CharField(
        null=True, max_length=1024, default=None)
    # '售后申请日期'
    post_sale_apply_date = models.DateTimeField(null=True, default=None)
    # '几天退款'
    refund_days = models.IntegerField(null=True, default=None)
    # '结算时间'
    settle_time = models.DateTimeField(null=True, default=None)
    # '结算金额'
    settle_amount = models.DecimalField(null=True,
                                        max_digits=5, decimal_places=2, default=None)
    # '收入合计'
    total_income = models.DecimalField(null=True,
                                       max_digits=5, decimal_places=2, default=None)
    # '平台服务费'
    platform_service_amount = models.DecimalField(null=True,
                                                  max_digits=5, decimal_places=2, default=None)
    # '平台补贴'
    platform_subsidy = models.DecimalField(null=True,
                                           max_digits=5, decimal_places=2, default=None)
    # '达人补贴'
    partner_subsidy = models.DecimalField(null=True,
                                          max_digits=5, decimal_places=2, default=None)
    # '抖音支付补贴'
    dy_pay_subsidy = models.DecimalField(null=True,
                                         max_digits=5, decimal_places=2, default=None)
    # '抖音月付营销补贴'
    dy_month_subsidy = models.DecimalField(null=True,
                                           max_digits=5, decimal_places=2, default=None)
    # '用户实付'
    user_total_pay = models.DecimalField(null=True,
                                         max_digits=5, decimal_places=2, default=None)
    # '佣金'
    commission = models.DecimalField(
        null=True, max_digits=5, decimal_places=2, default=None)
    # '渠道分成'
    channel_commission = models.DecimalField(null=True,
                                             max_digits=5, decimal_places=2, default=None)
    # '招商服务费'
    investment_commission = models.DecimalField(null=True,
                                                max_digits=5, decimal_places=2, default=None)
    # '直播间站外推广'
    live_3part_commission = models.DecimalField(null=True,
                                                max_digits=5, decimal_places=2, default=None)
    # '其他分成'
    other_commission = models.DecimalField(null=True,
                                           max_digits=5, decimal_places=2, default=None)
    # '其他分成说明'
    other_commission_desc = models.CharField(
        null=True, max_length=1024, default=None)
    # '支出合计'
    total_expend = models.DecimalField(null=True,
                                       max_digits=5, decimal_places=2, default=None)
    # '备注'
    remark = models.CharField(null=True, max_length=1024, default=None)

    def _is_module_need_update(self, old, new):
        ret = False
        updates = {}
        default_compare = ['name',
                           'p_id',
                           'p_count',
                           'p_specs',
                           'p_price',
                           'payable',
                           'pay_way',
                           'service_charge',
                           'user_name',
                           'user_phone',
                           'province',
                           'city',
                           'area',
                           'street',
                           'detailed_address',
                           'msg_from_user',
                           'order_submit_time',
                           'shop_remarks',
                           'order_finish_time',
                           'order_pay_time',
                           'app_chanel',
                           'user_from',
                           'order_status',
                           'promised_delivery_time',
                           'order_type',
                           'partner_id',
                           'partner_name',
                           'post_sale_status',
                           'cancel_reason',
                           'scheduled_delivery_time',
                           'safe_buy',
                           'ad_chanel',
                           'platform_pay_discount_amount',
                           'shop_pay_discount_amount',
                           'partner_pay_discount_amount',
                           'estimated_delivery_time',
                           'order_submit_month',
                           'order_submit_date',
                           'estimated_collection_amount',
                           'express_delivery_date',
                           'express_delivery_days',
                           'post_sale_id',
                           'post_sale_type',
                           'post_sale_apply_time',
                           'post_sale_reason',
                           'post_sale_reason_tag',
                           'return_express_number',
                           'return_delivery_time',
                           'post_sale_apply_agree_time',
                           'shop_refund_time',
                           'user_arrival_time',
                           'post_sale_close_time',
                           'arbitration_status',
                           'responsible',
                           'post_sale_finish_time',
                           'order_remarks',
                           'user_post_sale_desc',
                           'after_sale_remarks',
                           'post_sale_apply_date',
                           'refund_days',
                           'settle_time',
                           'settle_amount',
                           'total_income',
                           'platform_service_amount',
                           'platform_subsidy',
                           'partner_subsidy',
                           'dy_pay_subsidy',
                           'dy_month_subsidy',
                           'user_total_pay',
                           'commission',
                           'channel_commission',
                           'investment_commission',
                           'live_3part_commission',
                           'other_commission',
                           'other_commission_desc',
                           'total_expend',
                           'remark']
        for com in default_compare:
            old_item = getattr(old, com)
            new_item = new[com]
            if pd.isna(old_item) and pd.notna(new_item):
                updates[com] = new_item
                ret = True
                continue
            elif pd.isna(new_item) and pd.notna(old_item):
                continue
            elif new_item != old_item:
                ret = True
                updates[com] = new_item
        return ret, updates
