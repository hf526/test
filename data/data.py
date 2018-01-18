#coding=utf-8
import xlrd,os
from public.log import Logger
from public import public
import requests,json

logger=Logger().get_loger()
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
            case_name.append(public.get_content(table, j, 1))
            method.append(public.get_content(table, j, 2))
            URL.append(public.get_content(table, j, 3))
            data.append(public.get_content(table, j, 4))
            harder.append(public.get_content(table, j, 5))
            chick .append(public.get_content(table, j, 6))

    url= URL[0].encode("UTF-8")
    d=json.dumps(data[0])
    h=json.loads(harder[0])
    # d=json.load(data1)
    # print isinstance(h,str),isinstance(data1,str)
    # print url=="http://iacloud.ceway.com.cn/gatewaytest/api/token/create.do",data[0]=={'encData':'{"loginName":"cw4996",  "password":"321123",   "appId":"ceway1000",   "appSecret":"VJPXUHUqy0CU4GV0gczqEjDBNSSdZWfRitBdCJjhcUU0eqGS5Nga0CHqDd1kPOIZ"}'}
    # print json.loads(harder[0])=={"Content-Type": "application/x-www-form-urlencoded"}
    #print type(json.dumps(data[0])),type({'encData':'{"loginName":"cw4996",  "password":"321123",   "appId":"ceway1000",   "appSecret":"VJPXUHUqy0CU4GV0gczqEjDBNSSdZWfRitBdCJjhcUU0eqGS5Nga0CHqDd1kPOIZ"}'})
    # print "%s"%url,data[0],harder[0]
    r = requests.post(url,json=d, headers=h)
    # html = requests.post(table.cell(2, 2), json=data)
    # print r.text
    # r = requests.post("http://iacloud.ceway.com.cn/gatewaytest/api/token/create.do", data={'encData':'{"loginName":"cw4996",  "password":"321123",   "appId":"ceway1000",   "appSecret":"VJPXUHUqy0CU4GV0gczqEjDBNSSdZWfRitBdCJjhcUU0eqGS5Nga0CHqDd1kPOIZ"}'}, headers={"Content-Type": "application/x-www-form-urlencoded"})
    # r = requests.post("%s"%url,data=d, headers=h)
    print r.text
get_case()
