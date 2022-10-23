from doctest import FAIL_FAST
import requests   
import csv
import pandas as pd

def download_file(url):
    with requests.Session() as s:
        download = s.get(url)
        return download.content
    return False

def read_file_to_csv(content):
    #decoded_content = content.decode('utf-8')
    ##cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    cr = pd.read_csv(content)
    return cr

def orders_pares(orders, custom, settle):
    content = download_file(custom)
    if(content != False):
        csv = read_file_to_csv(content)
        print (csv)
        return 200
    return 201


