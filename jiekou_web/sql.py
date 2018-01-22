#coding=utf-8
import MySQLdb,time,datetime

from flask import Flask,render_template,request

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='interface',port=3306)  #连接数据库
db = conn.cursor()  #获取游标
def insert():
    data = request.form.to_dict()  #获取请求参数
    print data
    t=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")    #获取当前时间
    db.execute("insert into interface_message (case_name,name, apiurl, harder,data,method,creat_time) values ('%s','%s','%s','%s','%s','%s','%s')"\
    %(data['case'].encode('utf-8'),data['name'].encode('utf-8'),data['url'].encode('utf-8'), data['harder'].encode('utf-8')\
    ,data['data'].encode('utf-8') ,data['method'].encode('utf-8'),t ))  #执行语句
    conn.commit() #提交事务
    db.close()   #关闭游标
    conn.close()  #关闭数据库连接
print datetime.datetime.now()