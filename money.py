#!/usr/bin/env python
# coding: utf-8
from ast import Num
from pickle import TRUE
import pandas as pd
import datetime
from openpyxl import load_workbook
from openpyxl.styles import Alignment
import dy_tool as tool
import numpy as np

import warnings

from dy_tool import get_product_name_from_table
# 财务计算
warnings.filterwarnings("ignore")

config = {'订单表名': '订单表.csv',
          '结算表名': '结算表.csv',
          '成本表名': '成本表.csv',
          '计算月份': ['2022-08', '2022-09']
          }


orders_from_file = {}
orders_settle_from_file = {}
orders_cost_from_file = {}

if '订单表名' in config:
    orders_from_file = pd.read_csv(config['订单表名'])
else:
    print('！！！！！！！！订单表不存在,请检查文件 ！！！！！！！！')
    exit()

if '结算表名' in config:
    orders_settle_from_file = pd.read_csv(config['结算表名'])
else:
    print('！！！！！！！！结算表名不存在,请检查文件 ！！！！！！！！')
    exit()


if '成本表名' in config:
    orders_cost_from_file = pd.read_csv(config['成本表名'])
else:
    print('！！！！！！！！结算表名不存在,请检查文件 ！！！！！！！！')
    exit()

if ('计算月份' not in config) or len(config['计算月份']) == 0:
    print('！！！！！！！！请输入要计算的月份 ！！！！！！！！')
    exit()


def Currency_to_float(e):
    if isinstance(e, str):
        return e.replace(',', '')
    return e


############################################# 初始化数据 ##################################################
# 提取订单提交日期：yyyy-mm-dd
# orders_from_file['订单提交日期'] = pd.to_datetime(orders_from_file['订单提交时间']).dt.date
orders_from_file['订单提交月份'] = pd.to_datetime(
    orders_from_file['订单提交时间']).dt.month

# \ orders_from_file['优惠总金额'] - orders_from_file['红包抵扣']
orders_from_file['预估收款金额'] = pd.to_numeric(orders_from_file['订单应付金额'].map(
    lambda x: Currency_to_float(x)), downcast='float')


ret = {}
month_source_data = []
# 先按月份取出订单


def get_sum_size_from_status(orders, order_status, after_status):
    status = orders[(orders['订单状态'] == order_status) & (
        orders['售后状态'] == after_status)]
    if len(status):
        return status.iloc[0]['sum'], status.iloc[0]['size']
    else:
        return 0, 0


