from logging import Logger
from django.http import HttpResponse, JsonResponse
import logging

from orders.mul.order_parse import orders_pares, set_task_status
# 日志输出常量定义


def hello(request):
    return HttpResponse("Hello world ! ")


def more(request):
    item_id = None
    try:
        print(request.GET)
        ret = 201
        if request.method == "GET":  # 获取判断请求方式
            get = request.GET.dict()
            if 'orders' in get and 'custom' in get and 'settle' in get:
                if ('item' in get):
                    item_id = get['item']
                # 处理数据
                set_task_status(item_id, '开始执行任务')
                ret = orders_pares(
                    item_id, get['orders'], get['custom'], get['settle'])
                ret = 201
        # ret = orders_pares(
        #    'https://app.informat.cn/file/441d8b327b5e4c85a0b58a1d7ec9ec3e_p.csv',
        #    'https://app.informat.cn/file/f824c0464cbb4920aa6ed29735d86684_p.csv',
        #    'https://app.informat.cn/file/ade5d69dcf0442c0875b802980b170f5_p.csv')
    except Exception as e:
        tb = e
        set_task_status(item_id, '执行失败' + e)
        return HttpResponse(tb)
    else:
        ret = 200
    request_data = {"code": ret, "message": "success"}
    return JsonResponse(request_data)
