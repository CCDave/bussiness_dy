from django.db import models

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
    # '子订单编号'
    order_id = models.BigIntegerField(primary_key=True, unique=True, default=0)
    # '主订单编号'
    parent_id = models.BigIntegerField(db_index=True, default=None)
    # '商品名称'
    name = models.CharField(null=True, max_length=512, default=None)
    # '商品规格'
    p_specs = models.CharField(null=True, max_length=128, default=None)
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

    def _is_module_need_update(self, mode):
        ret = False
        self.post_sale_apply_agree_time
        return ret

    def _df_2_module(self, df):
        self.order_id = df['子订单编号']
        self.parent_id = df['主订单编号']
        self.name = df['商品名称']
        self.p_specs = df['商品规格']
        self.p_price = df['商品单价']
        self.payable = df['订单应付金额']
        self.pay_way = df['支付方式']
        self.service_charge = df['手续费']
        self.user_name = df['收件人']
        self.user_phone = df['收件人手机号']
        self.province = df['省']
        self.city = df['市']
        self.area = df['区']
        self.street = df['街道']
        self.detailed_address = df['详细地址']
        self.msg_from_user = df['买家留言']
        self.order_submit_time = df['订单提交时间']
        self.shop_remarks = df['商家备注']
        self.order_finish_time = df['订单完成时间']
        self.order_pay_time = df['支付完成时间']
        self.app_chanel = df['APP渠道']
        self.user_from = df['流量来源']
        self.order_status = df['订单状态']
        self.promised_delivery_time = df['承诺发货时间']
        self.order_type = df['订单类型']
        self.partner_id = df['达人ID']
        self.partner_name = df['达人昵称']
        self.post_sale_status = df['售后状态']
        self.cancel_reason = df['取消原因']
        self.scheduled_delivery_time = df['预约发货时间']
        self.safe_buy = df['是否安心购']
        self.ad_chanel = df['广告渠道']
        self.platform_pay_discount_amount = df['平台实际承担优惠金额']
        self.shop_pay_discount_amount = df['商家实际承担优惠金额']
        self.partner_pay_discount_amount = df['达人实际承担优惠金额']
        self.estimated_delivery_time = df['预计送达时间']
        self.order_submit_month = df['订单提交月份']
        self.order_submit_date = df['订单提交日期']
        self.estimated_collection_amount = df['预估收款金额']
        self.express_delivery_date = df['发货日期']
        self.express_delivery_days = df['几天发货']
        self.post_sale_id = df['售后单号']
        self.post_sale_type = df['售后类型']
        self.post_sale_apply_time = df['售后申请时间']
        self.post_sale_reason = df['售后原因']
        self.post_sale_reason_tag = df['售后原因标签']
        self.return_express_number = df['退货物流单号']
        self.return_delivery_time = df['退货发货时间']
        self.post_sale_apply_agree_time = df['同意售后申请时间']
        self.shop_refund_time = df['商家退款时间']
        self.user_arrival_time = df['用户到账时间']
        self.post_sale_close_time = df['售后关闭时间']
        self.arbitration_status = df['仲裁状态']
        self.responsible = df['纠纷责任方']
        self.post_sale_finish_time = df['售后完结时间']
        self.order_remarks = df['订单备注']
        self.user_post_sale_desc = df['用户售后说明']
        self.after_sale_remarks = df['售后备注']
        self.post_sale_apply_date = df['售后申请日期']
        self.refund_days = df['几天退款']
        self.settle_time = df['结算时间']
        self.settle_amount = df['结算金额']
        self.total_income = df['收入合计']
        self.platform_service_amount = df['平台服务费']
        self.platform_subsidy = df['平台补贴']
        self.partner_subsidy = df['达人补贴']
        self.dy_pay_subsidy = df['抖音支付补贴']
        self.dy_month_subsidy = df['抖音月付营销补贴']
        self.user_total_pay = df['用户实付']
        self.commission = df['佣金']
        self.channel_commission = df['渠道分成']
        self.investment_commission = df['招商服务费']
        self.live_3part_commission = df['直播间站外推广']
        self.other_commission = df['其他分成']
        self.other_commission_desc = df['其他分成说明']
        self.total_expend = df['支出合计']
        self.remark = df['备注']
