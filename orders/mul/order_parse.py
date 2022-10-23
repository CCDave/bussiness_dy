
import requests

def orders_pares():
    ## 下载文件
    url = "https://app.informat.cn/file/JTdCJTIyaWQlMjIlM0ElMjJjOGU4NTVmZjk0Y2I0YWI5OTNkZWRlZmZkZWE2YWZjN19wLmNzdiUyMiUyQyUyMm5hbWUlMjIlM0ElMjIlRTglQUUlQTIlRTUlOEQlOTUlRTglQTElQTguY3N2JTIyJTdE?download=true"
    data = requests.get(url)
    print (data)
