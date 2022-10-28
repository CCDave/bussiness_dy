from bisect import insort
import datetime
from decimal import Decimal
from doctest import FAIL_FAST
from lib2to3.pgen2 import token
import requests
import csv
from openpyxl import load_workbook
import pandas as pd
from OrdersModel.models import Orders
import json
import numpy as np


def currency_to_float(e):
    if isinstance(e, str):
        return e.replace(',', '')
    return e


def string_replace(e, s):
    if isinstance(e, str):
        return e.replace(s, '')
    return e


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


def trans_number(params):
    ret = None
    try:
        if pd.isna(params):
            ret = None
        elif isinstance(params, int):
            ret = params
        elif isinstance(params, pd.Timedelta):
            ret = params.days  # astype('timedelta64[D]').astype(int)
        else:
            if isinstance(params, str):
                params = params.replace(",", "")
            ret = pd.to_numeric(params)
            if isinstance(ret, np.int64):
                ret = ret.astype(Decimal)
            else:
                ret = Decimal(ret).quantize(Decimal('0.00'))
            # if isinstance(ret, np.float64):
            #    ret = Decimal(ret)
            # print(type(ret))
    except Exception as e:
        print(e)
        ret = None
    if pd.isna(ret):
        ret = None
    return ret


def trans_string(params):
    ret = None
    try:
        if isinstance(params, str):
            ret = params
        else:
            ret = str(params)
    except Exception as e:
        print(e)
        ret = None

    if isinstance(ret, str):
        ret = ret.replace('\t', '')
    if pd.isna(ret) or ret == 'nan':
        ret = None
    return ret


def trans_time(params):
    ret = None
    try:
        if pd.isna(params):
            ret = None
        if isinstance(params, datetime.datetime):
            ret = params
        elif isinstance(params, str):
            if params == '-':
                ret = None
            else:
                params = params.replace('\t', '')
                ret = pd.to_datetime(params)
        else:
            ret = pd.to_datetime(params)
    except Exception as e:
        print(e)
        ret = None

    if pd.isna(params):
        ret = None
    return ret


def make_order_status_values(item):
    # 给订单类型设置状态
    order_status = item['order_status']
    post_sale_status = item['post_sale_status']
    express_delivery_date = item['express_delivery_date']
    settle_date = item['settle_date']
    settle_amount = item['settle_amount']
    if order_status == '已关闭':
        if post_sale_status == '-':
            item['r_order_status'] = '未付款'
        elif post_sale_status == '同意退款，退款成功':
            if pd.isna(express_delivery_date):
                item['r_order_status'] = '发货前退款'
            else:
                item['r_order_status'] = '发货后退款'
        else:
            item['r_order_status'] = '未知'
    elif order_status == '已发货':
        if post_sale_status == '-':
            item['r_order_status'] = '已发货'
        elif post_sale_status == '补寄/换货，待买家收货':
            item['r_order_status'] = '已发货'
        elif post_sale_status == '待买家退货处理':
            item['r_order_status'] = '发货后退款'
        elif post_sale_status == '待商家收货':
            item['r_order_status'] = '发货后退款'
        elif post_sale_status == '售后关闭':
            item['r_order_status'] = '已发货'
        else:
            item['r_order_status'] = '未知'
    elif order_status == '已完成':
        if post_sale_status == '-':
            item['r_order_status'] = '已发货'
        elif post_sale_status == '补寄/换货成功':
            item['r_order_status'] = '已发货'
        elif post_sale_status == '待买家退货处理':
            item['r_order_status'] = '发货后退款'
        elif post_sale_status == '待商家收货':
            item['r_order_status'] = '发货后退款'
        elif post_sale_status == '售后关闭':
            item['r_order_status'] = '已发货'
        elif post_sale_status == '同意退款，退款成功':
            item['r_order_status'] = '发货后退款'
        else:
            item['r_order_status'] = '未知'
    elif order_status == '备货中':
        item['r_order_status'] = '备货中'

    if pd.notna(settle_date) and pd.notna(settle_amount):
        if settle_amount > 0:
            item['r_order_settle_status'] = '已结算'
        else:
            item['r_order_settle_status'] = '反结算'
    elif item['r_order_status'] == '备货中' or item['r_order_status'] == '已发货':
        item['r_order_settle_status'] = '待结算'
    elif item['r_order_status'] == '未付款' or\
            item['r_order_status'] == '发货前退款' or\
            item['r_order_status'] == '发货后退款':
        item['r_order_settle_status'] = '退单'
    else:
        item['r_order_settle_status'] = None
    return item


