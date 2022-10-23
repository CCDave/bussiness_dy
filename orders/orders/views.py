from logging import Logger
from django.http import HttpResponse, JsonResponse
import logging

from orders.mul.order_parse import orders_pares

 
# 日志输出常量定义

def hello(request):
    return HttpResponse("Hello world ! ")


def more(request):
    print (request.GET)
    ret = 201
    if request.method == "GET": #获取判断请求方式
        get = request.GET.dict()
        if 'orders' in get and 'custom' in get and 'settle' in get:
            #处理数据
            ret = orders_pares(get['orders'], get['custom'], get['settle'])
    request_data = {"code":ret,"message":"success"}
    return JsonResponse(request_data)
