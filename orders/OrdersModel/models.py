from django.db import models

# Create your models here.
## 订单表

#'主订单编号','子订单编号','商品名称','商品规格','商品单价','订单应付金额','支付方式','手续费'
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
    #'子订单编号'
    order_id = models.BigIntegerField(primary_key=True, unique=True, default = 0)
    #'主订单编号'
    parent_id = models.BigIntegerField(db_index = True, default = 0)
    #'商品名称'
    name = models.CharField(max_length=512,default = '')
    #'商品规格'
    p_specs = models.CharField(max_length=128,default = '')
    #'商品单价'
    p_price = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'订单应付金额'
    payable = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'支付方式'
    pay_way = models.CharField(max_length=128,default = '')
    #'手续费'
    service_charge = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    #'收件人'
    user_name = models.CharField(max_length=512,default = '')
    #'收件人手机号'
    user_phone = models.CharField(max_length=512,default = '')
    #'省'
    province = models.CharField(max_length=128,default = '')
    #'市'
    city = models.CharField(max_length=128,default = '')
    #'区'
    area = models.CharField(max_length=128,default = '')
    #'街道'
    street = models.CharField(max_length=512,default = '')
    #'详细地址'
    detailed_address = models.CharField(max_length=2046,default = '')
    #'买家留言'    
    msg_from_user = models.CharField(max_length=2046,default = '')
    #'订单提交时间'
    order_submit_time = models.DateTimeField(null=True, default =None)
    #'商家备注'
    shop_remarks = models.CharField(max_length=2046, default = '')
    #'订单完成时间'
    order_finish_time = models.DateTimeField(null=True, default =None)
    #'支付完成时间'
    order_pay_time = models.DateTimeField(null=True, default =None)
    #'APP渠道'
    app_chanel = models.CharField(max_length=128,default = '')
    #'流量来源'
    user_from = models.CharField(max_length=128,default = '')
    #'订单状态'
    order_status = models.CharField(max_length=128,default = '')
    #'承诺发货时间'
    promised_delivery_time = models.DateTimeField(null=True, default =None)
    #'订单类型'
    order_type = models.CharField(max_length=128, default = '')
    #'达人ID'
    partner_id = models.CharField(max_length=128, default = '')
    #'达人昵称'
    partner_name = models.CharField(max_length=128, default = '')
    #'售后状态'
    post_sale_status = models.CharField(max_length=128, default = '')
    #'取消原因'
    cancel_reason = models.CharField(max_length=128, default = '')
    #'预约发货时间'
    scheduled_delivery_time = models.DateTimeField(null=True, default = None)
    #'是否安心购'
    safe_buy = models.CharField(max_length=128, default = '')
    #'广告渠道'    
    ad_chanel = models.CharField(max_length=128,default = '')
    #'平台实际承担优惠金额'
    platform_pay_discount_amount = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    #'商家实际承担优惠金额'
    shop_pay_discount_amount = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    #'达人实际承担优惠金额'
    partner_pay_discount_amount = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    #'预计送达时间'
    estimated_delivery_time = models.DateTimeField(null=True, default = None)
    #'订单提交月份'
    order_submit_month = models.IntegerField(default = 0)
    #'订单提交日期'
    order_submit_date = models.DateTimeField(null=True, default = None)
    #'预估收款金额'
    estimated_collection_amount = models.DecimalField(max_digits=5, decimal_places=2,default = 0)
    #'发货日期'
    express_delivery_date = models.DateTimeField(null=True, default = None)
    #'几天发货'
    express_delivery_days = models.IntegerField(default = 0)
    #'售后单号'
    post_sale_id = models.BigIntegerField(default = 0)
    #'售后类型'
    post_sale_type = models.CharField(max_length=128,default = '')
    #'售后申请时间'
    post_sale_apply_time = models.DateTimeField(null=True, default = None)
    #'售后原因'
    post_sale_reason = models.CharField(max_length=128 ,default = '')
    #'售后原因标签'
    post_sale_reason_tag = models.CharField(max_length=128 ,default = '')
    #'退货物流单号'
    return_express_number = models.CharField(max_length=128 ,default = '')
    #'退货发货时间'
    return_delivery_time = models.DateTimeField(null=True,  default = None)
    #'同意售后申请时间'
    post_sale_apply_agree_time = models.DateTimeField(null=True, default = None)
    #'商家退款时间'
    shop_refund_time = models.DateTimeField(null=True, default = None)
    #'用户到账时间'
    user_arrival_time = models.DateTimeField(null=True, default = None)
    #'售后关闭时间'
    post_sale_close_time = models.DateTimeField(null=True, default = None)
    #'仲裁状态'
    arbitration_status = models.CharField(max_length=128,default = '')
    #'纠纷责任方'
    responsible = models.CharField(max_length=128, default = '')
    #'售后完结时间'
    post_sale_finish_time = models.DateTimeField(null=True, default = None)
    #'订单备注'
    order_remarks = models.CharField(max_length=1024, default = '')
    #'用户售后说明'
    user_post_sale_desc = models.CharField(max_length=1024, default = '')
    #'售后备注'
    after_sale_remarks = models.CharField(max_length=1024, default = '')
    #'售后申请日期'
    post_sale_apply_date = models.DateTimeField(null=True, default = None)
    #'几天退款'
    refund_days = models.IntegerField(default = 0)
    #'结算时间'
    settle_time = models.DateTimeField(null=True, default = None)
    #'结算金额'
    settle_amount = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'收入合计'
    total_income = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'平台服务费'
    platform_service_amount = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'平台补贴'
    platform_subsidy = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'达人补贴'
    partner_subsidy = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'抖音支付补贴'
    dy_pay_subsidy = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'抖音月付营销补贴'
    dy_month_subsidy = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'用户实付'
    user_total_pay = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'佣金'
    commission = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'渠道分成'
    channel_commission = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'招商服务费' 
    investment_commission = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'直播间站外推广'
    live_3part_commission = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'其他分成'
    other_commission = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'其他分成说明'
    other_commission_desc = models.CharField(max_length=1024, default = '')
    #'支出合计'
    total_expend = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    #'备注'
    remark = models.CharField(max_length=1024, default = '')