def transOl2dict(df):
    obj = {}
    obj['order_id'] = trans_string(df['子订单编号'])
    obj['parent_id'] = trans_string(df['主订单编号'])
    obj['name'] = trans_string(df['选购商品'])

    obj['p_id'] = trans_string(df['商品ID'])
    obj['p_count'] = trans_number(df['商品数量'])
    p_specs = trans_string(df['商品规格'])
    obj['p_specs'] = p_specs
    sku_code = ''
    if len(p_specs):
        values = p_specs.split(';')
        if len(values) == 2:
            sku_code = values[0]
        elif len(values) == 3:
            sku_code = values[0] + '-' + values[1]
    obj['sku_code'] = sku_code
    obj['p_price'] = trans_number(df['商品单价'])
    obj['payable'] = trans_number(df['订单应付金额'])
    obj['pay_way'] = trans_string(df['支付方式'])
    obj['service_charge'] = trans_number(df['手续费'])
    obj['user_name'] = trans_string(df['收件人'])
    obj['user_phone'] = trans_string(df['收件人手机号'])
    obj['province'] = trans_string(df['省'])
    obj['city'] = trans_string(df['市'])
    obj['area'] = trans_string(df['区'])
    obj['street'] = trans_string(df['街道'])
    obj['detailed_address'] = trans_string(df['详细地址'])
    obj['msg_from_user'] = trans_string(df['买家留言'])
    obj['order_submit_time'] = trans_time(df['订单提交时间'])
    obj['shop_remarks'] = trans_string(df['商家备注'])
    obj['order_finish_time'] = trans_time(df['订单完成时间'])
    obj['order_pay_time'] = trans_time(df['支付完成时间'])
    obj['app_chanel'] = trans_string(df['APP渠道'])
    obj['user_from'] = trans_string(df['流量来源'])
    obj['order_status'] = trans_string(df['订单状态'])
    obj['promised_delivery_time'] = trans_time(df['承诺发货时间'])
    obj['order_type'] = trans_string(df['订单类型'])
    obj['partner_id'] = trans_string(df['达人ID'])
    obj['partner_name'] = trans_string(df['达人昵称'])
    obj['post_sale_status'] = trans_string(df['售后状态'])
    obj['cancel_reason'] = trans_string(df['取消原因'])
    obj['scheduled_delivery_time'] = trans_time(df['预约发货时间'])
    obj['safe_buy'] = trans_string(df['是否安心购'])
    obj['ad_chanel'] = trans_string(df['广告渠道'])
    obj['platform_pay_discount_amount'] = trans_number(df['平台实际承担优惠金额'])
    obj['shop_pay_discount_amount'] = trans_number(df['商家实际承担优惠金额'])
    obj['partner_pay_discount_amount'] = trans_number(df['达人实际承担优惠金额'])
    obj['estimated_delivery_time'] = trans_time(df['预计送达时间'])
    obj['order_submit_month'] = trans_number(df['订单提交月份'])
    obj['order_submit_date'] = trans_time(df['订单提交日期'])
    obj['estimated_collection_amount'] = trans_number(df['预估收款金额'])

    obj['express_delivery_time'] = trans_time(df['发货时间'])
    obj['express_delivery_date'] = trans_time(df['发货日期'])
    obj['express_delivery_days'] = trans_number(df['几天发货'])
    obj['post_sale_id'] = trans_number(df['售后单号'])
    obj['post_sale_type'] = trans_string(df['售后类型'])
    obj['post_sale_apply_time'] = trans_time(df['售后申请时间'])
    obj['post_sale_reason'] = trans_string(df['售后原因'])
    obj['post_sale_reason_tag'] = trans_string(df['售后原因标签'])
    obj['return_express_number'] = trans_string(df['退货物流单号'])
    obj['return_delivery_time'] = trans_time(df['退货发货时间'])
    obj['post_sale_apply_agree_time'] = trans_time(df['同意售后申请时间'])
    obj['shop_refund_time'] = trans_time(df['商家退款时间'])
    obj['user_arrival_time'] = trans_time(df['用户到账时间'])
    obj['post_sale_close_time'] = trans_time(df['售后关闭时间'])
    obj['arbitration_status'] = trans_string(df['仲裁状态'])
    obj['responsible'] = trans_string(df['纠纷责任方'])
    obj['post_sale_finish_time'] = trans_time(df['售后完结时间'])
    obj['order_remarks'] = trans_string(df['订单备注'])
    obj['user_post_sale_desc'] = trans_string(df['用户售后说明'])
    obj['after_sale_remarks'] = trans_string(df['售后备注'])
    obj['post_sale_apply_date'] = trans_time(df['售后申请时间'])
    obj['refund_days'] = trans_number(df['几天退款'])

    obj['settle_time'] = trans_time(df['结算时间'])
    obj['settle_amount'] = trans_number(df['结算金额'])
    obj['settle_date'] = trans_time(df['结算日期'])
    obj['settle_days'] = trans_number(df['几天结算'])

    obj['total_income'] = trans_number(df['收入合计'])
    obj['platform_service_amount'] = trans_number(df['平台服务费'])
    obj['platform_subsidy'] = trans_number(df['平台补贴'])
    obj['partner_subsidy'] = trans_number(df['达人补贴'])
    obj['dy_pay_subsidy'] = trans_number(df['抖音支付补贴'])
    obj['dy_month_subsidy'] = trans_number(df['抖音月付营销补贴'])
    obj['user_total_pay'] = trans_number(df['用户实付'])
    obj['commission'] = trans_number(df['佣金'])
    obj['channel_commission'] = trans_number(df['渠道分成'])
    obj['investment_commission'] = trans_number(df['招商服务费'])
    obj['live_3part_commission'] = trans_number(df['直播间站外推广'])
    obj['other_commission'] = trans_number(df['其他分成'])
    obj['other_commission_desc'] = trans_string(df['其他分成说明'])
    obj['total_expend'] = trans_number(df['支出合计'])
    obj['remark'] = trans_string(df['备注'])
    obj = make_order_status_values(obj)
    return obj


