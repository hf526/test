#coding=utf-8
import sql

def savedata():
    sql.get_api()
    sql.insert()

def interface_access():
    sql.get_api()
    s=sql.d
    r=sql.api_test(sql.method,sql.url,sql.d,sql.harder)
    return r.text