for month in config['计算月份']:
    current_month_orders = orders_from_file[orders_from_file['订单提交月份'] == pd.to_datetime(
        month).month]
    # 取出这个月的所有商品
    pid_orders = current_month_orders.groupby('商品ID')
    pro_data = []
    for name, orders in pid_orders:

        # if name != 3562294316670045829:
        #    continue

        # 商品名称
        product_name = get_product_name_from_table(orders)
        # 商品订单数
        order_total_count = len(orders)
        order_total_pre = orders['预估收款金额'].sum()

        # if order_total_count < 100:
        #    print(name + '订单量小于100')
        #    continue

        # 商品付款订单数
        orders_count = orders.groupby(['订单状态', '售后状态'])['商品数量'].agg(
            [np.sum, np.size]).reset_index()
        money_count = orders.groupby(['订单状态', '售后状态'])['预估收款金额'].agg(
            [np.sum, np.size]).reset_index()
        # print(money_count)

        # result.append({'month': month, 'pid': name, 'data': orders_count})
        # 订单状态  ['备货中', '已关闭', '已完成', '已发货']
        # 售后状态:['-','补寄/换货成功','待买家退货处理','待商家处理','待商家收货', '售后关闭', '同意退款，退款成功','退货后拒绝退款']

        # 实际收款订单数
        pay_order_count = 0

        # 实际收款商品数
        pay_product_count = 0

        # 实际预估收款金额
        pay_pre = 0

        # 邮费次数
        postage_count = 0
        # 补寄/换货订单数
        more_postage_count = 0

        # 退款订单数
        return_order_count = 0
        # 退款货品数
        return_product_count = 0
        return_order_pay_pre = 0

        # 未支付订单数
        no_pay_order_count = 0
        no_pay_order_pay_pre = 0
        # 未支付商品数
        no_pay_product_count = 0

        sum, size = get_sum_size_from_status(orders_count, '备货中', '-')
        sum_pre, size_pre = get_sum_size_from_status(money_count, '备货中', '-')
        pay_pre = pay_pre + sum_pre
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum

        postage_count = postage_count + size

        sum, size = get_sum_size_from_status(orders_count, '已发货', '补寄/换货成功')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已发货', '补寄/换货成功')
        pay_pre = pay_pre + sum_pre
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum

        postage_count = postage_count + size
        more_postage_count = more_postage_count + size

        sum, size = get_sum_size_from_status(orders_count, '已发货', '待买家退货处理')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已发货', '待买家退货处理')
        postage_count = postage_count + size
        return_order_pay_pre = return_order_pay_pre + sum_pre
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum

        sum, size = get_sum_size_from_status(orders_count, '已发货', '待商家收货')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已发货', '待买家退货处理')
        postage_count = postage_count + size
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum
        return_order_pay_pre = return_order_pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已发货', '售后关闭')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已发货', '售后关闭')
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum
        postage_count = postage_count + size
        pay_pre = pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已发货', '退货后拒绝退款')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已发货', '退货后拒绝退款')
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum
        postage_count = postage_count + size
        pay_pre = pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '-')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '-')
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum
        postage_count = postage_count + size
        pay_pre = pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '补寄/换货成功')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '补寄/换货成功')
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum
        postage_count = postage_count + size
        more_postage_count = more_postage_count + size
        pay_pre = pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '待买家退货处理')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '待买家退货处理')
        postage_count = postage_count + size
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum
        return_order_pay_pre = return_order_pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '待商家处理')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '待商家处理')
        postage_count = postage_count + size
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum
        return_order_pay_pre = return_order_pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '待商家收货')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '待商家收货')
        postage_count = postage_count + size
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum
        return_order_pay_pre = return_order_pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '售后关闭')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '售后关闭')
        pay_order_count = pay_order_count + size
        pay_product_count = pay_product_count + sum
        postage_count = postage_count + size
        pay_pre = pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已完成', '同意退款，退款成功')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已完成', '同意退款，退款成功')
        postage_count = postage_count + size
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum
        return_order_pay_pre = return_order_pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已关闭', '-')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已关闭', '-')
        no_pay_order_count = no_pay_order_count + size
        no_pay_product_count = no_pay_product_count + sum
        no_pay_order_pay_pre = no_pay_order_pay_pre + sum_pre

        sum, size = get_sum_size_from_status(orders_count, '已关闭', '同意退款，退款成功')
        sum_pre, size_pre = get_sum_size_from_status(
            money_count, '已关闭', '同意退款，退款成功')
        return_order_count = return_order_count + size
        return_product_count = return_product_count + sum
        return_order_pay_pre = return_order_pay_pre + sum_pre

        pro_data.append({
            '商品ID': name,
            '商品名字': product_name,
            '所有订单数': order_total_count,
            '所有订单预估收款': order_total_pre,
            '实收订单数': pay_order_count,
            '实收商品数': pay_product_count,
            '预估收款金额': pay_pre,
            '邮费次数': postage_count,
            '补寄/换货次数': more_postage_count,
            '退款订单数': return_order_count,
            '退款商品数': return_product_count,
            '预估退款金额': return_order_pay_pre,
            '未支付订单数': no_pay_order_count,
            '未支付订商品数': no_pay_product_count,
            '预估未支付金额': no_pay_order_pay_pre,
        })
    month_source_data.append({'month': month, 'data': pro_data})

month_result = []
for source_data in month_source_data:
    pro_datas = source_data['data']
    month = source_data['month']
    pid_result = []
    for pid_data in pro_datas:

        # 计算成本
        product_cost_infos = orders_cost_from_file[orders_cost_from_file['商品ID']
                                                   == pid_data['商品ID']]
        pid_data['成本'] = []
        pid_data['快递成本'] = []
        pid_data['赠品成本'] = []
        for i in range(0, len(product_cost_infos)):
            pid_data['成本'].append({'单价': product_cost_infos.iloc[i]
                                   ['产品单价'], '数量': product_cost_infos.iloc[i]['成本数量'], '金额': product_cost_infos.iloc[i]
                                   ['产品单价'] * product_cost_infos.iloc[i]['成本数量']})
            pid_data['快递成本'].append({'单价': product_cost_infos.iloc[i]
                                     ['快递单价'], '数量': product_cost_infos.iloc[i]['成本数量'], '金额': product_cost_infos.iloc[i]
                                     ['快递单价'] * product_cost_infos.iloc[i]['成本数量']})
            pid_data['赠品成本'].append({'单价': product_cost_infos.iloc[i]
                                     ['赠品单价'], '数量': product_cost_infos.iloc[i]['成本数量'], '金额': product_cost_infos.iloc[i]
                                     ['赠品单价'] * product_cost_infos.iloc[i]['成本数量']})

        pid_data['成本'].sort(key=lambda x: x['单价'])
        pid_data['快递成本'].sort(key=lambda x: x['单价'])
        pid_data['赠品成本'].sort(key=lambda x: x['单价'])
        pid_result.append(pid_data)
    month_result.append({'month': month, 'data': pid_result})