def orders_mul(item_id, orders_from_file, orders_return_from_file, orders_settle_from_file):
    ret = False

    # 所有订单最近三个月的销售情况 所有订单数 未支付 退款 退货退款订单 实收订单  邮费次数  赠品次数
    # 订单提交月份
    orders_from_file['订单提交月份'] = pd.to_datetime(
        orders_from_file['订单提交时间']).dt.month

    # 订单提交日期
    orders_from_file['订单提交日期'] = pd.to_datetime(
        orders_from_file['订单提交时间']).dt.date

    # 订单应付金额
    orders_from_file['订单应付金额'] = pd.to_numeric(orders_from_file['订单应付金额'].map(
        lambda x: currency_to_float(x)), downcast='float')
    # 预估收款金额
    orders_from_file['预估收款金额'] = orders_from_file['订单应付金额']

    # 发货日期
    orders_from_file['发货日期'] = pd.to_datetime(
        orders_from_file['发货时间']).dt.date

    # 几天发货
    orders_from_file["几天发货"] = orders_from_file["发货日期"] - \
        orders_from_file["订单提交日期"]

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

    orders_all["结算日期"] = pd.to_datetime(
        orders_all['结算时间']).dt.date

    orders_all["几天结算"] = orders_all["结算日期"] - \
        orders_all["订单提交日期"]

    orders_all['商品ID'] = pd.to_numeric(
        orders_all['商品ID'])

    orders_all = safe_keep_ol(orders_all,
                              ['主订单编号', '子订单编号', '商品ID', '商品数量', '选购商品', '商品规格', '商品单价', '订单应付金额',
                               '支付方式', '手续费', '收件人', '收件人手机号', '省', '市', '区', '街道',
                               '详细地址', '买家留言', '订单提交时间', '商家备注', '订单完成时间', '支付完成时间',
                               'APP渠道', '流量来源', '订单状态', '发货时间', '承诺发货时间', '订单类型', '达人ID', '达人昵称',
                               '售后状态', '取消原因', '预约发货时间', '是否安心购', '广告渠道', '平台实际承担优惠金额',
                               '商家实际承担优惠金额', '达人实际承担优惠金额', '预计送达时间', '订单提交月份', '订单提交日期',
                               '预估收款金额', '发货日期', '几天发货', '售后单号', '售后类型', '售后申请时间', '售后原因',
                               '售后原因标签', '退货物流单号', '退货发货时间', '同意售后申请时间', '商家退款时间', '用户到账时间',
                               '售后关闭时间', '仲裁状态', '纠纷责任方', '售后完结时间', '订单备注', '用户售后说明', '售后备注',
                               '售后申请日期', '几天退款', '结算时间', '结算日期', '几天结算', '结算金额', '收入合计', '平台服务费', '平台补贴',
                               '达人补贴', '抖音支付补贴', '抖音月付营销补贴', '用户实付', '佣金', '渠道分成', '招商服务费',
                               '直播间站外推广', '其他分成', '其他分成说明', '支出合计', '备注'])
    orders_dict = orders_all.to_dict('records')
    # 更新数据库数据
    ret = data_base_update(item_id, orders_dict)
    return ret


