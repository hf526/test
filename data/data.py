#coding=utf-8
import xlrd,os
from public.log import Logger
from public import public
import requests,json

logger=Logger().get_loger()
t1={"Content-Type": "application/x-www-form-urlencoded"}

case_numer = []
case_name = []
method = []
URL = []
data = []
harder = []
chick = []

number=None
def get_case():
    global number
    public.open_excil('F:\hf\data\case.xlsx')
    table=public.get_excil('case')
    number=public.get_row_number(table)
    for j in range(1,number):  #[0.1.2]
            case_numer.append((public.get_content(table, j,0)))
            case_name.append(public.get_content(table, j, 1).encode("UTF-8"))
            method.append(public.get_content(table, j, 2).encode("UTF-8"))
            URL.append(public.get_content(table, j, 3).encode("UTF-8"))
            data.append(eval(public.get_content(table, j, 4).encode("UTF-8")))
            harder.append(public.get_content(table, j, 5).encode("UTF-8"))
            chick.append(public.get_content(table, j, 6).encode("UTF-8"))


    # url= URL[0].encode("UTF-8")
    # d=json.dumps(data[0])
    # h=json.loads(harder[0])

get_case()