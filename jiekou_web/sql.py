#coding=utf-8
import MySQLdb,time,datetime,requests
from flask import Flask,request


h= "{'Content-Type': 'application/json'}"
h2='{"Content-Type": "application/x-www-form-urlencoded"}'
data,case,name,url,harder,d,method,jcd=None,None,None,None,None,None,None,None

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='interface',port=3306)  #连接数据库
db = conn.cursor()  #获取游标

def get_api():
    global data,case,name,url,harder,d,method,jcd
    data=request.form.to_dict()
    case = data['case'].encode('utf-8')
    name = data['name'].encode('utf-8')
    url = data['url'].encode('utf-8')
    harder = data['harder'].encode('utf-8')
    d = data['data'].encode('utf-8')
    method = data['method'].encode('utf-8')
    jcd = data['jcd'].encode('utf-8')
def insert():  #获取请求参数
    data = request.form.to_dict()
    t=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")    #获取当前时间
    d2=d.replace("\'", "\*")
    d1 = d2.replace("\"", "\^")
    h = harder.replace("\,", "\"")
    try:
        db.execute("insert into interface_message (case_name,name, apiurl, harder,value,method,creat_time) values ('%s','%s','%s','%s','%s','%s','%s')" \
    %(case,name,url,h,d1 ,method,t))  #执行语句
    except BaseException as e:
        print "插入数据库出错%s" % e
    conn.commit() #提交事务
    db.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
def api_test(method, url, d, harder):  #处理请求
    try:
        if method.lower()=="get":
            r= requests.get(url, params=d, headers=harder)
        elif method.lower() == "post" and harder == h:
            r= requests.post(url, json=d, headers=harder)
        elif method.lower()=="post" and harder == h2:
            r = requests.post(url, data=eval(d), headers=eval(harder))
        return r
    except BaseException as e:
        print "处理请求出错%s"%e
    # if method == "put":
    #     results = requests.put(url, data, headers=header)
    # if method == "delete":
    #     results = requests.delete(url, headers=header)
    # if method == "patch":
    #     results == requests.patch(url, data, headers=header)
    # if method == "options":
    #     results == requests.options(url, headers=header)

db.execute("select * from interface_message")# 执行语句
results = db.fetchall()