def data_base_update(item_id, datas):
    ret = False
    create = 0
    update = 0
    count = 0
    for data in datas:
        try:
            order_model = transOl2dict(data)
            # print(order_model)
        except Exception as e:
            print(e)
        try:
            olds = Orders.objects.filter(order_id=order_model['order_id'])
            if len(olds) > 0:
                # 判断是否需要更新
                old = olds[0]
                update, update_data = old._is_module_need_update(
                    old, order_model)
                if update:
                    olds.update(**update_data)
                    update = update + 1
                    print('update:'+order_model['order_id'])
            else:
                # 创建
                Orders.objects.update_or_create(
                    order_id=order_model['order_id'], defaults=order_model)
                create = create + 1
                print('create:'+order_model['order_id'])
            count = count + 1
            # if count > 10:
            #    break
            ret = True
        except Exception as e:
            print(e)
        if (count / 500 == 0):
            set_task_status(item_id, '执行中 新增:{create}, 更新:{update}'.format(
                create=create, update=update))

    set_task_status(item_id, '完成 新增:{create}, 更新:{update}'.format(
        create=create, update=update))
    return ret


def orders_pares(item_id, orders, custom, settle):
    orders = pd.read_csv(orders, low_memory=False)
    # custom_orders = pd.read_excel(custom, low_memory=False)
    custom_orders = pd.read_excel(custom)
    settle_orders = pd.read_csv(settle, low_memory=False)
    ret = 201
    if (orders_mul(item_id, orders, custom_orders, settle_orders)):
        ret = 200
    return ret

    # str | 团队ID (optional) 1Z4ySU1lUp3Mh8MV 1Z09a100a3c2694ea68634e049066acf10
    # str | 应用ID (optional) 1Z4y1lUqaPPisC 1Zc50dd09228a34e54aeea521ff12b8952


def set_task_status(item_id, status):
    headers = {
        "Content-Type": "application/json; charset=utf-8"}
    data = {'appId': '1Z4y1lUqaPPisC',
            'apiKey': '1Zc50dd09228a34e54aeea521ff12b8952'}
    response = requests.post(
        'https://app.informat.cn/webapi/v2/app/token', data=json.dumps(data), headers=headers)
    token = json.loads(response.text)

    url = 'https://app.informat.cn/webapi/v2/table_record/update'

    headers = {"Content-Type": "application/json; charset=utf-8",
               "Authorization": "Bearer " + token['data']['accessToken']}

    data = {
        "tableId": "1Z4y4y3FiqWbGrU0",
        "id": item_id,
        "rowData": {
            "1Z4y4y3I0OrTllz9": status,
        },
        "updateFields": ["1Z4y4y3I0OrTllz9"]
    }

    response = requests.post(
        url, data=json.dumps(data), headers=headers)
    print(response.text)

    # orders_pares(
    #    'https://app.informat.cn/file/441d8b327b5e4c85a0b58a1d7ec9ec3e_p.csv',
    #    'https://app.informat.cn/file/f824c0464cbb4920aa6ed29735d86684_p.csv',
    #    'https://app.informat.cn/file/ade5d69dcf0442c0875b802980b170f5_p.csv')

    # SELECT  p_id a, order_submit_date b, COUNT(*) c, express_delivery_days d FROM "OrdersModel_orders" GROUP BY p_id, order_submit_date, express_delivery_days
