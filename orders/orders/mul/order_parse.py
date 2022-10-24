import datetime
from doctest import FAIL_FAST
import requests   
import csv
from openpyxl import load_workbook
import pandas as pd

orders_cul = ['主订单编号','子订单编号','选购商品'
    ,'商品规格','商品数量','商品ID','商品单价'
    ,'订单应付金额','支付方式','省','买家留言'
    ,'订单提交时间','商家备注','订单完成时间','支付完成时间'
    ,'APP渠道','流量来源','订单状态','承诺发货时间'
    ,'达人昵称','售后状态','取消原因','预约发货时间'
    ,'是否安心购','广告渠道','发货时间','预计送达时间']
custom_cul = ['售后单号','订单号','商品单号'
    ,'商品名称','商品ID','商品发货状态','售后类型'
    ,'退商品金额（元）','售后申请时间','售后原因','退货物流单号'
    ,'退货异常','退货发货时间','同意售后申请时间','商家退款时间'
    ,'用户到账时间','售后关闭时间','商家退货地址','商家退货联系人姓名'
    ,'仲裁状态','纠纷责任方','发货物流单号','发货物流状态'
    ,'换货物流单号','退货物流状态','售后完结时间','订单备注'
    ,'用户售后说明','售后备注','售后完结时间','订单备注']
settle_cul = ['订单号','子订单号','结算时间'
    ,'结算金额','结算账户','结算单类型','有结算前退款'
    ,'下单时间','商品总价','结算前退款金额','平台补贴'
    ,'达人补贴','抖音支付补贴','抖音月付营销补贴','用户实付'
    ,'收入合计','支出合计']

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
    #orders_all.to_csv(writer)
    writer.save()
    writer.close()

def trans_head2_string(data, key):
    for k in key:
        data[k] = data[k].astype('str')
    return data

def get_pandas_from_url (url):
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
       data = data.drop(labels = to_drop, axis=axis)
    return data

