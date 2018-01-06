#coding=utf-8
import requests,unittest,json
from data.data import get_case

def api(way,url,data,*hearder):
    if way.upper()=="POST":
        return requests.post(url,data=data, headers=hearder[0])
    elif way.upper()=="GET":
        return requests.get(url, data=data, headers=hearder[0])
    else:
        print way.upper()