result_data = []

for real_data in month_result:
    month = real_data['month']
    data_month = real_data['data']
    index = 0
    ret = {}
    ret = pd.DataFrame(data=None, columns=['商品ID', '商品名字',
                                           '所有订单数', '所有订单预估收款',
                                           '实收订单数', '实收商品数', '预估收款金额',
                                           '邮费次数', '补寄/换货次数',
                                           '退款订单数', '退款商品数', '预估退款金额',
                                           '未支付订单数', '未支付订商品数', '预估未支付金额',
                                           '产品单价', '数量', '产品总成本',
                                           '物流单价', '数量', '物流总成本',
                                           '赠品单价', '数量', '赠品总成本',
                                           '总成本', '总预估收款'
                                           ], index=list(range(len(data_month) + 1)))

    for data in data_month:

        ret.iloc[index][0] = data['商品ID']
        ret.iloc[index][1] = data['商品名字']
        ret.iloc[index][2] = data['所有订单数']
        ret.iloc[index][3] = data['所有订单预估收款']
        ret.iloc[index][4] = data['实收订单数']
        ret.iloc[index][5] = data['实收商品数']
        ret.iloc[index][6] = data['预估收款金额']
        ret.iloc[index][7] = data['邮费次数']
        ret.iloc[index][8] = data['补寄/换货次数']
        ret.iloc[index][9] = data['退款订单数']
        ret.iloc[index][10] = data['退款商品数']
        ret.iloc[index][11] = data['预估退款金额']
        ret.iloc[index][12] = data['未支付订单数']
        ret.iloc[index][13] = data['未支付订商品数']
        ret.iloc[index][14] = data['预估未支付金额']

        if len(data['成本']) > 0:
            ret.iloc[index][15] = data['成本'][0]['单价']
            ret.iloc[index][16] = data['实收商品数']
            ret.iloc[index][17] = data['成本'][0]['单价'] * data['实收商品数']
        else:
            ret.iloc[index][15] = 0
            ret.iloc[index][16] = 0
            ret.iloc[index][17] = 0

        if len(data['快递成本']) > 0:
            ret.iloc[index][18] = data['快递成本'][0]['单价']
            ret.iloc[index][19] = data['邮费次数']
            ret.iloc[index][20] = data['快递成本'][0]['单价'] * data['邮费次数']
        else:
            ret.iloc[index][18] = 0
            ret.iloc[index][19] = 0
            ret.iloc[index][20] = 0

        if len(data['赠品成本']) > 0:
            ret.iloc[index][21] = data['赠品成本'][0]['单价']
            ret.iloc[index][22] = data['实收商品数']
            ret.iloc[index][23] = data['赠品成本'][0]['单价'] * data['实收商品数']
        else:
            ret.iloc[index][21] = 0
            ret.iloc[index][22] = 0
            ret.iloc[index][23] = 0

        ret.iloc[index][24] = ret.iloc[index][17] + \
            ret.iloc[index][20] + ret.iloc[index][23]
        ret.iloc[index][25] = data['预估收款金额']

        index = index + 1

    ret['商品ID'] = ret['商品ID'].astype('str')
    result_data.append({'month': month, 'data': ret})

if len(result_data) > 0:
    file_name = str(datetime.datetime.now())+'财务统计数据.xlsx'
    writer = pd.ExcelWriter(
        file_name, mode='w', engine='openpyxl')
    for ret in result_data:
        ret['data'].to_excel(writer, ret['month']+'月数据')
    writer.save()
    writer.close()

print('计算完成')
