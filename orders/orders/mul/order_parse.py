import datetime
from doctest import FAIL_FAST
import requests
import csv
from openpyxl import load_workbook
import pandas as pd
from OrdersModel.models import Orders
import json
import numpy as np

# 将class转dict,以_开头的属性不要


def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value) and not name.startswith('_'):
            pr[name] = value
    return pr
# 将class转dict,以_开头的也要


def props_with_(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr
# dict转obj，先初始化一个obj


def dict2obj(obj, dict):
    obj.__dict__.update(dict)
    return obj


def currency_to_float(e):
    if isinstance(e, str):
        return e.replace(',', '')
    return e


def string_replace(e, s):
    if isinstance(e, str):
        return e.replace(s, '')
    return e


def get_last_months(count):
    ret = []
    now_date_time = datetime.datetime.now()
    for i in range(0, count):
        ret.append(now_date_time.date)
        now_date_time = (now_date_time - datetime.timedelta(days=30))
        i = i + 1
    return ret


def write_excel_file(file_path, sheet, data):
    file_name = file_path
    writer = pd.ExcelWriter(file_name, mode='w', engine='openpyxl')
    data.to_excel(writer, sheet)
    # orders_all.to_csv(writer)
    writer.save()
    writer.close()


def trans_head2_string(data, key):
    for k in key:
        data[k] = data[k].astype('str')
    return data


def get_pandas_from_url(url):
    return pd.read_csv(url)


def safe_change_name(data, old, new):
    if old in data:
        data[new] = data[old]
    return data


def safe_drop_ol(data, drops, axis):
    to_drop = []
    for drop in drops:
        if (drop in data):
            to_drop.append(drop)

    if len(to_drop) > 0:
        data = data.drop(labels=to_drop, axis=axis)
    return data


def safe_keep_ol(data, keeps):
    drop_col = []
    for col in data.columns:
        if (col not in keeps):
            drop_col.append(col)
    if len(drop_col) > 0:
        data = safe_drop_ol(data, drop_col, axis=1)
    return data


def trans_params(params):
    if isinstance(params, datetime.datetime):
        params = str(params)

    if pd.isna(params):
        params = None

    if isinstance(params, str):
        params = params.replace('\t', '')

    if params == '-':
        params = None

    return params


def transol2dict(df):
    return {'order_id': trans_params(df['子订单编号']),
            'parent_id': trans_params(df['主订单编号']),
            'name': trans_params(df['商品名称']),
            'p_specs': trans_params(df['商品规格']),
            'p_price': trans_params(df['商品单价']),
            'payable': trans_params(df['订单应付金额']),
            'pay_way': trans_params(df['支付方式']),
            'service_charge': trans_params(df['手续费']),
            'user_name': trans_params(df['收件人']),
            'user_phone': trans_params(df['收件人手机号']),
            'province': trans_params(df['省']),
            'city': trans_params(df['市']),
            'area': trans_params(df['区']),
            'street': trans_params(df['街道']),
            'detailed_address': trans_params(df['详细地址']),
            'msg_from_user': trans_params(df['买家留言']),
            'order_submit_time': trans_params(df['订单提交时间']),
            'shop_remarks': trans_params(df['商家备注']),
            'order_finish_time': trans_params(df['订单完成时间']),
            'order_pay_time': trans_params(df['支付完成时间']),
            'app_chanel': trans_params(df['APP渠道']),
            'user_from': trans_params(df['流量来源']),
            'order_status': trans_params(df['订单状态']),
            'promised_delivery_time': trans_params(df['承诺发货时间']),
            'order_type': trans_params(df['订单类型']),
            'partner_id': trans_params(df['达人ID']),
            'partner_name': trans_params(df['达人昵称']),
            'post_sale_status': trans_params(df['售后状态']),
            'cancel_reason': trans_params(df['取消原因']),
            'scheduled_delivery_time': trans_params(df['预约发货时间']),
            'safe_buy': trans_params(df['是否安心购']),
            'ad_chanel': trans_params(df['广告渠道']),
            'platform_pay_discount_amount': trans_params(df['平台实际承担优惠金额']),
            'shop_pay_discount_amount': trans_params(df['商家实际承担优惠金额']),
            'partner_pay_discount_amount': trans_params(df['达人实际承担优惠金额']),
            'estimated_delivery_time': trans_params(df['预计送达时间']),
            'order_submit_month': trans_params(df['订单提交月份']),
            'order_submit_date': trans_params(df['订单提交日期']),
            'estimated_collection_amount': trans_params(df['预估收款金额']),
            'express_delivery_date': trans_params(df['发货日期']),
            'express_delivery_days': trans_params(df['几天发货']),
            'post_sale_id': trans_params(df['售后单号']),
            'post_sale_type': trans_params(df['售后类型']),
            'post_sale_apply_time': trans_params(df['售后申请时间']),
            'post_sale_reason': trans_params(df['售后原因']),
            'post_sale_reason_tag': trans_params(df['售后原因标签']),
            'return_express_number': trans_params(df['退货物流单号']),
            'return_delivery_time': trans_params(df['售后申请时间']),
            'post_sale_apply_agree_time': trans_params(df['售后申请时间']),
            'shop_refund_time': trans_params(df['售后申请时间']),
            'user_arrival_time': trans_params(df['售后申请时间']),
            'post_sale_close_time': trans_params(df['售后申请时间']),
            'arbitration_status': trans_params(df['仲裁状态']),
            'responsible': trans_params(df['纠纷责任方']),
            'post_sale_finish_time': trans_params(df['售后申请时间']),
            'order_remarks': trans_params(df['订单备注']),
            'user_post_sale_desc': trans_params(df['用户售后说明']),
            'after_sale_remarks': trans_params(df['售后备注']),
            'post_sale_apply_date': trans_params(df['售后申请时间']),
            'refund_days': trans_params(df['几天退款']),
            'settle_time': trans_params(df['结算时间']),
            'settle_amount': trans_params(df['结算金额']),
            'total_income': trans_params(df['收入合计']),
            'platform_service_amount': trans_params(df['平台服务费']),
            'platform_subsidy': trans_params(df['平台补贴']),
            'partner_subsidy': trans_params(df['达人补贴']),
            'dy_pay_subsidy': trans_params(df['抖音支付补贴']),
            'dy_month_subsidy': trans_params(df['抖音月付营销补贴']),
            'user_total_pay': trans_params(df['用户实付']),
            'commission': trans_params(df['佣金']),
            'channel_commission': trans_params(df['渠道分成']),
            'investment_commission': trans_params(df['招商服务费']),
            'live_3part_commission': trans_params(df['直播间站外推广']),
            'other_commission': trans_params(df['其他分成']),
            'other_commission_desc': trans_params(df['其他分成说明']),
            'total_expend': trans_params(df['支出合计']),
            'remark': trans_params(df['备注'])}


def orders_mul(orders_from_file, orders_return_from_file, orders_settle_from_file):
    mul_months = get_last_months(3)

    # 所有订单最近三个月的销售情况 所有订单数 未支付 退款 退货退款订单 实收订单  邮费次数  赠品次数
    # 订单提交月份
    orders_from_file['订单提交月份'] = pd.to_datetime(
        orders_from_file['订单提交时间']).dt.month

    # 订单提交日期
    orders_from_file['订单提交日期'] = pd.to_datetime(
        orders_from_file['订单提交时间']).dt.date

    # 预估收款金额
    orders_from_file['预估收款金额'] = pd.to_numeric(orders_from_file['订单应付金额'].map(
        lambda x: currency_to_float(x)), downcast='float')

    # 发货日期
    orders_from_file['发货日期'] = pd.to_datetime(
        orders_from_file['发货时间']).dt.date

    # 几天发货
    orders_from_file["几天发货"] = orders_from_file["发货日期"] - \
        orders_from_file["订单提交日期"]

    # print(len(orders_return_from_file))

    # 售后订单处理
    # orders_return_from_file['订单号'] = orders_return_from_file['订单号'].astype('str')
    # orders_return_from_file['售后单号'] = orders_return_from_file['售后单号'].astype('str')
    # orders_return_from_file['商品单号'] = orders_return_from_file['商品单号'].astype('str')

    orders_return_from_file['主订单编号'] = pd.to_numeric(
        orders_return_from_file['订单号'])
    orders_return_from_file['子订单编号'] = pd.to_numeric(
        orders_return_from_file['商品单号'])

    orders_return_from_file['售后申请日期'] = pd.to_datetime(
        orders_return_from_file['售后申请时间']).dt.date

    # 去重
    orders_return_from_file = orders_return_from_file.sort_values(
        by='售后申请时间', ascending=False)
    orders_return_from_file = orders_return_from_file.drop_duplicates(
        subset=['子订单编号'], keep='first')
    # print(len(orders_return_from_file))

    orders_all = pd.merge(
        orders_from_file, orders_return_from_file, on=['子订单编号', '主订单编号'], how='left')
    # print(len(orders_all))

    orders_all["几天退款"] = orders_all["售后申请日期"] - \
        orders_all["订单提交日期"]

    # 处理结算表
    orders_settle_from_file = orders_settle_from_file.drop(index=0)

    orders_settle_from_file['主订单编号'] = orders_settle_from_file['订单号']
    orders_settle_from_file['子订单编号'] = orders_settle_from_file['子订单号']

    orders_settle_from_file['子订单编号'] = orders_settle_from_file['子订单号'].map(
        lambda x: string_replace(x, "'"))

    orders_settle_from_file['主订单编号'] = orders_settle_from_file['订单号'].map(
        lambda x: string_replace(x, "'"))

    orders_settle_from_file['子订单编号'] = pd.to_numeric(
        orders_settle_from_file['子订单编号'])
    orders_settle_from_file['主订单编号'] = pd.to_numeric(
        orders_settle_from_file['主订单编号'])

    # 去重
    # print(len(orders_settle_from_file))
    # write_excel_file('1.xlsx', 'a', orders_settle_from_file)
    orders_settle_from_file = orders_settle_from_file.sort_values(
        by='结算金额', ascending=True)
    # print(len(orders_settle_from_file))

    orders_settle_from_file = orders_settle_from_file.drop_duplicates(
        subset=['子订单编号'], keep='first')
    # print(len(orders_settle_from_file))
    # write_excel_file('2.xlsx','a',orders_settle_from_file)

    # print(type(orders_settle_from_file['子订单编号'][1]))
    # print(orders_settle_from_file['子订单编号'][1])
    # print(type(orders_all['子订单编号'][0]))

    orders_all = pd.merge(
        orders_all, orders_settle_from_file, on=['子订单编号', '主订单编号'], how='left')

    # print(len(orders_all))
    # print(list(orders_all.columns))
    # orders_all['主订单编号'] = orders_all['主订单编号_x'].astype('str')
    # orders_all['子订单编号'] = orders_all['子订单编号'].astype('str')
    # orders_all = trans_head2_string(orders_all, ['主订单编号', '子订单编号'])
    orders_all = safe_change_name(orders_all, '商品数量_x', '商品数量')
    orders_all = safe_change_name(orders_all, '商品ID_x', '商品ID')
    orders_all = safe_change_name(orders_all, '订单类型_x', '订单类型')
    orders_all = safe_change_name(orders_all, '售后状态_x', '售后状态')

    orders_all = safe_keep_ol(orders_all,
                              ['主订单编号', '子订单编号', '商品名称', '商品规格', '商品单价', '订单应付金额',
                               '支付方式', '手续费', '收件人', '收件人手机号', '省', '市', '区', '街道',
                               '详细地址', '买家留言', '订单提交时间', '商家备注', '订单完成时间', '支付完成时间',
                               'APP渠道', '流量来源', '订单状态', '承诺发货时间', '订单类型', '达人ID', '达人昵称',
                               '售后状态', '取消原因', '预约发货时间', '是否安心购', '广告渠道', '平台实际承担优惠金额',
                               '商家实际承担优惠金额', '达人实际承担优惠金额', '预计送达时间', '订单提交月份', '订单提交日期',
                               '预估收款金额', '发货日期', '几天发货', '售后单号', '售后类型', '售后申请时间', '售后原因',
                               '售后原因标签', '退货物流单号', '退货发货时间', '同意售后申请时间', '商家退款时间', '用户到账时间',
                               '售后关闭时间', '仲裁状态', '纠纷责任方', '售后完结时间', '订单备注', '用户售后说明', '售后备注',
                               '售后申请日期', '几天退款', '结算时间', '结算金额', '收入合计', '平台服务费', '平台补贴',
                               '达人补贴', '抖音支付补贴', '抖音月付营销补贴', '用户实付', '佣金', '渠道分成', '招商服务费',
                               '直播间站外推广', '其他分成', '其他分成说明', '支出合计', '备注'])
    # write_excel_file('aa.xlsx', 'a', orders_all)
    orders_dict = orders_all.to_dict('records')
    # 更新数据库数据
    ret = data_base_update(orders_dict)

    if ret:
        return 200
    return 201


def data_base_update(datas):
    print('data_base_update')
    print(datas[0])
    coount = 0
    for data in datas:
        order_model = transol2dict(data)
        print('11111111111111111111111111111')
        count = 0
        print(order_model)
        Orders.objects.update_or_create(
            order_id=order_model['order_id'], defaults=order_model)
        count = count + 1
        if count > 10:
            break
    return True


def orders_pares(orders, custom, settle):
    orders = pd.read_csv(orders)
    custom_orders = pd.read_csv(custom)
    settle_orders = pd.read_csv(settle)
    ret = 201
    if (orders_mul(orders, custom_orders, settle_orders)):
        ret = 200
    return ret


# orders_pares(
#    'https://app.informat.cn/file/441d8b327b5e4c85a0b58a1d7ec9ec3e_p.csv',
#    'https://app.informat.cn/file/f824c0464cbb4920aa6ed29735d86684_p.csv',
#    'https://app.informat.cn/file/ade5d69dcf0442c0875b802980b170f5_p.csv')