def safe_keep_ol(data, keeps):
    drop_col = []
    for col in data.columns:
        if (col not in keeps):
            drop_col.append(col)
    if len(drop_col)> 0:
        data = safe_drop_ol(data, drop_col, axis= 1)
    return data

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

    print(len(orders_return_from_file))

    # 售后订单处理
    #orders_return_from_file['订单号'] = orders_return_from_file['订单号'].astype('str')
    #orders_return_from_file['售后单号'] = orders_return_from_file['售后单号'].astype('str')
    #orders_return_from_file['商品单号'] = orders_return_from_file['商品单号'].astype('str')
    
    orders_return_from_file['主订单编号'] = pd.to_numeric(orders_return_from_file['订单号'])
    orders_return_from_file['子订单编号'] = pd.to_numeric(orders_return_from_file['商品单号'])

    orders_return_from_file['售后申请日期'] = pd.to_datetime(
        orders_return_from_file['售后申请时间']).dt.date

    # 去重
    orders_return_from_file = orders_return_from_file.sort_values(by='售后申请时间',ascending=False)
    orders_return_from_file = orders_return_from_file.drop_duplicates(subset=['子订单编号'], keep='first')
    print(len(orders_return_from_file))

    orders_all = pd.merge(
        orders_from_file, orders_return_from_file, on=['子订单编号','主订单编号'], how='left')
    print(len(orders_all))

    orders_all["几天退款"] = orders_all["售后申请日期"] - \
        orders_all["订单提交日期"]

    ## 处理结算表
    orders_settle_from_file = orders_settle_from_file.drop(index=0)

    orders_settle_from_file['主订单编号'] = orders_settle_from_file['订单号']
    orders_settle_from_file['子订单编号'] = orders_settle_from_file['子订单号']

    orders_settle_from_file['子订单编号'] = orders_settle_from_file['子订单号'].map(
        lambda x: string_replace(x, "'")) 

    orders_settle_from_file['主订单编号'] = orders_settle_from_file['订单号'].map(
    lambda x: string_replace(x, "'")) 

    orders_settle_from_file['子订单编号'] = pd.to_numeric(orders_settle_from_file['子订单编号'])
    orders_settle_from_file['主订单编号'] = pd.to_numeric(orders_settle_from_file['主订单编号'])
    

    ## 去重
    #print(len(orders_settle_from_file))
    #write_excel_file('1.xlsx', 'a', orders_settle_from_file)
    orders_settle_from_file = orders_settle_from_file.sort_values(by='结算金额',ascending=True)
    #print(len(orders_settle_from_file))

    orders_settle_from_file = orders_settle_from_file.drop_duplicates(subset=['子订单编号'], keep='first')
    #print(len(orders_settle_from_file))
    #write_excel_file('2.xlsx','a',orders_settle_from_file)
    

    #print(type(orders_settle_from_file['子订单编号'][1]))
    #print(orders_settle_from_file['子订单编号'][1])
    #print(type(orders_all['子订单编号'][0]))

    orders_all = pd.merge(
        orders_all, orders_settle_from_file, on=['子订单编号','主订单编号'], how='left')
    print(len(orders_all))
    print (list(orders_all.columns))
    #orders_all['主订单编号'] = orders_all['主订单编号_x'].astype('str')
    #orders_all['子订单编号'] = orders_all['子订单编号'].astype('str')
    orders_all = trans_head2_string(orders_all,['主订单编号','子订单编号'])
    orders_all = safe_change_name(orders_all,'商品数量_x','商品数量')
    orders_all = safe_change_name(orders_all,'商品ID_x','商品ID')
    orders_all = safe_change_name(orders_all,'订单类型_x','订单类型')
    orders_all = safe_change_name(orders_all,'售后状态_x','售后状态')

    orders_all = safe_keep_ol(orders_all,
     ['主订单编号','子订单编号','商品名称','商品规格','商品单价','订单应付金额','支付方式','手续费'
     ,'收件人','收件人手机号','省','市','区','街道','详细地址','买家留言'
     ,'订单提交时间','商家备注','订单完成时间','支付完成时间','APP渠道','流量来源','订单状态','承诺发货时间'
     ,'订单类型','达人ID','达人昵称','售后状态','取消原因','预约发货时间','是否安心购','广告渠道'
      ,'平台实际承担优惠金额','商家实际承担优惠金额','达人实际承担优惠金额','预计送达时间','订单提交月份','订单提交日期','预估收款金额','发货日期'
      ,'几天发货','售后单号','售后类型','售后申请时间','售后原因','售后原因标签','退货物流单号','退货发货时间'
      ,'同意售后申请时间','商家退款时间','用户到账时间','售后关闭时间','仲裁状态','纠纷责任方','售后完结时间','订单备注'
      ,'用户售后说明','售后备注','售后申请日期','几天退款','结算时间','结算金额','收入合计','平台服务费'
      ,'平台补贴','达人补贴','抖音支付补贴','抖音月付营销补贴','用户实付','佣金','渠道分成','招商服务费'
      ,'直播间站外推广','其他分成','其他分成说明','支出合计','备注'])
    write_excel_file('aa.xlsx', 'a', orders_all)
    count=0
    for tup in zip(orders_from_file['主订单编号'], orders_from_file['子订单编号'], orders_from_file['订单提交日期']):
        print(tup, type( tup[1:] ))
        ##print(tup)
        count+=1
        if count>5:
            break 


def orders_pares(orders, custom, settle):
    orders = pd.read_csv(orders)
    custom_orders = pd.read_csv(custom)
    settle_orders = pd.read_csv(settle)
    ret = 201
    if (orders_mul(orders, custom_orders, settle_orders)):
        ret = 200
    return ret


#orders_pares(
#    'https://app.informat.cn/file/441d8b327b5e4c85a0b58a1d7ec9ec3e_p.csv',
#    'https://app.informat.cn/file/f824c0464cbb4920aa6ed29735d86684_p.csv',
#     'https://app.informat.cn/file/ade5d69dcf0442c0875b802980b170f5_p.csv')