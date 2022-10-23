from logging import Logger
from django.http import HttpResponse, JsonResponse
from orders.mul.order_parse import orders_pares
import logging
 
# 日志输出常量定义

def hello(request):
    return HttpResponse("Hello world ! ")


def more(request):
    print (request.GET)
    if request.method == "GET": #获取判断请求方式
        get = request.GET.dict()
        if 'a' in get:
            request_data = {"code":200,"message":"请求成功", "a":get['a']}
        ## 下載文件數據
        ## 計算文件數據
        ## 數據入庫
        orders_pares()
        return JsonResponse(request_data)
