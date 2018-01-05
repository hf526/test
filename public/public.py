#coding=utf-8
import requests,unittest,json
from data import data

def api(way,url,data,*hearder):
    if way.upper()=="POST":
        return requests.post(url,data=data, headers=hearder[0])
    else:
        print way.upper()
