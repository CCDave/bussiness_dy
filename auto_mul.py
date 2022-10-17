#!/usr/bin/env python
# coding: utf-8
from ast import Num
from ctypes.wintypes import PUSHORT
from pickle import TRUE
import pandas as pd
import datetime
from openpyxl import load_workbook
from openpyxl.styles import Alignment
import dy_tool as tool
import numpy as np

import warnings

from dy_tool import currency_to_float, get_last_months, get_product_name_from_table
# 财务计算
warnings.filterwarnings("ignore")

config = {'订单表名': '订单表.csv',
          '结算表名': '结算表.csv',
          '售后表名': '售后表.csv',
          '成本表名': '成本表.csv'
          }


orders_from_file = {}
orders_settle_from_file = {}
orders_cost_from_file = {}
orders_return_from_file = {}

# 计算最近三个月的订单
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


if '售后表名' in config:
    orders_return_from_file = pd.read_csv(config['售后表名'])
else:
    print('！！！！！！！！结算表名不存在,请检查文件 ！！！！！！！！')
    exit()

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


# 售后订单处理
orders_return_from_file['子订单编号'] = orders_return_from_file['订单号']
orders_return_from_file['售后申请日期'] = pd.to_datetime(
    orders_return_from_file['售后申请时间']).dt.date

orders_all = pd.merge(
    orders_from_file, orders_return_from_file, on='子订单编号', how='left')

orders_all["几天退款"] = orders_all["售后申请日期"] - \
    orders_all["订单提交日期"]

# 获取 月订单 日订单 产品订单 算订单数据 几天退款 几天发货  未支付订单 支付发货前退款订单 退货退款订单
# 总订单数
orders_all.sum()
# 未支付退款数

file_name = str(datetime.datetime.now())+'退货数据统计11111.xlsx'
writer = pd.ExcelWriter(
    file_name, mode='w', engine='openpyxl')
orders_all.to_excel(writer, '合并订单数据')
writer.save()
writer.close()
