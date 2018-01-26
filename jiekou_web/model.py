#coding=utf-8
import sql

def savecase():
    sql.get_api()
    sql.insert()

def interface_access():
    try:
        sql.get_api()
        s=sql.d
        r=sql.api_test(sql.method,sql.url,sql.d,sql.harder)
        # return r.text
        return sql.get_api()
    except BaseException as e:
        return sql.get_api()

