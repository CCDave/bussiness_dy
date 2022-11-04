from logging import Logger
from django.http import HttpResponse, JsonResponse
import logging

from orders.mul.order_parse import orders_pares, set_task_status
# 日志输出常量定义


def hello(request):
    return HttpResponse("Hello world ! ")


def more(request):
    ret = orders_pares('123',
                       'https://app.informat.cn/file/JTdCJTIyaWQlMjIlM0ElMjJiZDFhY2FkY2QzMmM0MDAzOTU0MmY5ZmYyOTNkOGIxYV9wLmNzdiUyMiUyQyUyMm5hbWUlMjIlM0ElMjIxNjY3MTEzMDA1XzNiMjZjODUxMjZhZGM3ZDUyODQyZTUzMjcxOGEwZWVja1dqZVVXUEEuY3N2JTIyJTdE?download=true',
                       'https://app.informat.cn/file/JTdCJTIyaWQlMjIlM0ElMjI2OTcyZmM4NzY4ZDE0ZTJmYjc3MDM0NmVhZDIxNmY3Zl9wLnhsc3glMjIlMkMlMjJuYW1lJTIyJTNBJTIyJUU1JTk0JUFFJUU1JTkwJThFJUU1JThEJTk1LTIwMjItMTAtMzAlMjAwMl81NV80OC54bHN4JTIyJTdE?download=true',
                       'C:\\Users\\jy027\\Downloads\\DL202210301834031469272617.csv')
    # 'https://app.informat.cn/file/JTdCJTIyaWQlMjIlM0ElMjJlMjQ5N2I0Mjc1ZDk0OGQ2OTNhMjM3Mzc1NWY2Y2UyNF9wLmNzdiUyMiUyQyUyMm5hbWUlMjIlM0ElMjJETDIwMjIxMDMwMTQ1ODM5MTI2NjkzMDIxNi5jc3YlMjIlN0Q=?download=true')
    return 201
    try:
        print(request.GET)
        ret = 201
        if request.method == "GET":  # 获取判断请求方式
            get = request.GET.dict()
            if 'orders' in get and 'custom' in get and 'settle' in get:
                if ('item' in get):
                    item_id = get['item']
                # 处理数据
                set_task_status(item_id, '1/1,开始执行任务')
                ret = orders_pares(
                    item_id, get['orders'], get['custom'], get['settle'])
                ret = 201

    except Exception as e:
        tb = e
        set_task_status(item_id, '1/1,执行失败' + e)
        return HttpResponse(tb)
    else:
        ret = 200
    request_data = {"code": ret, "message": "success"}
    return JsonResponse(request_data)
