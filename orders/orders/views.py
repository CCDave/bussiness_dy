from logging import Logger
from django.http import HttpResponse, JsonResponse
import logging

from orders.mul.order_parse import orders_pares
# 日志输出常量定义


def hello(request):
    return HttpResponse("Hello world ! ")


def more(request):
    try:
        print(request.GET)
        ret = 201
        if request.method == "GET":  # 获取判断请求方式
            get = request.GET.dict()
            if 'orders' in get and 'custom' in get and 'settle' in get:

                # 处理数据
                #ret = orders_pares(get['orders'], get['custom'], get['settle'])
                ret = 201
        ret = orders_pares(
            'https://app.informat.cn/file/441d8b327b5e4c85a0b58a1d7ec9ec3e_p.csv',
            'https://app.informat.cn/file/f824c0464cbb4920aa6ed29735d86684_p.csv',
            'https://app.informat.cn/file/ade5d69dcf0442c0875b802980b170f5_p.csv')
    except Exception as e:
        tb = e.format_exc()
        return HttpResponse(tb)
    else:
        ret = 200
    request_data = {"code": ret, "message": "success"}
    return JsonResponse(request_data)
